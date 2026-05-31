#!/usr/bin/env python3
import json
import sys

import argparse
import typing

from pathlib import Path

# easter egg frfr
from typing import Literal
type Ternary = Literal[True, False, None]

type ColorMode = Literal['never', 'auto', 'always']
type Point = tuple[int, int]
GRID_SIZE: int = 27

ansi: Ternary = None
def error(*args):
    if ansi is True:
        print("\033[1;31merror:\033[0m ", end='')
    else:
        print("error: ", end='')
    print(*args)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    error("failed to import PIL (make sure its installed using pip)")
    error("details: ", e)
    exit(1)

def tern2dec(s:str) -> int:
    return int(s, 3)

def cellify(i: int) -> Point:
    return (i // GRID_SIZE, i % GRID_SIZE)

class CliArgs:
    font_path: Path 
    font_size: int
    spec_path: Path
    out_path:  Path
    cell_size: int
    color: ColorMode

    @staticmethod
    def get_color_mode(sel: ColorMode) -> Ternary:
        if sel == 'always':
            return True
        if sel == 'never':
            return False
        return sys.stderr.isatty()

    @staticmethod
    def input_file(param: str):
        path = Path(param)
        if not path.is_file():
            raise argparse.ArgumentTypeError(f"the file '{param}' does not exist.")
        return path
   
    @staticmethod
    def output_file(param: str):
        path = Path(param)
        if not path.parent.is_dir():
            raise argparse.ArgumentTypeError(f"the directory '{path.parent}' does not exist.")
        return path

class CharData(typing.TypedDict):
    code:        str
    name:        str
    description: str
    unicode:     typing.NotRequired[str]
    mnemonic:    typing.NotRequired[str]
    ascii:       typing.NotRequired[str]

def do_the_conversion(args: CliArgs) -> int:
    spec: dict
    with open(args.spec_path, 'r', encoding='utf-8') as f:
        try:
            spec = json.load(f)
        except json.JSONDecodeError as err:
            error('invalid json in spec file')
            error('details:', err)
            return 1

    characters: dict[str, CharData] | None = spec.get("characters")
    if characters is None:
        error(f'the characters list in {args.spec_path} is empty')
        exit(3)

    img_size = args.cell_size * GRID_SIZE
    
    image = Image.new('RGBA', (img_size, img_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    font: ImageFont.FreeTypeFont
    try:
        font = ImageFont.truetype(str(args.font_path), size=args.font_size)
    except Exception as err:
        error('failed to load font')
        error('details:', err)
        return 1

    for code, data in characters.items():
        if len(code) != 6:
            continue
        
        index = tern2dec(code)
        row, col = cellify(index)

        glyph = get_glyph(data)
        if glyph:
            x = col * args.cell_size
            y = row * args.cell_size

            bbox = draw.textbbox((0, 0), glyph, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]

            offset_x = (args.cell_size - w) // 2
            offset_y = (args.cell_size - h) // 2

            draw.text((x + offset_x, y + offset_y), glyph, font=font, fill=(255, 255, 255, 255))

    image.save(args.out_path)
    return 0

def get_glyph(char_data: CharData):
    if "unicode" in char_data:
        cp_str = char_data["unicode"]
        if cp_str and cp_str != "U+????":
            try:
                cp_val = int(cp_str.replace('U+', ''), 16)
                if cp_val <= 0x20:
                    return chr(0x2400 + cp_val)
                if cp_val == 0x7F:
                    return chr(0x2421) # DEL
                return chr(cp_val)
            except ValueError:
                pass

    mnemonic = char_data.get("mnemonic")
    if mnemonic is not None:
        return "\uFFFD"

    ascii_val = char_data.get("ascii")
    if ascii_val is not None:
        if len(ascii_val) == 1:
            return ascii_val

    raise AssertionError("should've not get here")

def main() -> int:
    ap = argparse.ArgumentParser(description="convert a ttf/otf font to TSCS spritesheet")
    ap.add_argument('font_path',        type=CliArgs.input_file,                       help="font path")
    ap.add_argument('--font-size',      type=int,                 default=10,          help="font size")
    ap.add_argument('--spec-path',      type=CliArgs.input_file,  default="spec.json", help="path to spec.json")
    ap.add_argument('-o', '--out-path', type=CliArgs.output_file, required=True,       help="output file path")
    ap.add_argument('--cell-size',      type=int,                 default=16,          help="single glyph size")

    ap.add_argument(
        '--color',
        choices=['never', 'auto', 'always'],
        default='auto',
        help='use ansi colors?',
    )

    # this is ugly but i cant live without auto complete
    args = typing.cast(CliArgs, ap.parse_args())
    global ansi
    ansi = CliArgs.get_color_mode(args.color)

    return do_the_conversion(args)

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python
import json
import argparse
from pathlib import Path

def code_to_index(code: str) -> int:
    return int(code, 3)

def esc(s):
    if s is None:
        return ""
    return (
        str(s)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
        .replace("\b", "\\b")
    )

def parse_unicode(u_str):
    if not u_str or not u_str.startswith("U+"):
        return None
    try:
        hex_part = u_str[2:]
        if '?' in hex_part:
            return None
        return int(hex_part, 16)
    except ValueError:
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate C character tables from TSCS spec.")
    parser.add_argument("input", help="Input spec.json file")
    parser.add_argument("--out-h", default="characters.h", help="Output header file")
    parser.add_argument("--out-c", default="characters.c", help="Output source file")
    parser.add_argument("--inc-path", help="#include {what???}")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {args.input} not found.")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = []
    ascii_map = [-1] * 128
    unicode_map = []

    for code, info in data["characters"].items():
        idx = code_to_index(code)
        entries.append((idx, info))

        # ASCII mapping
        ascii_char = info.get("ascii")
        if ascii_char and len(ascii_char) == 1:
            ascii_code = ord(ascii_char)
            if 0 <= ascii_code < 128:
                ascii_map[ascii_code] = idx

        # Unicode mapping
        u_str = info.get("unicode")
        u_val = parse_unicode(u_str)
        if u_val is not None:
            unicode_map.append((u_val, idx))

    # Sort unicode_map by unicode codepoint for binary search
    unicode_map.sort()

    max_index = max(idx for idx, _ in entries)
    table_size = max_index + 1

    h_filename = Path(args.out_h).name
    guard = h_filename.replace(".", "_").upper()

    header = f"""\
#ifndef {guard}
#define {guard}

#include <stdint.h>
#include <stddef.h>

#define TSCS_TABLE_SIZE {table_size}

typedef struct {{
    uint32_t index;
    const char* code;
    const char* mnemonic;
    const char* name;
    const char* description;
}} tscs_char;

typedef struct {{
    uint32_t unicode;
    uint32_t index;
}} tscs_unicode_mapping;

extern const tscs_char tscs_table[TSCS_TABLE_SIZE];

/**
 * Direct lookup from ASCII (0-127).
 * Returns -1 if no mapping exists.
 */
extern const int16_t tscs_from_ascii[128];

/**
 * Sorted list of Unicode to TSCS index mappings.
 */
extern const tscs_unicode_mapping tscs_from_unicode[];
extern const size_t tscs_from_unicode_count;

/**
 * Find TSCS index from Unicode codepoint using binary search.
 * Returns -1 if not found.
 */
int32_t tscs_find_unicode(uint32_t unicode);

#endif // {guard}
"""

    source = [
        f'#include {args.inc_path}',
        '#include <stdlib.h>',
        "",
        f"const tscs_char tscs_table[{table_size}] = {{"
    ]

    for idx, info in sorted(entries):
        source.extend([
            f"    [{idx}] = {{",
            f"        .index = {idx},",
            f'        .code = "{esc(info.get("code", ""))}",',
            f'        .mnemonic = "{esc(info.get("mnemonic", ""))}",',
            f'        .name = "{esc(info.get("name", ""))}",',
            f'        .description = "{esc(info.get("description", ""))}"',
            "    },",
        ])

    source.append("};")
    source.append("")

    # ASCII array
    source.append("const int16_t tscs_from_ascii[128] = {")
    for i in range(128):
        source.append(f"    [{i}] = {ascii_map[i]},")
    source.append("};")
    source.append("")

    # Unicode mappings
    source.append(f"const tscs_unicode_mapping tscs_from_unicode[{len(unicode_map)}] = {{")
    for u_val, idx in unicode_map:
        source.append(f"    {{ .unicode = 0x{u_val:04X}, .index = {idx} }},")
    source.append("};")
    source.append("")
    source.append(f"const size_t tscs_from_unicode_count = {len(unicode_map)};")
    source.append("")

    # Helper function using bsearch
    source.append("""
static int compare_unicode(const void* a, const void* b) {
    uint32_t key = *(const uint32_t*)a;
    const tscs_unicode_mapping* map = b;
    if (key < map->unicode) return -1;
    if (key > map->unicode) return 1;
    return 0;
}

int32_t tscs_find_unicode(uint32_t unicode) {
    if (tscs_from_unicode_count == 0) return -1;
    const tscs_unicode_mapping* res = bsearch(
        &unicode,
        tscs_from_unicode,
        tscs_from_unicode_count,
        sizeof(tscs_unicode_mapping),
        compare_unicode
    );
    if (res) return (int32_t)res->index;
    return -1;
}
""")

    Path(args.out_h).write_text(header, encoding="utf-8")
    Path(args.out_c).write_text("\n".join(source), encoding="utf-8")
    print(f"Generated {args.out_h} and {args.out_c} with {len(entries)} entries.")

if __name__ == "__main__":
    main()

# Character Codes

This document defines the mapping between tryte values and characters in the Ternary Standard Character Set (TSCS).

> [!IMPORTANT]
> The specific mapping of numeric values to characters is currently a WIP.

## Control Codes

Control codes occupy the first few positions in the character set. They are used for signaling and text formatting rather than representing graphic symbols.

| Code   | Decimal | Mnemonic | Name             | Description                                       |
|:-------|:--------|:---------|:-----------------|:--------------------------------------------------|
| 000000 | 0       | NUL      | Null             | String terminator or filler.                      |
| 000001 | 1       | BEL      | Bell             | Alert/Notification (audio or visual).             |
| 000002 | 2       | BS       | Backspace        | Move the cursor back one position.                |
| 000010 | 3       | TAB      | Horizontal Tab   | Move the cursor to the next tab stop.             |
| 000011 | 4       | EOL      | End of line      | Move the cursor to the next line.                 |
| 000012 | 5       | CR       | Carriage Return  | Move the cursor to the start of the current line. |
| 000020 | 6       | ESC      | Escape           | Start of an escape or control sequence.           |
| 000021 | 7       | DEL      | Delete           | Remove the character at or before the cursor.     |
| 000022 | 8       | EOF      | End of File      | Explicit marker for the end of a file or stream.  |
| 000100 | 9       | RS       | Record Separator | Used to separate records in a data stream.        |
| 000101 | 10      | US       | Unit Separator   | Used to separate units within a record.           |

> [!NOTE]
> All codes from 000102 to 000222 are reserved for new control codes and other future extensions

## Graphic Characters

### Letters (Latain)
| Code   | Decimal | Name                   |
|:-------|:--------|:-----------------------|
| 001000 | 27      | Latin Small Letter a   |
| 001001 | 28      | Latin Small Letter b   |
| 001002 | 29      | Latin Small Letter c   |
| 001010 | 30      | Latin Small Letter d   |
| 001011 | 31      | Latin Small Letter e   |
| 001012 | 32      | Latin Small Letter f   |
| 001020 | 33      | Latin Small Letter g   |
| 001021 | 34      | Latin Small Letter h   |
| 001022 | 35      | Latin Small Letter i   |
| 001100 | 36      | Latin Small Letter j   |
| 001101 | 37      | Latin Small Letter k   |
| 001102 | 38      | Latin Small Letter l   |
| 001110 | 39      | Latin Small Letter m   |
| 001111 | 40      | Latin Small Letter n   |
| 001112 | 41      | Latin Small Letter o   |
| 001120 | 42      | Latin Small Letter p   |
| 001121 | 43      | Latin Small Letter q   |
| 001122 | 44      | Latin Small Letter r   |
| 001200 | 45      | Latin Small Letter s   |
| 001201 | 46      | Latin Small Letter t   |
| 001202 | 47      | Latin Small Letter u   |
| 001210 | 48      | Latin Small Letter v   |
| 001211 | 49      | Latin Small Letter w   |
| 001212 | 50      | Latin Small Letter x   |
| 001220 | 51      | Latin Small Letter y   |
| 001221 | 52      | Latin Small Letter z   |
| 001222 | 53      | Latin Capital Letter A |
| 002000 | 54      | Latin Capital Letter B |
| 002001 | 55      | Latin Capital Letter C |
| 002002 | 56      | Latin Capital Letter D |
| 002010 | 57      | Latin Capital Letter E |
| 002011 | 58      | Latin Capital Letter F |
| 002012 | 59      | Latin Capital Letter G |
| 002020 | 60      | Latin Capital Letter H |
| 002021 | 61      | Latin Capital Letter I |
| 002022 | 62      | Latin Capital Letter J |
| 002100 | 63      | Latin Capital Letter K |
| 002101 | 64      | Latin Capital Letter L |
| 002102 | 65      | Latin Capital Letter M |
| 002110 | 66      | Latin Capital Letter N |
| 002111 | 67      | Latin Capital Letter O |
| 002112 | 68      | Latin Capital Letter P |
| 002120 | 69      | Latin Capital Letter Q |
| 002121 | 70      | Latin Capital Letter R |
| 002122 | 71      | Latin Capital Letter S |
| 002200 | 72      | Latin Capital Letter T |
| 002201 | 73      | Latin Capital Letter U |
| 002202 | 74      | Latin Capital Letter V |
| 002210 | 75      | Latin Capital Letter W |
| 002211 | 76      | Latin Capital Letter X |
| 002212 | 77      | Latin Capital Letter Y |
| 002220 | 78      | Latin Capital Letter Z |

### Digits
| Code   | Decimal | Name            |
|:-------|:--------|:----------------|
| 002221 | 79      | Digit Zero (0)  |
| 002222 | 80      | Digit One (1)   |
| 010000 | 81      | Digit Two (2)   |
| 010001 | 82      | Digit Three (3) |
| 010002 | 83      | Digit Four (4)  |
| 010010 | 84      | Digit Five (5)  |
| 010011 | 85      | Digit Six (6)   |
| 010012 | 86      | Digit Seven (7) |
| 010020 | 87      | Digit Eight (8) |
| 010021 | 88      | Digit Nine (9)  |

### Symbols 
| Code   | Decimal | Name                 |
|:-------|:--------|:---------------------|
| 010022 | 89      | Space                |
| 010100 | 90      | Exclamation Mark     |
| 010101 | 91      | Quotation Mark       |
| 010102 | 92      | Number Sign          |
| 010110 | 93      | Dollar Sign          |
| 010111 | 94      | Percent Sign         |
| 010112 | 95      | Ampersand            |
| 010120 | 96      | Apostrophe           |
| 010121 | 97      | Left Parenthesis     |
| 010122 | 98      | Right Parenthesis    |
| 010200 | 99      | Asterisk             |
| 010201 | 100     | Plus Sign            |
| 010202 | 101     | Comma                |
| 010210 | 102     | Hyphen-Minus         |
| 010211 | 103     | Full Stop            |
| 010212 | 104     | Solidus (Slash)      |
| 010220 | 105     | Colon                |
| 010221 | 106     | Semicolon            |
| 010222 | 107     | Less-Than Sign       |
| 011000 | 108     | Equals Sign          |
| 011001 | 109     | Greater-Than Sign    |
| 011002 | 110     | Question Mark        |
| 011010 | 111     | Commercial At        |
| 011011 | 112     | Left Square Bracket  |
| 011012 | 113     | Reverse Solidus      |
| 011020 | 114     | Right Square Bracket |
| 011021 | 115     | Circumflex Accent    |
| 011022 | 116     | Low Line             |
| 011100 | 117     | Grave Accent         |
| 011101 | 118     | Left Curly Bracket   |
| 011102 | 119     | Vertical Line        |
| 011110 | 120     | Right Curly Bracket  |
| 011111 | 121     | Tilde                |
| 011112 | 122     | Rightwards Arrow     |
| 011120 | 123     | Leftwards Arrow      |
| 011121 | 124     | Upwards Arrow        |
| 011122 | 125     | Downwards Arrow      |
| 011200 | 126     | Bullet               |
| 011201 | 127     | Degree Sign          |
| 011202 | 128     | Plus-Minus Sign      |
| 011210 | 129     | Not Equal To         |

### Math Symbols
| Code   | Decimal | Name                     |
|:-------|:--------|:-------------------------|
| 011211 | 130     | Multiplication Sign      |
| 011212 | 131     | Division Sign            |
| 011220 | 132     | Less-Than or Equal To    |
| 011221 | 133     | Greater-Than or Equal To |
| 011222 | 134     | Approximately Equal To   |
| 012000 | 135     | Identical To             |
| 012001 | 136     | Square Root              |
| 012002 | 137     | Infinity                 |
| 012010 | 138     | Integral                 |
| 012011 | 139     | Partial Differential     |
| 012012 | 140     | N-ary Summation          |
| 012020 | 141     | N-ary Product            |
| 012021 | 142     | Increment                |
| 012022 | 143     | Greek Small Letter Pi    |
| 012100 | 144     | Logical AND              |
| 012101 | 145     | Logical OR               |
| 012102 | 146     | Logical NOT              |
| 012110 | 147     | For All                  |
| 012111 | 148     | There Exists             |
| 012112 | 149     | Empty Set                |
| 012120 | 150     | Element Of               |
| 012121 | 151     | Not An Element Of        |
| 012122 | 152     | Intersection             |
| 012200 | 153     | Union                    |
| 012201 | 154     | Subset Of                |
| 012202 | 155     | Subset Of Or Equal To    |
| 012210 | 156     | Therefore                |
| 012211 | 157     | Because                  |
| 012212 | 158     | Proportional To          |
| 012220 | 159     | Much Less-Than           |
| 012221 | 160     | Much Greater-Than        |

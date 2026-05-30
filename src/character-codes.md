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

## Graphic Characters

<!-- TODO: Define graphic character mapping --> 

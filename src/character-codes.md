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

### Latin Letters
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

### Extended Latin
| Code   | Decimal | Name                                        |
|:-------|:--------|:--------------------------------------------|
| 002221 | 79      | Latin Capital Letter A with grave           |
| 002222 | 80      | Latin Capital Letter A with acute           |
| 010000 | 81      | Latin Capital Letter A with circumflex      |
| 010001 | 82      | Latin Capital Letter A with tilde           |
| 010002 | 83      | Latin Capital Letter A with diaeresis       |
| 010010 | 84      | Latin Capital Letter A with ring above      |
| 010011 | 85      | Latin Capital Letter AE                     |
| 010012 | 86      | Latin Capital Letter C with cedilla         |
| 010020 | 87      | Latin Capital Letter E with grave           |
| 010021 | 88      | Latin Capital Letter E with acute           |
| 010022 | 89      | Latin Capital Letter E with circumflex      |
| 010100 | 90      | Latin Capital Letter E with diaeresis       |
| 010101 | 91      | Latin Capital Letter I with grave           |
| 010102 | 92      | Latin Capital Letter I with acute           |
| 010110 | 93      | Latin Capital Letter I with circumflex      |
| 010111 | 94      | Latin Capital Letter I with diaeresis       |
| 010112 | 95      | Latin Capital Letter ETH                    |
| 010120 | 96      | Latin Capital Letter N with tilde           |
| 010121 | 97      | Latin Capital Letter O with grave           |
| 010122 | 98      | Latin Capital Letter O with acute           |
| 010200 | 99      | Latin Capital Letter O with circumflex      |
| 010201 | 100     | Latin Capital Letter O with tilde           |
| 010202 | 101     | Latin Capital Letter O with diaeresis       |
| 010210 | 102     | Latin Capital Letter O with stroke          |
| 010211 | 103     | Latin Capital Letter U with grave           |
| 010212 | 104     | Latin Capital Letter U with acute           |
| 010220 | 105     | Latin Capital Letter U with circumflex      |
| 010221 | 106     | Latin Capital Letter U with diaeresis       |
| 010222 | 107     | Latin Capital Letter Y with acute           |
| 011000 | 108     | Latin Capital Letter Thorn                  |
| 011001 | 109     | Latin Small Letter Sharp S                  |
| 011002 | 110     | Latin Small Letter a with grave             |
| 011010 | 111     | Latin Small Letter a with acute             |
| 011011 | 112     | Latin Small Letter a with circumflex        |
| 011012 | 113     | Latin Small Letter a with tilde             |
| 011020 | 114     | Latin Small Letter a with diaeresis         |
| 011021 | 115     | Latin Small Letter a with ring above        |
| 011022 | 116     | Latin Small Letter ae                       |
| 011100 | 117     | Latin Small Letter c with cedilla           |
| 011101 | 118     | Latin Small Letter e with grave             |
| 011102 | 119     | Latin Small Letter e with acute             |
| 011110 | 120     | Latin Small Letter e with circumflex        |
| 011111 | 121     | Latin Small Letter e with diaeresis         |
| 011112 | 122     | Latin Small Letter i with grave             |
| 011120 | 123     | Latin Small Letter i with acute             |
| 011121 | 124     | Latin Small Letter i with circumflex        |
| 011122 | 125     | Latin Small Letter i with diaeresis         |
| 011200 | 126     | Latin Small Letter eth                      |
| 011201 | 127     | Latin Small Letter n with tilde             |
| 011202 | 128     | Latin Small Letter o with grave             |
| 011210 | 129     | Latin Small Letter o with acute             |
| 011211 | 130     | Latin Small Letter o with circumflex        |
| 011212 | 131     | Latin Small Letter o with tilde             |
| 011220 | 132     | Latin Small Letter o with diaeresis         |
| 011221 | 133     | Latin Small Letter o with stroke            |
| 011222 | 134     | Latin Small Letter u with grave             |
| 012000 | 135     | Latin Small Letter u with acute             |
| 012001 | 136     | Latin Small Letter u with circumflex        |
| 012002 | 137     | Latin Small Letter u with diaeresis         |
| 012010 | 138     | Latin Small Letter y with acute             |
| 012011 | 139     | Latin Small Letter thorn                    |
| 012012 | 140     | Latin Small Letter y with diaeresis         |
| 012020 | 141     | Latin Capital Letter A with macron          |
| 012021 | 142     | Latin Small Letter a with macron            |
| 012022 | 143     | Latin Capital Letter A with breve           |
| 012100 | 144     | Latin Small Letter a with breve             |
| 012101 | 145     | Latin Capital Letter A with ogonek          |
| 012102 | 146     | Latin Small Letter a with ogonek            |
| 012110 | 147     | Latin Capital Letter C with acute           |
| 012111 | 148     | Latin Small Letter c with acute             |
| 012112 | 149     | Latin Capital Letter C with circumflex      |
| 012120 | 150     | Latin Small Letter c with circumflex        |
| 012121 | 151     | Latin Capital Letter C with dot above       |
| 012122 | 152     | Latin Small Letter c with dot above         |
| 012200 | 153     | Latin Capital Letter C with caron           |
| 012201 | 154     | Latin Small Letter c with caron             |
| 012202 | 155     | Latin Capital Letter D with caron           |
| 012210 | 156     | Latin Small Letter d with caron             |
| 012211 | 157     | Latin Capital Letter D with stroke          |
| 012212 | 158     | Latin Small Letter d with stroke            |
| 012220 | 159     | Latin Capital Letter E with macron          |
| 012221 | 160     | Latin Small Letter e with macron            |
| 012222 | 161     | Latin Capital Letter E with breve           |
| 020000 | 162     | Latin Small Letter e with breve             |
| 020001 | 163     | Latin Capital Letter E with dot above       |
| 020002 | 164     | Latin Small Letter e with dot above         |
| 020010 | 165     | Latin Capital Letter E with ogonek          |
| 020011 | 166     | Latin Small Letter e with ogonek            |
| 020012 | 167     | Latin Capital Letter E with caron           |
| 020020 | 168     | Latin Small Letter e with caron             |
| 020021 | 169     | Latin Capital Letter G with circumflex      |
| 020022 | 170     | Latin Small Letter g with circumflex        |
| 020100 | 171     | Latin Capital Letter G with breve           |
| 020101 | 172     | Latin Small Letter g with breve             |
| 020102 | 173     | Latin Capital Letter G with dot above       |
| 020110 | 174     | Latin Small Letter g with dot above         |
| 020111 | 175     | Latin Capital Letter G with cedilla         |
| 020112 | 176     | Latin Small Letter g with cedilla           |
| 020120 | 177     | Latin Capital Letter H with circumflex      |
| 020121 | 178     | Latin Small Letter h with circumflex        |
| 020122 | 179     | Latin Capital Letter H with stroke          |
| 020200 | 180     | Latin Small Letter h with stroke            |
| 020201 | 181     | Latin Capital Letter I with tilde           |
| 020202 | 182     | Latin Small Letter i with tilde             |
| 020210 | 183     | Latin Capital Letter I with macron          |
| 020211 | 184     | Latin Small Letter i with macron            |
| 020212 | 185     | Latin Capital Letter I with breve           |
| 020220 | 186     | Latin Small Letter i with breve             |
| 020221 | 187     | Latin Capital Letter I with ogonek          |
| 020222 | 188     | Latin Small Letter i with ogonek            |
| 021000 | 189     | Latin Capital Letter I with dot above       |
| 021001 | 190     | Latin Small Letter dotless i                |
| 021002 | 191     | Latin Capital Ligature IJ                   |
| 021010 | 192     | Latin Small Ligature ij                     |
| 021011 | 193     | Latin Capital Letter J with circumflex      |
| 021012 | 194     | Latin Small Letter j with circumflex        |
| 021020 | 195     | Latin Capital Letter K with cedilla         |
| 021021 | 196     | Latin Small Letter k with cedilla           |
| 021022 | 197     | Latin Small Letter kra                      |
| 021100 | 198     | Latin Capital Letter L with acute           |
| 021101 | 199     | Latin Small Letter l with acute             |
| 021102 | 200     | Latin Capital Letter L with cedilla         |
| 021110 | 201     | Latin Small Letter l with cedilla           |
| 021111 | 202     | Latin Capital Letter L with caron           |
| 021112 | 203     | Latin Small Letter l with caron             |
| 021120 | 204     | Latin Capital Letter L with middle dot      |
| 021121 | 205     | Latin Small Letter l with middle dot        |
| 021122 | 206     | Latin Capital Letter L with stroke          |
| 021200 | 207     | Latin Small Letter l with stroke            |
| 021201 | 208     | Latin Capital Letter N with acute           |
| 021202 | 209     | Latin Small Letter n with acute             |
| 021210 | 210     | Latin Capital Letter N with cedilla         |
| 021211 | 211     | Latin Small Letter n with cedilla           |
| 021212 | 212     | Latin Capital Letter N with caron           |
| 021220 | 213     | Latin Small Letter n with caron             |
| 021221 | 214     | Latin Small Letter n preceded by apostrophe |
| 021222 | 215     | Latin Capital Letter ENG                    |
| 022000 | 216     | Latin Small Letter eng                      |
| 022001 | 217     | Latin Capital Letter O with macron          |
| 022002 | 218     | Latin Small Letter o with macron            |
| 022010 | 219     | Latin Capital Letter O with breve           |
| 022011 | 220     | Latin Small Letter o with breve             |
| 022012 | 221     | Latin Capital Letter O with double acute    |
| 022020 | 222     | Latin Small Letter o with double acute      |
| 022021 | 223     | Latin Capital Ligature OE                   |
| 022022 | 224     | Latin Small Ligature OE                     |
| 022100 | 225     | Latin Capital Letter R with acute           |
| 022101 | 226     | Latin Small Letter r with acute             |
| 022102 | 227     | Latin Capital Letter R with cedilla         |
| 022110 | 228     | Latin Small Letter r with cedilla           |
| 022111 | 229     | Latin Capital Letter R with caron           |
| 022112 | 230     | Latin Small Letter r with caron             |
| 022120 | 231     | Latin Capital Letter S with acute           |
| 022121 | 232     | Latin Small Letter s with acute             |
| 022122 | 233     | Latin Capital Letter S with circumflex      |
| 022200 | 234     | Latin Small Letter s with circumflex        |
| 022201 | 235     | Latin Capital Letter S with cedilla         |
| 022202 | 236     | Latin Small Letter s with cedilla           |
| 022210 | 237     | Latin Capital Letter S with caron           |
| 022211 | 238     | Latin Small Letter s with caron             |
| 022212 | 239     | Latin Capital Letter T with cedilla         |
| 022220 | 240     | Latin Small Letter t with cedilla           |
| 022221 | 241     | Latin Capital Letter T with caron           |
| 022222 | 242     | Latin Small Letter t with caron             |
| 100000 | 243     | Latin Capital Letter T with stroke          |
| 100001 | 244     | Latin Small Letter t with stroke            |
| 100002 | 245     | Latin Capital Letter U with tilde           |
| 100010 | 246     | Latin Small Letter u with tilde             |
| 100011 | 247     | Latin Capital Letter U with macron          |
| 100012 | 248     | Latin Small Letter u with macron            |
| 100020 | 249     | Latin Capital Letter U with breve           |
| 100021 | 250     | Latin Small Letter u with breve             |
| 100022 | 251     | Latin Capital Letter U with ring above      |
| 100100 | 252     | Latin Small Letter u with ring above        |
| 100101 | 253     | Latin Capital Letter U with double acute    |
| 100102 | 254     | Latin Small Letter u with double acute      |
| 100110 | 255     | Latin Capital Letter U with ogonek          |
| 100111 | 256     | Latin Small Letter u with ogonek            |
| 100112 | 257     | Latin Capital Letter W with circumflex      |
| 100120 | 258     | Latin Small Letter w with circumflex        |
| 100121 | 259     | Latin Capital Letter Y with circumflex      |
| 100122 | 260     | Latin Small Letter y with circumflex        |
| 100200 | 261     | Latin Capital Letter Y with diaeresis       |
| 100201 | 262     | Latin Capital Letter Z with acute           |
| 100202 | 263     | Latin Small Letter z with acute             |
| 100210 | 264     | Latin Capital Letter Z with dot above       |
| 100211 | 265     | Latin Small Letter z with dot above         |
| 100212 | 266     | Latin Capital Letter Z with caron           |
| 100220 | 267     | Latin Small Letter z with caron             |
| 100221 | 268     | Latin Small Letter Long S                   |

### Digits
| Code   | Decimal | Name            |
|:-------|:--------|:----------------|
| 100222 | 269     | Digit Zero (0)  |
| 101000 | 270     | Digit One (1)   |
| 101001 | 271     | Digit Two (2)   |
| 101002 | 272     | Digit Three (3) |
| 101010 | 273     | Digit Four (4)  |
| 101011 | 274     | Digit Five (5)  |
| 101012 | 275     | Digit Six (6)   |
| 101020 | 276     | Digit Seven (7) |
| 101021 | 277     | Digit Eight (8) |
| 101022 | 278     | Digit Nine (9)  |

### Symbols 
| Code   | Decimal | Name                 |
|:-------|:--------|:---------------------|
| 101100 | 279     | Space                |
| 101101 | 280     | Exclamation Mark     |
| 101102 | 281     | Quotation Mark       |
| 101110 | 282     | Number Sign          |
| 101111 | 283     | Dollar Sign          |
| 101112 | 284     | Percent Sign         |
| 101120 | 285     | Ampersand            |
| 101121 | 286     | Apostrophe           |
| 101122 | 287     | Left Parenthesis     |
| 101200 | 288     | Right Parenthesis    |
| 101201 | 289     | Asterisk             |
| 101202 | 290     | Plus Sign            |
| 101210 | 291     | Comma                |
| 101211 | 292     | Hyphen-Minus         |
| 101212 | 293     | Full Stop            |
| 101220 | 294     | Solidus (Slash)      |
| 101221 | 295     | Colon                |
| 101222 | 296     | Semicolon            |
| 102000 | 297     | Less-Than Sign       |
| 102001 | 298     | Equals Sign          |
| 102002 | 299     | Greater-Than Sign    |
| 102010 | 300     | Question Mark        |
| 102011 | 301     | Commercial At        |
| 102012 | 302     | Left Square Bracket  |
| 102020 | 303     | Reverse Solidus      |
| 102021 | 304     | Right Square Bracket |
| 102022 | 305     | Circumflex Accent    |
| 102100 | 306     | Low Line             |
| 102101 | 307     | Grave Accent         |
| 102102 | 308     | Left Curly Bracket   |
| 102110 | 309     | Vertical Line        |
| 102111 | 310     | Right Curly Bracket  |
| 102112 | 311     | Tilde                |
| 102120 | 312     | Rightwards Arrow     |
| 102121 | 313     | Leftwards Arrow      |
| 102122 | 314     | Upwards Arrow        |
| 102200 | 315     | Downwards Arrow      |
| 102201 | 316     | Bullet               |
| 102202 | 317     | Degree Sign          |
| 102210 | 318     | Plus-Minus Sign      |
| 102211 | 319     | Not Equal To         |

### Math Symbols
| Code   | Decimal | Name                     |
|:-------|:--------|:-------------------------|
| 102212 | 320     | Multiplication Sign      |
| 102220 | 321     | Division Sign            |
| 102221 | 322     | Less-Than or Equal To    |
| 102222 | 323     | Greater-Than or Equal To |
| 110000 | 324     | Approximately Equal To   |
| 110001 | 325     | Identical To             |
| 110002 | 326     | Square Root              |
| 110010 | 327     | Infinity                 |
| 110011 | 328     | Integral                 |
| 110012 | 329     | Partial Differential     |
| 110020 | 330     | N-ary Summation          |
| 110021 | 331     | N-ary Product            |
| 110022 | 332     | Increment                |
| 110100 | 333     | Greek Small Letter Pi    |
| 110101 | 334     | Logical AND              |
| 110102 | 335     | Logical OR               |
| 110110 | 336     | Logical NOT              |
| 110111 | 337     | For All                  |
| 110112 | 338     | There Exists             |
| 110120 | 339     | Empty Set                |
| 110121 | 340     | Element Of               |
| 110122 | 341     | Not An Element Of        |
| 110200 | 342     | Intersection             |
| 110201 | 343     | Union                    |
| 110202 | 344     | Subset Of                |
| 110210 | 345     | Subset Of Or Equal To    |
| 110211 | 346     | Therefore                |
| 110212 | 347     | Because                  |
| 110220 | 348     | Proportional To          |
| 110221 | 349     | Much Less-Than           |
| 110222 | 350     | Much Greater-Than        |

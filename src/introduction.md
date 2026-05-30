# TSCS (Ternary Standard Character Set)

The Ternary Standard Character Set (TSCS) is a character encoding designed for ternary computing systems.
It provides a mapping between numeric values (represented as trytes) and human-readable characters.

TSCS is designed mainly for the TC-48 architecture and TVA (TC-48 Video Array) standard.

## Encoding Scheme
TSCS represents each character as a single **tryte**. 

In the context of TSCS or TC-48 in general, a tryte is defined as a sequence of **6 trits**.

### Capacity
Since each trit can have one of three values \\(\\{0, 1, 2\\}\\),
a 6-trit tryte can represent \\(3^6 = 729\\) unique character codes.

It is important to note that not all 729 character codes are assigned to a specific character.
Some of them are reserved for control codes, future expansion, or left unassigned.

## Document Scope
This document specifies the encoding format and mapping for the Ternary Standard Character Set (TSCS).
Its purpose is to ensure interoperability between software and hardware components within the TC-48 ecosystem.

The scope of this document includes:

- **Encoding definition:** The structure and capacity of the TSCS tryte.
- **Character mapping:** The defined relationships between tryte values and specific glyphs or control functions.

## Character Set Mapping
All character codes are listed in the [Character Codes](./character-codes.md) chapter.

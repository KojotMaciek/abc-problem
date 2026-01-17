You are given a collection of ABC blocks (maybe like the ones you had when you were a kid).
There are twenty blocks with two letters on each block.
A complete alphabet is guaranteed amongst all sides of the blocks.
The sample collection of blocks:

 (B O)
 (X K)
 (D Q)
 (C P)
 (N A)
 (G T)
 (R E)
 (T G)
 (Q D)
 (F S)
 (J W)
 (H U)
 (V I)
 (A N)
 (O B)
 (E R)
 (F S)
 (L Y)
 (P C)
 (Z M)

Task
Write a function that takes a string (word) and determines whether the word can be spelled with the given collection of blocks.
The rules are simple:
   1. Once a letter on a block is used that block cannot be used again
   2. The function should be case-insensitive
   3. Show the output on this page for the following 7 words in the following example

Example

>>> can_make_word("A")
True
can_make_word("BARK")
True
can_make_word("BOOK")
False
can_make_word("TREAT")
True
can_make_word("COMMON")
False
can_make_word("SQUAD")
True
can_make_word("CONFUSE")
True

[Source https://rosettacode.org/wiki/ABC_Problem]

## Solution

The solution is implemented in `abc_problem.py` with the following structure:

### Functions
- **`load_blocks(filename)`**: Reads block pairs from a file and returns a list of tuples.
- **`can_make_word(blocks, word)`**: Determines if a word can be formed using the given blocks.

### Key Implementation Details
- Each block can only be used once per word
- The function is case-insensitive
- Uses a set to efficiently track which blocks have been used

### Testing

Comprehensive unit tests are included in `tests/test_abc_problem.py`. All 7 test cases pass:

```
✓ test_can_make_word_A: True
✓ test_can_make_word_BARK: True
✓ test_can_make_word_BOOK: False
✓ test_can_make_word_TREAT: True
✓ test_can_make_word_COMMON: False
✓ test_can_make_word_SQUAD: True
✓ test_can_make_word_CONFUSE: True
```

Run tests with: `pytest tests/test_abc_problem.py -v`
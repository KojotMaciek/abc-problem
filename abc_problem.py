def load_blocks(filename) -> list:
    """
    Load block pairs from a file.

    Each line in the file should be in the format (A B), where A and B are letters.
    Returns a list of tuples, e.g., [('A', 'B'), ...]
    """
    blocks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('(') and line.endswith(')'):
                    content = line[1:-1].strip()
                    parts = content.split()
                    if len(parts) == 2 and all(part.isalpha() and len(part) == 1 for part in parts):
                        blocks.append((parts[0].upper(), parts[1].upper()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    return blocks

def can_make_word(blocks, word) -> bool:
    """
    Check if a word can be formed using the given blocks.

    Each block can be used at most once, and each letter in the word must be
    present on one of the blocks.

    Args:
        blocks: List of tuples, each tuple containing two letters (e.g., [('A', 'B'), ...])
        word: String to check

    Returns:
        bool: True if the word can be formed, False otherwise
    """
    word = word.upper()
    used_blocks = set()

    for letter in word:
        if not letter.isalpha():
            return False  # Invalid character
        found_block = False
        for i, block in enumerate(blocks):
            if i not in used_blocks and letter in block:
                used_blocks.add(i)
                found_block = True
                break
        if not found_block:
            return False
    return True

if __name__ == "__main__":
    blocks = load_blocks('blocks.txt')
    if not blocks:
        print("No blocks loaded. Exiting.")
        exit(1)

    test_word = "BOOK"
    if can_make_word(blocks, test_word):
        print(f"Yes, '{test_word}' can be made with the blocks.")
    else:
        print(f"No, '{test_word}' cannot be made with the blocks.")

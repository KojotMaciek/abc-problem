import unittest

from abc_problem import load_blocks, can_make_word

class TestABCProblem(unittest.TestCase):
    def setUp(self):
        # Load blocks from blocks.txt for all tests
        self.blocks = load_blocks('blocks.txt')
        self.assertIsNotNone(self.blocks)
        self.assertGreater(len(self.blocks), 0)

    def test_can_make_word_A(self):
        self.assertTrue(can_make_word(self.blocks, "A"))

    def test_can_make_word_BARK(self):
        self.assertTrue(can_make_word(self.blocks, "BARK"))

    def test_can_make_word_BOOK(self):
        self.assertFalse(can_make_word(self.blocks, "BOOK"))

    def test_can_make_word_TREAT(self):
        self.assertTrue(can_make_word(self.blocks, "TREAT"))

    def test_can_make_word_COMMON(self):
        self.assertFalse(can_make_word(self.blocks, "COMMON"))

    def test_can_make_word_SQUAD(self):
        self.assertTrue(can_make_word(self.blocks, "SQUAD"))

    def test_can_make_word_CONFUSE(self):
        self.assertTrue(can_make_word(self.blocks, "CONFUSE"))

if __name__ == '__main__':
    unittest.main()

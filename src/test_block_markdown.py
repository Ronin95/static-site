import unittest
# Import the function to be tested
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        # Test case from the prompt
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks,
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        # My test for handling extra blank lines
        md = """

First block

\n\n\n
Second block

"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "First block",
                "Second block",
            ],
            blocks,
        )

    def test_markdown_to_blocks_no_breaks(self):
        # My test for a single block
        md = "This is all one block."
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "This is all one block.",
            ],
            blocks,
        )

    def test_markdown_to_blocks_leading_trailing(self):
        # My test for leading/trailing whitespace
        md = "   \n\n   Block 1   \n\n   Block 2   \n\n   "
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "Block 1",
                "Block 2",
            ],
            blocks,
        )

if __name__ == "__main__":
    unittest.main()
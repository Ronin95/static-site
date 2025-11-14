import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

class TestBlockMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        # The multiline string is now flush with the left margin
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
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
        md = "\n\nFirst block\n\n\n\nSecond block\n\n"
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "First block",
                "Second block",
            ],
            blocks,
        )

    def test_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### Too many"), BlockType.PARAGRAPH)

    def test_block_type_code(self):
        block = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block_no_end = "```\ncode"
        self.assertEqual(block_to_block_type(block_no_end), BlockType.PARAGRAPH)

    def test_block_type_quote(self):
        block = "> line 1\n> line 2\n> line 3"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block_mixed = "> line 1\nnot a quote"
        self.assertEqual(block_to_block_type(block_mixed), BlockType.PARAGRAPH)

    def test_block_type_ulist(self):
        block_minus = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block_minus), BlockType.UNORDERED_LIST)
        block_star = "* item 1\n* item 2"
        self.assertEqual(block_to_block_type(block_star), BlockType.UNORDERED_LIST)
        block_mixed = "- item 1\n* item 2"
        self.assertEqual(block_to_block_type(block_mixed), BlockType.PARAGRAPH)

    def test_block_type_olist(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block_wrong_order = "1. first\n3. third"
        self.assertEqual(block_to_block_type(block_wrong_order), BlockType.PARAGRAPH)
        block_no_space = "1.first\n2.second"
        self.assertEqual(block_to_block_type(block_no_space), BlockType.PARAGRAPH)

    def test_block_type_paragraph(self):
        block = "This is a normal paragraph.\nIt can span multiple lines."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
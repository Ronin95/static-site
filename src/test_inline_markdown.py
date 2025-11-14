import unittest
# Import the function to be tested
from inline_markdown import split_nodes_delimiter
# Import TextNode and TextType to create test data
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    
    def test_split_code(self):
        """
        Tests splitting a node with a single code block.
        """
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_bold(self):
        """
        Tests splitting a node with a single bold block.
        """
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_italic(self):
        """
        Tests splitting a node with a single italic block.
        """
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_multiple_delimiters(self):
        """
        Tests splitting a node with multiple delimiters of the same type.
        """
        node = TextNode("This `is` multiple `code` blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.CODE),
            TextNode(" multiple ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" blocks", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_at_start_and_end(self):
        """
        Tests splitting when the delimited text is at the start and end.
        """
        node = TextNode("**Start** middle **End**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Start", TextType.BOLD),
            TextNode(" middle ", TextType.TEXT),
            TextNode("End", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_non_text_node(self):
        """
        Tests that a non-TEXT node is passed through unchanged.
        """
        node = TextNode("This is already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("This is already bold", TextType.BOLD)]
        self.assertEqual(new_nodes, expected)

    def test_invalid_markdown_raises_error(self):
        """
        Tests that an unclosed delimiter raises an Exception.
        """
        node = TextNode("This is `invalid code", TextType.TEXT)
        # Use assertRaises to confirm that the correct exception is thrown
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
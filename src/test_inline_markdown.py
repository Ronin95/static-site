import unittest
# Import all functions to be tested
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_invalid_markdown_raises_error(self):
        node = TextNode("This is `invalid code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_extract_markdown_images(self):
        # Test from prompt
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        # Test with multiple images
        text = "This is text with ![image1](url1) and ![image2](url2)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image1", "url1"), ("image2", "url2")], matches)

    def test_extract_markdown_links(self):
        # Test from prompt
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    def test_extract_links_and_images(self):
        # Test with mixed links and images
        text = "This is text with an ![image](img.png) and a [link](link.url)"
        
        # Test images
        images = extract_markdown_images(text)
        self.assertListEqual([("image", "img.png")], images)
        
        # Test links
        links = extract_markdown_links(text)
        self.assertListEqual([("link", "link.url")], links)


if __name__ == "__main__":
    unittest.main()
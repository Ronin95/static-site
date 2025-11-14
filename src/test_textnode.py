import unittest
# Use a relative import to get the classes from textnode.py
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # This is the test you provided
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # Test for inequality when text_type is different
    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    # Test for inequality when text is different
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a DIFFERENT node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # Test for inequality when one URL is None
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    # Test for equality when URLs are the same
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "httpss://boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, "httpss://boot.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
import unittest
# Use an absolute import since 'src' is in the test path
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_basic(self):
        """
        Tests formatting a dictionary with multiple attributes.
        """
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        """
        Tests that an empty props dictionary returns an empty string.
        """
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        """
        Tests that props=None returns an empty string.
        """
        node = HTMLNode() # props defaults to None
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        """
        Tests a single attribute.
        """
        props = {"class": "my-class"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' class="my-class"')

    def test_repr_method(self):
        """
        Tests the __repr__ method for accurate debug output.
        """
        children = [HTMLNode("b", "child")]
        props = {"href": "https://boot.dev"}
        node = HTMLNode("a", "parent", children, props)
        expected = "HTMLNode(a, parent, [HTMLNode(b, child, None, None)], {'href': 'https://boot.dev'})"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
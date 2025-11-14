import unittest
# Import both classes from the htmlnode module
from htmlnode import HTMLNode, LeafNode

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

    def test_leaf_to_html_p(self):
        # The test provided in the prompt
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        # Test with attributes (props)
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        # Test with no tag (raw text)
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_leaf_value_error(self):
        # Test for ValueError when value is None
        node = LeafNode("p", None)
        # Use assertRaises to check if the correct exception is raised
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https..."})
        self.assertEqual(repr(node), "LeafNode(a, Click me!, {'href': 'https...'})")


if __name__ == "__main__":
    unittest.main()
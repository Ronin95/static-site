import unittest
# Import all three classes from the htmlnode module
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_basic(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_leaf_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https..."})
        self.assertEqual(repr(node), "LeafNode(a, Click me!, {'href': 'https...'})")

    def test_to_html_with_children(self):
        # Test from prompt
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        # Test from prompt
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_multiple_children(self):
        # My test with multiple children
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i></p>")

    def test_parent_to_html_with_props(self):
        # My test with props on the parent
        children = [LeafNode("span", "child")]
        parent_node = ParentNode("div", children, {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_parent_no_tag(self):
        # Test for ValueError if tag is missing
        node = ParentNode(None, [LeafNode("b", "bold")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_children(self):
        # Test for ValueError if children are missing
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
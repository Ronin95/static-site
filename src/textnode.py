from enum import Enum
# Import LeafNode from htmlnode
from htmlnode import LeafNode

# Define all the text node types
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        # The text content of the node
        self.text = text
        # The type of text (e.g., TEXT, BOLD, LINK)
        self.text_type = text_type
        # The URL for link or image nodes, default to None
        self.url = url

    def __eq__(self, other):
        """
        Checks if two TextNode objects are equal.
        """
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        """
        Provides a string representation of the TextNode object.
        """
        # Uses .value to get the string from the TextType enum
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    """
    Converts a TextNode object into a LeafNode (HTMLNode) object.
    """
    if text_node.text_type == TextType.TEXT:
        # Raw text, no tag
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
        
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
        
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
        
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Invalid TextNode: LINK type requires a URL")
        # Text is the anchor text, URL is the href
        return LeafNode("a", text_node.text, {"href": text_node.url})
        
    if text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Invalid TextNode: IMAGE type requires a URL")
        # Value is empty string, text is the alt text, URL is the src
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
    # If none of the above match, raise an error
    raise ValueError(f"Unknown text type: {text_node.text_type}")


from enum import Enum

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
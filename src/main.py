# Import the TextNode and TextType classes from the textnode.py file
from .textnode import TextNode, TextType

def main():
    # Create a new TextNode object
    node = TextNode(
        "This is some anchor text", 
        TextType.LINK, 
        "https://www.boot.dev"
    )
    
    # Print the object's string representation
    print(node)

# Call the main function to run the program
main()
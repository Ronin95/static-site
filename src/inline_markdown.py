# Import the TextNode and TextType classes from textnode.py
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits TextNodes of type TEXT based on a delimiter.
    
    Args:
        old_nodes (list): A list of TextNode objects.
        delimiter (str): The markdown delimiter (e.g., "**", "`").
        text_type (TextType): The TextType to apply to delimited text.

    Returns:
        list: A new list of TextNode objects.
    """
    new_nodes = []
    
    # Iterate over all nodes in the input list
    for node in old_nodes:
        # If the node is not a TEXT node, add it to the list and continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # If we're here, the node is a TEXT node, so we split it
        split_parts = node.text.split(delimiter)
        
        # Check for invalid markdown (missing a closing delimiter)
        if len(split_parts) % 2 == 0:
            raise Exception(f"Invalid markdown: missing closing delimiter '{delimiter}' in text: {node.text}")
        
        # Process the split parts
        for i in range(len(split_parts)):
            part = split_parts[i]
            
            # Skip any empty strings that result from the split
            if len(part) == 0:
                continue
            
            # If the index is even, it's regular text
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            # If the index is odd, it's the delimited text
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes
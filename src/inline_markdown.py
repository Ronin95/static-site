import re
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
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_parts = node.text.split(delimiter)
        
        if len(split_parts) % 2 == 0:
            raise Exception(f"Invalid markdown: missing closing delimiter '{delimiter}' in text: {node.text}")
        
        for i in range(len(split_parts)):
            part = split_parts[i]
            
            if len(part) == 0:
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes

def extract_markdown_images(text):
    """
    Extracts all markdown images from text.
    Returns a list of tuples: (alt_text, url)
    """
    # Pattern: ![alt_text](url)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    """
    Extracts all markdown links from text.
    Returns a list of tuples: (anchor_text, url)
    """
    # Pattern: [anchor_text](url)
    # The (?<!!) is a "negative lookbehind" that ensures
    # the link is NOT preceded by a !, (which would make it an image)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
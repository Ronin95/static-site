import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    """
    Splits TextNodes based on markdown images.
    """
    new_nodes = []
    for node in old_nodes:
        # If not a TEXT node, pass it through
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        images = extract_markdown_images(original_text)
        
        # If no images, pass the node through
        if not images:
            new_nodes.append(node)
            continue

        # We have images to split
        text_to_split = original_text
        for alt_text, url in images:
            # Split the text at the image
            delimiter = f"![{alt_text}]({url})"
            sections = text_to_split.split(delimiter, 1)
            
            # The text before the image
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            # The image node itself
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # The remaining text becomes the new string to split
            text_to_split = sections[1]
        
        # Add any remaining text after the last image
        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits TextNodes based on markdown links.
    """
    new_nodes = []
    for node in old_nodes:
        # If not a TEXT node, pass it through
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)
        
        # If no links, pass the node through
        if not links:
            new_nodes.append(node)
            continue

        # We have links to split
        text_to_split = original_text
        for anchor_text, url in links:
            # Split the text at the link
            delimiter = f"[{anchor_text}]({url})"
            sections = text_to_split.split(delimiter, 1)
            
            # The text before the link
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            # The link node itself
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            
            # The remaining text becomes the new string to split
            text_to_split = sections[1]
        
        # Add any remaining text after the last link
        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            
    return new_nodes
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
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        images = extract_markdown_images(original_text)
        
        if not images:
            new_nodes.append(node)
            continue

        text_to_split = original_text
        for alt_text, url in images:
            delimiter = f"![{alt_text}]({url})"
            sections = text_to_split.split(delimiter, 1)
            
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text_to_split = sections[1]
        
        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)
        
        if not links:
            new_nodes.append(node)
            continue

        text_to_split = original_text
        for anchor_text, url in links:
            delimiter = f"[{anchor_text}]({url})"
            sections = text_to_split.split(delimiter, 1)
            
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text_to_split = sections[1]
        
        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            
    return new_nodes


def text_to_textnodes(text):
    """
    Converts a raw text string into a list of TextNode objects.
    """
    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Run all the splitting functions in order
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Return the final list of nodes
    return nodes
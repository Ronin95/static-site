from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    """
    Splits a markdown string into a list of blocks.
    
    Blocks are separated by one or more blank lines.
    Leading/trailing whitespace is stripped from each block.
    Empty blocks are removed.
    """
    blocks = markdown.split("\n\n")
    new_blocks = []
    
    for block in blocks:
        stripped_block = block.strip()
        if len(stripped_block) > 0:
            new_blocks.append(stripped_block)
            
    return new_blocks


def block_to_block_type(block):
    """
    Determines the BlockType of a given markdown block.
    """
    
    # Check for Heading (1-6 '#' followed by a space)
    for i in range(1, 7):
        if block.startswith("#" * i + " "):
            return BlockType.HEADING
            
    # Check for Code (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
        
    lines = block.split('\n')
    
    # Check for Quote (all lines start with '>')
    if lines and all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
        
    # Check for Unordered List (all lines start with '* ' or '- ')
    if lines and all(line.startswith("* ") for line in lines):
        return BlockType.UNORDERED_LIST
    if lines and all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
        
    # Check for Ordered List (lines start with 1. , 2. , 3. ...)
    if lines:
        is_ordered = True
        for i, line in enumerate(lines):
            # Check if the line starts with "i+1." followed by a space
            if not line.startswith(f"{i + 1}. "):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ORDERED_LIST
            
    # If none of the above, it's a paragraph
    return BlockType.PARAGRAPH
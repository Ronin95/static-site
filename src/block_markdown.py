def markdown_to_blocks(markdown):
    """
    Splits a markdown string into a list of blocks.
    
    Blocks are separated by one or more blank lines.
    Leading/trailing whitespace is stripped from each block.
    Empty blocks are removed.
    """
    # 1. Split the text by one or more blank lines (2+ newlines)
    blocks = markdown.split("\n\n")
    
    new_blocks = []
    
    # 2. Iterate, strip, and check for empty
    for block in blocks:
        # 3. Strip leading/trailing whitespace
        stripped_block = block.strip()
        
        # 4. Remove empty blocks
        if len(stripped_block) > 0:
            new_blocks.append(stripped_block)
            
    return new_blocks
import os
import shutil

# Make sure this import matches your file name
# (You renamed it to markdown_blocks)
from markdown_blocks import (
    markdown_to_html_node,
    extract_title
)

def copy_directory(source_path, dest_path):
    """
    Recursively copies all contents from source_path to dest_path.
    """
    if not os.path.exists(source_path):
        raise Exception(f"Source path does not exist: {source_path}")

    # Clear the destination directory if it exists
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    
    print(f"Creating directory: {dest_path}")
    os.mkdir(dest_path)
    
    # Get items in the source directory
    items = os.listdir(source_path)
    
    for item in items:
        source_item_path = os.path.join(source_path, item)
        dest_item_path = os.path.join(dest_path, item)
        
        # If it's a file, copy it
        if os.path.isfile(source_item_path):
            print(f"  Copying file: {source_item_path} -> {dest_item_path}")
            shutil.copy(source_item_path, dest_item_path)
        
        # If it's a directory, call this function recursively
        elif os.path.isdir(source_item_path):
            copy_directory(source_item_path, dest_item_path)

def generate_page(from_path, template_path, dest_path, basepath="/"):
    """
    Generates an HTML page from a markdown file and a template.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # 1. Read markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
        
    # 2. Read template file
    with open(template_path, 'r') as f:
        template_content = f.read()
        
    # 3. Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # 4. Extract title from markdown
    title = extract_title(markdown_content)
    
    # 5. Replace placeholders
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    # --- FIX 2: Add the basepath link replacements ---
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')
    
    # 6. Write to destination path
    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    # Write the new HTML file
    with open(dest_path, 'w') as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    """
    Recursively finds markdown files in a content directory,
    and generates HTML pages from them.
    """
    # List all items in the current content directory
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item) # e.g., "content/blog"
        
        # If it's a file, check if it's markdown and generate a page
        if os.path.isfile(item_path):
            if item.endswith(".md"):
                # Build the destination path
                # Change the extension from .md to .html
                dest_file_name = os.path.splitext(item)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, dest_file_name)
                
                # --- FIX 4: Pass basepath to generate_page ---
                generate_page(
                    from_path=item_path,
                    template_path=template_path,
                    dest_path=dest_path,
                    basepath=basepath
                )
        
        # If it's a directory, recurse
        elif os.path.isdir(item_path):
            # Build the new destination directory path
            new_dest_dir_path = os.path.join(dest_dir_path, item) # e.g., "public/blog"
            # --- FIX 5: Pass basepath to the recursive call ---
            generate_pages_recursive(
                dir_path_content=item_path,
                template_path=template_path,
                dest_dir_path=new_dest_dir_path,
                basepath=basepath
            )
            
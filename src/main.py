import sys  # Import sys to read arguments
import os
from generation import copy_directory, generate_pages_recursive

def main():
    # Define paths
    static_path = "static"
    # Change output directory to "docs"
    public_path = "docs"
    content_path = "content"
    template_path = "template.html"
    
    # 2. Get basepath from sys.argv
    basepath = "/"  # Default for local testing
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    # 1. Clean docs dir and copy static files
    print(f"Copying static files to {public_path} directory...")
    copy_directory(static_path, public_path)
    
    # 2. Generate all pages recursively
    print("Generating all pages...")
    generate_pages_recursive(
        dir_path_content=content_path,
        template_path=template_path,
        dest_dir_path=public_path,
        basepath=basepath  # 3. Pass basepath
    )
    
    print("...Site generation complete!")

# Call the main function to run the script
main()
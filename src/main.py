# Import the new functions from generation.py
from generation import copy_directory, generate_page
import os

def main():
    # Define paths
    static_path = "static"
    public_path = "public"
    content_path = "content/index.md"
    template_path = "template.html"
    dest_file_path = "public/index.html"
    
    # 1. Clean public dir and copy static files
    print("Copying static files to public directory...")
    copy_directory(static_path, public_path)
    
    # 2. Generate the page
    generate_page(
        from_path=content_path,
        template_path=template_path,
        dest_path=dest_file_path
    )
    
    print("...Site generation complete!")

# Call the main function to run the script
main()
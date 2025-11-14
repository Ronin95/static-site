from generation import copy_directory, generate_pages_recursive
import os

def main():
    # Define paths
    static_path = "static"
    public_path = "public"
    content_path = "content"  # This is now the root content dir
    template_path = "template.html"
    
    # 1. Clean public dir and copy static files
    print("Copying static files to public directory...")
    copy_directory(static_path, public_path)
    
    # 2. Generate all pages recursively
    print("Generating all pages...")
    generate_pages_recursive(
        dir_path_content=content_path,
        template_path=template_path,
        dest_dir_path=public_path
    )
    
    print("...Site generation complete!")

# Call the main function to run the script
main()
import os
import shutil

def copy_directory(source_path, dest_path):
    """
    Recursively copies all contents from source_path to dest_path.
    
    1. Deletes dest_path if it exists.
    2. Creates dest_path.
    3. Iterates through items in source_path.
    4. If file, copies it to dest_path.
    5. If directory, recursively calls copy_directory.
    """
    # 1. Check if source path exists
    if not os.path.exists(source_path):
        raise Exception(f"Source path does not exist: {source_path}")

    # 2. Delete the destination directory to ensure a clean copy
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    
    # 3. Create the new destination directory
    print(f"Creating directory: {dest_path}")
    os.mkdir(dest_path)
    
    # 4. Get items in the source directory
    items = os.listdir(source_path)
    
    for item in items:
        # Get full paths for source and destination
        source_item_path = os.path.join(source_path, item)
        dest_item_path = os.path.join(dest_path, item)
        
        # 5. If it's a file, copy it
        if os.path.isfile(source_item_path):
            print(f"  Copying file: {source_item_path} -> {dest_item_path}")
            shutil.copy(source_item_path, dest_item_path)
        
        # 6. If it's a directory, call this function recursively
        elif os.path.isdir(source_item_path):
            copy_directory(source_item_path, dest_item_path)

def main():
    # Define static and public paths
    static_path = "static"
    public_path = "public"
    
    # Call the copy function
    print("Copying static files to public directory...")
    copy_directory(static_path, public_path)
    print("...copy complete!")

# Call the main function to run the script
main()
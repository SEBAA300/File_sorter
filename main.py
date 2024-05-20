import os
import shutil

# Get username
username = os.getlogin()

# Directory paths
base_dir = os.path.join("/home", username)
sort_dir = os.path.join(base_dir, "Projects/test_file")

# Supported extensions
category_name = {
    "Pictures": [".jpg",".jpeg",".png",".gif"],
    "Documents": [".txt",".pdf",".doc",".docx",".odt"],
    "Music": [".mp3"],
    "Videos": [".mp4"]}

def categorize_files(file_path, directory, category_name):
    fielname, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    for category, extensions in category_name.items():
        if ext in extensions:
            new_dir = os.path.join(directory, category)
            try:
                os.makedirs(new_dir, exist_ok=True) # Create directories if they don't exist
                shutil.move(file_path, new_dir)
                return True
            except Exception as er:
                print(f"Error moving '{file_path}': {er}")
                return False
    else:
        print(f"Unsupported file type: {file_path}")
        return False

# Process files
for file in os.listdir(sort_dir):
    file_path = os.path.join(sort_dir, file)
    categorize_files(file_path, sort_dir, category_name)
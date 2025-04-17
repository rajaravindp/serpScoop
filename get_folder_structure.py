import os

def get_folder_structure(root_path, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {"venv", "__pycache__"} 

    structure = ""
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        level = root.replace(root_path, '').count(os.sep)
        indent = ' ' * 4 * level
        structure += f"{indent}{os.path.basename(root)}/\n"
        
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            structure += f"{subindent}{f}\n"

    return structure

root_path = r"path\to-your\project-root-dir"  
folder_structure = get_folder_structure(root_path, exclude_dirs={"venv", "__pycache__"})
print(folder_structure)

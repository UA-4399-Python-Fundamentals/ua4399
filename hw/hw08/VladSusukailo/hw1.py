import os
os.makedirs("project_folder/models", exist_ok=True)
os.makedirs("project_folder/utils", exist_ok=True)

files = [
    "project_folder/main.py",
    "project_folder/models/__init__.py",
    "project_folder/models/admin.py",
    "project_folder/models/user.py",
    "project_folder/utils/__init__.py",
    "project_folder/utils/formatter.py",
    "project_folder/utils/logger.py"
]

for file_path in files:
    with open(file_path, 'w') as f:
        pass

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Text-Summarizer'
list_of_files = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for file_path in list_of_files:
    file_path = Path(file_path) # convert to path object for easy manipulation
    filedir, filename = os.path.split(file_path)

    if (filedir != ""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if (filename != "") or (not os.path.exists(file_path)):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"{filename} is present.skipping this......")

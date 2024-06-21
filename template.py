import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", #used to help the deployment in cloud
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
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
    "research/trials.ipynb",

]


for filepath in list_of_files:
    #it will give all the path without throwing any error for windows and linux
    filepath = Path(filepath)
    #split the filepath and give filedir and filename
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        #if filedir not present, then create the directory
        os.makedirs(filedir, exist_ok=True)
        #log the message after creating the directory
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        #if file not present or file size is 0, then create the file and open with 'writing' mode
        with open(filepath,'w') as f:
            pass
        #log the message after creating the file
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        #if file already exists, then log the message 'filename exists'
        logging.info(f"{filename} is already exists")

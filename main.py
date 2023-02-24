
from sre_parse import CATEGORIES
import os
from pathlib import Path


CATEGORIES = {
    "IMAGE":[".jpeg",".jpg",".heic"],
    "VIDEO" :[".mp4",".mov",],
    "DOCUMENT":[".txt",".docx",".pdf"],
    "COMPRESSED" :[".zap","zip",".rar",".7zip"], #for stephen1
}

def checkType(type):
    for category,suffixes in CATEGORIES.items():
        for suffix in suffixes:
            if type == suffix:
                return category.lower()
    return "others"

def fileOrganizer():
    for file in os.scandir():
        if file.is_dir() or str(Path(file)) == "main.py"  :
            continue
        filePath = Path(file)

        fileType = filePath.suffix.lower()
        directoryName = checkType(fileType)
        directoryPath = Path(directoryName)
        if directoryPath.is_dir() == False:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
            
fileOrganizer()

        
        
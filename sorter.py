import os
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("file_sorter.log"),
        logging.StreamHandler()
    ]
)

# File extension categories
directory = {
    'IMAGES': ['.jpg', '.jpeg', '.png', '.jfif', '.webp'],
    'MOVIES': ['.mov', '.mp4', '.m4a', '.mkv', '.avi'],
    'DOCUMENTS': ['.doc', '.docx', '.pdf', '.rtf', '.txt', '.md'],
    'AUDIO': ['.mp3', '.wav', '.flac'],
    'INSTALLER': ['.exe', '.apk', '.jar', '.msi'],
    'CODE': ['.py', '.java', '.c', '.html', '.css', '.js'],
    'NOTEBOOKS': ['.ipynb'],
    'COMPRESSED': ['.zip', '.rar', '.7z', '.tar.gz'],
    'CISCO': ['.pkt'],
    'MATLAB': ['.mlx'],
    'EXCEL': ['.xlsx', '.xls', '.csv'],
    'POWERPOINT': ['.ppt', '.pptx']
}

def pickDirectory(value):
    for category, suffixes in directory.items():
        if value in suffixes:
            return category
    return 'Misc'

def orgDirectory():
    downloads_path = Path.home() / "Downloads"
    os.chdir(downloads_path)

    for item in os.scandir():
        if item.is_dir() or item.name.startswith(".") or item.name == "file_sorter.log" or item.name == "sorter.py" or item.name == "run_sorter.bat":    # Skip directories and hidden files
            continue

        filePath = Path(item)
        filetype = filePath.suffix.lower()
        folder = pickDirectory(filetype)
        directoryPath = Path(folder)

        # Create directory if it doesn't exist
        if not directoryPath.is_dir():
            directoryPath.mkdir()

        newfilePath = directoryPath / filePath.name
        i = 1
        # Handle name collisions
        while newfilePath.exists() and i < 300:
            newfilePath = directoryPath / f"{filePath.stem}_{i}{filePath.suffix}"
            i += 1

        if newfilePath.exists():
            logging.warning(f"Failed to rename file {filePath.name}")
        else:
            filePath.rename(newfilePath)
            logging.info(f"Moved '{filePath.name}' to '{directoryPath}/'")

if __name__ == "__main__":
    orgDirectory()
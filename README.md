📁 File Sorter Script

This Python script helps you automatically organize files in a folder by moving them into subfolders based on file types (e.g., Images, Documents, Videos, etc.).


🧾 Files Included

- sorter.py – The main script that sorts files.
- run_sorter.bat – A Windows batch file to run the script easily without using the command line.


✅ How to Use

Place both sorter.py and run_sorter.bat in the folder you want to organize.
For example: your Downloads or any folder with many files.

Double-click run_sorter.bat.

The script will:

Sort all files in the current folder based on their extensions.

Create folders like IMAGES, DOCUMENTS, AUDIO, etc.

Move the files into the corresponding folders.

Show a "Sorting completed" message at the end.


📝 Notes

Files already in folders will not be moved.

Hidden files and the script's own log file (file_sorter.log) are ignored.

If a file with the same name already exists in the destination folder, it will be renamed (e.g., file_1.pdf, file_2.pdf, etc.).

The script logs all actions to file_sorter.log for reference.


⚙️ Requirements

Python 3.x installed on your system

No external libraries required (uses only the standard library)


"""
Author: Luis Gonzalez, PhD
Email: lujogre@gmail.com
Creation Date: February 7, 2024

One-Line Content Wrapper
Description:
This Python script wraps the content of files within a specified directory into a single line and saves them in a new directory with a timestamp.

Usage:
Ensure Python 3.x is installed on your system.
Modify the directory_path variable in the script to point to the directory containing the files you want to process.
Run the script.

Functionality:
- Walks through the specified directory, reads each file's content, and combines the lines into one line.
- Creates a new directory with a timestamp and saves the modified files in this directory.

Requirements:
- Python 3.x
- Compatible with all operating systems.

Example Usage:
python content_wrapper.py
"""

import os
from datetime import datetime

def wrap_content_in_one_line(directory_path, timestamp):
    new_directory = os.path.join(directory_path, timestamp)
    os.makedirs(new_directory, exist_ok=True)

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):  # Ensure it's a file
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                # Combine lines into one line
                content = ' '.join([line.strip() for line in lines])

                # Write back to a new file in the timestamp directory
                new_file_path = os.path.join(new_directory, file_name)
                with open(new_file_path, 'w') as new_file:
                    new_file.write(content)


if __name__ == "__main__":
    directory_path = r"C:/Users/"  # Update with the correct directory path

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    wrap_content_in_one_line(directory_path, timestamp)
    print("Content in files wrapped into one line and saved in the timestamp directory successfully.")

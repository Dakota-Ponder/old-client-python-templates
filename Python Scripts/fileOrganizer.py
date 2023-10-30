# program that organizes files in a directory based on their extension.
import os
import logging

logging.basicConfig(filename='organizer.log', level=logging.INFO)

DIR_PATH = 'path_to_directory'

for filename in os.listdir(DIR_PATH):
    ext = filename.split('.')[-1]
    ext_dir = os.path.join(DIR_PATH, ext)
    os.makedirs(ext_dir, exist_ok=True)  # Create directory if it doesn't exist
    os.rename(os.path.join(DIR_PATH, filename),
              os.path.join(ext_dir, filename))
    logging.info(f"Moved {filename} to {ext_dir}")

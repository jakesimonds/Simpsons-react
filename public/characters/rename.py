import os
import glob
from datetime import datetime

# Directory containing the .webp files
directory = '.'  # Current directory, change if needed

# Get all .webp files in the directory
webp_files = glob.glob(os.path.join(directory, '*.webp'))

# Sort files by modification time
sorted_files = sorted(webp_files, key=os.path.getmtime)

# Rename files
for index, file in enumerate(sorted_files, start=1):
    new_name = f'{index}.webp'
    new_path = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(file, new_path)
    print(f'Renamed {file} to {new_name}')

print('Renaming complete.')

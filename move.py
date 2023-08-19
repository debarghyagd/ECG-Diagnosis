import os
import shutil
import random

def move_files(source_dir, destination_dir):
    # Get a list of all files in the source directory
    files = list(set([i[:-5] for i in os.listdir(source_dir)]))
    
    # Calculate the number of files to move
    num_files_to_move = len(files)*0.2
    
    # Iterate over the files and move them based on the condition
    for file_name in files:
        source_file_path = os.path.join(source_dir, file_name)
        destination_file_path = os.path.join(destination_dir, file_name)
        
        # Use random function to determine if the file should be moved
        if random.random() >= 0.5 and num_files_to_move > 0:
            shutil.move(source_file_path, destination_file_path)
            num_files_to_move -= 1

# Example usage
source_directory = './WFDB_ShaoxingUniv_Train'
destination_directory = './WFDB_ShaoxingUniv_Test'

move_files(source_directory, destination_directory)

#192.168.29.157
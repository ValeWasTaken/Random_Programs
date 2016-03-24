# Python 3.4
# Counts the .jpgs inside of all of a folder (and its sub-folders)
import os

def search(directory):
    file_count = 0
    for root, subdirs, files in os.walk(directory, topdown=True):
        subdirs[:] = [d for d in subdirs]
        for file in files:
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                img = os.path.join(root, file)
                file_count += 1
    print(file_count)
search(input('Enter complete directory route: '))

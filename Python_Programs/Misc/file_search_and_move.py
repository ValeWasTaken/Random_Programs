'''
Searches all specified directory and all sub-directories for all .jpg
or .jpeg files. Then moves each file to a single folder and renames
them as "Wallpaper_{number}.jpg"
'''
# Python 3.4
import os

def search(directory):
    x = 0
    for root, subdirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                 origin = os.path.join(root, file)
                 x += 1
                 output = 'C:/Users/Test/Desktop/Output/Wallpaper_{0}.jpg'.format(x)
                 os.rename(origin, output)
    print('All done!')

search(input('Enter name of directory to search: '))

import os

dir_to_flatten = os.getcwd()+"/"+"files/unzipped/A"
dir_to_putfiles = os.getcwd() + "/files/Anew"

"""
For the code to work Anew should already be existing before starting the code
dirpath = parent directory to flatten
dirnames = directory inside parent directory
For first loop if folllowing directory is to be flattened /Users/aruneshn/PycharmProjects/Kbdev/src/files/A/A00/
then
dirpath = /Users/aruneshn/PycharmProjects/Kbdev/src/files/A
dirnames = ['A00']
"""

for dirpath, dirnames, filenames in os.walk(dir_to_flatten):
    for filename in filenames:
        try:
            os.rename(os.path.join(dirpath, filename), os.path.join(dir_to_putfiles, filename))
            print(dirpath,dirnames,filename)
        except OSError:
            print ("Could not move %s " % os.path.join(dirpath, filename))
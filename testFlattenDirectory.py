import os, sys

dir_to_flatten = "/home/psinha/python/KB_dev/poc1/files/unzipped"

for dirpath, dirnames, filenames in os.walk(dir_to_flatten):
    for filename in filenames:
        try:
            os.rename(os.path.join(dirpath, filename), os.path.join(dir_to_flatten, filename))
        except OSError:
            print ("Could not move %s " % os.path.join(dirpath, filename))
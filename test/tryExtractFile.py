import tarfile
import os

print(os.getcwd())
filedir = os.getcwd()+ "/" + "files" + "/" + "archives/acl-arc-160301-parscit"
outdir = os.getcwd()+ "/" + "files" + "/" + "unzipped"
for file in os.listdir(filedir):
    if file.endswith(".tgz"):
        with tarfile.open(filedir+"/"+file, 'r') as t:
            try:
               t.extractall(outdir)
            except:
                print(filedir+"/"+file)

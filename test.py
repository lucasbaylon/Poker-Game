import os
from os import listdir
from os.path import isfile, join

monRepertoire = "cards/"

fichiers = [f for f in listdir(monRepertoire) if isfile(join(monRepertoire, f))]

print(fichiers)

# file_oldname = os.path.join("c:\\Folder-1", "OldFileName.txt")
# file_newname_newfile = os.path.join("c:\\Folder-1", "NewFileName.NewExtension")
#
# os.rename(file_oldname, file_newname_newfile)
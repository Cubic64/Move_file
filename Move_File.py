import os
import shutil

from_dir = "C:/Users/siddh/Downloads"
to_dir = "C:/Users/siddh/Documents/Documents_file"

list_of_files = os.listdir(from_dir)



for i in list_of_files:
  name, extension = os.path.splitext(i)
  print(name + extension)
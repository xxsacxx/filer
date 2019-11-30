import os
from os import listdir
from os.path import isfile, join
import shutil
import ntpath
import errno
import traceback

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail

def move_files(dirs, file):
    """
    :param file_paths: appends all file_paths
  
    """

    file_paths = []
    path = str(os.path.join(dirs, file))
   

    if path[-3:] == ".py":
        sub_fldr = "scripts"
    elif path[-5:] == "ipynb":
        sub_fldr = "notebooks"
    else:
        sub_fldr = "others"
    file_paths.append(path)
    moving_dir = os.path.join(dirs,sub_fldr)
    try:
        
        os.makedirs(moving_dir, exist_ok=True)
        for fp in file_paths:
            
            fname = path_leaf(fp)
            shutil.move(fp, str(dirs)+"/"+sub_fldr+"/"+str(fname))
    except OSError as exc:
 
        logger.error(traceback.format_exc()) 
        logger.info("Creation of the directory %s failed" % moving_dir)




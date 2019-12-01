import os
import sys
from os import listdir
import logging
from moving_files import move_files
import traceback


logger = logging.getLogger(__name__)  
here = os.getcwd()
#here = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(here, 'filer.log')
# set log level
logger.setLevel(logging.DEBUG)
# define file handler and set formatter
file_handler = logging.FileHandler(log_file)
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


path = sys.argv[1] if len(sys.argv) > 1 else '.'
# print("path {0}".format(path))

for root, dirs, files in os.walk(path):
    logger.info("root: {0},dirs: {1},files: {2}".format(root,dirs,files))
    for file in files:
        try:
            logger.info("moving file {0}".format(file))
            move_files(path,file)
            break
        except:
            logger.error(traceback.format_exc())

        # print("path: {0} file :{1}".format(path,file))
    
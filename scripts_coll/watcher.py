

import logging
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.DEBUG)
import moving_files
from moving_files import *
import logging
# from scripts_coll.moving_files import *

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

class MyEventHandler(FileSystemEventHandler):
    def catch_all_handler(self, event):
        logging.info(event)
        if "File"  in event.__class__.__name__: 
             logger.info("changed file is {0}".format(((moving_files.path_leaf(event.src_path)))))
             moving_files.move_files(path,moving_files.path_leaf(event.src_path))

        
           

    # def on_moved(self, event):
    #     self.catch_all_handler(event)

    def on_created(self, event):
        self.catch_all_handler(event)

    # def on_deleted(self, event):
    #     self.catch_all_handler(event)

    def on_modified(self, event):
        self.catch_all_handler(event)
        # print("event {0}".format(event.src_path))




event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
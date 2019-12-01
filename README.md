# Filer #
### Your personal filer which helps you maintain your filesystem tidy . ##

![Filer](https://i.imgur.com/hz3xEma.jpg)

This is your personal intelligent Filer which will help you keep your sanity by keeping your filesystem well arranged.
It will keep looking in the specified directory for any file added or modifed, depending on the file extension it will create and move files to their respective category directories.

## Use case
-----------
You download everything in a specific folder and later it become so hard for you to find a file in need .This "filer"
will arrange the files in their respective directories at the time of download.Making your life easy!

## Download
-----------
    $ git clone https://github.com/xxsacxx/filer.git
    
   
### Requirements to use it:
-----------
      $ pip3 install -r /req.txt

### To run it:
------------
      $ python3 /scripts_coll/watcher.py [path/to/dir/you/want/to/tidy]

### Example:
------------

      python3 /scripts_coll/watcher.py ~/Downloads/ 

### It currently filters :
------------
          .py       :  scripts
          .ipynb    :  notebooks
          other ext :  others
          

### TODO :
------------
        Add more ext
        Add Date logic
        
        
### Acknowlegement :
------------------
            Shout out to https://github.com/gorakhargosh/watchdog for watchdog

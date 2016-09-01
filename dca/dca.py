import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import io


class MyHandler(FileSystemEventHandler):
    def on_moved(self, event):

        """Called when a file or a directory is moved or renamed.

        """
        print("on_moved")
        print(event.src_path)

    def on_created(self, event):

        """Called when a file or directory is created.

        """
        print("on_creeated")
        print(event.src_path)

    def on_deleted(self, event):

        """Called when a file or directory is deleted.

        """
        print("on_deleted")
        print(event.src_path)

    def on_modified(self, event):

        """Called when a file or directory is modified.

        """
        print("on_modified")
        print(event.src_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    path = raw_input("Enter the path of directory to be checked ")
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    from subprocess import call
    import subprocess


    filename12 = raw_input("Enter path of file to be tested ")
    filetype = filename12.split(".")[-1]

    # for running the js file
    if filetype == "js":
        call(["node", filename12])

    # for running the python file
    elif filetype == "py":
        cmd = 'python ' + filename12
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        result = out.split('\n')
        for lin in result:
            if not lin.startswith('#'):
                print(lin)

    # here code can be added for running other languages file
    else :
        print("This file is not supported")



    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()



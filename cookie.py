import time
import os
import sys
import random
import shutil

from watchdog.observers import Observerfrom watchdog.events import FileSystemEventHandler

source=r"cookie"
destination=r"cookie - Copy"

dict_Type={
"Image_Files":['.jpg','.png','.gif','.jfif','.tiff','.jpeg',],
"video_Files":['.mp4','.webm','mpg','avi','.mp2','.mpeg','.mpv','.wmv',],
"Document_Files":['.ppt','.pdf','.xls','.csv','.txt','xlsv'],
"Audio_Files":['.mp3','.adts',],
"setup_Files":['.exe','.bin','.cmd','.msi','.dmg',],
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension=path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dict_Type.items():
            time.sleep(1)
           if extension in value:
            file_name= os.path.basename(event.src_path)
            print(event.src_path)
            print("Downloaded:::"+file_name)

        path1=source+"/"+file_name
        path2=destination+"/"+key
        path3=destination"/"+key+"/"+file_name

        if os.path.exists(path2):
            print("dict exists")
            print("Moving")+file_name+"...")
            shutil.move(path1,path3)
            time.sleep(1)
        else:
            print("Making new dirt...")
            os.makedirs(path2)
            print("Moving")+file_name+"...")
            shutil.move(path1,path3)
            time.sleep(1)


           

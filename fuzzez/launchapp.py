import sys
import os
import yaml
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "\geckodriver.exe"
#driver = webdriver.Firefox(driver_path)
folder_path = ""
syzkaller_work_dir = ""
isFuzzing = False
imageAlreadyExists = False
requirements_satisfied = False
class fuzzez(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("fuzzez - prototype")
        self.populate_dependency_list()
        self.fileUploadError.setText(" ")
        self.browseButton.clicked.connect(self.browsefiles)
        self.fuzzButton.clicked.connect(self.startfuzz)

    def populate_dependency_list(self):
        self.dependencyList.clear()

        missing_modules = [] #missing modules ka list
        self.dependencyList.addItems(missing_modules)
    
    '''
    def takefilepath(self):
        folder_path = self.filePath.text()
        self.filePath.returnPressed.connect(self.checkIfValidPath(folder_path))
    '''

    def checkIfValidPath(self, fpath):
        if os.path.exists(fpath):
            self.fileUploadError.setText(fpath)
            return True  
        else:
            self.fileUploadError.setText("INVALID FILE PATH.")
            return False
    
    def checkIfImageExists(self, fpath):
        imagepath = fpath+str('\arch\x86\boot\bzImage')
        if os.path.exists(imagepath):
            return True
        else:
            return False
    
    def browsefiles(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Kernel Directory",options=options)  #kernel directory path
        self.filePath.setText(folder_path)
        self.checkIfValidPath(folder_path)

    def startfuzz(self):
        if self.checkIfValidPath(folder_path):
            isFuzzing = True
            self.checkMissingDependencies(folder_path)
            self.buildKernelImage(folder_path)
            self.launchSyzkaller()
            #self.scrapeAndShowResults()
        
    def checkMissingDependencies(self, fpath):
        self.fileUploadError.setText("Checking dependencies...")
        print("check this shi")
    
    def buildKernelImage(self, fpath):
        os.system('sudo apt install flex \
                  sudo apt update \
                  sudo apt install make gcc flex bison libncurses-dev libelf-dev libssl-dev debootstrap \
                  cp ../.config .config \
                  make oldconfig \
                  make -j$(nproc) \
                  make modules -j$(nproc) \
                  sudo make modules_install install \
                  sudo update-grub')

    def launchSyzkaller(self):
        #change send_kernel.yml ka linux folder path
        def set_src_to_linuxfolder(path):
            # Read the YAML file
            with open(path, "r") as f:
                data = yaml.safe_load(f)

            # Find the task that copies the Linux Kernel folder
            for task in data["tasks"]:
                if task["name"] == "Copy Linux Kernel folder to remote nodes":
                    task["args"]["src"] = folder_path
                    break

            # Write the updated YAML file
            with open(path, "w") as f:
                yaml.dump(data, f)

        # LETSGO
        path = "send_kernel.yaml"
        set_src_to_linuxfolder(path)
        
        os.system('ansible-playbook send_kernel.yml')
        print("ansible launches syzkaller on each server")

    def scrapeAndShowResults(self):
        print("show this shi")
        print("need the ips and shi")

    '''
    driver.get("{ip1}")  #coverage
    r = driver.find_elements_by_xpath("//table[@class= 'spTable']/tbody/tr")
    c = driver.find_elements_by_xpath("//*[@class= 'spTable']/tbody/tr[3]/td")
    rc = len (r)'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = fuzzez()
    qt_app.show()
    app.exec_()

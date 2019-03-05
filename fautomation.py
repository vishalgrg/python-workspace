from Tkinter import *
import tkFileDialog
import sys
import os

#owner:----VISHAL GARG--------

MACHINE_ = "machine:"
BATCH_FILE_PATH_ = "command:"


class Fautomation:
    def __init__(self,root):
        path = ""
        machinename = ""
        batchpath = ""
        label_0 = Label(root, text="Autosys Job Migration",width=20,font=("bold", 20))
        label_0.place(x=80,y=53)
        
        self.pathselectBtn = Button(root, text="Select JIL File Path",width=20,font=("bold", 10),
                               command=lambda: self.openDir(root))
        self.pathselectBtn.place(x=80,y=130)
        self.pathLabel = Label(root)
        self.pathLabel.place(x=260,y=130)

        self.machinelabel = Label(root, text="Enter new machine name ",width=20,font=("bold", 10))
        self.machinelabel.place(x=80,y=180)
        self.entry_machine = Entry(root)
        self.entry_machine.place(x=240,y=180)
        
        self.batchPathlabel = Label(root, text="Enter new new batch path",width=20,font=("bold", 10))
        self.batchPathlabel.place(x=80,y=230)
        self.entry_batchPath = Entry(root)
        self.entry_batchPath.place(x=245,y=230)
        self.startMigBtn = Button(root,text = "Start Migration", width =20,font=("bold", 10),bg='brown',fg='white',
                               command=lambda: self.updateMachine())
        self.startMigBtn.place(x=150,y=380)

    def openDir(self,root):
        try:
            root.directory = tkFileDialog.askdirectory()
            self.pathLabel.config(text=root.directory)
            self.path = root.directory
            print (root.directory)

        except Exception as e:
                print("error %s" % str(e))

    def updateMachine(self):
         try:
             nM = self.entry_machine.get()
             print nM
             for root, dirs, files in os.walk(self.path):
                 for file in files:
                     print file
                     if file.endswith(".txt"):
                         
                         fileN = os.path.join(root,file)
                         with open(fileN) as nfile:
                             for line in nfile:
                                 if MACHINE_ in line:
                                     self.inplace_change(fileN,line,MACHINE_+nM+'\n')
                           
         except Exception as e:
                print("error %s" % str(e))
         pass

    def updateBatchpath(self):
        pass
        
        
    def inplace_change(self,filename, old_string, new_string):
    # Safely read the input filename using 'with'
        with open(filename) as f:
            s = f.read()
            if old_string not in s:
                print('"{old_string}" not found in {filename}.'.format(**locals()))
                return

    # Safely write the changed content, if found in the file
        with open(filename, 'w') as f:
            print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
            s = s.replace(old_string, new_string)
            f.write(s)

root = Tk()
root.geometry('600x450')
root.title("Autosys Job Migration Tool")
f= Fautomation(root)
root.mainloop()

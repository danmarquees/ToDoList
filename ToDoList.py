from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = tkinter.Listbox(self.root)
        self.entry = tkinter.Entry(self.root)
        self.addButton = tkinter.Button(self.root, text="Add Task", command=self.add_task)
        self.delButton = tkinter.Button(self.root, text="Delete Task", command=self.delete_task)

         #GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()

def add_task(self):
    task = self.entry.get()
    if task != "":
        self.listbox.insert(tkinter.END, task)
        self.entry.delete(0, tkinter.END)

def delete_task(self):
    try:
        task_index = self.listbox.curselection()[0]
        self.listbox.delete(task_index)
    except:
        pass

root = tkinter.Tk()
root.title("Python To-Do List")
root.geometry("300x400") #Ajusta o tamanho da janela
to_do_list = ToDoList(root)
root.mainloop()
        
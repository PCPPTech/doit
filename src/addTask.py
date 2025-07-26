from tkinter import *
from customtkinter import *
import json

def addTaskFunc():
    def increment_task(num, path):
        with open(path, "r+") as f:
            tasks = json.load(f)
            tasks["tasks"] += num
            f.seek(0)
            json.dump(tasks, f, indent=4)
            f.truncate()
    def submit(event):
        task = task_entry.get()
        # read tasks first
        taskdict = {}
        with open("src/data/task_list.json", "r") as f:
            try:
                taskdict = json.load(f)
            except json.JSONDecodeError:
                taskdict = {}


        if task.strip() == "":
            errLabel.configure(text="Error: Task cannot be empty!")
            return
        elif task in taskdict:
            errLabel.configure(text="Error: Task already exists!")
        else:
            increment_task(1, "src/data/task_count.json") 
        
        with open("src/data/task_list.json", "r+") as f:
            tasks = json.load(f)
            tasks[task] = {"completed": False}
            f.seek(0)
            json.dump(tasks, f, indent=4)
            f.truncate()
        
        task_entry.delete(0, END)
        print(f"[*] Task '{task}' added successfully!")

    at = CTk()
    at.title("DOIT - Add Task")
    at.geometry("800x600")
    at.configure(fg_color="#2b2b2b")  # Dark background
    at.resizable(False, False)

    # Entry where user types the task
    task_entry = CTkEntry(at, width=400, height=40, font=("Cascadia Code", 16), fg_color="#444", text_color="white", insertwidth=8)
    task_entry.pack(pady=20)


    errLabel = CTkLabel(at, text="", font=("Cascadia Code", 14), text_color="red")
    errLabel.pack(pady=10)

    submit_button = CTkButton(
        at, 
        text="Add Task", 
        font=("Cascadia Code", 16), 
        command=lambda: submit(None), 
        cursor="hand2",
        width=200, 
        height=40, 
        fg_color="#4CAF50",
        hover_color="#45a049",
        text_color="white"
    )
    task_entry.bind("<Return>", submit)
    submit_button.pack(pady=20)

    at.mainloop()

if __name__ == "__main__":
    addTaskFunc()
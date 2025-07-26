import os
import json
from src.addTask import *
from src.removeTask import *
from src.guide import *
from src.shop import *
from src.user_profile import *
from src.clearTasks import *

"""
Hello! PCPPTech is here ONCE again.
In this project I decided to utilize AI and learn the basics since AI is the future.
I've heard some companies are going 100% AI. My philosophy is that AI cannot replace
10 Programmers, but 1 Programmer who utilizes AI well can replace 10 Programmers.

I only used AI for the frontend since that isn't really my sweet spot,
but the backend was coded 100% by me. My creativity is just as good as a pickle's haha

So basically AI only helped me with the frontend and autocompletion which spared a lot of time.
"""

#! button functions
#! error near these parts, TODO fix

"""
def taskCompletedCHECKED(taskName):
    with open("src/data/task_list.json", "r") as f:
        data = json.load(f)
    if taskName in data:
        data[taskName]["completed"] = True
        with open("src/data/task_list.json", "w") as f:
            json.dump(data, f, indent=4)

    

def taskCompletedUNCHECKED(taskName):
    with open("src/data/task_list.json", "r") as f:
        data = json.load(f)
    if taskName in data:
        data[taskName]["completed"] = False
        with open("src/data/task_list.json", "w") as f:
            json.dump(data, f, indent=4)
clickcount = 0
def clickedDone():
    global clickcount
    clickcount += 1
    if clickcount % 2 == 0:
        with open("src/data/task_list.json", "r") as f:
            data = json.load(f) #! I dont know what to do next, we can't assume the task but we lack data of which task was checked
        taskCompletedCHECKED()
        print("Task marked as completed!")
    else:
        taskCompletedUNCHECKED()
        print("Task marked as not completed!")
        
"""
theCLICKCOUNT = 0

def labelClicked(dataNAME, task):
    global theCLICKCOUNT
    theCLICKCOUNT += 1
    if theCLICKCOUNT % 2 == 0:
        dataNAME[task]["completed"]=False
        print(f"Task {task} marked as completed!")
    else:
        dataNAME[task]["completed"]=True
        print(f"Task {task} marked as not completed!")



try:
    from tkinter import *
except ModuleNotFoundError:
    print("Important module `tkinter` was not found. Do you want me to install it for you")
    print("using `pip install tkinter`? (y/n, default is no)")
    ans = input("> ").lower()
    if ans == "y":
        os.system("pip install tkinter")
    else:
        print("Note: without the 'tkinter' module you cannot run the app.")
        quit()

try:
    from customtkinter import *  # type: ignore
except ModuleNotFoundError:
    print("Important module `customtkinter` was not found. Do you want me to install it for you")
    print("using `pip install customtkinter`? (y/n, default is no)")
    ans = input("> ").lower()
    if ans == "y":
        os.system("pip install customtkinter")
    else:
        print("Note: without the 'customtkinter' module you cannot run the app.")
        quit()

# Initialize main window
mainWindow = CTk()  # Use CTk for a modern look
mainWindow.title("DOIT - Menu")
mainWindow.geometry("1200x700")
mainWindow.configure(fg_color="#2b2b2b")  # Dark background
mainWindow.resizable(True, True)

# Header
header = CTkFrame(mainWindow, fg_color="#444", height=80, corner_radius=0)
header.pack(side=TOP, fill=X)

header_label = CTkLabel(header, text="DOIT - Main Menu", font=("Consolas", 24, "bold"), text_color="white")
header_label.pack(pady=20)

# Sidebar
sidebar = CTkFrame(mainWindow, fg_color="#333", border_width=2, corner_radius=10, border_color="#555", width=200)
sidebar.pack(side=LEFT, fill=Y, padx=10, pady=10)
sidebar.pack_propagate(False)  # Makes sure the sidebar doesn't change it's width relatively to its children

# Sidebar buttons
button_addTask = CTkButton(
    sidebar, 
    width=175, 
    text="➕ Add Task", 
    font=("Cascadia Code", 16), 
    height=45, 
    cursor="hand2", 
    fg_color="#4CAF50",
    hover_color="#45a049",
    text_color="white",
    command=addTaskFunc
)
button_addTask.pack(pady=10)

button_removeTask = CTkButton(
    sidebar, 
    width=175, 
    text="❌ Remove Task", 
    font=("Cascadia Code", 16), 
    height=45, 
    cursor="hand2", 
    fg_color="#f44336",
    hover_color="#d32f2f",
    text_color="white"
)
button_removeTask.pack(pady=10)

button_guide = CTkButton(
    sidebar,
    width=175,
    text="📖 Guide",
    font=("Cascadia Code", 16),
    height=45,
    cursor="hand2",
    fg_color="#2196F3",
    hover_color="#1976D2",
    text_color="white",
    command=guideFunc
)
button_guide.pack(pady=10)

button_shop = CTkButton(
    sidebar,
    width=175,
    text="🛒 Shop",
    font=("Cascadia Code", 16),
    height=45,
    cursor="hand2",
    fg_color="#FF9800",
    hover_color="#F57C00",
    text_color="white"
)
button_shop.pack(pady=10)

button_profile = CTkButton(
    sidebar,
    width=175,
    text="👤 Profile",
    font=("Cascadia Code", 16),
    height=45,
    cursor="hand2",
    fg_color="#9C27B0",
    hover_color="#7B1FA2",
    text_color="white"
)
button_profile.pack(pady=10)

button_clearTasks = CTkButton(
    sidebar,
    width=175,
    text="🗑️ Clear Tasks",
    font=("Cascadia Code", 16),
    height=45,
    cursor="hand2",
    fg_color="#E91E63",
    hover_color="#D81B60",
    text_color="white",
    command=clearAllTasksFunc
)
button_clearTasks.pack(pady=10)

# Main content area
content_frame = CTkFrame(mainWindow, fg_color="#2b2b2b", corner_radius=10)
content_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)


content_label = CTkLabel(content_frame, text="Welcome to DOIT!", font=("Cascadia Code", 18), text_color="white")
content_label.pack(pady=10)

#! here we will have the tasks...
#! This is gonna be hard as fuck
#? nevermind it was easy :3

listoftasks = {}

def auto_update():
    with open("src/data/task_list.json", "r") as file:
        data = json.load(file) # get the contents of task_list.json


    for k, v in data.items():
        if k not in listoftasks:
            listoftasks[k] = v
            tasks = CTkButton(
                content_frame,
                text=f"{k} - {'✅' if data[k]["completed"] else '❌'}",
                font=("Cascadia Code", 14),
                height=40,
                width=300,
                cursor="hand2",
                fg_color="#4CAF50" if data[k]["completed"] else "#f44336",
                hover_color="#45a049" if data[k]['completed'] else "#d32f2f",
                text_color="white",
                command=lambda task=k: labelClicked(data, task)
            )

            tasks.pack(pady=5)


        else:
            pass

        mainWindow.after(200, auto_update)
auto_update() # start recursion
        
    
    




# Hover effects
def addTaskHOVER(event):
    button_addTask.configure(fg_color="#45a049")

def addTaskSTOP(event):
    button_addTask.configure(fg_color="#4CAF50")

def removeTaskHOVER(event):
    button_removeTask.configure(fg_color="#d32f2f")

def removeTaskSTOP(event):
    button_removeTask.configure(fg_color="#f44336")

# Binds
button_addTask.bind("<Enter>", addTaskHOVER)
button_addTask.bind("<Leave>", addTaskSTOP)

button_removeTask.bind("<Enter>", removeTaskHOVER)
button_removeTask.bind("<Leave>", removeTaskSTOP)

mainWindow.mainloop()
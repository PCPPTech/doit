import os
from src.addTask import *
from src.removeTask import *

"""
Hello! PCPPTech is here ONCE again.
In this project I decided to utilize AI and learn the basics since AI is the future.
I've heard some companies are going 100% AI. My philosophy is that AI cannot replace
10 Programmers, but 1 Programmer who utilizes AI well can replace 10 Programmers.

I only used AI for the frontend since that isn't really my sweet spot,
but the backend was coded 100% by me. My creativty is just as good as a pickle's haha

So basically AI only helped me with the frontend and autocompletion which spared a lot of time.
"""



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
mainWindow.resizable(False, False)

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
    text_color="white"
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
    text_color="white"
)
button_guide.pack(pady=10)

# Main content area
content_frame = CTkFrame(mainWindow, fg_color="#2b2b2b", corner_radius=10)
content_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

content_label = CTkLabel(content_frame, text="Welcome to DOIT!", font=("Cascadia Code", 18), text_color="white")
content_label.pack(pady=20)

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
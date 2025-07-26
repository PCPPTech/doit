import json
from tkinter import *
from customtkinter import *

def clearAllTasksFunc():
    def overwritetoYes():
        with open("src/data/uncategorized.json", "r+") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
            file.seek(0)
            data["clearAllNAG"] = False
            file.truncate()
            json.dump(data, file, indent=4)
            
    try:
        with open("src/data/task_list.json", "r+") as f:
            content = f.read().strip()
            if content and json.loads(content):
                with open("src/data/uncategorized.json", "r+") as uncatfile:
                    content = uncatfile.read().strip()
                    ask = json.loads(content) if content else {}

                    askorno = True # default
                    # get value of clearAllNAG
                    for k, v in ask.items():
                        if k == "clearAllNAG":
                            askorno = v
                            break




                    if askorno == False:
                        print("[*] Clearing all tasks...")
                        with open("src/data/task_list.json", "w") as clear_file:
                            clear_file.write("{}")
                    else: # if it's true then ask in gui
                        warning_window = CTk()
                        warning_window.title("Warning")
                        warning_window.geometry("400x200")
                        warning_window.configure(fg_color="#2b2b2b")
                        warning_window.resizable(False, False)

                        warning_label = CTkLabel(
                            warning_window, 
                            text="Are you sure you want to clear all tasks?", 
                            font=("Cascadia Code", 14), 
                            text_color="white"
                        )
                        warning_label.pack(pady=20)

                        button_frame = CTkFrame(warning_window, fg_color="#2b2b2b")
                        button_frame.pack(pady=10)

                        warning_button = CTkButton(
                            button_frame, 
                            text="Yes, clear all", 
                            font=("Cascadia Code", 14), 
                            command=lambda: [f.seek(0), f.truncate(), json.dump({}, f, indent=4), warning_window.destroy()]
                        )
                        warning_button.pack(side=LEFT, padx=10)

                        warning_button_no = CTkButton(
                            button_frame, 
                            text="No, cancel", 
                            font=("Cascadia Code", 14), 
                            command=warning_window.destroy
                        )
                        warning_button_no.pack(side=LEFT, padx=10)

                        neverShowthisAgain = CTkCheckBox(
                            warning_window, 
                            text="Never show this again", 
                            command=overwritetoYes, 
                            font=("Cascadia Code", 12),
                        )

                        neverShowthisAgain.pack(pady=10)

                        warning_window.mainloop()
                print("[*] All tasks cleared successfully!")

            else:
                print("[!] Error: File is already empty!")
                fileEmptyErr = CTk()
                fileEmptyErr.title("Error")
                width = 300
                height = 100
                sw = fileEmptyErr.winfo_screenwidth()
                sh = fileEmptyErr.winfo_screenheight()
                x = (sw - width) // 2
                y = (sh - height) // 2 # centrizing algorithm

                fileEmptyErr.geometry(f"{width}x{height}+{x}+{y}")


                fileEmptyErr.configure(fg_color="black")
                fileEmptyErr.resizable(False, False)

                fileEmptyLabel = CTkLabel(
                    fileEmptyErr, 
                    text="Task list is already empty!", 
                    font=("Cascadia Code", 14), 
                    text_color="red"
                )
                fileEmptyLabel.pack(pady=20)


                fileEmptyErr.mainloop()
    except FileNotFoundError:
        print("[!] Error: Task list file not found!")
if __name__ == "__main__":
    clearAllTasksFunc()
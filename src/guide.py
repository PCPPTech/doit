from tkinter import *
from customtkinter import *  # type: ignore

def guideFunc():
    guide_window = CTk()
    guide_window.title("Guide")
    guide_window.geometry("1000x800")
    guide_window.configure(fg_color="#2b2b2b")
    guide_window.resizable(False, False)

    # Header
    header = CTkFrame(guide_window, fg_color="#444", height=80, corner_radius=0)
    header.pack(side=TOP, fill=X)

    header_label = CTkLabel(header, text="📖 Guide", font=("Cascadia Code", 24, "bold"), text_color="white")
    header_label.pack(pady=20)

    content_frame = CTkFrame(guide_window, fg_color="#333", corner_radius=10)
    content_frame.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)

    # Add a scrollbar
    scrollbar = Scrollbar(content_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Text widget for guide content
    guide_text = Text(
        content_frame,
        wrap=WORD,
        bg="#2b2b2b",
        fg="white",
        font=("Consolas", 12),
        yscrollcommand=scrollbar.set,
        relief=FLAT,
        insertbackground="white",  # Cursor color
    )
    guide_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
    scrollbar.config(command=guide_text.yview)

    guide_content = """
    About DOIT:
    DOIT is a task management application designed to help you organize and manage your tasks efficiently.
    It sounds like an ordinary task manager, however by completing the tasks you add you can earn DOIT coins,
    which can be used in the SHOP section to purchase cosmetics and spice up your profile! 🌶

    1. Add Task:

    2. Remove Task:

    3. Shop:

    4. Profile:

    ** guide still under development, be patient 😉 **
    """
    guide_text.insert(END, guide_content)
    guide_text.config(state=DISABLED)  # Make the text read-only

    # Close button
    close_button = CTkButton(
        guide_window,
        text="Close",
        fg_color="#f44336",
        hover_color="#d32f2f",
        text_color="white",
        font=("Cascadia Code", 16),
        command=guide_window.destroy,
    )
    close_button.pack(pady=10)

    # Run the window
    guide_window.mainloop()


if __name__ == "__main__":
    guideFunc()
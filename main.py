#IMPORTS
from tkinter import filedialog, Tk, Button, Label, ttk, font, messagebox,PhotoImage,Frame
import os, datetime
import pyperclip
import sys, os

def resource_path(relative_path):
    """Возвращает правильный путь к файлу — работает и в .py, и в .exe"""
    try:
        base_path = sys._MEIPASS  # Временная папка PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#App config
root = Tk()
root.geometry("500x500")
#Frames
top_frame = Frame(root)
top_frame.pack(side="top", fill="x", pady=20)

frame = Frame(root)
frame.pack()


root.title("SimpleFileOpener")
img = PhotoImage(file=resource_path("4701269.ico"))
root.iconphoto(False, img)
style = ttk.Style()
style.configure("My.TButton", font=("Arial"), padding=10)

#Variables
message = ""
file = 'empty'
file_size = 0
file_datetime = 0

#Font Config
label_font = font.Font(
    family="Arial",
    size=15,
    weight="bold",
    slant="italic"
    )
# Function for file opening
def open_file():
    global file
    global file_size
    global file_datetime

    selected_file = filedialog.askopenfilename(parent=root)

    if selected_file:
    
        file = selected_file
        fileinfo.config(text=file)
        #Getting file size
        file_size = os.path.getsize(file)
        file_size_info.config(text=f'Size: {file_size}')
        #Getting file datetime
        file_datetime = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        file_datetime_info.config(text=f"Datetime: {file_datetime:%Y-%m-%d}")

def copy_file_path():
    global file
    pyperclip.copy(file)
    if file != "empty":
            pyperclip.copy(file)
            messagebox.showwarning(title="Action", message="Path successfully copied")
    else:
            messagebox.showwarning(title="Warning", message="Path is empty!\nFile path is not copied.")
    
def app_info():
    messagebox.showinfo(title="Info", message="SimpleFileOpener v0.0.2.\nv0.0.3 soon!.")


#Buttons
button = ttk.Button(frame,text="Open file", command=open_file, style="My.TButton",width=8)
button.grid(row=0, column=0, padx=10, pady=10)
copy_button = ttk.Button(frame,text="Copy path", command=copy_file_path ,style="My.TButton",width=8)
copy_button.grid(row=0, column=1, padx=10,pady=10)
app_info_button = ttk.Button(frame,text="App info", command=app_info, style="My.TButton",width=8)
app_info_button.grid(row=1,column=0,columnspan=2, padx=10)
#Labels
fileinfo = ttk.Label(top_frame,text = file, font=label_font)
file_datetime_info = ttk.Label(top_frame,text=f'Datetime: {file_datetime}', font=label_font)
file_size_info = ttk.Label(top_frame,text = f'Size: {file_size}', font=label_font)
#Config
fileinfo.pack()
file_datetime_info.pack()
file_size_info.pack()


root.resizable(False, False)
root.mainloop()
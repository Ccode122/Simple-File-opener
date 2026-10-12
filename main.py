from tkinter import filedialog, Tk, Button, Label, ttk, font
import os, datetime
import pyperclip

root = Tk()
root.geometry("400x400")
root.title("Test")
style = ttk.Style()
style.configure("My.TButton", font=("Arial"), padding=10)

file = 'empty'
file_size = 0
file_datetime = 0
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
    

#Just font for labels and buttons
big_font = font.Font(family="Arial", size=16, weight="bold")
btn_font = font.Font(family="Arial", size=16, weight="bold")

#Other things

fileinfo = ttk.Label(text = file, font=big_font)
button = ttk.Button(text="open file", command=open_file, style="My.TButton")
copy_button = ttk.Button(text="Copy path", command=copy_file_path ,style="My.TButton")
file_size_info = ttk.Label(text = f'Size: {file_size}', font=big_font)

file_datetime_info = ttk.Label(text=f'Datetime: {file_datetime}', font=big_font)

file_datetime_info.pack()
fileinfo.pack()
file_size_info.pack()


button.pack()
copy_button.pack()
root.mainloop()
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

# Create window interface
root = tk.Tk()


# Browse your data to combine
def browse_files():
	global file_path
	file_path = filedialog.askopenfilenames()


# Start combining
def merge_files():
	fout = open("{}.csv".format(file_name.get()), "a")
	for num in range(0, len(file_path)):
		f = open(file_path[num])
		if skip_check.get() == 1:
			next(f)
		for line in f:
			fout.write(line)
		fout.write("\n")
		f.close()
	fout.close()
	tkinter.messagebox.showinfo("Successfully Combined", "Your Files Successfully Combined")


# CREATE INTERFACE / GUI
file_name_text = tk.Label(text="New combined file name:", font=("Courier", 14))
file_name_text.grid(row=0, column=0, columnspan=1)
file_name = tk.Entry()
file_name.grid(row=0, column=1, columnspan=1)
skip_check = tk.IntVar()
skip_header = tk.Label(text="Do you want to skip header ?", font=("Courier", 8))
skip_header.grid(row=1, column=0, columnspan=1)
radio_bu = tk.Checkbutton(text="", variable=skip_check, onvalue=1, offvalue=0)
radio_bu.grid(row=1, column=1, columnspan=1)
browse = tk.Button(command=browse_files, width=15, height=1, font=("Courier", 12), text="BROWSE")
browse.grid(row=2, column=0, columnspan=1)
create = tk.Button(command=merge_files, foreground="red", width=10, height=1, font=("Courier", 12), text="CREATE")
create.grid(row=2, column=1, columnspan=1)
# Mainloop TKINTER
root.mainloop()

import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir= '/', title= "Select a filename please")
    return filename

# Function to perform compression
def compression(input_file, output_file):
    compress(input_file, output_file)

# Create the main window
window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")  # Note: There should not be a space between "600" and "x".




# Create a button for compression
compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), "compressedoutput1.txt"))
compress_button.grid(row=2, column=1)

# Start the Tkinter event loop
window.mainloop()

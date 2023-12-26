import tkinter as tk
from compressmodule import compress, decompress

# Function to perform compression
def compression(input_file, output_file):
    compress(input_file, output_file)

# Create the main window
window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")  # Note: There should not be a space between "600" and "x".

# Create Entry widgets for input and output file names
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

# Place Entry widgets in the window
input_entry.grid(row=0, column=1)
output_entry.grid(row=1, column=1)

# Create labels for input and output
input_label = tk.Label(window, text="File to be compressed")
output_label = tk.Label(window, text="Name of the compressed file")

# Create a button for compression
compress_button = tk.Button(window, text="Compress", command=lambda: compression(input_entry.get(), output_entry.get()))

# Place labels and button in the window
input_label.grid(row=0, column=0)
output_label.grid(row=1, column=0)
compress_button.grid(row=2, column=1)

# Start the Tkinter event loop
window.mainloop()

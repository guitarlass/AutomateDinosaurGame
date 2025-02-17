import tkinter as tk

root = tk.Tk()

x, y = 280, 650
root.geometry(f"+{x}+{y}")  # Moves to (280, 555)

# Remove window decorations
root.overrideredirect(True)

label = tk.Label(root, text="Hello!", font=("Arial", 20), fg="white", bg="black")
label.pack()

# Keep window always on top
root.attributes('-topmost', True)

root.mainloop()

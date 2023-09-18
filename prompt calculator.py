import tkinter as tk

# Function to update the display when a button is clicked
def button_click(event):
    current = display_var.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(current))
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif text == "C":
        display_var.set("")
    else:
        display_var.set(current + text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and configure the display
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 20))
display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create the buttons for the calculator
button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in button_texts:
    button = tk.Button(button_frame, text=text, font=("Helvetica", 20), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

# Start the GUI main loop
root.mainloop()

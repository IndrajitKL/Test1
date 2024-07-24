import tkinter as tk

def welcome_window():
    # Create the main window
    root = tk.Tk()
    root.title("Welcome to My Python Program")
    
    # Create a label with the welcome message
    welcome_label = tk.Label(root, text="Welcome to My Python Program!", font=("Helvetica", 16))
    welcome_label.pack(padx=20, pady=30)
    
    # Run the main loop
    root.mainloop()

# Call the function to display the welcome window
welcome_window()

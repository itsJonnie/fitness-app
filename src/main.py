import tkinter as tk
from tkinter import ttk
from database.db_setup import create_database

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.geometry("800x600")
        
        # Configure grid weight to enable centering
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create main container
        self.main_container = ttk.Frame(self.root, padding="20")
        self.main_container.grid(row=0, column=0, sticky="nsew")
        
        # Configure main container grid weights
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        # Style configuration
        style = ttk.Style()
        style.configure('Large.TLabel', font=('Helvetica', 24))
        style.configure('Large.TButton', font=('Helvetica', 14), padding=10)

        # Add welcome label
        self.welcome_label = ttk.Label(
            self.main_container, 
            text="Welcome to Fitness Tracker",
            style='Large.TLabel'
        )
        self.welcome_label.grid(row=0, column=0, pady=(100, 20))

        # Add login button
        self.login_button = ttk.Button(
            self.main_container,
            text="Login",
            command=self.show_login,
            style='Large.TButton',
            width=20
        )
        self.login_button.grid(row=1, column=0, pady=(0, 100))

    def show_login(self):
        # To be implemented
        pass

if __name__ == "__main__":
    # Create database if it doesn't exist
    create_database()
    
    # Start the application
    root = tk.Tk()
    # Set minimum window size
    root.minsize(600, 400)
    app = FitnessApp(root)
    root.mainloop() 
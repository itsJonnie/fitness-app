import customtkinter as ctk
from database.exercise_data import MUSCLE_GROUPS

class WorkoutForm(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Log Workout")
        self.geometry("800x800")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create scrollable frame
        self.main_frame = ctk.CTkScrollableFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Log Your Workout",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)
        
        # Muscle Group Selection
        muscle_frame = ctk.CTkFrame(self.main_frame)
        muscle_frame.pack(fill="x", pady=10)
        
        ctk.CTkLabel(
            muscle_frame,
            text="Muscle Group:",
            font=ctk.CTkFont(size=16)
        ).pack(pady=5)
        
        # Muscle Group Buttons
        self.muscle_buttons_frame = ctk.CTkFrame(muscle_frame)
        self.muscle_buttons_frame.pack(fill="x", padx=20, pady=5)
        
        self.selected_muscle = None
        self.muscle_buttons = {}
        
        # Create grid of muscle group buttons
        row = 0
        col = 0
        for muscle_group, data in MUSCLE_GROUPS.items():
            btn = ctk.CTkButton(
                self.muscle_buttons_frame,
                text=f"{data['icon']} {muscle_group}",
                command=lambda m=muscle_group: self.select_muscle_group(m),
                width=150
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.muscle_buttons[muscle_group] = btn
            
            col += 1
            if col > 2:  # 3 buttons per row
                col = 0
                row += 1
        
        # Exercise Selection (initially hidden)
        self.exercise_frame = ctk.CTkFrame(self.main_frame)
        self.exercise_buttons = {}
        
        # Exercise Info Frame
        self.info_frame = ctk.CTkFrame(self.main_frame)
        self.description_label = ctk.CTkLabel(
            self.info_frame,
            text="",
            wraplength=600
        )
        self.target_label = ctk.CTkLabel(
            self.info_frame,
            text="",
            wraplength=600
        )
        self.equipment_label = ctk.CTkLabel(
            self.info_frame,
            text="",
            wraplength=600
        )
        
        # Workout Details Frame (initially hidden)
        self.details_frame = ctk.CTkFrame(self.main_frame)
        
        # Sets, Reps, Weight inputs
        self.sets_var = ctk.StringVar(value="1")
        self.reps_var = ctk.StringVar(value="1")
        self.weight_var = ctk.StringVar(value="0")
        
    def select_muscle_group(self, muscle_group):
        # Reset previous selection
        if self.selected_muscle:
            self.muscle_buttons[self.selected_muscle].configure(
                fg_color=("gray75", "gray25")
            )
        
        # Update selection
        self.selected_muscle = muscle_group
        self.muscle_buttons[muscle_group].configure(
            fg_color=("blue", "darkblue")
        )
        
        # Show exercises for selected muscle group
        self.show_exercises(muscle_group)
    
    def show_exercises(self, muscle_group):
        # Clear previous exercises
        for widget in self.exercise_frame.winfo_children():
            widget.destroy()
        
        # Create new exercise buttons
        ctk.CTkLabel(
            self.exercise_frame,
            text="Choose Exercise:",
            font=ctk.CTkFont(size=16)
        ).pack(pady=10)
        
        exercises = MUSCLE_GROUPS[muscle_group]['exercises']
        for exercise_name in exercises:
            btn = ctk.CTkButton(
                self.exercise_frame,
                text=exercise_name,
                command=lambda e=exercise_name: self.select_exercise(muscle_group, e),
                width=200
            )
            btn.pack(pady=5)
            self.exercise_buttons[exercise_name] = btn
        
        self.exercise_frame.pack(fill="x", pady=10)
        
    def select_exercise(self, muscle_group, exercise):
        # Show exercise information
        info = MUSCLE_GROUPS[muscle_group]['exercises'][exercise]
        
        self.description_label.configure(text=f"Description: {info['description']}")
        self.target_label.configure(text=f"Target Muscles: {info['target_muscles']}")
        self.equipment_label.configure(text=f"Equipment: {info['equipment']}")
        
        for label in [self.description_label, self.target_label, self.equipment_label]:
            label.pack(pady=5)
        
        self.info_frame.pack(fill="x", pady=10)
        
        # Show workout details form
        self.show_workout_details()
    
    def show_workout_details(self):
        # Clear previous details
        for widget in self.details_frame.winfo_children():
            widget.destroy()
        
        # Create input fields
        details_grid = ctk.CTkFrame(self.details_frame)
        details_grid.pack(pady=10)
        
        # Sets
        ctk.CTkLabel(details_grid, text="Sets:").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkEntry(
            details_grid,
            textvariable=self.sets_var,
            width=60
        ).grid(row=0, column=1, padx=5, pady=5)
        
        # Reps
        ctk.CTkLabel(details_grid, text="Reps:").grid(row=0, column=2, padx=5, pady=5)
        ctk.CTkEntry(
            details_grid,
            textvariable=self.reps_var,
            width=60
        ).grid(row=0, column=3, padx=5, pady=5)
        
        # Weight
        ctk.CTkLabel(details_grid, text="Weight (kg):").grid(row=0, column=4, padx=5, pady=5)
        ctk.CTkEntry(
            details_grid,
            textvariable=self.weight_var,
            width=60
        ).grid(row=0, column=5, padx=5, pady=5)
        
        # Save button
        ctk.CTkButton(
            self.details_frame,
            text="Save Workout",
            command=self.save_workout
        ).pack(pady=20)
        
        self.details_frame.pack(fill="x", pady=10)
    
    def save_workout(self):
        # For now, just print the workout details
        print(f"Muscle Group: {self.selected_muscle}")
        print(f"Sets: {self.sets_var.get()}")
        print(f"Reps: {self.reps_var.get()}")
        print(f"Weight: {self.weight_var.get()} kg")
        self.destroy() 
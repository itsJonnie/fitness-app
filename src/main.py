import customtkinter as ctk
from database.db_setup import create_database
from ui.workout_form import WorkoutForm
from PIL import Image  # customtkinter uses PIL for images

class FitnessApp:
    def __init__(self, root):
        self.user_id = 1  # TODO: Replace with actual user authentication
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.geometry("1000x800")  # Made window bigger
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main container with more padding
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Load and display logo
        try:
            logo_image = Image.open("src/assets/images/rich_piana.png")
            # Resize image to reasonable dimensions (adjust size as needed)
            logo_image = logo_image.resize((300, 300))
            self.logo = ctk.CTkImage(
                light_image=logo_image,
                dark_image=logo_image,
                size=(300, 300)
            )
            
            self.logo_label = ctk.CTkLabel(
                self.main_container,
                image=self.logo,
                text=""  # No text, just image
            )
            self.logo_label.pack(pady=(20, 0))
        except Exception as e:
            print(f"Could not load logo: {e}")
        
        # Add welcome label with cleaner font
        self.welcome_label = ctk.CTkLabel(
            self.main_container, 
            text="FITNESS TRACKER 💪",  # Capitalized for cleaner look
            font=ctk.CTkFont(family="Helvetica", size=48, weight="bold")
        )
        self.welcome_label.pack(pady=40)
        
        # Add bigger Log Workout button
        self.workout_button = ctk.CTkButton(
            self.main_container,
            text="LOG WORKOUT",  # Capitalized for consistency
            command=self.show_workout_form,
            width=300,  # Made button wider
            height=60,  # Made button taller
            font=ctk.CTkFont(family="Helvetica", size=24),  # Bigger font
            corner_radius=15  # Rounded corners
        )
        self.workout_button.pack(pady=40)

    def show_workout_form(self):
        workout_form = WorkoutForm(self.root)
        workout_form.grab_set()

if __name__ == "__main__":
    # Create database if it doesn't exist
    create_database()
    
    # Start the application
    root = ctk.CTk()
    app = FitnessApp(root)
    root.mainloop() 
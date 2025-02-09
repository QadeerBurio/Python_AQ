from tkinter import *
from PIL import Image, ImageTk


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")

        # Set the window size to cover the entire screen
        self.root.attributes('-fullscreen', True)

        # Define dimensions for input fields
        input_width = 300
        input_height = 40

        # Load and resize images using Pillow
        self.bg_image = Image.open("depositphotos_4308060-stock-photo-project.jpg")
        self.bg_image = self.bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.user_image = Image.open("man - Copy.png")
        self.user_image = self.user_image.resize((input_height, input_height),
                                                 Image.LANCZOS)  # Match input field height
        self.user_image = ImageTk.PhotoImage(self.user_image)

        self.pass_image = Image.open("rates.png")
        self.pass_image = self.pass_image.resize((input_height, input_height),
                                                 Image.LANCZOS)  # Match input field height
        self.pass_image = ImageTk.PhotoImage(self.pass_image)

        # Background image
        bg_label = Label(self.root, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="lightblue")
        title.pack(pady=40)

        # Username Frame
        user_frame = Frame(self.root, bg="lightblue")
        user_frame.pack(pady=20, fill=X)

        user_icon_label = Label(user_frame, image=self.user_image, bg="lightblue")
        user_icon_label.pack(side=LEFT, padx=10)

        user_label = Label(user_frame, text="Username", font=("times new roman", 20), bg="lightblue")
        user_label.pack(side=LEFT)

        self.user_entry = Entry(user_frame, font=("times new roman", 20), width=30)  # Adjust width
        self.user_entry.pack(pady=5, padx=10, fill=X)

        # Password Frame
        pass_frame = Frame(self.root, bg="lightblue")
        pass_frame.pack(pady=20, fill=X)

        pass_icon_label = Label(pass_frame, image=self.pass_image, bg="lightblue")
        pass_icon_label.pack(side=LEFT, padx=10)

        pass_label = Label(pass_frame, text="Password", font=("times new roman", 20), bg="lightblue")
        pass_label.pack(side=LEFT)

        self.pass_entry = Entry(pass_frame, show="*", font=("times new roman", 20), width=30)  # Adjust width
        self.pass_entry.pack(pady=5, padx=10, fill=X)

        # Login Button
        login_button = Button(self.root, text="Login", font=("times new roman", 20), command=self.login)
        login_button.pack(pady=30)

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        # For simplicity, just print the credentials (not secure for real applications)
        print(f"Username: {username}, Password: {password}")


# Create the Tkinter window
root = Tk()

# Create an instance of LoginSystem
app = LoginSystem(root)

# Start the Tkinter event loop
root.mainloop()

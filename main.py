# Created by Alon Rubin
import os
import tkinter
import atexit
from objects import NewImage

# Global settings
background_color = "#353740"
screen_width, screen_height = 1280, 720

# Create new tkinter window
root = tkinter.Tk()
root.title("Mini Shop")
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background=background_color)

# Create tkinter panel
new_panel = tkinter.Label(root)
new_panel.configure(background=background_color)


# Exit handler
def exit_handler():
    emp_path = r"Temp.jpeg"
    try:
        os.remove(emp_path)
    except FileNotFoundError:
        print('File not found:', emp_path)


# Create buttons GUI
def create_buttons(image):
    x = 10
    buttons_label = {"gray_scale": "Gray scale", "invert_gray": "Invert gray",
                     "rotate_image": "Rotate image", "mirror_image": "Mirror image",
                     "flip_image": "Flip image", "blur_image": "Blur image",
                     "sharpen_image": "Sharpen image", "tint_image": "Tint image",
                     "tint_color": "Tint color"}
    button_width = (screen_width - 20) / len(buttons_label)
    for label, text in buttons_label.items():
        functions_name = getattr(image, label)
        button = tkinter.Button(root, text=text, command=functions_name)
        button.place(x=x, y=50, height=30, width=button_width)
        x += button_width


# Create image
new_image = NewImage(new_panel, root, screen_width, screen_height)

# Create buttons
create_buttons(new_image)

# Update
root.mainloop()

# Exit
atexit.register(exit_handler)




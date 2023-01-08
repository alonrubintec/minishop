import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
import tkinter.colorchooser as cc


class NewImage:
    temp_path = r"Temp.jpeg"
    isButton = True
    color = (0, 0, 0)

    def __init__(self, panel, app_root, screen_width, screen_height):
        self.file_path = ""
        self.panel = panel
        self.app_root = app_root
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.load_button = tkinter.Button(self.app_root, text="Load Image", command=self.load_img)
        self.load_button.place(x=10, y=10, height=40, width=screen_width/2)
        self.save_button = tkinter.Button(self.app_root, text="Save Image", command=self.save_img)
        self.save_button.place(x=screen_width/2 +10, y=10, height=40, width=screen_width/2-20)

    def load_img(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path == "":
            return
        new_img = Image.open(self.file_path)
        new_img.save(self.temp_path)
        self.refresh_panel(new_img)
        self.isButton = False

    def save_img(self):
        if self.file_path == "":
            return
        save_path = filedialog.asksaveasfilename(defaultextension='.jpeg')
        if save_path:
            save_image = Image.open(self.temp_path)
            save_image.save(save_path)

    def scale_image(self, img_ent):
        # Determine the aspect ratio of the image
        aspect_ratio = img_ent.size[0] / img_ent.size[1]

        # Calculate the new dimensions of the image based on the aspect ratio
        if aspect_ratio > 1:
            # Landscape image
            new_width = int(self.screen_height * aspect_ratio)
            new_height = self.screen_height
            if new_width > self.screen_width:
                new_width = self.screen_width
                new_height = int(self.screen_width / aspect_ratio)
        else:
            # Portrait image
            new_width = self.screen_width
            new_height = int(self.screen_width / aspect_ratio)
            if new_height > self.screen_height:
                new_width = int(self.screen_height * aspect_ratio)
                new_height = self.screen_height

        # Resize the image to fit the screen size
        img_ent = img_ent.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
        return img_ent

    def refresh_panel(self, img_ent):
        img_ent = self.scale_image(img_ent)
        tk_image = ImageTk.PhotoImage(img_ent)

        # Create a new label with the new image
        self.panel.destroy()
        self.panel = tkinter.Label(self.app_root, image=tk_image)

        # Resize image to fit window size
        x = (self.screen_width - img_ent.size[0]) // 2
        y = (self.screen_height - img_ent.size[1]) // 2 + self.screen_height/8
        self.panel.place(x=x, y=y, height=img_ent.size[1], width=img_ent.size[0])
        self.panel.image = tk_image

    def gray_scale(self):
        if self.isButton:
            return
        image = Image.open(self.temp_path)
        gray_image = image.convert('L')
        gray_image.save(self.temp_path)
        self.refresh_panel(gray_image)

    def invert_gray(self):
        if self.isButton:
            return
        image = Image.open(self.temp_path)
        gray_image = image.convert('L')
        tint_image = Image.new(gray_image.mode, gray_image.size, 50)
        tint_image = tint_image.point(lambda x: x + 100)
        invert_gray_image = Image.blend(gray_image, tint_image, alpha=2)
        invert_gray_image.save(self.temp_path)
        self.refresh_panel(invert_gray_image)

    def rotate_image(self):
        if self.isButton:
            return
        rotate_image = Image.open(self.temp_path).transpose(Image.Transpose.ROTATE_90)
        rotate_image.save(self.temp_path)
        self.refresh_panel(rotate_image)

    def mirror_image(self):
        if self.isButton:
            return
        mirror_image = Image.open(self.temp_path).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        mirror_image.save(self.temp_path)
        self.refresh_panel(mirror_image)

    def flip_image(self):
        if self.isButton:
            return
        flip_image = Image.open(self.temp_path).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        flip_image.save(self.temp_path)
        self.refresh_panel(flip_image)

    def blur_image(self):
        if self.isButton:
            return
        blur_image = Image.open(self.temp_path).filter(ImageFilter.BLUR)
        blur_image.save(self.temp_path)
        self.refresh_panel(blur_image)

    def sharpen_image(self):
        if self.isButton:
            return
        sharpen_image = Image.open(self.temp_path).filter(ImageFilter.SHARPEN)
        sharpen_image.save(self.temp_path)
        self.refresh_panel(sharpen_image)

    def tint_image(self):
        if self.isButton:
            return
        image = Image.open(self.temp_path)
        tint_image = Image.new('RGB', image.size, self.color[1])
        tint_image = Image.blend(image, tint_image, 0.5)  # Blend 50%
        tint_image.save(self.temp_path)
        self.refresh_panel(tint_image)

    def tint_color(self):
        self.color = cc.askcolor()
        if self.color[1] is not None:
            return self.color[1]








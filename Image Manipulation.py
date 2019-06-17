import os
from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()

path = ''

for image in range(0, len(os.listdir(path))):
    image = 'frame{count}.jpg'.format(count=image)
    image_path = path + image
    image = Image.open(image_path)
    w, h = image.size
    #cropped_image = image.rotate(90)
    cropped_image = image.crop((100, 100, w-100, h-100))
    #basewidth = 75
    #wpercent = (basewidth/float(cropped_image.size[0]))
    #hsize = int((float(cropped_image.size[1])*float(wpercent)))
    #resized_img = cropped_image.resize((basewidth, hsize), Image.ANTIALIAS)
    cropped_image.save(image)
resized_img = ImageTk.PhotoImage(cropped_image)
lbl = tk.Label(window, image=resized_img).pack()
window.mainloop()

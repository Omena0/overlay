from PIL import Image, ImageTk, ImageFilter
import tkinter
import sys

root = tkinter.Tk()
root.title('Overlay thingy')
root.geometry('300x100')

window_width = 300
window_height = 100

root.wm_attributes("-transparentcolor", root['bg'], '-topmost', True)

original_img = Image.open(sys.argv[1])

original_img.point

def convert(img:Image, size):
    new_img = img.copy()
    new_img:Image.Image = new_img.resize(size)

    new_img = new_img.point(lambda p: 255 if p > 200 else 0)
    new_img = new_img.filter(ImageFilter.EDGE_ENHANCE)

    # Remove pixels that are not close to pure white
    return ImageTk.PhotoImage(new_img)

def update_image(event):
    global window_width, window_height
    if (window_width == event.width) and (window_height == event.height):
        return

    window_width = event.width
    window_height = event.height

    global img
    img = convert(original_img, (root.winfo_width(), root.winfo_height()))
    canvas.delete('all')
    canvas.create_image(0, 0, image=img, anchor='nw')

canvas = tkinter.Canvas(root, bg=root['bg'], width=10000, height=1000)
canvas.pack()

img = convert(original_img, (300, 100))
canvas.create_image(0, 0, image=img, anchor='nw')

root.bind('<Configure>', update_image)

root.mainloop()


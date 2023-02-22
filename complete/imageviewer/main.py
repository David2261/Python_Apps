from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Image Viewer')
root.geometry("400x600")

root.iconbitmap('img/logo.ico')


img_1 = ImageTk.PhotoImage(Image.open("img/freedom.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("img/life.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("img/omh.jpg"))

image_list = [img_1, img_2, img_3]


my_label = Label(image=img_3)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number - 1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: forward(image_number-1))

	if image_number == 3:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)


def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number - 1])
	button_forward = Button(root, text=">>", command=lambda: back(image_number + 1))
	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back)
button_forward = Button(root, text=">>", command=lambda: forward(1))
button_exit = Button(root, text="Exit", command=root.quit)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()

# https://www.notabug.org/Tonypythony/AleApp

# conda create -n TEST python=3.5
### conda activate TEST

# pip install Pillow
# pip install cx-Freeze

### conda deactivate

from pathlib import Path
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image #, ImageFont, ImageDraw
from time import time

root = Tk()

current_dir = Path.cwd() # путь текущей директории
filename = filedialog.askopenfilename(initialdir = current_dir, # initialdir = "/run/media/rick/DATA/Kazahi"
 title = "Select imagefile", filetypes = (("jpg files", "*.jpg"),("jpeg files", "*.jpeg"),
 										("JPG files", "*.JPG"),("png files", "*.png"),
 										("bmp files", "*.bmp"),("all files", "*.*")))

# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())

y_size_screen = int(root.winfo_screenheight()*1/2)
# print(y_size_screen)


# def crop(im, s):
#     w, h = im.size
#     k = w / s[0] - h / s[1]
#     if k > 0: im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
#     elif k < 0: im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
#     return im.resize(s, Image.ANTIALIAS)


image = Image.open(filename).convert('L')

width, height = image.size
# print("size width ", width)
# print("size height ", height)


x_size_screen = int((width / height) * y_size_screen)

image = image.resize((x_size_screen,y_size_screen)) #((540,540))
new_image_crop = image #####

width, height = image.size
print("size width ", width)
print("size height ", height)

x_size_root = int(x_size_screen + x_size_screen/3)
y_size_root = int(y_size_screen + y_size_screen/2)

root.geometry('{}x{}'.format(x_size_root,y_size_root)) #(536,506))

canvas = Canvas(root,width=x_size_screen,height=y_size_screen)

canvas.pack()


pilimage = ImageTk.PhotoImage(image)

imagesprite = canvas.create_image(0,0,image=pilimage, anchor=NW)

container = Frame() # создаём контейнер на главном окне для расположения кнопок и полей ввода
container.pack(side='top', fill='both', expand=True)

M = 255 # условие max
L = 1 # min
x_size = 0 # пока не отрезает изображение слева сверху
y_size = 0 # пока не отрезает изображение справа снизу

########################################################################

lbl1 = Label(container, text="Max = ")  
lbl1.grid(column=4, row=1) 

def get_val_motion(event):
	global M
	M = scal.get()
	
scal = Scale(container, orient=HORIZONTAL, length=int(image.size[0]*0.6), from_=1, to=255,
			tickinterval=20, resolution=1)
scal.bind("<B1-Motion>", get_val_motion)
scal.grid(column=5, row=1)

########################################################################

lbl2 = Label(container, text="Min = ")  
lbl2.grid(column=4, row=2) 

def get_val_motion_1(event_1):
	global L
	L = scal1.get()
	
scal1 = Scale(container, orient=HORIZONTAL, length=int(image.size[0]*0.6), from_=1, to=255,
			tickinterval=20, resolution=1)
scal1.bind("<B1-Motion>", get_val_motion_1)
scal1.grid(column=5, row=2)

########################################################################

lbl8_1 = Label(container, text="left-up = ")  
lbl8_1.grid(column=4, row=3) 

def get_val_motion_8_1(event_2):
	global x_size
	global y_size
	x_size = int(scal8_1.get())
	
	global image # нужно для возможности сохранения в дальнейшем
	
	#area = (x_size, x_size, width, height)
	area = (x_size, x_size, width - y_size , height - y_size)
	global new_image_crop
	new_image_crop = image.crop(area)

	global pilimage
	pilimage = ImageTk.PhotoImage(new_image_crop)
	global imagesprite
	imagesprite = canvas.create_image(0,0,image=pilimage, anchor=NW)
	
scal8_1 = Scale(container, orient=HORIZONTAL, length=int(image.size[0]*0.6), from_=0, to=x_size_screen,
			tickinterval=50, resolution=10)
scal8_1.bind("<B1-Motion>", get_val_motion_8_1)
scal8_1.grid(column=5, row=3)

########################################################################

lbl8_2 = Label(container, text="right-down = ")  
lbl8_2.grid(column=4, row=4) 

def get_val_motion_8_2(event_2):
	global x_size
	global y_size
	y_size = int(scal8_2.get())
	#print(radius)
	global image # нужно для возможности сохранения в дальнейшем
	
	area = (x_size, x_size, width - y_size , height - y_size) # ?
	global new_image_crop
	new_image_crop = image.crop(area)

	#new_image = image.crop(x_size, x_size)
	#new_image.putalpha(prepare_mask(size_R, antialias))

	global pilimage
	pilimage = ImageTk.PhotoImage(new_image_crop)
	global imagesprite
	imagesprite = canvas.create_image(0,0,image=pilimage, anchor=NW)
	
scal8_2 = Scale(container, orient=HORIZONTAL, length=int(image.size[0]*0.6), from_=0, to=y_size_screen,
			tickinterval=50, resolution=10)
scal8_2.bind("<B1-Motion>", get_val_motion_8_2)
scal8_2.grid(column=5, row=4)

########################################################################

def my_callback3(): # показывает исходную фотографию
	#print('return button pushed')
	global pilimage
	pilimage = ImageTk.PhotoImage(image)
	global imagesprite
	#imagesprite = canvas.create_image(int(image.size[0]*kx_imagesprite),int(image.size[1]*kx_imagesprite),image=pilimage)
	imagesprite = canvas.create_image(0,0,image=pilimage, anchor=NW)

button3 = Button(container , text="Source Image" , command=my_callback3)
button3.grid(row=2 ,column=0)

########################################################################

def my_callback4(): # сохраняет результат
	file_name = filedialog.asksaveasfilename(initialdir = current_dir,
							filetypes = (("png files", "*.png"),
 										("jpg files", "*.jpg"), 
 										("bmp files", "*.bmp"),("all files", "*.*")), defaultextension="")
	global new_image
	new_image.save(file_name)

button4 = Button(container , text="Save Result" , command=my_callback4)
button4.grid(row=3 ,column=0)

########################################################################

def my_callback6(): # открыть новое маленькое изображение
	global filename
	filename = filedialog.askopenfilename(initialdir = current_dir, # initialdir = "/run/media/rick/DATA/Kazahi"
 				title = "Select imagefile", filetypes = (("JPG files", "*.JPG"),("jpeg files", "*.jpeg"),
 										("jpg files", "*.jpg"),("png files", "*.png"),
 										("bmp files", "*.bmp"),("all files", "*.*")))
	global image
	image = Image.open(filename).convert('L')
	

	image = image.resize((x_size_screen,y_size_screen)) #((540,540))
	
	global pilimage
	pilimage = ImageTk.PhotoImage(image)
	global imagesprite
	
	imagesprite = canvas.create_image(0,0,image=pilimage, anchor=NW)

button6 = Button(container , text="Open New Image" , command=my_callback6)
button6.grid(row=4 ,column=0)

########################################################################

def calibration_percert():
	N = 0 # счётчик
	new_im = []
	
	#global image
	#global new_image_crop

	image = new_image_crop ######
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if (image.getpixel((i,j)) >= 1) and (image.getpixel((i,j)) <= 255):
				N += 1
				new_im.append((i,j,image.getpixel((i,j))))
	
	percent = N/(image.size[0]*image.size[1])*100
	return percent

########################################################################

def my_callback7(): # главная функция - для расчёта маленького изображения
	N = 0 # счётчик
	new_im = []
	start = time() # для тестирования скорости работы

	#global new_image_crop

	image = new_image_crop ######
	
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if (image.getpixel((i,j)) >= L) and (image.getpixel((i,j)) <= M):
				N += 1
				new_im.append((i,j,image.getpixel((i,j))))
	
	percent = N/(image.size[0]*image.size[1])*100
	print("\nCurrent Percent = {0:.2f} %".format(percent))
	print("Time {0:.3f} s".format(float(round((time()-start)*1e3)/1e3))) # для тестирования скорости работы

	print("Calibration percent = {0:.2f} %".format(calibration_percert()))

	main_percent = (percent / calibration_percert())*100

	print("\nMain Percent = {0:.2f} %".format(main_percent))
	print("Max = ", M, "Min = ", L, "left-up = ", x_size, "right-down = ", y_size)

	global new_image # нужно для возможности сохранения в дальнейшем
	new_image = Image.new("L", (image.size[0], image.size[1]))
	for i in range(len(new_im)):
		new_image.putpixel((new_im[i][0], new_im[i][1]), new_im[i][2])

	global pilimage
	pilimage = ImageTk.PhotoImage(new_image)
	global imagesprite
	
	imagesprite = canvas.create_image(0,0,image=pilimage, anchor=NW)

button7 = Button(container , text="Result Image" , command=my_callback7)
button7.grid(row=1 ,column=0)


root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog
import random
import json

WIDTH, HEIGHT = 900, 900
topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None
n = 0
window = tk.Tk()
window.title("Выделение меток")
window.geometry('%sx%s' % (WIDTH, HEIGHT))
window.configure(background='grey')
marks = {}
k = []


class drawrect(object):
    def __init__(self, canvas, topx, topy, botx, boty, color):
        global s
        s = textExample.get("1.0", "end")
        self.canvas = canvas
        self.id = canvas.create_rectangle(
            topx, topy, botx, boty, fill='', outline=color, tags=(s, 'rect'), width=5)


def open_img():
    global canvas
    global rect_id
    path = filedialog.askopenfilename(title='open')
    img = Image.open(path)

    img = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(window, width=img.width(), height=img.height(),
                       borderwidth=0, highlightthickness=0)
    canvas.pack(expand=True)
    canvas.img = img
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    rect_id = canvas.create_rectangle(topx, topy, topx, topy,
                                      dash=(2, 2), fill='', outline='white')

    canvas.bind('<Button-1>', get_mouse_posn)
    canvas.bind('<B1-Motion>', update_sel_rect)


def get_mouse_posn(event):
    global topy, topx, item
    z = 0
    topx, topy = event.x, event.y
    item = canvas.find_closest(event.x, event.y)[0]
    # print(item)
    tags = canvas.gettags(item)
    # print(tags)


def update_sel_rect(event):

    global rect_id
    global topy, topx, botx, boty

    botx, boty = event.x, event.y
    canvas.coords(rect_id, topx, topy, botx, boty)


def drrect():
    global canvas, marks, k
    color1 = 'white'
    obj = drawrect(canvas,  topx, topy, botx, boty, color1)
    marks[obj.id] = obj
    print(topx, topy, botx, boty)


def new_tag():
    global item
    if item == 1 or item == 2:
        print(1)
    else:
        canvas.addtag_withtag(textExample.get("1.0", "end"), item)


def delete_tag():
    global item
    if item == 1 or item == 2:
        print(1)
    else:
        canvas.dtag(item, textExample.get("1.0", "end"))


def change_colors():
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    canvas.itemconfigure(textExample.get("1.0", "end"),
                         outline=random.choice(colors))


def change_colors1():
    canvas.itemconfigure(textExample.get("1.0", "end"), outline='white')


def delete_rectangle():
    global item
    if item == 1 or item == 2:
        print(1)
    else:
        canvas.delete(item)


def delete_img():
    canvas.destroy()
    list.clear(marks)


def lll():
    global marks
    for i in marks:
        tags = canvas.gettags(i)
        print(tags)
   # print(tags)


def saveToJSON():
    global marks
    with open("marks.json", "w") as jsonFile:
        json.dump(canvas.gettags(marks.values), jsonFile)
        print(canvas.gettags(marks.values))


textExample = tk.Text(window, width=15, height=1)
textExample.place(x=145, y=50)
openImgBut = Button(window, text='Открыть изображение',
                    command=open_img).place(x=1, y=1)
highlightAreaBut = Button(window, text='Выделить область ',
                          command=drrect).place(x=140, y=1)
setAreaBut = Button(window, text='Назначить выделение ',
                    command=change_colors).place(x=6, y=50)
deleteAreaBut = Button(window, text='Снять выделение ',
                       command=change_colors1).place(x=275, y=50)
deleteImgBut = Button(window, text='Удалить картинку ',
                      command=delete_img).place(x=1024, y=0)
deleteSquareBut = Button(window, text='Удалить квадрат ',
                         command=delete_rectangle).pack()
setTagBut = Button(window, text='Добавить тег', command=new_tag).pack()
deleteTagBut = Button(window, text='Удалить тег', command=delete_tag).pack()
outputInfBut = Button(window, text='У тег', command=lll).pack()
convertJSONTag = Button(window, text='Super slaves', command=saveToJSON).pack()


window.mainloop()

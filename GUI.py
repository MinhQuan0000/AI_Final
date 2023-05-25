import numpy as np
import matplotlib.pyplot as plt
from keras.models import  load_model
from keras.utils import load_img, img_to_array
from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

doan=load_model('C:\\Users\\Admin\\Documents\\AI\\emtion\\nhandancamxucR.h5')
img =0
def dich():
    global doan
    global img
    #lb1.config('')
    vat = {1: 'angry',2:'disgusted', 3:'fearful', 4:'happy', 5:'neutral', 6:'sad', 7:'suprised' }
    result  = np.argmax(doan.predict(img),axis=1)
    lb1.config(text=' {} emotion'.format(vat[result[0]]))



    #textbox.insert(1.0, s)
def doi():
    global img
    filename=askopenfilename(initialdir='c:\\python31\\',filetypes=[('jpg files', '.jpg')])
    load = Image.open(filename)
    load=load.resize((200,100))
    render = ImageTk.PhotoImage(load)
    img = load_img(filename,target_size=(30,40))
    plt.imshow(img)
    img = img_to_array(img)
    img=img.reshape(1,30,40,3)
    img = img.astype('float32')
    img =img/255
    ketqua.configure(image=render)
    ketqua.image = render
    DOI["state"] = "normal"
    lb1.config(text='')

def xoa():
    global ketqua
    ketqua.destroy()
    ketqua= Label()
    ketqua.place(x=50, y=215)
    DOI["state"] = DISABLED
    lb1.config(text='')
    #pass

root = Tk()
root.geometry("1000x600")


lb1 = Label(text='',font=('times',30))
lb2 = Label(text='Kết quả',font=('times',30))

ketqua= Label()

lb3 = Label(text='Ảnh Cần Xác Định',font=('times',24))
lb4 = Label(text='=>',font=('times',50))

lb4.place(x=425, y=250)
lb3.place(x=50, y=50)


ketqua.place(x=50, y=215)
lb1.place(x=600, y=250)
lb2.place(x=650, y=50)


#dele
xoa = Button(text='Xóa/Hủy', font=('Verdana', 24),command=xoa)
xoa.place(x=400, y=450)

chuyen = Button(text='Chọn ảnh', font=('Verdana', 24),command=doi)
chuyen.place(x=50, y=450)

#ĐỔI
DOI = Button(text='Định Dạng', font=('Verdana', 24),command=dich)
DOI.place(x=700, y=450)

DOI["state"] = DISABLED


    
mainloop()
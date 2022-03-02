from tkinter import *
from PIL import ImageTk, Image


root=Tk()
root.title("Attēlu galerija")
root.iconbitmap("C:/Users/Skolnieks/Desktop/Sanija Feodosova/02.03.2022 attelu galerija/kirsis.ico")

attels1=ImageTk.PhotoImage(Image.open('bildes/bilde_v.png'))
attels2=ImageTk.PhotoImage(Image.open('bildes/bilde_d.png'))
attels3=ImageTk.PhotoImage(Image.open('bildes/bilde_t.png'))

atteli=[attels1, attels2, attels3]

atteli[2]

nosaukums=Label(image=attels1)
nosaukums.grid(row=0,column=0,columnspan=3)
status=Label(root,text="Bildes 1 no"+str(len(atteli)), bd=1, relief=SUNKEN, anchor=E)


#Definēju funkciju, kas šķir bildes uz priekšu

def forward(image_number):
    global nosaukums
    global button_back
    global button_forward

    nosaukums.grid_forget()
    nosaukums=Label(image=atteli[image_number-1])

    button_forward=Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda:back(image_number-1))

#ko darīt lai pēdējo bildi pašķirot nav tukšums
    if image_number==3:
        button_forward=Button(root, text=">>", state=DISABLED)

    nosaukums.grid(row=1, column=0, columnspan=3)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status=Label(root, text="Bildes" + str(image_number) + " no " + str(len(atteli)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    return 

def back(image_number):
    global nosaukums
    global button_forward
    global button_back
    
    nosaukums.grid_forget()
    nosaukums=Label(image=atteli[image_number-1])

    button_forward=Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda:back(image_number-1))

    status=Label(root, text="Bildes " + str(image_number) + " no " + str(len(atteli)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    if image_number==1:
        button_forward=Button(root, text="<<", state=DISABLED)

    nosaukums.grid(row=1, column=0, columnspan=3)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    return


poga_iziet=Button(root, text="Iziet", command=root.quit)

button_back=Button(root, text="<<", command=back, state=DISABLED)
button_forward=Button(root, text=">>", command=lambda:forward(2))


button_back.grid(row=1, column=0)
poga_iziet.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2,column=0, columnspan=3)

root.mainloop()
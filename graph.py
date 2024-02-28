import tkinter as tk
from tkinter import ttk
from math import *
import time

def launch_App(window):
    global check

    def Graph_(window,s):
        global unitX , unitY , f , check

        frame_.destroy()

        frame = tk.Frame(window,bg='light blue')

        if True:
            #height = window.winfo_screenheight()
            #width = window.winfo_screenwidth()

            height = 500
            width = 500

            LabelVar = tk.StringVar(window)

            label = tk.Label(frame,background='light green')

            def fonction2():
                try :
                    label.config(text='Graph Maker')
                    window.after(1000,fonction3)
                except:
                    pass
            
            def fonction3():
                try:
                    label.config(text='. Graph Maker .')
                    window.after(1000,fonction4)
                except:
                    pass
            
            def fonction4():
                try:
                    label.config(text='. . Graph Maker . .')
                    window.after(1000,fonction5)
                except:
                    pass
            
            def fonction5():
                try:
                    label.config(text='. . . Graph Maker . . .')
                    window.after(1000,fonction2)
                except:
                    pass
            
            fonction2()

            label.grid(row=0,column=0,sticky='news')

            canvas = tk.Canvas(frame,width=width,height=height,bg='#EEEEEE')
            canvas.grid(row=1,column=0)

            points = {}
            i=width/2
            while i<=width:
                canvas.create_line((i,0,i,height),fill='#8DE0E0',activefill='blue')
                canvas.create_line((width -i,0,width -i,height),fill='#8DE0E0',activefill='blue')
                i += unitX

            i=height/2
            while i<=height:
                canvas.create_line((0,i,width,i),fill='#8DE0E0',activefill='blue')
                canvas.create_line((0,height-i,width,height-i),fill='#8DE0E0',activefill='blue')
                i += unitY


            canvas.create_line((width/2+unitX,height/2-5,width/2+unitX,height/2+5),fill='black',activefill='white')
            canvas.create_line((width/2-5,height/2-unitY,width/2+5,height/2-unitY),fill='black',activefill='white')
            for i in range(-(width//2 +1)*10,(width//2 +1)*10):
                try:
                    x=i/(unitX*10)
                    x1=(i+1)/(unitX*10)
                    y=f(x)*unitY
                    y1=f(x1)*unitY
                    x=x*unitX
                    x1=x1*unitX
                    points[x] = canvas.create_line((width/2+x,height/2-y),(width/2+x1,height/2-y1),fill='#EB5956')
                except :
                    pass


            canvas.create_line((0,height/2,width,height/2),fill='black',activefill='white')
            canvas.create_line((width/2,0,width/2,height),fill='black',activefill='white')

            frame1 = tk.Frame(frame,bg='light green')
            frame1.grid(row=2,column=0,sticky='news')

            widthf = frame1.winfo_width()

            label1 = tk.Label(frame1,bg='light green',text='   f(')
            label2 = tk.Label(frame1,bg='light green')
            label3 = tk.Label(frame1,bg='light green',text=') = !')
            entry4 = tk.Entry(frame1,bg='white',width=3,relief='flat')

            label1.pack(side='left')
            entry4.pack(side='left')
            label3.pack(side='left')
            label2.pack(side='right')

            def update(n):
                timeS = time.strftime("%I:%M %p %d-%m-%Y   ")
                label2.config(text=timeS)
                try:
                    yy = f(float(entry4.get()))
                except :
                    yy = '!'
                label3.config(text=') = '+str(yy))
                if check:
                    if check_var.get():
                        for i0 in points:
                            canvas.delete(points[i0])
                        for i in range(-(width//2 +1)*10,(width//2 +1)*10):
                            try:
                                x=i/(unitX*10)
                                x1=(i+1)/(unitX*10)
                                y=f(x+n)*unitY
                                y1=f(x1+n)*unitY
                                x=x*unitX
                                x1=x1*unitX
                                points[x] = canvas.create_line((width/2+x,height/2-y),(width/2+x1,height/2-y1),fill='#EB5956')
                            except :
                                pass
                n += 1
                window.after(1000,lambda : update(n))

            update(0)

            def fonction6(event):
                label1.config(text=f'   x = {round((event.x - width / 2)/unitX,2)}   ;   y = {round(-(event.y - height / 2)/unitY,2)}   ;  f(')

            canvas.bind('<Motion>',fonction6)

        def fonction(_):
            frame__.destroy()
            frame.pack()
            label00 = tk.Label(window,text='by OUAZENE ABDELMOHSEN',bg='light green')
            label00.pack(expand=True,fill='both')
        
        frame__ = tk.Frame(window,width=500,height=600,bg='light green')
        frame__.pack(expand=True,fill='both')

        Label = tk.Label(frame__,text=f"""
                        
    - Unit of Axe X = {unitX}
    - Unit of Axe Y = {unitY}

    - The function : 
        f(x) = {s}




        Created By OUAZENE-2065
                        
                        Monday December 11th,2023
    """,bg='light green',width=30,font=('Ink free',16,'bold'))
        Label.pack(padx=10,pady=5,expand=True,fill='both')

        Button = tk.Label(frame__,text='Design The Graph',bg='#3078A6',fg='white')
        Button.pack(padx=10,pady=5,ipadx=20,ipady=10)

        Button.bind('<Button-1>',fonction)

    height = 580
    width = 505
    if check:
        window2 = tk.Tk()
    else :
        window2 = tk.Toplevel(window)
    window2.title('GRAPH MAKER')
    window2.geometry(f'{width}x{height}+{int(window2.winfo_screenwidth()/2 - width/2)}+{int(window2.winfo_screenheight()/2 - height/2)}')
    window2.resizable(False,False)

    project_icon = tk.PhotoImage(file=r"textures\apps_images\graph\icon.png")
    window2.iconphoto(False, project_icon)

    frame_ = tk.Frame(window2)
    frame_.pack(padx=10,pady=10,expand=True,fill='both')

    frame2 = tk.Frame(frame_)
    frame2.pack(padx=10,pady=10)

    label11 = ttk.Label(frame2,text='Enter the unit of Axe X : ',font=('Ink free',11,'bold'))
    label11.grid(row=0,column=0,padx=10,pady=15)
    entry1 = ttk.Entry(frame2,font=('Ink free',13,'bold'),width=8)
    label12 = ttk.Label(frame2,text='Enter the unit of Axe Y : ',font=('Ink free',11,'bold'))
    label12.grid(row=0,column=1,padx=10,pady=15)
    entry2 = ttk.Entry(frame2,font=('Ink free',13,'bold'),width=8)
    entry1.grid(row=1,column=0,padx=10,pady=5)
    entry2.grid(row=1,column=1,padx=10,pady=5)

    label13 = ttk.Label(frame2,text='Enter the function (exepression in Python): ',font=('Ink free',13,'bold'))
    label13.grid(row=2,column=0,columnspan=2,padx=10,pady=15)
    entry3 = ttk.Entry(frame2,width=15,font=('Ink free',30))
    entry3.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

    def fonctionV():
        try : 
            global unitX , unitY , f , Var
            unitX = float(entry1.get())
            unitY = float(entry2.get())
            s= entry3.get()
            def f(x):
                return eval(s)
            if unitX:
                if unitY:
                    if f:
                        frame_.destroy()
                        Graph_(window2,s)
        except :
            label16.config(text='Error in values')
            entry1.delete(0,"end")
            entry2.delete(0,"end")
            try :
                label16.after(3000,lambda : label16.config(text=''))
            except:
                pass
    if check:
        check_var = tk.BooleanVar(window2,False)
        check_button = tk.Checkbutton(frame_,text='Do you want to simulate "oscilloscope" ? \n(not recommended)',variable=check_var,foreground='#FF7714',font=('Ink free',14,'bold'))
        check_button.pack(padx=10,pady=15)
    Button = ttk.Button(frame_,text='Valid',command=fonctionV,width=20)
    Button.pack(padx=10,pady=15)
    label16 = tk.Label(frame_,font=('Ink free',14,'bold'),fg='red')
    label16.pack(padx=10,pady=15)
    label14 = ttk.Label(frame_,text='by OUAZENE ABDELMOHSEN',font=('Ink free',16,'bold'))
    label14.pack(side='bottom')

    if check:
        window2.mainloop()
    else : return window2

check = False

if __name__ == "__main__":
    check = True
    launch_App(0)

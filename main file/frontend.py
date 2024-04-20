from tkinter import *
import backend
from tkinter import messagebox
db1 = backend.database('D:/python project/learning center/learningcenter.db')
root = Tk()
root.geometry('800x400')
root.title('فرم ثبت نام')
root.resizable(0,0)
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight() 
window_width = 800
window_height = 400
x = (screen_width - window_width) / 2
y = (screen_height - window_height) / 2
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

#function
def itemshowing():
    listbox_.delete(0,END)
    records = db1.fetch()
    for i in records:
        listbox_.insert(END,i)

def clear():
    name_entry.delete(0,END)
    lastname_entry.delete(0,END)
    pass_entry.delete(0,END)
    dore_entry.delete(0,END)
    passin_entry.delete(0,END)




def insert():
    if name_entry.get() == '' or lastname_entry.get() == '' or pass_entry.get() == '':
        messagebox.showerror('نام و نام خانوادگی و رمز ورود را پر کنید','نام و نام خانوادگی و رمز ورود را پر کنید')
    else:
        db1.insert(name_entry.get(),lastname_entry.get(),pass_entry.get(),dore_entry.get())
        listbox_.insert(END,(name_entry.get() , lastname_entry.get() , pass_entry.get() , dore_entry.get()))
        clear()
        itemshowing()



def exitapp():
    res = messagebox.askquestion('EXIT?','ARE YOU SURE')
    if res == 'yes':
        root.destroy()
    else:
        pass

def selecteditem(event):
    global usedseleceditem
    global select
    index = listbox_.curselection()
    select = listbox_.get(index)
    clear()
    name_entry.insert(END,select[1])
    lastname_entry.insert(END,select[2])
    pass_entry.insert(END,select[3])
    dore_entry.insert(END,select[4])


def deleteitem():
    global usedseleceditem
    result = messagebox.askquestion('delete','ARE YOU SURE?')
    if result == 'yes':
        db1.remove(select[0])
        clear()
        itemshowing()



def passin():
    passinget = passin_entry.get()
    passinget2 = pass_entry.get()
    if passinget == '123456789' or passinget2 == '123456789':
        top = Toplevel(root)
        top.resizable(0,0)
        screen_width = top.winfo_screenwidth() 
        screen_height = top.winfo_screenheight() 
        window_width = 200
        window_height = 200
        x = (screen_width - window_width) / 2
        y = (screen_height - window_height) / 2
        top.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        top.title('')
        welcom = Label(top,text='!!!خوش آمدید')
        welcom.pack()
        info = Label(top,text='ساخته شده توسط امیر مهدی طاعتی',font="arial 10")
        info.place(x=22,y=180)
        top.mainloop()
    else:
        messagebox.showerror('the pass isnt right','The password isnt right TRY AGAIN!!')
        
#labels
lastname_label = Label(root,text=':نام خانوادگی')
lastname_label.place(x=230,y=10)

name_label = Label(root,text=':نام')
name_label.place(x=680,y=10)

pass_label = Label(root,text=':رمز ورود')
pass_label.place(x=230,y=50)

dore_label = Label(root,text=':نام دوره')
dore_label.place(x=680,y=50)

passin_label = Label(root,text=':رمز ورود')
passin_label.place(x=530,y=350)

name_star = Label(root,text='*',fg='red')
name_star.place(x=710,y=10)

lastname_star = Label(root,text='*',fg='red')
lastname_star.place(x=330,y=10)

pass_star = Label(root,text='*',fg='red')
pass_star.place(x=300,y=50)
#entry
name_entry = Entry(root)
name_entry.place(x=490,y=10)

lastname_entry = Entry(root)
lastname_entry.place(x=50,y=10)

pass_entry = Entry(root)
pass_entry.place(x=50,y=55)

dore_entry = Entry(root)
dore_entry.place(x=490,y=55)

passin_entry = Entry(root,width=50)
passin_entry.place(x=50,y=350)


#buttons
show_item = Button(root,text='مشاهده همه',width=25,command=itemshowing)
show_item.place(x=490,y=100)

insert_item = Button(root,text='اضافه کردن',width=25,command=insert)
insert_item.place(x=490,y=140)

clear_item = Button(root,text='خالی کردن ورودی ها',width=25,command=clear)
clear_item.place(x=490,y=180)

delete_item = Button(root,text='حذف کردن',width=25,command=deleteitem)
delete_item.place(x=490,y=220)

exit_item = Button(root,text='خروج',width=25,command=exitapp)
exit_item.place(x=490,y=260)

enter_item = Button(root,text='ورود به سامانه',width=25,command=passin)
enter_item.place(x=490,y=300)







#listbox
listbox_ = Listbox(root,width=50)
listbox_.place(x=50,y=110)
listbox_.bind('<<ListboxSelect>>',selecteditem)

root.mainloop()


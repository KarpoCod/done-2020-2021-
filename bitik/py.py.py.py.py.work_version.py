from tkinter import*
import random
#####################################################################
tk=Tk()
tk.title('MEGA RANDOMAISER 3000')
tk.geometry('1000x500')
tk.resizable(False, False)
#####################################################################
main_text = Label(tk,text='Считывать с : файл/консоль',font='arial, 19')
data_path = StringVar()
vvod_entry = Entry(tk,width=30,bd=5,textvariable=data_path)
main_text.pack(expand = True, side=TOP)
vvod_entry.pack(fill=X)
text_groups = Text(width=40, height=5, wrap=WORD)
scroll_text = Scrollbar(command=text_groups.yview)
text_groups.config(yscrollcommand=scroll_text.set)
#####################################################################
buttonR = Button(tk, text = 'Рестарт', width = 50)
buttonE = Button(tk, text = 'Выход', width = 50)
#####################################################################
num_of_st = 0
num_of_groups=0
num_of_members=0
choice=''
groups= []
st=[]
#####################################################################
def RandGroup():
    global st, groups, num_of_groups, num_of_mmembers
    for g in range(1,num_of_groups+1):
        groups [g] = [ ]
        for s in range(num_of_members):
            try:
                name = random.choice(st)
            except IndexError:
                groups[g].append(' ')
            else:
                if name not in groups[g]:
                    groups[g].append(name)
                    st.remove(name)
        if g == num_of_groups:
            if len (st)!=0:
                groups[num_of_groups+1]=[]
                for i in st:
                    groups[num_of_groups+1].append(i)
                st.clear()      
    return output_groups(), groups_write()

def GroupWrite():
    with open('uchastniki.txt',encoding='utf-8')as file:
        for g in groups.keys():
            file.write('\nГруппа #'+str(g)+':')
            for p in groups[g]:
                file.write(p+'; ')
    return None

def output_groups():
    scroll_text.pack(fill=Y,side=RIGHT)
    main_text.pack_forget()
    main_text.config(text='Результат: ')
    main_text.pack(expand=False, side=TOP)
    text_groups.pack(expand=True, side=TOP, fill=Y)
    buttonE.pack(padx = 10,pady = 10,side=BOTTOM)
    text_groups.configure(state='normal')
    for g in groups.keys():
        text_groups.insert(INSERT,'\nГруппа #'+str(g)+':\n')
        for p in groups[g]:
            text_groups(INSERT,p+'; ')
    text_groups.configure(state='disabled')
    return None

def restart(event):
    global num_of_st, num_of_groups, num_of_members, choice, groups
    text_groups.configure(state='normal')
    text_groups.delete(1.0, END)
    text_groups.pack_forget()
    text_groups.configure(state='disabled')
    scroll_text.pack_forget()
    buttonE.pack_forget()
    buttonR.pack_forget()
    main_text.config(text='Считывать с : файл/консоль')
    main_text.pack(expand = True, side=TOP)
    vvod_entry.pack(fill=X)
    groups.clear()
    num_of_st = 0
    num_of_groups=0
    num_of_members=0
    choice=''
    return None

def exit_p(event):
    return tk.destroy()

def read_path(event):
    global num_of_st, num_of_groups, num_of_members, choice, st
    if choice != True:
        if data_path.get() == 'файл':
            main_text.config(text='Введи имя файла:')
            choice = 'ф'
        elif choice == 'ф':
            try:
                with open (data_path.get(),encoding='utf-8') as file:
                    for line in (file):
                        line=line.rstrip('\n')
                        st=line.split(' ')
                num_of_st=len(st)
                choice = True
            except FileNotFoundError:
                main_text.config(text='файл не найден, попробуйте другое имя:')
        elif data_path.get() == 'консоль':
            main_text.config(text='Сколько участников?')
            choice = 'к'
        elif (choice == 'к') and (num_of_st==0):
            num_of_st = int(data_path.get())
            if len(st)==num_of_st:
                choice = True
        if (choice == True):
            main_text.config(text='Ввидите число команд:')
    else:
        if (num_of_groups != 0)and(num_of_members == 0):
            if data_path.get().isdigit():
                num_of_members=int(data_path.get())
            else:
                num_of_meembers=int(num_of_st/num_of_groups)
            vvod_entry.pack_forget()
            RandGroup()
        elif num_of_groups == 0:
            num_of_groups = int(data_path.get())
            main_text.config(text='Как разбить группы(поровну\число)')
    return vvod_entry.delete(0, END)
#####################################################################
buttonR.bind('<Button-1>', restart)
buttonE.bind('<Button-1>', exit_p)
vvod_entry.focus_set()
tk.bind('<Return>', read_path)
tk.mainloop()
#####################################################################

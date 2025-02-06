from tkinter import*
import random

tk=Tk()
tk.title('MEGA RANDOMAISER 3000')
tk.geometry('1000x500')
num_of_groups=1
num_of_st = 0
st=[]
auto_mode=2
num_of_members=' '


def auto():
    global auto_mode
    auto_mode=1

def not_auto():
    global auto_mode
    auto_mode=0
choise_info_text=Label(tk,text='1-Я крутой составлю списки сам. 2-я ленивый и возьму из файла.',font=('Times New Roman',20), state='normal')
not_auto = Button(tk, text='1', font=('Times New Roman',25), bg='black', fg='white', command=not_auto(), state='normal')
auto = Button(tk, text='2', font=('Times New Roman',25), bg='black', fg='white', command=auto(),state='normal')
ex = Button(tk, text='Закрыть', font=('Times New Roman',15), bg='black', fg='white', command=exit)
ex.grid(column=2,row=8)
auto_mode=2
def start():
    choise_info_text.grid(column=2,row=1)
    auto.grid(column=4,row=3)
    not_auto.grid(column=1,row=3)
start()
while auto_mode==1 or auto_mode==0 or auto_mode==2:
    if auto_mode==0:
        choise_info_text(text='Сколько людей,А? ')
        choise_info_text.grid(column=1,row=1)
        A_num_of_st = Entry(tk,width=40)
        A_num_of_st.grid(column=1,row=3)
        A_num_of_st.focus()
        for i in range(num_of_st):
            st.append(' ')
            st[i]=input('Имя, фамилия? ')

    elif auto_mode==1:
        with open('uchastniki.txt',encoding='utf-8')as file:
            for line in (file):
                num_of_st=num_of_st+1
                line=line.rstrip('\n')
                st=line.split(' ')
    num_of_groups = int(input('кол-во команд'))
    num_of_members = input('кол-во участников (число\нет)')
    if num_of_members.isdigit():
        num_of_members=int(num_of_members)
    else:
        num_of_members=int(num_of_st/num_of_groups)
    groups = { }
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
                console_write(num_of_groups+1)

        print ('\nГруппа '+str(g)+':',end=' ')
        for p in groups[g]:
            print (p,end='; ')
    auto_mode=2
    tk.mainloop()


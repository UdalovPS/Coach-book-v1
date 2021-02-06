from tkinter import *
import tkinter.messagebox as mb


class DelMessage():
    def __init__(self, title='Delete',
                 message='Do you want to delete data'):
        self.del_msg = mb.askyesno(title, message)


class ScrollFrame(Frame):
    def __init__(self, master):
        frame1 = LabelFrame(master)
        frame1.pack(fill=BOTH, expand='YES', padx=5)
        canvas = Canvas(frame1)
        canvas.pack(side=LEFT, fill=BOTH, expand='YES')
        scroll = Scrollbar(frame1, orient='vertical',
                   command=canvas.yview, width=20)
        scroll.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scroll.set)
        canvas.bind('<Configure>',
                    lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        Frame.__init__(self, canvas)
        canvas.create_window((0, 0), window=self, anchor='nw')

class DateTimeFrame(LabelFrame):
    def __init__(self, master):
        LabelFrame.__init__(self, width=250)
        self.pack(side=LEFT, fill=Y)

class MiniFrame(Frame):
    def __init__(self, master):
        LabelFrame.__init__(self, master)
        self.pack(side=TOP, fill=X)


class HeadFrame(LabelFrame):
    def __init__(self, master, head_text, size=[10, 20, 50]):
        LabelFrame.__init__(self, master)
        self.pack(fill=X)
        count = 0
        for text in head_text:
            Label(self, text=text, width=size[count],
                  relief=RAISED,  font='20'
                  ).pack(side=LEFT, fill=Y)
            count += 1


class MyLabel(Label):
    def __init__(self, master, text, width):
        Label.__init__(self, master, text=text, width=width,
                       relief=RAISED,  font='20')
        self.pack(side=LEFT)


class MyFrame(Frame):
    def __init__(self, master=None, text=None, bg=None,
                 size=[10, 20, 20, 20]):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
        count = 0
        for item in text:
            Label(self, text=item, width=size[count],
                      relief=RAISED,  font='20',bg=bg
                  ).pack(side=LEFT)
            count += 1



class MyTk(Tk):
    def __init__(self, title=None, head_text=None,
                 date=None, time=None, members=None,
                 ch_btn_text=None, back_btn_text=None,
                 del_btn_text=None, key=None, back_btn_cmd=None,
                 change_btn_cmd=None, index=None,
                 del_btn_cmd=None, del_msg=None,
                 bg=('white', 'light green')):
        Tk.__init__(self)
        self.del_msg = del_msg
        self.del_btn_cmd = del_btn_cmd
        self.index = index
        self.change_btn_cmd = change_btn_cmd
        self.back_btn_cmd = back_btn_cmd
        self.key = key
        h_frame = HeadFrame(self, head_text=head_text)
        save_btn = Button(h_frame, text=ch_btn_text,
                          command=lambda: (self.change_cmd()),
                          font='Times 20').pack(side=LEFT)
        del_btn = Button(h_frame, text=del_btn_text,
                         command=lambda: (self.delete_cmd()),
                         font='Times 20').pack(side=LEFT)
        back_btn = Button(h_frame, text=back_btn_text,
                          command=lambda: (self.back_cmd()),
                          font='Times 20').pack(side=RIGHT)
        d_t_frame = DateTimeFrame(self)
        d_mini = MiniFrame(d_t_frame)
        mem_frame = ScrollFrame(self)
        date_lbl = MyLabel(d_mini, date, width=10)
        time_lbl = MyLabel(d_mini, time, width=20)
        number = 1
        for item in members:
            item.insert(0, number)
            MyFrame(mem_frame, text=item, bg=bg[number % 2])
            number += 1
        self.title(title)
        self.geometry('1500x500')
        self.mainloop()

    def back_cmd(self):
        self.destroy()
        self.back_btn_cmd(self.key)

    def change_cmd(self):
        self.destroy()
        self.change_btn_cmd(self.key, self.index)

    def delete_cmd(self):
        del_msg = mb.askyesno(title=self.del_msg[0],
                              message=self.del_msg[1])
        if del_msg:
            self.del_btn_cmd(self.key, self.index)
            self.destroy()
            self.back_btn_cmd(self.key)




if __name__ == '__main__':
    head_text = {'title': 'training',
                 'head': ['date', 'time', 'students'],
                 'change': 'change', 'back': 'back',
                 'del': 'delete'
                 }
    data_text = ['10.10.2020', '10:30',
                 [['Tomson', 'Tom', 'Tomas'],
                  ['Gregory', 'Greg', 'Grue']]
                 ]
    test = MyTk(title=head_text['title'], date=data_text[0],
                time=data_text[1], members=data_text[2],
                head_text=head_text['head'],
                ch_btn_text=head_text['change'],
                back_btn_text=head_text['back'],
                del_btn_text=head_text['del'])

from tkinter import *
import tkinter.messagebox as mb


class DateError():
    def __init__(self, title, message):
        mb.showerror(title, message)


class SaveMessage():
    def __init__(self, title='information',
                 message='data is save'):
        self.save_msg = mb.showinfo(title, message)


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
                  relief=RAISED, font='20').pack(side=LEFT, fill=Y)
            count += 1


class MyEntry(Entry):
    def __init__(self, master, text, width):
        Entry.__init__(self, master, width=width,
                       relief=RAISED, font='20')
        self.insert(0, text)
        self.pack(side=LEFT)


class MyFrame(Frame):
    def __init__(self, master=None, text=None,
                 size=[10, 20, 20, 20], bg=None):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
        count = 0
        for item in text:
            Label(self, text=item, width=size[count], font='20',
                      relief=RAISED, bg=bg).pack(side=LEFT)
            count += 1


class MyChek(Checkbutton):
    def __init__(self, master, var):
        Checkbutton.__init__(self, master, variable=var)
        self.pack(side=LEFT)


class MyTk(Tk):
    def __init__(self, title=None, head_text=None,
                 date=None, time=None, members=None,
                 ch_btn_text=None, back_btn_text=None,
                 back_btn_cmd=None, key=None, index=None,
                 save_btn_cmd=None, bg=('white', 'light green'),
                 error_date_text=None, save_msg=None):
        Tk.__init__(self)
        self.save_msg = save_msg
        self.error_date_text = error_date_text
        self.save_btn_cmd = save_btn_cmd
        self.index = index
        self.key = key
        self.back_btn_cmd = back_btn_cmd
        h_frame = HeadFrame(self, head_text=head_text)
        save_btn = Button(h_frame, text=ch_btn_text,
                          command=lambda: (self.save()),
                          font='Times 20').pack(side=LEFT)
        back_btn = Button(h_frame, text=back_btn_text,
                          command=lambda: (self.back_cmd()),
                          font='Times 20').pack(side=RIGHT)
        d_t_frame = DateTimeFrame(self)
        d_mini = MiniFrame(d_t_frame)
        mem_frame = ScrollFrame(self)
        self.date_ent = MyEntry(d_mini, date, width=10)
        self.time_ent = MyEntry(d_mini, time, width=20)
        number = 1
        self.var_list = []
        self.index_list = []
        for item in members:
            item.insert(0, number)
            self.frame = MyFrame(mem_frame, text=item,
                                 bg=bg[number % 2])
            self.item = BooleanVar()
            chek = MyChek(self.frame, self.item)
            self.index_list.append(number - 1)
            self.var_list.append(self.item)
            number += 1
        self.title(title)
        self.geometry('1300x500')
        self.mainloop()

    def back_cmd(self):
        self.destroy()
        self.back_btn_cmd(self.key)


    def save(self):
        var_list = []
        date_time = [self.date_ent.get(), self.time_ent.get()]
        for i in self.var_list:
            var_list.append(i.get())
        var_dict = dict(zip(self.index_list, var_list))
        try:
            self.save_btn_cmd(self.key, date_time, var_dict,
                              self.index)
        except (ValueError, IndexError, AttributeError):
            date_error = DateError(self.error_date_text[0],
                                   self.error_date_text[1])
        else:
            SaveMessage(title=self.save_msg[0],
                        message=self.save_msg[1])


if __name__ == '__main__':
    head_text = {'title': 'training',
                 'head': ['date', 'time', 'students'],
                 'save': 'save', 'back': 'back'
                 }
    data_text = ['10.10.2020', '10:30',
                 [['Tomson', 'Tom', 'Tomas'],
                  ['Gregory', 'Greg', 'Grue']]
                 ]
    test = MyTk(title=head_text['title'], date=data_text[0],
                time=data_text[1], members=data_text[2],
                head_text=head_text['head'],
                ch_btn_text=head_text['save'],
                back_btn_text=head_text['back'])

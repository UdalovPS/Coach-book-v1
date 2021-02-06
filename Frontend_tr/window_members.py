from tkinter import *
import tkinter.messagebox as mb

class SaveMessage():
    def __init__(self, title='information',
                 message='data is save'):
        self.save_msg = mb.showinfo(title, message)

class ScrollFrame(Frame):
    def __init__(self, master):
        frame1 = LabelFrame(master)
        frame1.pack(fill=BOTH, expand='YES', padx=10)
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

class HeadFrame(Frame):
    def __init__(self, master=None, head_text=None,
                 wdg_size=None, color=None, number=0,
                 btn_text=None, key=None, details_cmd=None):
        count = 0
        Frame.__init__(self, master, padx=5)
        self.pack(fill=X)
        Label(self, width=1).pack(side=LEFT)
        for name in head_text:
            Label(self, text=name, padx=5, pady=5, font='20',
                  relief=RAISED, width=wdg_size[count],
                  bg=color).pack(side=LEFT)
            count += 1

class MyFrame(Frame):
    def __init__(self, master=None, head_text=None,
                 wdg_size=None, color=None, number=0,
                 btn_text=None, key=None, details_cmd=None,
                 main_tk=None, bg=None):
        self.main_tk = main_tk
        self.master = master
        self.details_cmd = details_cmd
        count = 0
        Frame.__init__(self, master, padx=5)
        self.pack(fill=X)
        for name in head_text:
            Label(self, text=name, padx=5, pady=5, font='20',
                  relief=RAISED, width=wdg_size[count],
                  bg=bg).pack(side=LEFT)
            count += 1


class MyChek(Checkbutton):
    def __init__(self, master, var):
        Checkbutton.__init__(self, master, variable=var)
        self.pack(side=LEFT)

class MyTk(Tk):
    def __init__(self, title=None, head_text=None,
                 wdg_size=[5, 30, 30, 30, 30, 10, 15, 10],
                 data_text=None, save_btn_text=None,
                 back_btn_text=None, key=None,
                 back_btn_cmd=None, save_btn_cmd=None,
                 save_msg=None, bg=('white', 'light green')):
        self.save_msg = save_msg
        self.save_btn_cmd = save_btn_cmd
        self.back_btn_cmd = back_btn_cmd
        self.key = key
        Tk.__init__(self)
        head_frame = HeadFrame(self, head_text, wdg_size)
        mbrs_btn = Button(head_frame, text=save_btn_text,
                          command=lambda: (self.add_members()),
                          font='Times 20').pack(side=LEFT)
        back_btn = Button(head_frame, text=back_btn_text,
                          command=lambda: (self.back_cmd()),
                          font='Times 20').pack(side=RIGHT)
        number = 1
        if data_text:
            scroll_frame = ScrollFrame(self)
            self.var_list = []
            self.person_key_list = []
            for item in data_text:
                data_text[item].insert(0, number)
                self.frame = MyFrame(scroll_frame, data_text[item],
                                     wdg_size, number, key=item,
                                     main_tk=self, bg=bg[number % 2])
                self.item = BooleanVar()
                chek = MyChek(self.frame, self.item)
                number += 1
                self.person_key_list.append(item)
                self.var_list.append(self.item)
        self.title(title)
        self.geometry('1900x300')
        self.mainloop()

    def add_members(self):
        var_list = []
        for i in self.var_list:
            var_list.append(i.get())
        var_dict = dict(zip(self.person_key_list, var_list))
        self.save_btn_cmd(self.key, var_dict)
        SaveMessage(self.save_msg)

    def back_cmd(self):
        self.destroy()
        self.back_btn_cmd(self.key)


if __name__ == '__main__':
    head_text = {'title': 'add members',
                 'head': ['№', 'Tlast name', 'Tfirst name',
                              'Tpatronymic','Tbirthdate',
                              'Tweight', 'Tbelt'],
                 'save': 'save', 'back': 'back',
                 'save_msg': ['Save', 'data is save']
                 }
    data_text = {'student_0': ['Tomson', 'Tom', 'Tomas',
                               '01.01.2020', '20', 'white'],
                 'student_1': ['Daniels', 'Dan', 'Daniel',
                              '06.06.2006', '80', 'brown'],
                 'student_2': ['Daniels', 'Dan', 'Daniel',
                              '06.06.2006', '80', 'brown'],
                 'student_3': ['Daniels', 'Dan', 'Daniel',
                              '06.06.2006', '80', 'brown'],
                 'student_4': ['Daniels', 'Dan', 'Daniel',
                              '06.06.2006', '80', 'brown'],
                 'student_5': ['Daniels', 'Dan', 'Daniel',
                              '06.06.2006', '80', 'brown']}
    test = MyTk(title=head_text['title'],
                head_text=head_text['head'],
                data_text=data_text,
                save_btn_text=head_text['save'],
                back_btn_text=head_text['back'])

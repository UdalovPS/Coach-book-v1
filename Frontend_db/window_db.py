"""
This module is about TopLevel window DataBase.
DataBase window shows information about all students
    in database.
"""

from tkinter import *

class MyEntry(Entry):
    def __init__(self, master):
        Entry.__init__(self, master, font='20')
        self.pack(side=LEFT)


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


class NewButton(Frame):
    def __init__(self, master=None, text_new=None, new_cmd=None,
                 back_com=None, text_back=None, seach_cmd=None,
                 btn_font='Times 20', seach_btn_text=None):
        self.seach_cmd = seach_cmd
        self.new_cmd = new_cmd
        self.master = master
        self.back_com = back_com
        Frame.__init__(self, master)
        self.pack(fill=X)
        Label(self, width=60).pack(side=LEFT)
        new_btn = Button(self, relief=RAISED, width=20, font=btn_font,
                         text=text_new, command=lambda: (self.add_new())
                         ).pack(side=LEFT)
        back_btn = Button(self, relief=RAISED, width=10, font=btn_font,
                         text=text_back, command=lambda: (self.back_cmd())
                         ).pack(side=RIGHT)
        seach_frame = Frame(self)
        seach_frame.pack(fill=X)
        Label(seach_frame, width=30).pack(side=LEFT)
        seach_entry = MyEntry(seach_frame)
        seach_btn = Button(seach_frame, text=seach_btn_text, width=10, font=btn_font,
                           command=lambda: (self.seach(seach_entry))).pack(side=LEFT)

    def seach(self, entry):
        n = entry.get()
        print(n)
        self.master.destroy()
        self.seach_cmd(n)

    def add_new(self):
        self.master.destroy()
        self.new_cmd('new', 1)

    def back_cmd(self):
        self.master.destroy()
        self.back_com()



class HeadFrame(Frame):
    def __init__(self, master=None, head_text=None,
                 wdg_size=None, color=None, number=0,
                 btn_text=None, key=None, details_cmd=None):
        count = 0
        Frame.__init__(self, master, padx=5)
        self.pack(fill=X)
        Label(self, width=1).pack(side=LEFT)
        for name in head_text:
            Label(self, text=name, padx=5, pady=5,
                  relief=RAISED, width=wdg_size[count],
                  bg=color).pack(side=LEFT)
            count += 1


class MyFrame(Frame):
    def __init__(self, master=None, head_text=None,
                 wdg_size=None, color=None, number=0,
                 btn_text=None, key=None, details_cmd=None,
                 main_tk=None):
        self.main_tk = main_tk
        self.master = master
        self.details_cmd = details_cmd
        count = 0
        Frame.__init__(self, master, padx=5)
        self.pack(fill=X)
        for name in head_text:
            Label(self, text=name, padx=5, pady=5,
                  relief=RAISED, width=wdg_size[count],
                  bg=color).pack(side=LEFT, fill=Y)
            count += 1
        if number > 0:
            Button(self, text=btn_text, relief=RAISED,
                   width=wdg_size[count], bg=color,
                   command=lambda: (self.det_command(key)),
                   font='Times 20'
                   ).pack(side=LEFT)

    def det_command(self, key):
        self.main_tk.destroy()
        self.details_cmd(key)


class DbWindow(Tk):
    def __init__(self, master=None, title=None,
                 head_text=None, data_text=None,
                 wdg_size=[5, 30, 30, 30, 30, 10, 15, 10],
                 color=('light green', 'white'), btn_text='Details',
                 details_cmd=None, back_com=None, seach_cmd=None,
                 new_btn_text=None, text_back=None, seach_btn_text=None):
        self.head_text = head_text
        Tk.__init__(self, master)
        new_btn = NewButton(self, text_new=new_btn_text,
                            text_back=text_back, new_cmd=details_cmd,
                            back_com=back_com, seach_cmd=seach_cmd,
                            seach_btn_text=seach_btn_text)
        HeadFrame(self, head_text, wdg_size, color[0])
        number = 1
        if data_text:
            scroll_frame = ScrollFrame(self)
            for item in data_text:
                data_text[item].insert(0, number)
                MyFrame(scroll_frame,
                        data_text[item], wdg_size,
                        color[number % 2], number,
                        btn_text, key=item,
                        details_cmd=details_cmd,
                        main_tk=self)
                number += 1
        self.title(title)
        self.geometry('1500x800')
        self.mainloop()


if __name__ == '__main__':
    def test_com(arg, new_person=None):
        if new_person:
            print(arg, new_person, 'add new')
        else:
            print(arg, 'test details command')

    def test_back():
        print('test back')

    t_text = {'title': 'TdataBase',
              'head': ['№', 'Tlast name', 'Tfirst name',
                              'Tpatronymic','Tbirthdate',
                              'Tweight', 'Tbelt'],
              'btn': 'TDetails', 'new': 'add new',
              'back': 'back'
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
    test = DbWindow(title=t_text['title'],
                    head_text=t_text['head'],
                    data_text=data_text, btn_text=t_text['btn'],
                    details_cmd=test_com, new_btn_text=t_text['new'],
                    text_back=t_text['back'], back_com=test_back
                    )

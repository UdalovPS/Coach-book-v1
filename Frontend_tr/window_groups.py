from tkinter import *


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


class OpenBtn(Button):
    def __init__(self, master, text, btn_cmd=None,
                 main_wnd=None, add_lb=None, side=LEFT):
        self.add_lb = add_lb
        self.main_wnd = main_wnd
        self.btn_cmd = btn_cmd
        Button.__init__(self, master, text=text, font='Times 20',
                        command=lambda: (self.btn_command()))
        Label(master, width=10).pack(side=LEFT)
        self.pack(side=side)

    def btn_command(self):
        if not self.add_lb:             # back command
            self.main_wnd.destroy()
            self.btn_cmd()
        else:                           # add new
            self.main_wnd.destroy()
            self.btn_cmd('new', self.add_lb)



class HeadFrame(Frame):
    def __init__(self, master=None, head_text=None,
                 wdg_size=None, color=None):
        count = 0
        Frame.__init__(self, master, padx=5)
        self.pack(fill=X)
        Label(self, width=1).pack(side=LEFT)
        for name in head_text:
            Label(self, text=name, padx=5, pady=5, font='20',
                  relief=RAISED, width=wdg_size[count],
                  bg=color).pack(side=LEFT, fill=Y)
            count += 1


class BtnFrame(Frame):
    def __init__(self, master=None, data_text=None,
                 wdg_size=None, color=None, open_btn_text=None,
                 key=None, open_gr_cmd=None, main_wnd=None, bg=None):
        self.main_wnd = main_wnd
        self.open_gr_cmd = open_gr_cmd
        self.key = key
        count = 0
        Frame.__init__(self, master, padx=5,)
        self.pack(fill=X)
        for name in data_text:
            Label(self, text=name, padx=5, pady=5,
                  relief=RAISED, width=wdg_size[count],
                  bg=bg, font='20').pack(side=LEFT, fill=Y)
            count += 1
        Button(self, text=open_btn_text, relief=RAISED,
               font='Times 20', command=lambda: (self.btn_cmd()),
               bg=bg).pack(side=LEFT)

    def btn_cmd(self):
        self.main_wnd.destroy()
        self.open_gr_cmd(self.key)




class MyTk(Tk):
    def __init__(self, wdg_size=[5, 30, 20], title='title',
                 head_text=None, data_text=None, add_btn_text=None,
                 open_btn_text=None, back_btn_text=None,
                 back_cmd=None, open_gr_cmd=None,
                 add_gr_cmd=None, bg=('light green', 'white')):
        Tk.__init__(self)
        head_fr = HeadFrame(self, head_text, wdg_size)
        add_btn = OpenBtn(master=head_fr, text=add_btn_text,
                          main_wnd=self, btn_cmd=add_gr_cmd,
                          add_lb=1)
        back_btn = OpenBtn(master=head_fr, text=back_btn_text,
                           btn_cmd=back_cmd, main_wnd=self, side=RIGHT)
        number = 1
        if data_text:
            # print(data_text)
            scroll_frame = ScrollFrame(self)
            for key in data_text:
                data_text[key].insert(0, number)
                BtnFrame(scroll_frame, data_text[key], wdg_size,
                         open_btn_text=open_btn_text, key=key,
                         open_gr_cmd=open_gr_cmd, main_wnd=self,
                         bg=bg[number % 2])
                number += 1
        self.title(title)
        self.geometry('1300x800')
        self.mainloop()


if __name__ == '__main__':
    head_text = {'head': ['№', 'group name', 'number of students'],
                 'title': 'groups', 'add': 'Add group',
                 'open': 'open', 'back': 'back'}
    data_text = {'group_0': ['group 0 ', 8],
                 'group_1': ['group 1 ', 10]}
    test = MyTk(head_text=head_text['head'], title=head_text['title'],
                data_text=data_text, add_btn_text=head_text['add'],
                open_btn_text=head_text['open'],
                back_btn_text=head_text['back'])

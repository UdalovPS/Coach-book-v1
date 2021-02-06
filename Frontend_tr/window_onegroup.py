from tkinter import *
import tkinter.messagebox as mb


class SaveMessage():
    def __init__(self, title='information',
                 message='data is save'):
        self.save_msg = mb.showinfo(title, message)

class DateError():
    def __init__(self, title, message):
        mb.showerror(title, message)

class OpenButton(Button):
    def __init__(self, master, text, attr_key, key,
                 open_tr_cmd, main_tk, bg, index=None,
                 font=None):
        self.index = index
        self.open_tr_cmd = open_tr_cmd
        self.attr_key = attr_key
        self.key = key
        self.main_tk = main_tk
        Button.__init__(self, master, text=text, font=font,
                       bg=bg, command=lambda: self.btn_cmd())
        self.pack(side=LEFT)

    def btn_cmd(self):
        self.main_tk.destroy()
        self.open_tr_cmd(key=self.key, index=self.index)
        # print('btn was clicked', self.attr_key, self.key)


class StudHead(Frame):
    def __init__(self, master, text,
                 size=[10, 20, 20, 20]):
        Frame.__init__(self, master)
        self.pack(fill=X)
        count = 0
        Label(self, width=1).pack(side=LEFT)
        for item in text:
            Label(self, text=item, width=size[count],
                  relief=RAISED, height=2,
                  font='20').pack(side=LEFT)
            count += 1


class StudFrame(Frame):
    def __init__(self, master, text, bg,
                 size=[10, 20, 20, 20]):
        Frame.__init__(self, master)
        self.pack(fill=X)
        count = 0
        for item in text:
            if type(item) == list:
                Label(self, text=len(item), width=size[count],
                  relief=RAISED, font='20',
                      bg=bg).pack(side=LEFT, fill=Y)
            else:
                Label(self, text=item, width=size[count],
                      relief=RAISED, font='20',
                      bg=bg).pack(side=LEFT, fill=Y)
            count += 1


class TrFrame(Frame):
    def __init__(self, master, text,
                 size=[10, 20, 20, 20]):
        Frame.__init__(self, master)
        self.pack(fill=X)
        count = 0
        for item in text:
            Label(self, text=item, width=size[count],
                  relief=RAISED).pack(side=LEFT)
            count += 1



class BigFrame(Frame):
    def __init__(self, master, bg=None, width=None):
        Frame.__init__(self, master, bg=bg, width=width)
        self.pack(side=LEFT, fill=Y)
        self.pack_propagate(FALSE)



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


class MyEntry(Entry):
    def __init__(self, master, text):
        Entry.__init__(self, master)
        self.insert(0, text)
        self.pack(side=LEFT)

class HeadFrame(LabelFrame):
    def __init__(self, master, change_text, del_text,
                 group_name, back_btn_text, back_btn_cmd,
                 key, save_btn_cmd, del_btn_cmd,
                 del_msg, new_group, db_error_text, save_msg):
        self.save_msg=save_msg
        self.db_error_text = db_error_text
        self.new_group = new_group
        self.del_msg = del_msg
        self.del_btn_cmd = del_btn_cmd
        self.save_btn_cmd = save_btn_cmd
        self.back_btn_cmd = back_btn_cmd
        self.master = master
        self.key = key
        LabelFrame.__init__(self, master)
        self.pack(fill=X)
        empty_lbl = Label(self, width=60).pack(side=LEFT)
        self.gr_name = MyEntry(self, text=group_name)
        change_btn = Button(self, text=change_text, font='Times 20',
                            command=lambda: (self.change_name())
                            ).pack(side=LEFT)
        del_btn = Button(self, text=del_text, font='Times 20',
                          command=lambda: (self.delete_cmd())).pack(side=LEFT)
        back_btn = Button(self, text=back_btn_text, font='Times 20',
                          command=lambda: (self.back_cmd())
                          ).pack(side=RIGHT)

    def back_cmd(self):
        self.master.destroy()
        self.back_btn_cmd()

    def change_name(self):
        self.save_btn_cmd(key=self.key,
                          group_name=self.gr_name.get())
        SaveMessage(title=self.save_msg[0],
                    message=self.save_msg[1])

    def delete_cmd(self):
        del_msg = mb.askyesno(title=self.del_msg[0],
                              message=self.del_msg[1])
        if del_msg:
            if self.new_group:
                b_error = DateError(self.db_error_text[0],
                                     self.db_error_text[1])
            else:
                self.master.destroy()
                self.del_btn_cmd(self.key)
                self.back_btn_cmd()



class MyTk(Tk):
    def __init__(self, title=None, change_text=None,
                 del_text=None, group_name=None,
                 stud_btn_text=None, tr_btn_text=None,
                 stud_list=None, stud_head=None, back_btn_text=None,
                 back_btn_cmd=None, key=None, save_btn_cmd=None,
                 members_cmd=None, head_tr_text=None,
                 tr_list=None, open_btn_text=None,
                 open_tr_cmd=None, tr_btn_cmd=None,
                 del_btn_cmd=None, del_msg=None,
                 new_group=None, db_error_text=None,
                 save_msg=None, catch_error_func=None,
                 bg=('light green', 'white')):
        self.catch_error_func = catch_error_func
        self.tr_btn_cmd = tr_btn_cmd
        self.members_cmd = members_cmd
        self.key = key
        self.new_group = new_group
        self.db_error_text = db_error_text
        Tk.__init__(self)
        HeadFrame(self, change_text=change_text,
                   del_text=del_text, group_name=group_name,
                  back_btn_text=back_btn_text, back_btn_cmd=back_btn_cmd,
                  key=key, save_btn_cmd=save_btn_cmd,
                  del_btn_cmd=del_btn_cmd, del_msg=del_msg,
                  new_group=new_group, db_error_text=db_error_text,
                  save_msg=save_msg)
        big_st_fr = BigFrame(self, width=800)
        big_tr_fr = BigFrame(self, width=900)
        members = Button(big_st_fr, text=stud_btn_text, font='Times 20',
                         command=lambda: (self.open_members_wnd()),
                         bg='white').pack(fill=X)
        st_head_frame = StudHead(big_st_fr, text=stud_head)
        training = Button(big_tr_fr, text=tr_btn_text, font='Times 20',
                          command=lambda: (self.training_cmd()),
                          bg='light green').pack(fill=X)
        tr_head_frame = StudHead(big_tr_fr, text=head_tr_text)
        st_frame = ScrollFrame(big_st_fr)
        tr_frame = ScrollFrame(big_tr_fr)
        if stud_list:
            number = 1
            for obj in stud_list:
                obj.insert(0, number)
                StudFrame(st_frame, text=obj,
                          bg=bg[number % 2])
                number += 1
        if tr_list:
            index = len(tr_list) - 1
            number = 1
            for obj in reversed(tr_list):
                obj.insert(0, number)
                tr_fr = StudFrame(tr_frame, text=obj,
                                  bg=bg[number % 2])
                OpenButton(tr_fr, text=open_btn_text,
                           attr_key=obj, key=key,
                           open_tr_cmd=open_tr_cmd,
                           main_tk=self, index=index,
                           font='Times 20',  bg=bg[number % 2])
                index -= 1
                number += 1
        self.title(title)
        self.geometry('1700x800')
        self.mainloop()

    def open_members_wnd(self):
        try:
            self.catch_error_func(self.key)
            self.destroy()
            self.members_cmd(self.key)
        except KeyError:
            b_error = DateError(self.db_error_text[0],
                                self.db_error_text[1])

    def training_cmd(self):
        try:
            self.catch_error_func(self.key)
            self.destroy()
            self.tr_btn_cmd(self.key)
        except KeyError:
            b_error = DateError(self.db_error_text[0],
                                self.db_error_text[1])

if __name__ == '__main__':
    head_text = {'title': 'Tgroup', 'change': 'change group name',
                 'del': 'delete group', 'stud': 'students',
                 'train': 'training', 'open': 'open',
                 'stud_head': ['№', 'last name', 'first name', 'patronymic'],
                 'tr_head': ['№', 'date', 'time', 'number of \nstudents']
                 }
    data_text = {'group_name': 'TestGroup',
                 'members':[['Tomson', 'Tom', 'Tomas'],
                             ['Gregory', 'Greg', 'Grue']],
                 'training': [{'tr_0': ['18.12.2020', '10:00',
                                        [['Tomson', 'Tom', 'Tomas'],
                                        ['Gregory', 'Greg', 'Grue']]]
                               }]
                 }
    test = MyTk(title=head_text['title'],
                change_text=head_text['change'],
                del_text=head_text['del'],
                group_name=data_text['group_name'],
                stud_btn_text=head_text['stud'],
                tr_btn_text=head_text['train'],
                stud_list=data_text['members'],
                stud_head=head_text['stud_head'],
                key='testkey', head_tr_text=head_text['tr_head'],
                tr_list=data_text['training'],
                open_btn_text=head_text['open'])

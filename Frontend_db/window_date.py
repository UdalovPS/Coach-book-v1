"""
This module is about Toplevel window DateArgs.
DateArgs window shows information about weight or
    physicalform or belt.
"""

from tkinter import *
import tkinter.messagebox as mb

class DateError():
    def __init__(self, title, message):
        mb.showerror(title, message)


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


class SaveMessage():
    def __init__(self, title='information',
                 message='data is save'):
        self.save_msg = mb.showinfo(title, message)


class DelMessage():
    def __init__(self, title='Delete',
                 message='Do you want to delete data'):
        self.del_msg = mb.askyesno(title, message)


class MyEntry(Entry):
    def __init__(self, master, text):
        Entry.__init__(self, master, font='20')
        self.insert(0, text)
        self.pack(side=LEFT)

class MyFrame(Frame):
    def __init__(self, master, text, index, save_del_text,
                 main_key, key_item, save_cmd, del_cmd,
                 update_wnd, del_msg, save_msg, main_tk,
                 error_date_text, bg):
        self.error_date_text = error_date_text
        self.save_msg = save_msg
        self.del_msg = del_msg
        self.main_key = main_key
        self.key_item = key_item
        self.save_cmd = save_cmd
        self.del_cmd = del_cmd
        self.update_wnd = update_wnd
        self.master = master
        self.main_tk = main_tk
        Frame.__init__(self, master, bg=bg)
        self.pack(fill=X)
        self.get_list = []
        for item in text:
            self.item = MyEntry(self, text[item])
            self.get_list.append(self.item)
        btn_save = Button(self, text=save_del_text[0],
                          command=lambda: (self.save_in_db(index)),
                          font='Times 20', bg=bg).pack(side=LEFT)
        btn_del = Button(self, text=save_del_text[1],
                         command=lambda: (self.del_from_db(index)),
                         font='Times 20', bg=bg).pack(side=LEFT)

    def save_in_db(self, index):
        entry_list = []
        for item in self.get_list:
            entry_list.append(item.get())
        try:
            self.save_cmd(key_db=self.main_key, key_attr=self.key_item,
                          tmp=entry_list, index=index)
            SaveMessage(title=self.save_msg[0],
                        message=self.save_msg[1])
        except (IndexError, ValueError):
            error = DateError(self.error_date_text[0],
                              self.error_date_text[1])


    def del_from_db(self, index):
        del_msg = mb.askyesno(title=self.del_msg[0],
                              message=self.del_msg[1])
        if del_msg:
            self.del_cmd(key_db=self.main_key, key_attr=self.key_item,
                         index=index)
            self.main_tk.destroy()
            self.update_wnd(key=self.main_key, key_item=self.key_item)



class HeadFrame(Frame):
    def __init__(self, master, text, add_text, back_text,
                 main_key, back_cmd, add_cmd, key_item,
                 update_wnd, error_date_text):
        self.error_date_text = error_date_text
        self.master = master
        Frame.__init__(self, master)
        self.update_wnd = update_wnd
        self.key_item = key_item
        self.main_key = main_key
        self.back_cmd = back_cmd
        self.add_cmd = add_cmd
        self.pack(fill=X)
        self.get_list = []
        Label(self, width=1).pack(side=LEFT)
        for item in text:
            Label(self, text=item, relief=RAISED, font='20',
                  width=20, bg='white').pack(side=LEFT, fill=Y)
        btn_back = Button(self, text=back_text,
                          command=lambda: (self.back()),
                          font='Times 20').pack(side=RIGHT)
        add_frame = Frame(master)
        add_frame.pack(fill=X)
        Label(add_frame, width=1).pack(side=LEFT)
        for item in text:
            self.item = MyEntry(add_frame, text='-')
            self.get_list.append(self.item)
        btn_add = Button(add_frame, text=add_text,
                         command=lambda: (self.add_new()),
                         font='Times 20').pack(side=LEFT)

    def back(self):
        self.master.destroy()
        self.back_cmd(self.main_key)

    def add_new(self):
        get_list = []
        for item in self.get_list:
            get_list.append(item.get())
        try:
            self.add_cmd(key_db=self.main_key, key_attr=self.key_item,
                         tmp=get_list)
            self.master.destroy()
            self.update_wnd(key=self.main_key, key_item=self.key_item)
        except (IndexError, ValueError):
            error = DateError(self.error_date_text[0],
                              self.error_date_text[1])


class MyTk(Tk):
    def __init__(self, master=None, title=None,
                 data_text=None, head_text=None,
                 add_text=None, back_text=None, save_del_text=None,
                 main_key=None, back_cmd=None, key_item=None,
                 save_cmd=None, add_cmd=None, del_cmd=None,
                 update_wnd=None, del_msg=None, save_msg=None,
                 error_date_text=None, bg=('white', 'light green')):
        Tk.__init__(self, master)
        HeadFrame(self, text=head_text, add_text=add_text,
                  back_text=back_text, main_key=main_key,
                  back_cmd=back_cmd, add_cmd=add_cmd,
                  key_item=key_item, update_wnd=update_wnd,
                  error_date_text=error_date_text)
        index = len(data_text) - 1
        scroll_frame = ScrollFrame(self)
        for item in reversed(data_text):
            MyFrame(scroll_frame, text=item, index=index,
                    save_del_text=save_del_text,
                    main_key=main_key, key_item=key_item,
                    save_cmd=save_cmd, del_cmd=del_cmd,
                    update_wnd=update_wnd, del_msg=del_msg,
                    save_msg=save_msg, main_tk=self,
                    error_date_text=error_date_text,
                    bg=bg[index % 2])
            index -= 1
        self.title(title)
        self.geometry('1000x700')
        self.mainloop()



if __name__ == '__main__':
    head_text = {'title': 'Tweight', 'weight': ['date', 'value'],
                 'add': 'add new', 'back': 'back',
                 'physform': ['date', 'squats', 'abdominals'],
                 'save_del': ['save', 'delete'],
                 'error_date': ['error date', 'format date\ndd:mm:yyyy\nor "-"']}
    data_text = [{'date': '18.12.2020', 'value': 80},
                 {'date': '30.04.2021', 'value': 70}]
    data_text2 = [{'date': '18.12.2020', 'value': 80, 'squats': 30},
                 {'date': '30.04.2021', 'value': 70, 'squats': 30}]

    test = MyTk(title=head_text['title'], data_text=data_text2,
                head_text=head_text['weight'], add_text=head_text['add'],
                back_text=head_text['back'], save_del_text=head_text['save_del'],
                error_date_text=head_text['error_date'])

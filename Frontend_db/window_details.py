"""
This module is about Toplevel window Details.
Details window shows information all information
    about one student from database.
"""

from tkinter import *
import tkinter.messagebox as mb

class DelMessage():
    def __init__(self, title='Delete',
                 message='Do you want to delete data'):
        self.del_msg = mb.askyesno(title, message)


class SaveMessage():
    def __init__(self, title='information',
                 message='data is save'):
        self.save_msg = mb.showinfo(title, message)


class DateError():
    def __init__(self, title, message):
        mb.showerror(title, message)


class MyButton(Button):
    def __init__(self, master=None, text=None,
                 command=None, side=None):
        Button.__init__(self, master=master, text=text,
                        command=command, font='Times 20')
        self.pack(side=side)


class BigFrame(LabelFrame):
    def __init__(self, master=None, text=None, key=None,
                 ignor_btn=['parents', 'mother', 'father'],
                 h_text=None,open_date_cmd=None,
                 db_error_text=None, new_choice=None, bg=None):
        self.new_choice = new_choice
        self.db_error_text = db_error_text
        self.open_data_cmd = open_date_cmd
        self.key = key
        self.master = master
        LabelFrame.__init__(self, master, bg=bg)
        self.pack(fill=X, ipady=5)
        print(text)
        if text in ignor_btn:
            Label(self, text=h_text, relief=RAISED, bg=bg,
                  width=20, font='20').pack(side=LEFT, fill=Y)
        else:
            Button(self, text=h_text, relief=RAISED, bg=bg,
                  width=20, font='Times 20',
                   command=lambda: (self.open_data_det(text))
                   ).pack(side=LEFT, fill=Y)

    def open_data_det(self, arrt_key):
        if self.new_choice:
            key_error = DateError(self.db_error_text[0],
                                  self.db_error_text[1])
        else:
            self.master.destroy()
            self.open_data_cmd(self.key, arrt_key)


class MyEntry(Entry):
    def __init__(self, master=None, e_text=None,
                 head_text=None, bg=None):
        frame = Frame(master, bg=bg)
        frame.pack(fill=X, ipady=5)
        Entry.__init__(self, frame, font='20')
        Label(frame, text=head_text, relief=RAISED,
              width=20, font='20', bg=bg).pack(side=LEFT)
        self.insert(0, e_text)
        self.pack(side=LEFT)


class MyTk(Tk):
    def __init__(self, master=None, title=None, key='student_0',
                 head_text='My label', e_text='My entry',
                 date_key=['weight', 'belt', 'physform', 'parents'],
                 date_text='Big Frame', form_text='Form Text',
                 prts_date='Parents', mf_text='mother or father',
                 save='Tsave', cmd_save=None, back_text=None,
                 cmd_back=None, del_text=None, del_cmd=None,
                 open_date_cmd=None, del_msg=None, save_msg=None,
                 error_date_text=None, db_error_text=None,
                 new_choice=None, bg=('light green', 'white')):
        Tk.__init__(self, master)
        self.new_choice = new_choice
        self.db_error_text = db_error_text
        self.error_date_text = error_date_text
        self.save_msg = save_msg
        self.del_msg = del_msg
        self.title(title)
        self.open_date_cmd = open_date_cmd
        self.cmd_save = cmd_save
        self.cmd_back = cmd_back
        self.del_cmd = del_cmd
        count = 0
        self.get_list = []
        for item in e_text:
            if item in date_key:
                b_frm = BigFrame(self, text=item, h_text=head_text[count],
                                 key=key, open_date_cmd=open_date_cmd,
                                 db_error_text=db_error_text,
                                 new_choice=new_choice,
                                 bg=bg[count % 2])
                if item == 'parents':           # parents widget
                    j = 0
                    for obj in e_text[item]:
                        p_frm = BigFrame(b_frm, h_text=mf_text[j], text=item,
                                         bg=bg[count % 2], ignor_btn=['parents'])
                        x = 0
                        for name in obj:
                            self.name = MyEntry(p_frm, bg=bg[count % 2],
                                                head_text=prts_date[x],
                                                e_text=name)
                            self.get_list.append(self.name)
                            x += 1
                        j += 1
                    continue
                if item == 'physform':          # physical form widget
                    n = 0
                    for obj in e_text[item]:
                        self.obj = MyEntry(b_frm, bg=bg[count % 2],
                                           head_text=form_text[n],
                                           e_text=obj)
                        self.get_list.append(self.obj)
                        n += 1
                else:
                    i = 0
                    for obj in e_text[item]:    # date widget
                        self.obj = MyEntry(b_frm, bg=bg[count % 2],
                                           head_text=date_text[i],
                                           e_text=obj)
                        self.get_list.append(self.obj)
                        i += 1
            else:
                self.item = MyEntry(self,       # simple widget
                                    head_text=head_text[count],
                                    e_text=e_text[item],
                                    bg=bg[count % 2])
                self.get_list.append(self.item)
            count += 1
        save_btn = MyButton(self, text=save, side=LEFT,
                            command=lambda: (self.save(self.get_list,
                                                      key)))
        back_btn = MyButton(self, text=back_text, side=RIGHT,
                            command=lambda: (self.back()))
        del_btn = MyButton(self, text=del_text, side=LEFT,
                            command=lambda: (self.delete(key)))
        self.geometry('1500x900')
        self.mainloop()

    def save(self, get_list, key):
        entry_list = []
        for item in get_list:
            entry_list.append(item.get())
        try:
            self.cmd_save(key, entry_list)
            SaveMessage(title=self.save_msg[0],
                        message=self.save_msg[1])
        except (ValueError, IndexError):
            date_error = DateError(self.error_date_text[0],
                                   self.error_date_text[1])

    def back(self):
        self.destroy()
        self.cmd_back()

    def delete(self, key):
        del_msg = mb.askyesno(title=self.del_msg[0],
                              message=self.del_msg[1])

        if del_msg:
            if self.new_choice:
                db_error = DateError(self.db_error_text[0],
                                     self.db_error_text[1])
            else:
                self.destroy()
                self.del_cmd(key)
                self.cmd_back()





if __name__ == '__main__':
    def save_test(key, entry):
        print(key, entry, 'from details window')

    def del_test(key):
        print(key, 'delete func')

    def open_date_test(key, key_item):
        print(key, key_item)

    head_text = {'title': 'Details',
                'person': ['last name', 'first name',
                           'patronymic', 'birthdate',
                           'phone number', 'weight',
                           'belt', 'physical form',
                           'parents'],
                'date_v': ['date', 'value'],
                'head_p': ['last name', 'first name',
                           'patronymic', 'phone number'],
                'p_form': ['date', 'squats', 'abdominals'],
                 'm_or_d': ['mother', 'father'], 'save': 'save',
                 'del': 'delete'
              }
    data_text = {'lastName': 'Udalov', 'firstName': 'Pavel',
                 'patronymic': 'Sergeevich', 'birthdate': '01.03.1995',
                 'phoneNumber': '8-950-448-31-31',
                 'weight': ['12.12.2020', 70],
                 'belt': ['12.12.2020', 'white'],
                 'physform': ['12.12.2020', 20, 20],
                 'parents': [['Udalova', 'Valia', 'Aleksandrovna', '85'],
                             ['Udalov', 'Sergey', 'Anatolevich', '81']]
                 }
    test = MyTk(title=head_text['title'], head_text=head_text['person'],
                e_text=data_text, date_text=head_text['date_v'],
                form_text=head_text['p_form'], prts_date=head_text['head_p'],
                mf_text=head_text['m_or_d'], save=head_text['save'],
                cmd_save=save_test, del_text=head_text['del'],
                del_cmd=del_test, open_date_cmd=open_date_test)



"""
This module is about main window for program.
"""

from tkinter import *


class BigFrame(LabelFrame):
    def __init__(self, master):
        LabelFrame.__init__(self, master,
                            width=750)
        self.pack(side=LEFT, fill=Y)
        self.pack_propagate(FALSE)


class OpenBtn(Button):
    def __init__(self, master, b_text, open_com, main_wnd,
                 bg):
        self.main_wnd = main_wnd
        self.master = master
        self.open_com = open_com
        Button.__init__(self, master=master,
                        font='Times 30',
                        text=b_text, bg=bg,
                        command=lambda: (self.open_command()))
        self.pack()

    def open_command(self):
        self.main_wnd.destroy()
        self.open_com()


class MainWindow(Tk):
    def __init__(self, open_db_com=None, master=None,
                 title=None, btn_db_text=None,
                 btn_tr_text=None, open_tr_com=None):
        Tk.__init__(self, master)
        db_fr = BigFrame(self)
        db_btn = OpenBtn(db_fr, btn_db_text, open_db_com,
                         main_wnd=self, bg='steel blue')
        training_fr = BigFrame(self)
        tr_btn = OpenBtn(training_fr, btn_tr_text, open_tr_com,
                         main_wnd=self, bg='light green')
        self.title(title)
        self.geometry('1500x800')
        self.mainloop()



if __name__ == '__main__':
    def test_com():
        print('test DataBase command')
    text = {'title': 'TcoachBook',
            'database': 'TDatabase',
            'training': 'Training'}
    test = MainWindow(title=text['title'],
                      btn_db_text=text['database'],
                      open_db_com=test_com,
                      btn_tr_text=text['training'],
                      open_tr_com=test_com)


"""
This is main module in CoachBook program.
"""

from Frontend_db import window_main, window_db, window_details, window_date
from Frontend_tr import (window_groups, window_onegroup,
                         window_members, window_training,
                         window_change_tr)
from Widtext import head_main, head_db, head_details, head_date
from Widtext import (head_groups, head_onegroup, head_members,
                     head_training, head_change_tr)
from Database import data_shelve, data_training
from Processing import proc_data

LNG = 'eng'


def make_main_win():
    """ This func makes main window.
    """

    print('Start program')
    text = head_main.main_text(LNG)
    wnd = window_main.MainWindow(title=text['title'],
                                 btn_db_text=text['database'],
                                 open_db_com=open_db_win,
                                 btn_tr_text=text['training'],
                                 open_tr_com=open_groups_wnd)



def open_db_win(seach_value=None):
    """ This func makes TopLevel window - DataBase
    """

    head_text = head_db.db_window_text(LNG)
    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    if seach_value:
        data_text = proc_data.Processer(db=db,
                                        seach_value=seach_value).seach_wnd_db()
    else:
        data_text = proc_data.Processer(db=db).data_wnd_db()
    db.close()
    wnd = window_db.DbWindow(title=head_text['title'],
                             head_text=head_text['head'],
                             btn_text=head_text['btn'],
                             details_cmd=open_details_win,
                             data_text=data_text,
                             back_com=make_main_win,
                             new_btn_text=head_text['new'],
                             text_back=head_text['back'],
                             seach_cmd=open_db_win,
                             seach_btn_text=head_text['seach'])


def open_details_win(key, new_person=None):
    """This func makes Toplevel window - Details.
    :param new_person: is need in order to add new person in
        in database.
    :param key: is key of data in database about one student.
    """

    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    if new_person:
        new_choice = new_person
        data_text = proc_data.AddNewPerson().make_dict()
        key = data_shelve.AddExample(d_b=db).choice()
    else:
        new_choice = None
        data_text = proc_data.Processer(db=db,
                                    key=key).data_wnd_details()
    head_text = head_details.details_win_text(LNG)
    db.close()
    open = window_details.MyTk(key=key, title=head_text['title'],
                               head_text=head_text['person'],
                               e_text=data_text,
                               date_text=head_text['date_v'],
                               form_text=head_text['p_form'],
                               prts_date=head_text['head_p'],
                               mf_text=head_text['m_or_d'],
                               save=head_text['save'],
                               cmd_save=save_in_db,
                               back_text=head_text['back'],
                               cmd_back=open_db_win,
                               del_text=head_text['del'],
                               del_cmd=delete_in_db,
                               open_date_cmd=open_date_wnd,
                               del_msg=head_text['del_msg'],
                               save_msg=head_text['save_msg'],
                               error_date_text=head_text['error_date'],
                               db_error_text=head_text['db_error'],
                               new_choice=new_choice)


def save_in_db(key, entry):
    """
    This func saves data in data base.
    :param key: is key of data in database about one student.
        Key is need in order to know where save data.
    :param entry: is data, which need a save.
    """


    data_list = proc_data.ProcForMain(entry).collect_dict()
    data = data_shelve.DbShelve(*data_list).make_db_dict()
    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    if key in db:
        data['weight'] = db[key]['weight']
        data['belt'] = db[key]['belt']
        data['physform'] = db[key]['physform']
    db.close()
    save = data_shelve.SaveDb(data=data, key=key, db='shelve-db')
    save.save_db()



def delete_in_db(key):
    """
    This func deletes data in database by key.
    """

    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    del db[key]
    db.close()
    open_db_win()

def open_date_wnd(key, key_item):
    """
    This func makes TopLevel window - DateData
    :param key: It's a key by database. Open data
        about one person.
    :param key_item: It's a key by database about one
        attribute. (weight, belt, physform)
    """
    head_text = head_date.date_window_text(language=LNG,
                                           key=key_item)
    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    data_text = proc_data.Processer(db=db, key=key)
    data_text = data_text.data_wnd_date(key_item)
    db.close()
    open = window_date.MyTk(title=head_text['title'],
                            data_text=data_text,
                            head_text=head_text[key_item],
                            add_text=head_text['add'],
                            back_text=head_text['back'],
                            save_del_text=head_text['save_del'],
                            main_key=key, back_cmd=open_details_win,
                            key_item=key_item, save_cmd=change_item,
                            add_cmd=add_date_item,
                            del_cmd=del_data_item,
                            update_wnd=open_date_wnd,
                            del_msg=head_text['del_msg'],
                            save_msg=head_text['save_msg'],
                            error_date_text=head_text['error_date'])


def change_item(key_db, key_attr, tmp, index, db='shelve-db'):
    """
    This func changes one item in database in tmp.
    :param key_db:  It's a key by database. Open data
        about one person.
    :param key_attr: It's a key by database about one
        attribute. (weight, belt, physform)
    :param tmp: It's new data.
    :param index: It's index item in list from database.
    :param db: It's name database.
    """

    catch_error = data_shelve.DateArgs(*tmp)
    change = data_shelve.ChangeDateData(key_db=key_db,
                                        key_attr=key_attr,
                                        tmp=tmp, index=index,
                                        db=db)
    change.change_item()


def add_date_item(key_db, key_attr, tmp, db='shelve-db'):
    """
    This func adds one item in database in tmp.
    """

    catch_error = data_shelve.DateArgs(*tmp)
    add = data_shelve.ChangeDateData(key_db=key_db,
                                     key_attr=key_attr,
                                     tmp=tmp, db=db)
    add.append_to_list()



def del_data_item(key_db, key_attr, index, db='shelve-db'):
    """
    This func deletes one item in database in tmp.
    """
    # db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    delete = data_shelve.ChangeDateData(key_db=key_db,
                                        key_attr=key_attr,
                                        index=index, db=db)
    delete.delete_item()


def open_groups_wnd():
    """This fucn makes TopLevel window groups.
    Groups window shows information about group people
    for training.
    """
    head_text = head_groups.groups_win_text(LNG)
    db = data_training.OpenSaveDb().db
    data_text = proc_data.Processer(db).data_groups_wnd()
    db.close()
    open = window_groups.MyTk(title=head_text['title'],
                              head_text=head_text['head'],
                              add_btn_text=head_text['add'],
                              open_btn_text=head_text['open'],
                              data_text=data_text,
                              back_btn_text=head_text['back'],
                              back_cmd=make_main_win,
                              open_gr_cmd=open_onegroup_wnd,
                              add_gr_cmd=open_onegroup_wnd)

def open_onegroup_wnd(key, new_group=None):
    """This func makes TopLevel window about one group.
    OneGroup window shows information about one traning group
    """
    head_text = head_onegroup.members_win_text(LNG)
    db = data_training.OpenSaveDb().db
    if new_group:
        key = data_shelve.AddExample(d_b=db, example='group_').choice()
        data_text = proc_data.AddNewGroup().make_dict()
    else:
        data_text = db[key]
        if 'members' not in data_text:
            data_text['members'] = None
        if 'training' not in data_text:
            data_text['training'] = None
    db.close()
    open = window_onegroup.MyTk(title=head_text['title'],
                                change_text=head_text['change'],
                                del_text=head_text['del'],
                                group_name=data_text['groupName'],
                                stud_btn_text=head_text['stud'],
                                tr_btn_text=head_text['train'],
                                stud_list=data_text['members'],
                                stud_head=head_text['stud_head'],
                                back_btn_text=head_text['back'],
                                back_btn_cmd=open_groups_wnd,
                                key=key, save_btn_cmd=save_group_name,
                                members_cmd=open_members_wnd,
                                head_tr_text=head_text['tr_head'],
                                tr_list=data_text['training'],
                                open_btn_text=head_text['open'],
                                open_tr_cmd=open_trainig_wnd,
                                tr_btn_cmd=open_change_tr_wnd,
                                del_btn_cmd=del_group,
                                del_msg=head_text['del_msg'],
                                new_group=new_group,
                                db_error_text=head_text['db_error'],
                                save_msg=head_text['save_msg'],
                                catch_error_func=catch_error)

def save_group_name(key, group_name):
    db = data_training.OpenSaveDb().db
    if key not in db:                     # database[key] is not be
        tmp = {'groupName': group_name}
        db[key] = tmp
    else:                               # database[key] is be
        tmp = db[key]
        tmp['groupName'] = group_name
        db[key] = tmp
    db.close()

def open_members_wnd(key):
    """This func makes TopLevel window members.
    Members window adds students in group.
    :return:
    """
    head_text = head_members.onegroup_win_text(LNG)
    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    data_text = proc_data.Processer(db=db).data_wnd_db()
    db.close()
    open = window_members.MyTk(title=head_text['title'],
                               head_text=head_text['head'],
                               data_text=data_text,
                               save_btn_text=head_text['save'],
                               back_btn_text=head_text['back'],
                               key=key, back_btn_cmd=open_onegroup_wnd,
                               save_btn_cmd=save_members,
                               save_msg=head_text['save_msg'])

def catch_error(key):
    """This func is need for find mistakes.
    This func starts when you make open other window in program.
    """
    catch_error = data_shelve.OpenDbShelve(d_b='training-db').open_shelve()
    value = catch_error[key]
    catch_error.close()
    return value

def save_members(key, key_mem_dict, m_key='members'):
    """This func saves members in group.
    Start from members window.
    """
    db = data_shelve.OpenDbShelve(d_b='shelve-db').open_shelve()
    data = proc_data.Processer(db=db, key=key,
                            key_mem_dict=key_mem_dict).data_save_members()
    db.close()
    t_db = data_training.OpenSaveDb(data=data, attr_key=m_key,
                                    key=key).save_one_obj()

def del_group(key):
    with data_shelve.OpenDbShelve(d_b='training-db').open_shelve() as db:
        del db[key]
        db.close()


def open_trainig_wnd(key, index, tr_key='training'):
    head_text = head_training.training_win_text(LNG)
    with data_shelve.OpenDbShelve(d_b='training-db').open_shelve() as db:
        data = proc_data.Processer(db=db, key=key, index=index)
        data_text = data.data_training_wnd(tr_key)
        db.close()
    open = window_training.MyTk(title=head_text['title'], date=data_text[0],
                                time=data_text[1], members=data_text[2],
                                head_text=head_text['head'],
                                ch_btn_text=head_text['change'],
                                back_btn_text=head_text['back'],
                                del_btn_text=head_text['del'],
                                key=key, back_btn_cmd=open_onegroup_wnd,
                                change_btn_cmd=open_change_tr_wnd,
                                index=index, del_btn_cmd=delete_training,
                                del_msg=head_text['del_msg'])

def open_change_tr_wnd(key, index=None, tr_key='training',
                       m_key='members'):
    head_text = head_change_tr.change_tr_win_text(LNG)
    catch = catch_error(key)[m_key]
    print(head_text['error_date'])
    with data_shelve.OpenDbShelve(d_b='training-db').open_shelve() as db:
        data = proc_data.Processer(db=db, key=key, index=index)
        data_text = data.data_change_tr(tr_key, m_key)
        db.close()
    open = window_change_tr.MyTk(title=head_text['title'], date=data_text[0],
                                 time=data_text[1], members=data_text[2],
                                 head_text=head_text['head'],
                                 ch_btn_text=head_text['save'],
                                 back_btn_text=head_text['back'],
                                 back_btn_cmd=open_onegroup_wnd,
                                 key=key, index=index,
                                 save_btn_cmd=save_change_tr,
                                 error_date_text=head_text['error_date'],
                                 save_msg=head_text['save_msg'])


def save_change_tr(key, date_time, var_dict, index=None,
                   m_key='members', tr_key='training'):
    db = data_shelve.OpenDbShelve(d_b='training-db').open_shelve()
    tmp = proc_data.Processer(db=db[key][m_key],
                              key_mem_dict=var_dict).data_save_change_tr()
    db.close()
    data = data_training.Training(students=tmp, *date_time).make_dict()[-1]
    if index != None:
        change = data_training.OpenSaveDb(data=data, key=key, attr_key=tr_key,
                                          index=index).change_training()
    else:
        append = data_training.OpenSaveDb(data=data, key=key, attr_key=tr_key,
                                          index=index).append_training()


def delete_training(key, index):
    db = data_training.OpenSaveDb(key=key, index=index).db
    tmp = db[key]
    del tmp['training'][index]
    db[key] = tmp
    db.close()

if __name__ == '__main__':
    make_main_win()
    # open_db_win()
    # open_details_win('student_0')
    # open_groups_wnd()
    # open_onegroup_wnd('group_0', 1)
    # import shelve
    # n = shelve.open('training-db')
    # # # # open_members_wnd()
    # # # open_trainig_wnd('key', 'attr_key')
    # print(n['group_0']['training'])

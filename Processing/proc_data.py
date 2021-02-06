"""
This module processes data from test_shelve-db file, and return
    data in main module.
"""

import tkinter.messagebox as mb

class Processer():
    def __init__(self, db, db_keys=['lastName', 'firstName',
                                  'patronymic', 'birthdate',
                                  'weight', 'belt'],
                 key=None, det_keys=['weight', 'physform',
                                     'belt'],
                 seach_value=None,
                 members_keys=['lastName', 'firstName',
                                  'patronymic'],
                 key_mem_dict=None, index=None):
        self.db = db
        self.db_keys = db_keys
        self.key = key
        self.det_keys = det_keys
        self.seach_value = seach_value
        self.members_keys = members_keys
        self.key_mem_dict = key_mem_dict
        self.index = index

    def data_wnd_db(self):
        """ This method takes all data in database
            and processes for window_db.
        :return: Dict with data from database.
        Information from database takes by attribute self._keys.
        """

        data_dict = {}
        for key in self.db:
            data_list = []
            for item in self.db[key]:
                if item in self.db_keys:
                    if type(self.db[key][item]) == list:
                        data_list.append(self.db[key][item][-1][-1])
                        continue
                    data_list.append(self.db[key][item])
            data_dict[key] = data_list
        return data_dict

    def data_wnd_details(self):
        data_dict = {}
        db = self.db[self.key]
        for item in db:
            if item in self.det_keys:
                data_dict[item] = db[item][-1]
                continue
            data_dict[item] = db[item]
        return data_dict

    def data_wnd_date(self, key_item):
        date_list = []
        # date_dict = {}
        dict_key = {'weight': ['date', 'value'],
                    'belt': ['date', 'value'],
                    'physform': ['date', 'squats', 'abdominal']}
        db = self.db[self.key][key_item]
        # print('dict', dict_key[key_item])
        # print(db)
        for item in db:
            date_dict = dict(zip((dict_key[key_item]), item))
            date_list.append(date_dict)
        # print(date_list)
        return date_list

    def seach_wnd_db(self):
        """ This method seach seach_value in database.
        :return: Dict with data from database.
        Information from database takes by attribute self._keys.
        """
        data_dict = {}
        for key in self.data_wnd_db():
            for item in self.data_wnd_db()[key]:
                if item == self.seach_value:
                    data_dict[key] = self.data_wnd_db()[key]
        if data_dict:
            mb.showinfo('Seach', 'The item was found')
            return data_dict
        else:
            mb.showwarning('Seach', 'The item was not found')
            return self.data_wnd_db()

    def data_groups_wnd(self):
        data_dict = {}
        for key in self.db:
            data_list = []
            for item in self.db[key]:
                if item == 'groupName':
                    data_list.append(self.db[key][item])
                if item == 'members':
                    data_list.append(len(self.db[key][item]))
            data_dict[key]=data_list
        return data_dict

    def data_save_members(self):
        data_list = []
        for item in self.key_mem_dict:
            person_list = []
            if self.key_mem_dict[item] == True:
                for obj in self.db[item]:
                    if obj in self.members_keys:
                        person_list.append(self.db[item][obj])
            if person_list:
                data_list.append(person_list)
        return data_list

    def data_training_wnd(self, tr_key):
        # # print(self.db[self.key][tr_key][self.attr_key])
        return self.db[self.key][tr_key][self.index]

    def data_change_tr(self, tr_key, m_key):
        if self.index == None:
            data_list = ['-', '-', self.db[self.key][m_key]]
        else:
            data_list = [self.db[self.key][tr_key][self.index][0],
                         self.db[self.key][tr_key][self.index][1],
                         self.db[self.key][m_key]
                         ]
        return (data_list)

    def data_save_change_tr(self):
        data_list = []
        for key in self.key_mem_dict:
            if self.key_mem_dict[key] == True:
                data_list.append(self.db[key])
        return data_list



class ProcForMain():
    """
    This class takes data from main func save_in_db,
        processes in dict and return back
    """

    def __init__(self, det_data=None):
        self.lastName = det_data[0]
        self.firstName = det_data[1]
        self.patronymic = det_data[2]
        self.birthdate = det_data[3]
        self.phoneNumber = det_data[4]
        self.weight = det_data[5:7]
        self.belt = det_data[7:9]
        self.physform = det_data[9:12]
        self.parents = det_data[12:]

    def collect_dict(self):
        data_list = []
        for key in self.__dict__:
            data_list.append(self.__dict__[key])
        return data_list


class AddNewPerson():
    """
    This class return data in func (open_details_win) for
        main module.
    Data from this module is need in order to add new person
        in database.
    """

    def __init__(self):
        self.lastName = '-'
        self.firstName = '-'
        self.patronymic = '-'
        self.birthdate = '-'
        self.phoneNumber = '-'
        self.weight = ['-', '-']
        self.belt = ['-', '-']
        self.physform = ['-', '-', '-']
        self.parents = [['-', '-', '-', '-'],
                        ['-', '-', '-', '-']]

    def make_dict(self):
        data_dict = {}
        for key in self.__dict__:
            data_dict[key] = self.__dict__[key]
        return data_dict


class AddNewGroup(AddNewPerson):
    def __init__(self):
        self.groupName = '-'
        self.members = None
        self.training = None



if __name__ == '__main__':
    import shelve
    db = shelve.open('test_shelve-db')
    a = Processer(db, key='student_0').seach_wnd_db(70)
    print(a)


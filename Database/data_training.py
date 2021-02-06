"""
This module is about database.
This module make database with help Shelve module python.
With help this module you can take data from database,
    or save data in database.
"""

import shelve
import datetime

class TimeDate():
    """
    This class takes string data and return
        formatted data.
    """

    def __init__(self, date):
        self.date = date
        self.day = self.date[0:2]
        self.mounth = self.date[3:5]
        self.year = self.date[6:]

    def use_datetime(self):
        """
        This method changes attribute for datetime func.
        """
        if self.date == '-':
            form_date = self.date
        else:
            if self.day[0] == str(0):
                self.day = self.day[1]
            if self.mounth[0] == str(0):
                self.mounth = self.mounth[1]
            date = datetime.date(int(self.year),
                                 int(self.mounth),
                                 int(self.day))
            form_date = date.strftime('%d.%m.%Y')
        return form_date


class DbShelve():
    def __init__(self, groupName, members, training):
        self.groupName = groupName
        self.members = members
        self.training = Training(*training).make_dict()

    def make_dict(self):
        data_dict = {}
        for item in self.__dict__:
            data_dict[item] = self.__dict__[item]
        return data_dict

    def make_grname_dict(self):
        data_dict = {'groupName': self.groupName}
        return data_dict

class Training():
    def __init__(self, date, time, students):
        self.date = TimeDate(date).use_datetime()
        self.time = time
        self.students = students

    def make_dict(self):
        data_list = [self.date, self.time, self.students]
        return [data_list]


class OpenSaveDb():
    """
    This class save database in shevle file.
    """

    def __init__(self, data=None, key=None,
                 attr_key=None, db_name='training-db',
                 index=None):
        self.index = index
        self.data = data
        self.key = key
        self.db_name = db_name
        self.attr_key = attr_key
        self.db = self.open_shelve()

    def open_shelve(self):
        db = shelve.open(self.db_name)
        return db

    def save_db(self):
        self.db[str(self.key)] = self.data
        self.db.close()

    def save_one_obj(self):
        tmp = self.db[self.key]
        tmp[self.attr_key] = self.data
        self.db[self.key] = tmp
        self.db.close()

    def change_training(self):
        tmp = self.db[self.key]
        tmp[self.attr_key][self.index] = self.data
        self.db[self.key] = tmp
        self.db.close()

    def append_training(self):
        tmp = self.db[self.key]
        if self.attr_key not in tmp:
            tmp[self.attr_key] = []
        tmp[self.attr_key].append(self.data)
        self.db[self.key] = tmp
        self.db.close()






if __name__ == '__main__':
    stud = [['Tomson', 'Tom', 'Tomas'], ['Gregory', 'Greg', 'Grue']]
    test = DbShelve('group_1', stud, ('10.10.2020', '10:30', stud))
    data = test.make_dict()
    print(data)
    # test_save = OpenSaveDb(data=data, key='group_0').save_db()
    pass



"""
This module is about database.
This module make database with help Shelve module python.
With help this module you can take data from database,
    or save data in database.
"""

import shelve
import datetime
import tkinter.messagebox as mb

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
            # except:                                     # all mistakes with date

        return form_date


class DateArgs():
    """
    This class unites date and other data about person.
    """

    def __init__(self, date, *args):
        self.date = TimeDate(date).use_datetime()
        self.args = args

    def collect_list(self):
        """
        This method units data in list.
        :return: (list with data)
        """

        date_list = []
        date_list.append(self.date)
        for i in self.args:
            date_list.append(i)
        return date_list


class Parents():
    """
    This class init data about person parents.
    :return: Mom or Dad (last name, first name, patronymic,
        phone number)
    """

    def __init__(self, mom_lN='-', mom_fN='-', mom_p='-',
                 mom_phone='-', dad_lN='-', dad_fN='-',
                 dad_p='-', dad_phone='-'):
        self.mom_lN = mom_lN
        self.mom_fN = mom_fN
        self.mom_p = mom_p
        self.mom_phone = mom_phone
        self.dad_lN = dad_lN
        self.dad_fN = dad_fN
        self.dad_p = dad_p
        self.dad_phone = dad_phone
        self.mom = [self.mom_lN, self.mom_fN,
                    self.mom_p, self.mom_phone]
        self.dad = [self.dad_lN, self.dad_fN,
                    self.dad_p, self.dad_phone]

    def parents_list(self):
        return [self.mom, self.dad]

class DbShelve():
    """
    This class init data about one person.
    Class DbShelve uses other classes, such as:
        Parents, DateArgs.
    """

    def __init__(self, lastName, firstName, patronymic,
                 birthdate, phoneNumber, weight,
                 belt, physform, parents):
        self.lastName = lastName
        self.firstName = firstName
        self.patronymic = patronymic
        self.birthdate = TimeDate(birthdate).use_datetime()
        self.phoneNumber = phoneNumber
        self.weight = [DateArgs(*weight).collect_list()]
        self.belt = [DateArgs(*belt).collect_list()]
        self.physform = [DateArgs(*physform).collect_list()]
        self.parents = Parents(*parents).parents_list()

    def make_db_dict(self):
        db_dict = {}
        for key in self.__dict__:
            db_dict[key] = self.__dict__[key]
        return db_dict




class SaveDb():
    """
    This class save database in shevle file.
    """

    def __init__(self, data, key, db='test_shelve-db'):
        self.data = data
        self.key = key
        self.db = OpenDbShelve(d_b=db).open_shelve()

    def save_db(self):
        self.db[str(self.key)] = self.data
        self.db.close()



class OpenDbShelve():
    """
    This class open shelve file.
    """
    def __init__(self, key=None, d_b='test_shelve-db'):
        self.d_b = d_b
        self.key = key

    def open_shelve(self):
        db = shelve.open(self.d_b)
        return db

    def close_db(self):
        self.open_shelve().close()

    def open_about_one(self):
        db1 = self.open_shelve()[self.key]
        self.open_shelve().close()
        return db1


class ChangeDateData():
    """
    This class changes date date from database.
    db = name database
    key_db = example key in database. Give access to
        data about one person.
    key_attr = key attribute. Give access to one
        of data about person.
    tmp = new data.
    index = item index when need a change.
    """

    def __init__(self, key_db=None, key_attr=None,
                 tmp=None, index=None, db='test_shelve-db'):
        self.db = OpenDbShelve(d_b=db).open_shelve()
        # self.db = db
        self.key_db = key_db
        self.db_key_db = self.db[self.key_db]
        self.key_attr = key_attr
        if tmp:
            self.tmp = DateArgs(*tmp).collect_list()
        self.index = index


    def append_to_list(self):
        """
        This method append tmp data to key_attr data
            and save in database.
        Vars (key_db, key_attr, tmp, db) are
            mandatory vars for this func.
        """

        for item in self.db_key_db:
            if item == self.key_attr:
                main_obj = self.db_key_db[item]
                # print(main_obj)                       # test print
                break
        main_obj.append(self.tmp)
        self.db_key_db[item] = main_obj
        # print(self.db_key_db.__dict__[item])           # test print
        self.db[self.key_db] = self.db_key_db
        self.db.close()

    def change_item(self):
        """
        This method changes key_attr data to
            tmp data by index and save in database.
        Vars (key_db, key_attr, tmp, db, index) are
            mandatory vars for this func.
        """

        for item in self.db_key_db:
            if item == self.key_attr:
                main_obj = self.db_key_db[item]
                # print(main_obj)                       # test print
                break
        main_obj[self.index] = self.tmp
        self.db_key_db[item] = main_obj
        # print(self.db_key_db.__dict__[item])          # test print
        self.db[self.key_db] = self.db_key_db
        self.db.close()

    def delete_item(self):
        """
        This method delete item by index.
        Vars (key_db, key_attr, db, index) are
            mandatory vars for this func.
        """

        for item in self.db_key_db:
            if item == self.key_attr:
                main_obj = self.db_key_db[item]
                # print(main_obj)                       # test print
                break
        del main_obj[self.index]
        self.db_key_db[item] = main_obj
        # print(self.db_key_db.__dict__[item])          # test print
        self.db[self.key_db] = self.db_key_db
        self.db.close()

    def close_db(self):
        self.db.close()

class AddExample():
    """
    This class makes new key in order to add new person
        in database.
    """

    def __init__(self, example='student_',
                 d_b = 'test_shelve-db'):
        self.example = example
        self.d_b = d_b

    def make_first_example(self):
        """
        This method uses if database is clear.
        :return: key - student_0
        """
        return self.example + str(0)

    def open_example_database(self):
        db = OpenDbShelve(d_b='shevle-db').open_shelve()
        return db

    def find_number(self, key_list):
        """
        This method separates numbers from keys and
            make list with this numbers.
        Then finds number for new key.
        :param key_list: is list with keys in database.
        :return: Number for new key.
        """
        number_list = []
        for i in key_list:
            number_list.append(i[-1])
        count = 0
        for i in range(len(number_list)):
            if str(i) in number_list:
                #print('Number is finded')
                count +=1
            else:
                #print('Number is not finded')
                return str(i)
                break
            if count == len(number_list):
                return str(count)

    def make_new_example(self, database):
        l_db = []
        for key in database:
            l_db.append(key)
        number = self.find_number(l_db)
        return number


    def choice(self):
        if self.d_b:                            #if db is not clear
            n = self.make_new_example(self.d_b)
            return (self.example + n)
        else:                                   #if db is clear
            return self.make_first_example()
        self.d_b.close()



if __name__ == '__main__':
    test = DbShelve('Udalov', 'Pavel', 'Sergeevich',
                    '01.03.1995', '8-950-448-31-31',
                    ('12.12.2020', 70), ('12.12.2020', 'white'),
                    ('12.12.2020', 20, 20),('Udalova', 'Valia',
                                            'Aleksandrovna', '85',
                                            'Udalov', 'Sergey',
                                            'Anatolevich', '81'))
    test2 = DbShelve('Tomson', 'Tom', 'Tomas',
                    '10.01.2001', '40-132',
                    ('01.04.2020', 50), ('27.10.2020', 'Brown'),
                    ('01.10.2020', 100, 100),('Tomson', 'Vika',
                                            'Urivna', '40-178',
                                            'Tomson', 'Tomas',
                                            'Alik', '40-179'))
    # save = SaveDb(test.make_db_dict(), 'student_0').save_db()
    # save_2 = SaveDb(test2.make_db_dict(), 'student_1').save_db()
    a = AddExample()
    print(a.choice())

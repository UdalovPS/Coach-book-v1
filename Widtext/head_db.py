"""
This module return text for widget for db window.
Text depends about choice language.
"""

def db_window_text(language='eng'):
    if language == 'eng':
        text = {'title': 'DataBase',
              'head': ['№', 'last name', 'first name',
                       'patronymic','birthdate',
                       'weight', 'belt'],
              'btn': 'Details', 'new': 'add new',
              'back': 'back', 'seach': 'seach'
              }
    if language == 'rus':
        text = {'title': 'База данных',
              'head': ['№', 'Фамилия', 'Имя',
                       'Отчество','Дата рождения',
                       'Вес', 'Пояс'],
              'btn': 'Подробности', 'new': 'Добавить ученика',
              'back': 'Назад', 'seach': 'Поиск'
              }
    return text


if __name__ == '__main__':
    print(db_window_text())

"""
This module return text for widget for details window.
Text depends about choice language.
"""

def details_win_text(language='eng'):
    if language == 'eng':
        text = {'title': 'Details',
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
                'back': 'back', 'del': 'delete',
                'del_msg': ['Delete', 'Do you want to delete data'],
                'save_msg': ['Save', 'data is save'],
                'error_date': ['error date', 'format date\ndd:mm:yyyy\nor "-"'],
                'db_error': ['database error', 'database does not exist'],

              }

    if language == 'rus':
        text = {'title': 'Подробности',
                'person': ['Фамилия', 'Имя',
                           'Отчество', 'Дата рождения',
                           'Номер телефона', 'Вес',
                           'Пояс', 'Физическая форма',
                           'Родители'],
                'date_v': ['Дата', 'Значение'],
                'head_p': ['Фамилия', 'Имя',
                           'Отчество', 'Номер телефона'],
                'p_form': ['Дата', 'Отжимания', 'Пресс'],
                 'm_or_d': ['Мать', 'Отец'], 'save': 'Сохранить',
                'back': 'Назад', 'del': 'Удалить',
                'del_msg': ['Удаление', 'Вы действительно хотите удалить данные?'],
                'save_msg': ['Сохранение', 'Данные сохранены'],
                'error_date': ['Ошибка даты', 'Необходима дата в формате\nдд:мм:гггг\nили "-"'],
                'db_error': ['Ошибка базы данных', 'База данных не существует']
              }
    return text



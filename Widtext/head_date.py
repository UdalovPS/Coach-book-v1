"""
This module return text for widget for date window.
Text depends about choice language.
"""


def date_window_text(language='eng', key='weight'):
    if language == 'eng':
        title = {'weight': 'weight', 'belt': 'belt',
                 'physform': 'physical form'}
        text = {'weight': ['date', 'value'],
                'belt': ['date', 'value'],
                'add': 'add new', 'back': 'back',
                'physform': ['date', 'squats', 'abdominal'],
                'save_del': ['save', 'delete'],
                'del_msg': ['Delete', 'Do you want to delete data'],
                'save_msg': ['Save', 'data is save'],
                'error_date': ['error date', 'format date\ndd:mm:yyyy\nor "-"']
                }
        text['title'] = title[key]

    if language == 'rus':
        title = {'weight': 'Вес', 'belt': 'Пояс',
                 'physform': 'Физическая форма'}
        text = {'weight': ['Дата', 'Значение'],
                'belt': ['Дата', 'Значение'],
                'add': 'Добавить', 'back': 'Назад',
                'physform': ['Дата', 'Отжимания', 'Пресс'],
                'save_del': ['Сохранить', 'Удалить'],
                'del_msg': ['Удаление', 'Вы действительно хотите удалить данные'],
                'save_msg': ['Сохранение', 'Данные сохранены'],
                'error_date': ['Ошибка даты', 'Необходима дата в формате\nдд:мм:гггг\nили "-"']
                }
        text['title'] = title[key]

    return text


if __name__ == '__main__':
    print(date_window_text(key='physform'))

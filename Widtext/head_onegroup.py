"""

"""

def members_win_text(language='eng'):
    if language == 'eng':
        text = {'title': 'group', 'change': 'save group name',
                 'del': 'delete group', 'stud': 'students',
                 'train': 'training', 'open': 'open', 'back': 'back',
                 'stud_head': ['№', 'last name', 'first name', 'patronymic'],
                 'tr_head': ['№', 'date', 'time', 'number of \nstudents'],
                'del_msg': ['Delete', 'Do you want to delete data'],
                'db_error': ['database error', 'database does not exist'],
                'save_msg': ['Save', 'data is save'],
                 }

    if language == 'rus':
        text = {'title': 'Группа', 'change': 'Сохранить имя группы',
                 'del': 'Удалить группу', 'stud': 'Ученики',
                 'train': 'Тренеровки', 'open': 'Открыть', 'back': 'Назад',
                 'stud_head': ['№', 'Фамилия', 'Имя', 'Отчество'],
                 'tr_head': ['№', 'Дата', 'Время', 'Количество \nучеников'],
                'del_msg': ['Удаление', 'Вы действительно хотите удалить данные?'],
                'db_error': ['Ошибка базы данных', 'База данных не существует'],
                'save_msg': ['Сохранение', 'Данные сохранены'],
                 }
    return text

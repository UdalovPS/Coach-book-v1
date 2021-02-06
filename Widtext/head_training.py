



def training_win_text(language='eng'):
    if language == 'eng':
        text = {'title': 'training',
                 'head': ['date', 'time', 'students'],
                 'change': 'change', 'back': 'back',
                 'del': 'delete',
                'del_msg': ['Delete', 'Do you want to delete data']
                 }

    if language == 'rus':
        text = {'title': 'Тренеровки',
                 'head': ['Дата', 'Время', 'Ученики'],
                 'change': 'Изменить', 'back': 'Назад',
                 'del': 'Уалить',
                'del_msg': ['Удаление', 'Вы действительно хотите удалить данные?']
                 }
    return text

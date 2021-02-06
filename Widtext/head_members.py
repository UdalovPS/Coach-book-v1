


def onegroup_win_text(language='eng'):
    if language == 'eng':
        text = {'title': 'add members',
                'head': ['№', 'Tlast name', 'Tfirst name',
                         'Tpatronymic', 'Tbirthdate',
                         'Tweight', 'Tbelt'],
                'save': 'save', 'back': 'back',
                'save_msg': ['Save', 'data is save']
                }

    if language == 'rus':
        text = {'title': 'Члены группы',
                'head': ['№', 'Фамилия', 'Имя',
                         'Отчество', 'Дата рождения',
                         'Вес', 'Пояс'],
                'save': 'Сохранить', 'back': 'Назад',
                'save_msg': ['Сохранения', 'Данные сохранены']
                }
    return text

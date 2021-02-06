"""

"""

def groups_win_text(language='eng'):
    if language == 'eng':
        text = {'head': ['№', 'group name', 'number of \nstudents'],
                'title': 'groups', 'add': 'Add group',
                'open': 'open', 'back': 'back'
                }

    if language == 'rus':
        text = {'head': ['№', 'Имя группы', 'Количество\nучеников'],
                'title': 'Группы', 'add': 'Добавить группу',
                'open': 'Открыть', 'back': 'Назад'
                }
    return text

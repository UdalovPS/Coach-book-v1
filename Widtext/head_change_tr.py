



def change_tr_win_text(language='eng'):
    if language == 'eng':
        head_text = {'title': 'training',
                     'head': ['date', 'time', 'students'],
                     'save': 'save', 'back': 'back',
                     'error_date': ['error date', 'format date\ndd:mm:yyyy\nor "-"'],
                     'save_msg': ['Save', 'data is save']
                    }

    if language == 'rus':
        head_text = {'title': 'Тренеровки',
                     'head': ['Дата', 'Время', 'Ученики'],
                     'save': 'Сохранить', 'back': 'Назад',
                     'error_date': ['Ошибка даты', 'Необходима дата в формате\nдд:мм:гггг\nили "-"'],
                     'save_msg': ['Сохранение', 'Данные сохранены']
                     }
    return head_text

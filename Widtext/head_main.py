"""
This module return text for widget for main window.
Text depends about choice language.
"""

def main_text(language='eng'):
    if language == 'eng':
        text = {'title': 'Coach Book', 'database': 'Database',
                'training': 'Training'}
    if language == 'rus':
        text = {'title': 'Книга тренера', 'database': 'База данных',
                'training': 'Тренеровки'}
    return text

if __name__ == '__main__':
    print(main_text('eng'))

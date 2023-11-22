from genetic_scheduler import GeneticScheduler

DAYS_PER_WEEK = 5

SUBJECTS = [
    'Математичний аналіз',
    'Лінійна алгебра',
    'Аналітична геометрія',
    'Програмування',
    'Англійська мова',
    'Дискретна математика'
]

TEACHERS = [
    'Гончаренко Євген Васильович',
    'Юрченко Антон Андрійович',
    'Клименко Максим Віталійович',
    'Кош Бондан Васильович',
    'Марченко Марк Константинович',
    'Нестеренко Іван Юрійович'
]

GROUPS = [
    'КН-12',
    'КН-13',
    'КН-14',
    'КН-15',
    'КН-16',
    'КН-17'
]

CLASSES_PER_DAY = 3

if __name__ == '__main__':
    scheduler = GeneticScheduler(SUBJECTS, TEACHERS, GROUPS, CLASSES_PER_DAY, DAYS_PER_WEEK)
    best_schedule, fitness = scheduler.solve()
    WEEKDAYS = ["Понедіок", "Вівторок", "Середа", "Четвер", "П'ятниця"]

    sorted_schedule = sorted(best_schedule, key=lambda x: (x.day, x.time))

    for cls in sorted_schedule:
        weekday_name = WEEKDAYS[cls.day - 1]
        print(f'{weekday_name}, Пара {cls.time}: {cls.subject} в. {cls.teacher} для {cls.group}')

    print(f'Score: {fitness}')

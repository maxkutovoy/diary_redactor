import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)


def fix_marks(schoolkid):
    # Исправляем оценки
    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
        marks = Mark.objects.filter(schoolkid=kid, points__lt=4)
        if marks:
            for bad_mark in marks:
                bad_mark.points = random.randint(4, 5)
                bad_mark.save()
        else:
            print(f'Плохих оценок у ученика {kid} не найдено')
    except ObjectDoesNotExist:
        print('Ученик не найден')
    except MultipleObjectsReturned:
        print('Слишком много вариантов, уточните запрос')


def remove_chastisements(schoolkid):
    # Удаляем замечания от учителей
    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
        chastisements = Chastisement.objects.filter(schoolkid=kid)
        if chastisements:
            chastisements.delete()
        else:
            print(f'Замечаний для ученика {kid} не найдено')
    except ObjectDoesNotExist:
        print('Ученик не найден')
    except MultipleObjectsReturned:
        print('Слишком много вариантов, уточните запрос')


def create_commendation(schoolkid, subject):
    # Добавляем похвалу от учителя
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
        lessons = Lesson.objects.filter(year_of_study='6', group_letter='А', subject__title=subject).order_by('-date')
        if not lessons:
            raise ObjectDoesNotExist
        for lesson in lessons:
            commendation = Commendation.objects.filter(created=lesson.date, schoolkid=kid, subject=lesson.subject,
                                                       teacher=lesson.teacher)
            if not commendation:
                random_commendation = random.choice(commendations)
                Commendation.objects.create(text=random_commendation, created=lesson.date, schoolkid=kid,
                                            subject=lesson.subject, teacher=lesson.teacher)
                break
    except ObjectDoesNotExist:
        print('Ничего не найдено, проверьте правильность запроса')
    except MultipleObjectsReturned:
        print('Слишком много вариантов, уточните запрос')

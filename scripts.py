import random

from datacenter.models import (
    Chastisement,
    Commendation,
    Lesson,
    Mark,
    Schoolkid,
    Subject,
)


def find_schoolkid(schoolkid):
    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
        return kid
    except Schoolkid.ObjectDoesNotExist:
        print("Ученик не найден, проверьте правильность запроса")
    except Schoolkid.MultipleObjectsReturned:
        print("Слишком много вариантов, уточните запрос")


def fix_marks(kid):
    marks = Mark.objects.filter(schoolkid=kid, points__lt=4)
    if marks:
        for bad_mark in marks:
            bad_mark.points = random.randint(4, 5)
            bad_mark.save()
    else:
        print(f"Плохих оценок у ученика {kid} не найдено")


def remove_chastisements(kid):
    chastisements = Chastisement.objects.filter(schoolkid=kid)
    if chastisements:
        chastisements.delete()
    else:
        print(f"Замечаний для ученика {kid} не найдено")


def create_commendation(kid, subject):
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!",
    ]
    try:
        lessons = Lesson.objects.filter(
            year_of_study=kid.yeayear_of_study,
            group_letter=kid.group_letter,
            subject__title=subject,
        ).order_by("-date")
        if not lessons:
            raise Lesson.ObjectDoesNotExist
        for lesson in lessons:
            commendation = Commendation.objects.filter(
                created=lesson.date,
                schoolkid=kid,
                subject=lesson.subject,
                teacher=lesson.teacher,
            )
            if not commendation:
                random_commendation = random.choice(commendations)
                Commendation.objects.create(
                    text=random_commendation,
                    created=lesson.date,
                    schoolkid=kid,
                    subject=lesson.subject,
                    teacher=lesson.teacher,
                )
                break
    except Lesson.ObjectDoesNotExist:
        print("Предмет не найден, проверьте правильность запроса")

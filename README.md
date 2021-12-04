# Набор скриптов для редактирования электронного дневника школы


## Как это работает:

Файл `scripts.py` состоит из 4 частей:
 * Блок импортов:
```
import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)
```
 * Функция исправления оценок ниже 4 на 4 и 5:
```
def fix_marks(schoolkid):
    ...
```
* Функция удаления замечаний учителя:
```
def remove_chastisements(schoolkid):
    ...
```
* Функция добавления похвалы:
```
def create_commendation(schoolkid, subject):
    ...
```
Для работы скриптов необходимо запустить [электронный дневник](https://github.com/devmanorg/e-diary/tree/master) 
на своем компьютере. Так же понадобится файл с базой данных.


## Как использовать:

После запуска электронного дневника и подключения базы данных необходимо запустить `Django shell` командой:

```
python manage.py shell
```

ПРИМЕЧАНИЕ: `Django shell` лучше запускать в новом окне терминала, чтобы не выключать сайт.

Далее в `Django shell` необходимо скопировать импорты из файла `scripts.py`.

Затем скопировать какую-то конкретную функцию или сразу все.

Теперь можно запускать функции. Для функций `fix_marks` и `remove_chastisements` в качестве аргумента указываем 
Фамилию Имя ученика. Для функции `create_commendation` помимо Фамилии и Имени ученика необходимо так же указать предмет
по которому будет добавлена похвала. Если в базе есть несколько учеников с одинаковыми фамилией и именем можно 
указать дополнительную информацию в виде Отчества и класса. Например:
```
fix_marks('Фамилия Имя')
или
remove_chastisements('Фамилия Имя Отчество 6А')
или 
create_commendation('Фамилия Имя', 'Математика')
```
ПРИМЕЧАНИЕ: Копировать импорты и функции необходимо после каждого перезапуска `Django shell`

## Цель проекта:

Код написан в образовательных целях на курсе для web-разработчиков [dvmn.org](https://dvmn.org/).
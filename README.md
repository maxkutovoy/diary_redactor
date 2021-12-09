# Набор скриптов для редактирования электронного дневника школы


## Как это работает:


Для работы скриптов необходимо запустить [электронный дневник](https://github.com/devmanorg/e-diary/tree/master) 
на своем компьютере. Так же понадобится файл с базой данных.


## Как использовать:

После запуска электронного дневника и подключения базы данных необходимо запустить `Django shell` командой:

```
python manage.py shell
```

ПРИМЕЧАНИЕ: `Django shell` лучше запускать в новом окне терминала, чтобы не выключать сайт.

Далее в `Django shell` необходимо скопировать импорты из файла `scripts.py`. 

Обязательно копируем функцию: `find_schoolkid(schoolkid)` и вызывае ее в `Django shell`
присвоив результат ее выполнения произвольной переменной, например `kid`. В качестве аргумента
указываем Фамилию Имя ученика.

```python
kid = find_schoolkid('Фамилия Имя')
```
ПРИМЕЧАНИЕ: Если в базе есть несколько учеников с одинаковыми фамилией и именем нужно 
указать дополнительную информацию в виде Отчества и класса. Например:

```python
kid = find_schoolkid('Фамилия Имя Отчество 5а')
```
Затем скопировать какую-то конкретную функцию или сразу все:

* `fix_marks` - функция для исправления оценок ниже 4 на 4 и 5.
* `remove_chastisements` - функция для удаления замечаний учителя.
* `create_commendation` - функция для добавления похвалы. Добавляет похвалу
по выбранному предмету к последнему прошедшему уроку. Если к этому урок уже добавлена
похвала, то выбирается предыдущий урок.

ПРИМЕЧАНИЕ: в качестве аргумента указываем переменную, которй мы присвоили результат
выполнения функции `find_schoolkid`(например `kid`). Для функции `create_commendation` 
указваем дополнительный аргумент: название предмета по которому нужно добавить похвалу.

```python
fix_marks(kid)

remove_chastisements(kid)
 
create_commendation(kid, 'Математика')
```

ВНИАНИЕ! Копировать импорты и функции необходимо после каждого перезапуска `Django shell`

## Цель проекта:

Код написан в образовательных целях на курсе для web-разработчиков [dvmn.org](https://dvmn.org/).
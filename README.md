
Приложение для аренды велосипедов

Основной стек:

    Python 3.9
    Django 4.2.1
    Django Rest Framework 5.3.1
    Postgres

Подключение зависимостей:

    Менеджер зависимостей Poetry
    poetry add

Функции

    Аутентификация и пользователь (основное приложение):
        JWT аутентификация
        обновление профиля
        изменение пароля
    Основной интерфейс:
        базовый CRUD с фильтрами и сортировкой: доски, цели, категории, комментарии
        пользователь может просматривать элементы, связанные с досками, в которых он владелец/писатель/читатель
        пользователь может создавать категории, цели, комментарии, только если он является владельцем/автором соответствующей доски
        пользователь может обновлять, удалять, только если он является владельцем/писателем соответствующей доски
        пользователь может обновлять, удалять только свои комментарии
        когда доска, категория отмечена как is_deleted, все дочерние категории, цели также отмечены как is_deleted


Автоматическая сборка и деплой приложения на сервер:

    Deploy автоматизирован с github actions.
    Используемые файлы проекта:
        actions**: .github/workflows/actions.yaml
        compose file: docker-compose-ci.yaml
    Docker hub images:
        front: sermalenk/skypro-front:lesson-38
        back: mixola/todolist:
    Добавить администратора при первом запуске:
        подключиться к серверу и получить доступ к папке проекта
        docker exec -it <api container_id> /bin/bash
        ./manage.py createsuperuser
    Адреса:
        front: http://mixola.ga
        admin: http://mixola.ga/admin/

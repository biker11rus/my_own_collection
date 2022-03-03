Ansible Collection - my_own_namespace
=========

Роль для тестирования модуля my_own_namespace.

* Роль  my_own_role производит создание файла по пути path с содержимым content.
* Если файл отсутствует - создается файл `path` с сожержимым `content`
* Если по указному пути path файл уже существует, то модуль заканчивает работу пропуская шаг создания файла и его наполнения

Role Variables
--------------

| Variable name | Default | Description |
|-----------------------|----------|-------------------------|
| path | "./testfile" | Параметр определяющий имя и пусть до файла |
| content | "some text" | Параметр определяющий что будет записано в файл |


License
-------

ect

Author Information
------------------

Ruslan Khozyainov netology 

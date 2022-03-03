# Ansible Collection - my_own_namespace.yandex_cloud_elk

Modules
--------------

1. [my_own_module](plugins/modules/my_own_module.py)

* Модуль my_own_module производит создание файла по пути path с содержимым content.
* Если файл отсутствует - создается файл `path` с сожержимым `content`
* Если по указному пути path файл уже существует, то модуль заканчивает работу пропуская шаг создания файла и его наполнения

Roles
--------------

1. [my_own_role](roles/my_own_role/README.md)

* Данная роль использует модуль [my_own_module](plugins/modules/my_own_module.py)

Role Variables
--------------

| Variable name | Default | Description |
|-----------------------|----------|-------------------------|
| path | "./testfile" | Параметр определяющий имя и пусть до файла |
| content | "some text" | Параметр определяющий что будет записано в файл |

Example 
----------------
```yml
- hosts: all
    roles:
        - { role: my_own_namespace.yandex_cloud_elk.my_own_role }
```
or
```yml
- hosts: all
  collections:
    - my_own_namespace.yandex_cloud_elk
  tasks:
    - import_role:
        name: my_own_role
      vars:
          
```

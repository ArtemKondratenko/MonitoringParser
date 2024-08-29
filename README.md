****Проект MonitoringParser**
-

**Назначение проекта:**
* Данный проект написан как вспомагательный проект для выполнения функциональности записи в файл путей добавленых дерикторий, а так же считывания с файла содержимого и возврат содержимого во множестве. Также написаны unit tests которые проверяют логику методов ил файла monitoring_list_parser.py.

**Архитектура проекта:**

* Содержит логику добавления, считывание содержимого файла: monitoring_list_parser.py,  а так же написаны юнит тесты на проверку функциональсти методов: test_monitoring_list_parser.py.  Pyproject.toml для описание проекта и синхронизации импорта проектов. Для запуска приложения необходимо в терминале ввести команду pytest.

**Используемые библиотеки:**

* pathlib 
* collections.abc
* pytest
* tempfile
* typing
* os.path

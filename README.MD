### Модуль 2. Неделя 1. Пример класса со списком задач

В учебных целях в файле main.py реализована следующая логика:
1. Класс TaskManager с закрытым атрибутом __tasks = список задач пользователя. Инициализирован пустым списком в конструкторе.
2. Метод add_task позволяет добавлять задачи в список. Метод принимает параметры: title (название задачи) и description (описание задачи).
3. Внутри метода add_task создается объект задачи, содержащий title и description. Объект добавляется в список __tasks.
4. Метод get_tasks возвращает список всех задач пользователя. Используйте свойство с декоратором @property, чтобы обеспечить безопасный доступ к данным о задачах.
5. Атрибут __tasks и методы add_task и get_tasks инкапсулированы и не доступны напрямую извне класса.
6. В качестве проверки реализации создается объект класса TaskManger, в который передается на хранение 3 задачи, которые затем успешно выводятся в консоль с помощью метода get_tasks.
import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description):
        obj = Task(title, description)
        self.__tasks.append(obj)
        logging.info(f'Task added: {title}; {description}')

    @property
    def get_tasks(self):
        logging.info(f'Task list was requested')
        return self.__tasks


if __name__ == '__main__':
    manager = TaskManager()
    # предустановленные задачи
    manager.add_task('test task', 'important')
    manager.add_task('check email', 'very important')
    manager.add_task('wake up, Neo...', 'extremely important')

    while True:
        print('1 - добавить задачу, 2 - показать список задач, 0 - выход')
        answer = input('Введите команду: ')
        if answer not in ['0', '1', '2']:
            print('Недопустимая команда.')
            continue
        elif answer == '0':
            exit()
        elif answer == '1':
            title = input('Заголовок задачи: ')
            description = input('Описание: ')
            manager.add_task(title, description)
        elif answer == '2':
            tasks = manager.get_tasks
            for i, task in enumerate(tasks, start=1):
                print(f'Task {i}: {task.title} - {task.description}')

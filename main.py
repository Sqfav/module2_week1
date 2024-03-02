import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


class TaskManager:
    def __init__(self):
        self.__tasks = []

    class Task:
        def __init__(self, title, description):
            self.title = title
            self.description = description

    def add_task(self, title, description):
        obj = self.Task(title, description)
        self.__tasks.append(obj)
        logging.info(f'Task added: {title}; {description}')

    @property
    def get_tasks(self):
        logging.info(f'Task list was requested')
        return self.__tasks


if __name__ == '__main__':
    manager = TaskManager()

    manager.add_task('test task', 'important')
    manager.add_task('check email', 'very important')
    manager.add_task('wake up, Neo...', 'extremely important')

    tasks = manager.get_tasks

    for i, task in enumerate(tasks, start=1):
        print(f'Task {i}: {task.title} - {task.description}')

'''Place to try stuff out'''
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QCheckBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To Do App')
        
        layout = QVBoxLayout(self)
        self.resize(400, 300)

class Task(object):
    def __init__(self, parent, title):
        self.parent = parent
        self.title = title
        self.details = None
        self.completed = False
        self.due_date = None
        self.priority = None
        container = QHBoxLayout(self.parent)
        self.task_field = QLabel(self.title, container)
        self.completed_checkbox = QCheckBox("Completed", container)
        
class TaskList(object):
    def __init__(self, parent):
        self.parent = parent
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def remove_task(self, task):
        self.tasks.remove(task)
        
    def get_tasks(self):
        return self.tasks
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.layout.addWidget(QLabel("To Do List"))
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
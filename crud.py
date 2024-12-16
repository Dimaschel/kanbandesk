from sqlalchemy.orm import Session
from models import User, Project, Column, Task, TaskLog
from schemas import UserCreate, ProjectCreate, ColumnCreate, TaskCreate, TaskLogCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def create_column(db: Session, column: ColumnCreate):
    db_column = Column(name=column.name, project_id=column.project_id)
    db.add(db_column)
    db.commit()
    db.refresh(db_column)
    return db_column

def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description, column_id=task.column_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def create_task_log(db: Session, task_log: TaskLogCreate):
    db_log = TaskLog(task_id=task_log.task_id, action=task_log.action)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

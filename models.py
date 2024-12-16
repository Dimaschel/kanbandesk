from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)

    projects = relationship("Project", secondary="user_projects", back_populates="users")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)

    columns = relationship("KanbanColumn", back_populates="project")
    users = relationship("User", secondary="user_projects", back_populates="projects")


class UserProject(Base):
    __tablename__ = "user_projects"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)


class KanbanColumn(Base):  # Изменено имя класса
    __tablename__ = "columns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    tasks = relationship("Task", back_populates="column")
    project = relationship("Project", back_populates="columns")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    column_id = Column(Integer, ForeignKey("columns.id"), nullable=False)

    column = relationship("KanbanColumn", back_populates="tasks")
    logs = relationship("TaskLog", back_populates="task")  # Добавлено


class TaskLog(Base):
    __tablename__ = "task_logs"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    task = relationship("Task", back_populates="logs")

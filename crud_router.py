from fastapi import FastAPI
from pydantic import BaseModel, FilePath

app = FastAPI()


class Project(BaseModel):
    name: str
    icon: FilePath
    manager: str
    group: str
    deadline: str


projects = []


@app.post("/projects")  # создание проекта
def create_project(project: Project):
    projects.append(project)
    return {"message": "Проект успешно создан", "data": project}


# Роутер для получения списка всех проектов
@app.get("/projects")
def get_projects():
    return {"data": projects}


# Роутер для получения информации о конкретном проекте по его индексу
@app.get("/projects/{project_id}")
def get_project(project_id: int):
    if project_id < len(projects):
        return {"data": projects[project_id]}
    return {"message": "Проект не найден"}


# Роутер для обновления информации о проекте по его индексу
@app.put("/projects/{project_id}")
def update_project(project_id: int, project: Project):
    if project_id < len(projects):
        projects[project_id] = project
        return {"message": "Проект успешно обновлен", "data": project}
    return {"message": "Проект не найден"}


# Роутер для удаления проекта по его индексу
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    if project_id < len(projects):
        deleted_project = projects.pop(project_id)
        return {"message": "Проект успешно удален", "data": deleted_project}
    return {"message": "Проект не найден"}


# Запуск сервера FastAPI
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

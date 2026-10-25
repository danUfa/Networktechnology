from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "item": "Пример задачи: сдать практическую работу №4!"
                }
            ]
        }
    }
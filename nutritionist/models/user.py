from pydantic import BaseModel  # estrutura e validação de dados


class User(BaseModel):  # por padrão o basemodel já implementa um id.
    telegram_id: int
    name: str
    sex: str
    age: str
    height_cm: str
    weight_kg: str
    has_diabetes: str
    goal: str

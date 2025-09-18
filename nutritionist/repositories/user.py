from typing import Optional, List
from tinydb import Query
from models import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()  # função de inicialização da classe mãe BaseRepository
        self.user_table = self.get_table("users")

    def create_user(
        self,
        telegram_id: int,
        name: str,
        sex: str,
        age: str,
        height_cm: str,
        weight_kg: str,
        has_diabetes: str,
        goal: str,
    ) -> User:
        user = User(
            telegram_id=telegram_id,
            name=name,
            sex=sex,
            age=age,
            height_cm=height_cm,
            weight_kg=weight_kg,
            has_diabetes=has_diabetes,
            goal=goal,
        )
        self.user_table.insert(
            user.model_dump()
        )  # model_dump: para converter de BAsemodel para Dicionário (que é o que o banco de dados aceita)
        return user

    def get_user_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        UserQuery = Query()
        result = self.user_table.get(UserQuery.telegram_id == telegram_id)
        if not result:
            return None
        return User(
            **result
        )  # ** desempacota cada um dos dados conforme o modelo de User, assim não precisar fazer na mão

    def update_user(
        self,
        telegram_id: int,
        name: str,
        sex: str,
        age: str,
        height_cm: str,
        weight_kg: str,
        has_diabetes: str,
        goal: str,
    ) -> None:
        update_data = {
            "name": name,
            "sex": sex,
            "age": age,
            "height_cm": height_cm,
            "weight_kg": weight_kg,
            "has_diabetes": has_diabetes,
            "goal": goal,
        }

        UserQuery = Query()
        self.user_table.update(update_data, UserQuery.telegram_id == telegram_id)

    def delete_user(self, user_id: int) -> None:
        UserQuery = Query()
        self.user_table.remove(UserQuery.id == user_id)

    def get_all_users(self) -> List[User]:
        all_users = self.user_table.all()  # devolve uma lista de dicionários
        return [
            User(**user) for user in all_users
        ]  # para cada user dentro desta lista de dicionarios, desempacote utilizando o modelo User, e retorne todos dentro de uma lista.

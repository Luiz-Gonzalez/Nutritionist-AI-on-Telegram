from langchain.tools import BaseTool
from repositories.user import UserRepository


class UserInfoTool(BaseTool):
    name: str = "user_info"
    description: str = (
        "Use essa ferramenta para buscar informações de um usuário existente."
        "Ela requer o telegram_id do usuário como entrada para recuperar os dados."
    )

    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()

    def _run(self, telegram_id: int) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id=telegram_id)
            if not user:
                return f"Usuário com telegra_id {telegram_id} não encontrado."
            user_info = (
                f"Nome: {user.name}\n"
                f"Sexo: {user.sex}\n"
                f"Idade: {user.age}\n"
                f"Altura: {user.height_cm}\n"
                f"Peso: {user.weight_kg}\n"
                f"Diabetes: {'Sim' if user.has_diabetes else 'Não'}\n"
                f"Objetivo: {user.goal}\n"
            )
            return user_info
        except Exception as err:
            return f"Erro ao buscar as informações do usuário: {str(err)}"

    async def _arun(self, telegram_id: int) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")

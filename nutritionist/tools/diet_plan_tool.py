from langchain.tools import BaseTool
from typing import Optional
from repositories.diet_plan import DietPlanRepository
from repositories.user import UserRepository


class DietPlanTool(BaseTool):
    name: str = "diet_plan"
    description: str = (
        "Use esta ferramenta para criar um plano de dieta para um usuário. "
        "Entrada: telegram_id do usuário e pla_details para criar um novo plano ou buscar um plano já existente. "
        "A regra para essa tool é quando o usuário gostar do plano montado por você ai você está autorizado a usar esta tool para salvar o plano."
    )

    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        self._diet_plan_repo = DietPlanRepository()

    def _run(self, telegram_id: int, plan_details: str = None) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id=telegram_id)
            if not user:
                return "Usuário não encontrado. Por favor, registre o usuário primeiro."

            if plan_details:
                self._diet_plan_repo.create_diet_plan(
                    user_id=user.telegram_id, plan_details=plan_details
                )
                return f"Plano de dieta criado com sucesso para {user.name}"

            latest_plan = self._diet_plan_repo.get_latest_diet_plan_for_user(
                user_id=user.telegram_id
            )
            if latest_plan:
                return f"Plano de dieta para {user.name}:\n{latest_plan.details}"
            else:
                f"Nenhum plano de dieta encontrado para {user.name}"
        except Exception as e:
            return f"Erro na ferramenta de plano de dieta {str(e)}"

    async def _arun(self, plan_details: Optional[str] = None) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")

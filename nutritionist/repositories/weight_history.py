from typing import Optional, List
from tinydb import Query
from datetime import datetime
from models import WeightHistory
from repositories.base_repository import BaseRepository


class WeightHistoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.weight_history_table = self.get_table("weight_history")

    def add_weight_entry(self, user_id: int, weight_kg: str) -> WeightHistory:
        weight_entry = WeightHistory(user_id=user_id, weight_kg=weight_kg)
        entry_dict = weight_entry.model_dump()
        entry_dict["date"] = (
            weight_entry.date.isoformat()
        )  # 🔹 Converte datetime para string
        self.weight_history_table.insert(entry_dict)
        return weight_entry

    def get_weight_history(self, user_id: int) -> List[WeightHistory]:
        WeightHistoryQuery = Query()
        results = self.weight_history_table.search(
            WeightHistoryQuery.user_id == user_id
        )
        sorted_results = sorted(
            results, key=lambda entry: datetime.fromisoformat(entry["date"])
        )
        return [
            WeightHistory(**{**entry, "date": datetime.fromisoformat(entry["date"])})
            for entry in sorted_results
        ]  # 🔹 Converte string ISO de volta para datetime

    def get_weight_entry_by_id(self, weight_entry_id: int) -> Optional[WeightHistory]:
        WeightHistoryQuery = Query()
        result = self.weight_history_table.get(WeightHistoryQuery.id == weight_entry_id)
        if result:
            result["date"] = datetime.fromisoformat(
                result["date"]
            )  # 🔹 Converte de volta
            return WeightHistory(**result)
        return None

    def delete_weight_entry(self, weight_entry_id: int) -> None:
        WeightHistoryQuery = Query()
        self.weight_history_table.remove(WeightHistoryQuery.id == weight_entry_id)

    def get_all_weight_entries(self) -> List[WeightHistory]:
        all_entries = self.weight_history_table.all()
        return [
            WeightHistory(**{**entry, "date": datetime.fromisoformat(entry["date"])})
            for entry in all_entries
        ]

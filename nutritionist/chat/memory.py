from langchain.memory import ConversationBufferMemory  # curto prazo
from langchain_community.chat_message_histories import (
    SQLChatMessageHistory,
)  # longo prazo

MEMORY_KEY = "chat_history"


class SqliteMemory(SQLChatMessageHistory):
    def __init__(self, session_id: str, db_path: str = "sqlite:///memory.db"):
        super().__init__(session_id=session_id, connection=db_path)

        self.history = ConversationBufferMemory(
            memory_key=MEMORY_KEY,
            chat_memory=self,  # self aqui significa passar a própria instancia da classe SqliteMemory. chat_memory=self significa: "use eu mesmo (SqliteMemory) como o lugar onde as mensagens vão ser guardadas e recuperadas"
            return_messages=True,  # envia as mensagens para o agente automaticamente
        )

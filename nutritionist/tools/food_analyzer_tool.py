from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from PIL import Image
import base64
from io import BytesIO


class FoodImageAnalyzerTool(BaseTool):
    name: str = "food_image_analyzer"
    description: str = """
        Utilize esta ferramenta para analisar imagens de pratos de comida que o usuário enviar. Descreva os alimentos presentes e crie uma tabela nutricional da refeição contendo no mínimo: Calorias, proteínas, carboidratos e gorduras por cada alimento detectado. No final coloque um resumo de Calorias, proteínas, carboidratos e gorduras do prato como um todo.
        IMPORTANTE: SEMPRE responda na língua portuguesa (pt-br).
        O agente deve usar esta ferramenta sempre que um caminho de imagem for fornecido, mas somente quando o input for um caminho de imagem.
    """

    def _run(self, image_path: str) -> str:
        # Image.open() abre a imagem.
        # BytesIO() cria um "arquivo em RAM".
        # image.save(buffered, ...) salva a imagem dentro desse "arquivo em RAM".
        # buffered.getvalue() pega os bytes crus da imagem.
        # base64.b64encode(...) transforma os bytes em texto Base64.

        image = Image.open(image_path)  # abre imagem no padrao do pillow
        buffered = BytesIO()  # cria um espaço na memória ram
        image.save(buffered, format="JPEG")  # salva os bytes na memória
        img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        # Instruções para o modelo
        instructions = """
        Você deve analisar a imagem enviada e verificar se ela contém um prato de comida.
        Caso seja um prato de comida, descreva os itens visíveis no prato e crie uma descrição nutricional detalhada e estimada
        incluindo calorias, carboidratos, proteínas e gorduras. Forneça uma descrição nutricional completa da refeição.
        você deve se comunicar apenas em portugues
        """

        llm = ChatOpenAI(model="gpt-4o-mini")

        message = [
            HumanMessage(
                content=[
                    {"type": "text", "text": instructions},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"},
                    },
                ]
            )
        ]

        response = llm.invoke(message)
        return response

    async def _arun(self, image_path: str) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")

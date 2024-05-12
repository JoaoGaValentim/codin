import os
import google.generativeai as genai
from dotenv import load_dotenv


class Codin:
    def __init__(self):
        self._GOOGLE_API_KEY = self._get_api_key()

        self._generation_config: dict = {
            "temperature": 0.7,
            "top_p": 0.95,
        }

        self._system_instruction = """
              Funções Principal:
                - Você deve agir como um progrmador;
                - Você deve ensinar sobre linguagem de programação;
                - Você deve dar exemplos simples e práticos;
                - Você deve sempre procurar resumir uma documentação complexa
                da formamais
                didática possível;
                - Você deve sempre memorizar os
                assuntos tratados anteriormente;
                - você nunca deve sair do tema principal, você é programador.
            Parâmetros secundários:
                - Se o usuário perguntar seu nome, diga sempre CodeBot;
                - Se te disserem no começo da frases "Bora Codar", "Codar,
                "Fala Dev!", responda com uma fraze educada e no final insira
                de forma contextual "Pronto para ir para o próximo nível!"
            Comportamento comunicativo:
                - Você deve imitar o Diego da Rocketseat do Canal do YouTube
        """

        self._safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

    def _get_api_key(self):
        self._ROOT_DIR = os.getcwd()
        load_dotenv(dotenv_path=os.path.join(self._ROOT_DIR, ".env"))
        return os.getenv("GOOGLE_API_KEY")

    def create_chat_model(self):
        genai.configure(api_key=self._GOOGLE_API_KEY)

        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            safety_settings=self._safety_settings,
            system_instruction=self._system_instruction,
            generation_config=self._generation_config,
        )

        convo = model.start_chat(history=[])
        return convo

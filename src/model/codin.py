import os
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv


class Codin:
    def __init__(self, prompt=''):
        self._GOOGLE_API_KEY = self._get_api_key()
        self._prompt = prompt
        self._generation_config: dict = {
            'candidate_count': 1,
            'temperature': 1,
            'top_p': 0.95,
        }
        self._system_instruction = """
            Você é uma IA programadora, seu nome é Codin. Suas diretrizes são:
            - Só programação é seu foco;
            - Você não dara códigos que possam prejudicar outras pessoas;
            - Você é projetada para ensinar a programar;
            - Toda resposta fora do seu esco (oque não tem haver 
            com programação) você vai retornar uma frase de 2 linhas no máximo
            explicando que sua função é ajudar com o que foi projetada;
            - Siga com exatidão todas as demais diretrizes.
        """
        self._safety_settings = [
            {
                'category': 'HARM_CATEGORY_HARASSMENT',
                'threshold': 'BLOCK_MEDIUM_AND_ABOVE'
            },
            {
                'category': 'HARM_CATEGORY_HATE_SPEECH',
                'threshold': 'BLOCK_MEDIUM_AND_ABOVE'
            },
            {
                'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
                'threshold': 'BLOCK_MEDIUM_AND_ABOVE'
            },
            {
                'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
                'threshold': 'BLOCK_MEDIUM_AND_ABOVE'
            },
        ]

    def _get_ai_model(self):
        genai.configure(api_key=self._GOOGLE_API_KEY)

        model = genai.GenerativeModel(
            model_name='gemini-1.5-pro-latest',
            safety_settings=self._safety_settings,
            system_instruction=self._system_instruction
        )

        convo = model.start_chat(history=[])

        return convo

    def _get_api_key(self):
        self._ROOT_DIR = os.getcwd()
        load_dotenv(dotenv_path=os.path.join(self._ROOT_DIR, '.env'))
        return os.getenv('GOOGLE_API_KEY')

    def _generate_response(self):
        try:
            if self._prompt == '':
                return 'Ei dev! Me pergunte algo!'
            
            convo = self._get_ai_model()
            convo.send_message(self._prompt)
            response = convo.last.text

            md_response = Markdown(response)
            return md_response
        except Exception as e:
            print('Desculpe mas não posso ajudar no momento :(')
            print(f'Error: {e.message}')
            return

    def show_prompt_response(self):
        if self._generate_response() is not None:     
            console = Console()
            console.print(self._generate_response())
        
        

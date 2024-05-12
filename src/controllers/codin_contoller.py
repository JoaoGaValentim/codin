from src.models.codin import Codin
from rich.console import Console
from rich.markdown import Markdown
from time import sleep


class CodinController:
    @staticmethod
    def initialize_codin():
        list_sended_messages = []
        codin_exit_prompt = {"Tchau!", "Flw!", "Até!", "Fui!"}
        codin = Codin()
        chatbot = codin.create_chat_model()

        while True:
            try:
                codin_prompt = input("CODIN >> ")
                if codin_prompt in codin_exit_prompt:
                    break
                list_sended_messages.append(
                    chatbot.send_message(
                        content=codin_prompt,
                    )
                )
                sleep(3)
                console = Console()
                console.print(Markdown(chatbot.last.text))
            except KeyboardInterrupt:
                print("Opa! Já vai!")
                break
            except EOFError:
                print("Opa! Já vai!")
                break
            except Exception as e:
                print(e)
                break

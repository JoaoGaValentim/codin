from src.model.codin import Codin


class CodinController:
    @staticmethod
    def initialize_codin():
        codin_exit_prompt = {"Tchau!", "Flw!", "Até!", "Fui!"}
        while True:
            try:
                codin_prompt = input("CODIN >> ")
                codin = Codin(prompt=codin_prompt)
                codin.show_prompt_response()

                if codin_prompt in codin_exit_prompt:
                    break
            except KeyboardInterrupt:
                print("Opa! Já vai!")
                break
            except EOFError:
                print("Opa! Já vai!")
                break


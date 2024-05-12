from src.controllers.codin_contoller import CodinController


def header_app():
    print("=" * 4 + "CODIN (CODE ASSISTANT)" + "=" * 4)
    print("Developed By João Gabriel Valentim Theodoro")
    print("Github: JoaoGaValentim")


def app():
    header_app()
    CodinController.initialize_codin()


if __name__ == "__main__":
    app()

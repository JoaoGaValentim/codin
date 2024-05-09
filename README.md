# Em Português

## Codin seu assistente IA para Codar

### Introdução ao Codin

Codin é uma IA com o **Gemini-1.5-pro** por baixo do seu capô. Foi projetada para ajudar 
quem está iniciando na programação, utilizando exemplos simples de códigos e estrutura
de projetos.

Com ele você tem no seu terminal um ajudante para te ensinar
e auxiliar de maneira simples e bem legal.

### Criando o .env

Com sua IDE aberta você deve criar um arquivo **.env**. Dentro dele
vai ficar a variável de ambiente `GOOGLE_API_KEY`, portadora de sua
chave do Gemini.

```shell
GOOGLE_API_KEY=<YOUR_KEY>
```

### Inicializando o Ambiente Virtual De Desenvolvimento do Python (.venv)

Para iniciar você deve estar dentro da pasta do Codin para digitar o seguinte comando:

```shell
python -m venv .venv
```

Tudo pronto! Agora bora ativar o ambiente virtual. Para isso faça:

```shell
source .venv/bin/activate
```

Pronto!

## Instalação de dependências

Com tudo acima configurado vamos instalar as dependências:

```shell
pip install -r requirements.txt
```

Tudo finlizdo. Aproveite

# In English

### Codin your AI assistant for Coding

### Introduction to Codin

Codin is an AI with **Gemini-1.5-pro** under its hood. It was designed to help
who is starting out in programming, using simple code examples and structure
of projects.

With it you have a helper on your terminal to teach you
and help in a simple and cool way.

### Creating the .env

With your IDE open you must create a **.env** file. Inside him
the environment variable `GOOGLE_API_KEY` will remain, carrying your
Gemini key.

```shell
GOOGLE_API_KEY=<YOUR_KEY>
```

### Initializing the Python Virtual Development Environment (.venv)

To start you must be inside the Codin folder to type the following command:

```shell
python -m venv .venv
```

All ready! Now let's activate the virtual environment. To do this, do:

```shell
source .venv/bin/activate
```

Ready!

### Installation of dependencies

With everything above configured, let's install the dependencies:

```shell
pip install -r requirements.txt
```

Everything is over. Enjoy

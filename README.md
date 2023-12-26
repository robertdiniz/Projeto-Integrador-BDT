# Projeto-Integrador-BDT

## Sobre do Projeto
O sistema se resume a um aplicativo que visa guiar alunos com trilhas de estudos e oferecer oportunidades de projetos. Os alunos podem criar perfis para mostrar seu progresso nas trilhas de estudo, habilidades e competências. Dessa forma, os professores podem acompanhar o desenvolvimento do aluno e considerá-lo para participar de projetos reais, através de um website.

## Instalação

### Pré-requisitos

Certifique-se de ter Python e Django instalados em seu ambiente. Caso não tenha, siga as instruções em [Python](https://www.python.org/downloads/) e [Django](https://docs.djangoproject.com/en/4.2/topics/install/).

### Passos para a instalação:

1. Clone de Respositorio:
```sh
git clone https://github.com/robertdiniz/Projeto-Integrador-BDT.git
```
2. Acesse o seu Diretorio:
```sh
cd Projeto-Integrador-BDT
```
3. Crie o Ambiente Virtual:
```sh
python -m venv venv
```
4. Ativar Ambiente Virtual:
```sh
[Windows] .\venv\Scripts\activate
[Linux/Mac] source venv/bin/activate
```
5. Instale as Dependencias:
```sh
pip install -r requirements.txt
```
6. Execute as migrações:
```sh
python manage.py makemigrations
python manage.py migrate
```
7. Criar um superuser:
```sh
python manage.py createsuperuser
```
9. Inicie o servidor:
```sh
python manage.py runserver
```
  

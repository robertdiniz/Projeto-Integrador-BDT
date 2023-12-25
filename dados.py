import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.settings")

import django

django.setup()

import random
from usuarios.models import Perfil, Trilha
from django.contrib.auth.models import User
import requests
from faker import Faker
from django.core.files import File

fake = Faker()

def get_pdf_path():
    root_folder = os.getcwd()
    pdf_path = os.path.join(root_folder, "arquivos-exemplo", "matricula.pdf")
    if os.path.exists(pdf_path):
        return pdf_path
    return None


def populate_trilhas():
    trilhas = [
        {"nome": "Back-end", "imagem": "back-end.svg"},
        {"nome": "Front-end", "imagem": "front-end.svg"},
        {"nome": "Mobile", "imagem": "mobile.svg"},
        {"nome": "Design System", "imagem": "design-system.svg"},
    ]

    root_folder = os.getcwd()  # Obtém o diretório atual do script

    for trilha_data in trilhas:
        nome_trilha = trilha_data['nome']
        imagem_path = trilha_data['imagem']

        trilha = Trilha.objects.create(nome=nome_trilha)
        # Caminho completo para a imagem
        imagem_completa = os.path.join(root_folder, "arquivos-exemplo", imagem_path)

        # Verifica se o arquivo de imagem existe antes de tentar associá-lo
        if os.path.exists(imagem_completa):
            # Abre o arquivo de imagem e salva-o no campo Imagem da Trilha
            with open(imagem_completa, 'rb') as f:
                django_file = File(f)
                trilha.imagem.save(imagem_path, django_file, save=True)


def populate(value):
    for i in range(value):
        username = fake.name()
        user_email = fake.email()
        user_matricula = get_pdf_path()

        obj = User.objects.create(username=username, is_active=False, email=user_email)
        aluno = Perfil.objects.create(nome_completo=username, user=obj, matricula=user_matricula)


if __name__ == "__main__":
    populate(10)
    populate_trilhas()


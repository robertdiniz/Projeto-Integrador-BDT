import email
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.settings")

import django

django.setup()

import random
from usuarios.models import Perfil
from django.contrib.auth.models import User
import requests
from faker import Faker

fake = Faker()

def get_pdf_path():
    root_folder = os.getcwd()
    pdf_path = os.path.join(root_folder, "arquivos-exemplo", "matricula.pdf")
    if os.path.exists(pdf_path):
        return pdf_path
    return None


def populate(value):
    for i in range(value):
        username = fake.name()
        user_email = fake.email()
        user_matricula = get_pdf_path()

        obj = User.objects.create(username=username, is_active=False, email=user_email)
        aluno = Perfil.objects.create(nome_completo=username, user=obj, matricula=user_matricula)


if __name__ == "__main__":
    populate(10)
        


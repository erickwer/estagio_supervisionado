"""
WSGI config for Módulo_de_Gerenciamento_Estágio_e_TCC project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Módulo_de_Gerenciamento_Estágio_e_TCC.settings')

application = get_wsgi_application()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import * 

def Actualizar():
    # Borramos el contenido anterior
    run('sudo rm -rf ./IV-18-19-Proyecto')

    # Creamos la carpeta
    run('mkdir IV-18-19-Proyecto && cd IV-18-19-Proyecto')

    # Actualizamos con la nueva versión del repositorio
    run('git clone https://github.com/Thejokeri/IV-18-19-Proyecto.git')

    # Instalamos requirements
    run('pip3 install -r ./IV-18-19-Proyecto/requirements.txt')

def Iniciar():
    # Iniciamos el servicio
    run('cd IV-18-19-Proyecto && sudo gunicorn app:app -b 0.0.0.0:80')
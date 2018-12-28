#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import * 
import os 
import subprocess

exists = os.path.isdir('./IV-18-19-Proyecto')

# Funcion para instalar la aplicación en nuestra máquina
def Instalar():
    if exists:
        run('rm -rf ./IV-18-19-Proyecto')
    else:
        run('git clone https://github.com/Thejokeri/IV-18-19-Proyecto.git')
        run('pip3 install -r ./IV-18-19-Proyecto/requirements.txt')
        run('pip install --upgrade pip')


# Funcion que se encarga de actualizar la aplicación con el nuevo contenido de mi repositorio
def Actualizar():
    if exists:
        run('cd ./IV-18-19-Proyecto && git pull')
        run('pip3 install -r ./IV-18-19-Proyecto/requirements.txt')
        run('pip install --upgrade pip')
    else:
        print('Imposible actualizar la aplicación, debe de instalarla antes')


# Funcion que se encargar de Iniciar la aplicación
def Iniciar():
    if exists:
        run('cd IV-18-19-Proyecto && sudo gunicorn app:app -b 0.0.0.0:80')
    else:
        print('Imposible arrancar la aplicación, debe de instalarla antes')


# Funcion para testear si recibe correctamente el JSON
def TestDeploy():
    json = subprocess.check_output('curl 0.0.0.0:80')
    print(json)

# Funcion que se encarga de parar el proceso de ejecución de la aplicación
def Parar():
    run('pkill -f gunicorn')

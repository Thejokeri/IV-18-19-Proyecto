#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import * 
import os 

# Funcion para instalar la aplicación en nuestra máquina
def Instalar():
    run('git clone https://github.com/Thejokeri/IV-18-19-Proyecto.git')
    run('pip3 install -r ./IV-18-19-Proyecto/requirements.txt')
    run('pip install --upgrade pip')

# Funcion para borrar el archivo
def Borrar():
    run('sudo rm -rf ./IV-18-19-Proyecto')

# Funcion que se encarga de actualizar la aplicación con el nuevo contenido de mi repositorio
def Actualizar():
    exists = os.path.isdir('../IV-18-19-Proyecto')

    if exists:
        print('Existe el archivo, actualizamos la aplicación')
        run('cd ./IV-18-19-Proyecto && git pull')
        run('pip3 install -r ./IV-18-19-Proyecto/requirements.txt')
        run('pip install --upgrade pip')
    else:
        print('Imposible actualizar la aplicación, debe de instalarla antes')


# Funcion que se encargar de Iniciar la aplicación
def Iniciar():
    exists = os.path.isdir('../IV-18-19-Proyecto')

    if exists:
        print('Existe el archivo, iniciamos la aplicación')


        run('cd IV-18-19-Proyecto && sudo gunicorn app:app -b 0.0.0.0:80')
    else:
        print('Imposible arrancar la aplicación, debe de instalarla antes')


# Funcion para mostrar el STATUS del despliegue
def ShowDeploy():
    run('CURL=$(curl 0.0.0.0:80) && sudo export CURL')
    print(os.environ['CURL'])

# Funcion que se encarga de parar el proceso de ejecución de la aplicación
def Parar():
    run('sudo pkill -f gunicorn')

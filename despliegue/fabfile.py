#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import * 

# Funcion que se encarga de actualizar la aplicación con el nuevo contenido de mi repositorio
def Actualizar():
    run('sudo rm -rf ./IV-18-19-Proyecto')
    run('git clone https://github.com/Thejokeri/IV-18-19-Proyecto.git')
    run('pip3 install -r ./IV-18-19-Proyecto/requirements.txt')

# Funcion que se encargar de Iniciar la aplicación
def Iniciar():
    run('cd IV-18-19-Proyecto')
    run('sudo gunicorn app:app -b 0.0.0.0:80 &')
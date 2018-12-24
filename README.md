# IV-18-19-Proyecto

[![Build Status](https://travis-ci.com/Thejokeri/IV-18-19-Proyecto.svg?branch=master)](https://travis-ci.com/Thejokeri/IV-18-19-Proyecto)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## CloudyCloud

Proyecto de la asignatura de Infraestructura Virtual (2018-2019)

### Idea Principal

Crear un microservicio para encriptar documentos (PDF) y alojarlos en la nube. El objetivo principal, es la creación de un servicio para que los usuarios (en nuestro caso, personal sanitario) puedan almacenar archivos cifrados con información personal de los pacientes, garantizando la ley de protección de datos además de poder enviar dichos archivos a otros personales sanitarios a través de una red segura.

---

### Herramientas

Estas son las herramientas que voy a utilizar parar la creación del microservicio:

* [Python](https://www.python.org)
* [pyPdf 1.13](https://pypi.org/project/pyPdf/)
* [Flask](http://flask.pocoo.org/)
* [DEPOT - File Storage Made Easy](https://depot.readthedocs.io/en/latest/)
* [POSTGRESQL](https://www.postgresql.org)
* [psycopg](http://initd.org/psycopg/)

---

### Descripción del microservicio

El microservicio consta de una clase en la que se llevará a cabo todas las operaciones relacionadas con el microservicio, como la creación y eliminación de los usuarios determinados por un identificador correcto, además de todas las funcionalidades de añadido, eliminación y búsqueda de archivos. [Documentación de la clase](http://htmlpreview.github.io/?https://github.com/Thejokeri/IV-18-19-Proyecto/blob/master/doc/pdfupload.html) (Generado con pydoc):

```bash
pydoc -w pdfupload.py
```

La versión de Python que voy a utilizar es Python 2.7.15 ya que la versión mas reciente, no me permite ejecutar DEPOT.

Las [dependencias](./requirements.txt) que se han usado son las siguientes:

* filedepot: permite almacenar los ficheros pdf en un directorio con nombre (el identificador del fichero) y dentro del directorio, se alojará el binario del archivo, con un .json con los metadatos del fichero (nombre, fecha de creación, etc).
  
* pyPdf: se encarga de cifrar y descifrar el fichero.
  
* Flask: para la creación del microservicio web.
  
* psycopg2: es el adaptador PostgreSQL más popular para el lenguaje de programación Python. Permite realizar cualquier tipo de query de manera sencilla.

#### Para la instalación

```bash
pip install -r requirements.txt
```

#### Para arrancar los test

```bash
pytest test.py
```

#### Para arrancar el programa principal

```bash
python pdfupload.py
```

---

### Sistema de integración continua

Voy a utilizar [Travis](https://travis-ci.org/) como sistema de integración contínua, para el testeo de la clase. Está totalmente configurada y vinculada con la cuenta de GitHub.

---

### Despliegue en Heroku

El despliegue lo he realizado en Heroku. [Documentación](./doc/deploytoheroku.md)

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://cloudncloud.herokuapp.com/)

* Despliegue: [Aplicación en Heroku](https://cloudncloud.herokuapp.com/)
  
---

### Despliegue en Docker

El despliegue de Docker esta en el siguiente enlace: [Documentación.](./doc/deploytocontainer.md)

* Enlace a DockerHub: https://hub.docker.com/r/thejokeri/iv-18-19-proyecto/
* Contenedor: https://cloudncloud-container.herokuapp.com/status

### Despliegue en Zeit

El despliegue de Zeit esta en el siguiente enlace: [Documentación.](./doc/deploytocontainer.md)

* Enlace a Zeit: https://iv-18-19-proyecto-gbdylykmyc.now.sh/status

---

### Despliegue en la nube

El despliegue en la nube lo he realizado en Azure y en Google Cloud.

#### Azure

Despliegue final: 104.214.231.3

#### Google Cloud

Despliegue final: 35.232.122.71

[Documentación del despliegue en la nube.](./doc/deploytocloud.md)
# Descripción de instalación de dependencias

---

## Instalación y creación de virtualenv

En primer lugar, antes de instalar las dependencias, vamos a instalarnos y a crear un entorno virtual con virtualenv.

```bash
sudo python2 Downloads/get-pip.py
sudo python2 -m pip install virtualenv
```

### Crear un entorno

```bash
mkdir myproject
cd myproject
python3 -m venv venv
```

### Activar el entorno

```bash
source venv/bin/activate
```

### Desactivar el entorno 

```bash
deactivate
```

---

## Para instalar dependencias

```bash
pip install paquete
```

## Para listar dependecias

```bash
pip list
```

## Para buscar un paquete

```bash
pip search paquete
```

---

## Instalando las dependencias

### Instalando Flask

```bash
pip install Flask
```

### Instalando Depot

```bash
pip install filedepot
```

### Instalando Psycopg: PostgreSQL + Python

```bash
pip install psycopg2
```

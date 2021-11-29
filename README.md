# Desafio TredaSolutions

### Tecnologias usada en el desarrollo

- Python 3.7
- Django 3.2
- SQLite 3
- Visual studio code
- VirtualEnv

## Back-end

- Abrir un terminal en la carpeta del proyecto y ejecutar los siguientes comandos

```bash
# Preparar entorno con virtualenv
virtualenv env
env\Scripts\activate
```

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
```

- Una vez configurado, inicie el servidor backend

```bash
python manage.py runserver
```

- Dirigirse a http://127.0.0.1:8000/
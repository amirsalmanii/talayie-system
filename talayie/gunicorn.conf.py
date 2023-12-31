""" green unicorn WSGI server configuration. """
""" run: gunicorn -c gunicorn.conf.py config.wsgi & """
from multiprocessing import cpu_count
from config import BASE_DIR


def max_workers():    
    return cpu_count()


command = "" # gunicorn binary package path
pythonpath = BASE_DIR # project path 
bind = "0.0.0.0:5000"
workers = max_workers()
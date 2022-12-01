import os
from flask import Flask
from variables import cargarVariables

app = Flask(__name__)

app.config.from_pyfile('settings.py')
cargarVariables()
  
import rutas_inicio

import rutas_upload

import rutas_verfichero

import rutas_coches

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)

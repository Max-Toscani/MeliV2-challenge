from flask import Flask
#Declaro el objeto requerido por Flask acorde a la doc del proyecto
app = Flask(__name__)
#Linkeo con lo que defino en views
from app import views



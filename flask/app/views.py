from flask import request , jsonify
import re
from app import app

#Para crear las rutas
@app.route('/', methods=['GET'])

#Función principal

def apilibro():
    #Para tomar los args del string
    doc_name = request.args.get('doc_name')
    term = request.args.get('term')
    #return gettermino(doc_name,term) para devolver en json el resultado
    return jsonify({"frecuencia": gettermino(doc_name,term)})

#Función que abre los archivos y los normaliza

def gettermino(doc_name,term):
    workdir = '/app/app/libros/'    #Aca apunto a la carpeta dónde guarde la colección de Docs
    file = open(workdir+doc_name, "r",encoding='utf-8')
    string = file.read()
    lower_string = string.lower()
    no_number_string = re.sub(r'\d+','',lower_string)
    no_punc_string = re.sub(r'[^\w\s]','', no_number_string)
    no_wspace_string = no_punc_string.strip()
    lst_string = no_wspace_string.split()
    lst_string = lst_string.count(term)
    return lst_string


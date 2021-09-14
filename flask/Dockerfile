FROM python:3.9-buster
#Aca declaro la imagen. Es importante que sea esta por uWSGI. 
WORKDIR /app
#Aca defino el workdir en dónde alojar la app
ADD . /app
#Aca agrego el sudirectorio APP. También copio el contenido de la carpeta DOCS en /app/libros
RUN pip install -r requirements.txt
#instalo los paquetes necesarios
RUN pip install uwsgi
# tengo que instalar aparte uWGSI para que se haga correctamente
CMD ["uwsgi", "app.ini"]
#Aca inicio los servicios
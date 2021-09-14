from app import views
#Importo el source de la función que quiero testear

#Mi comprobación le pasa 2 valores que se que tienen que dar 37.
def test_gettermino():
    assert views.gettermino(doc_name='5985-8.txt',term='casa') == 37


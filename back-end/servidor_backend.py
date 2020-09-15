from config import *
from modelo import Roupa

@app.route("/")
def inicio():
    return 'Sistema para cadastro de roupas '+\
        '<a href="/listar_roupas">Listar Roupas</a>'

@app.route("/listar_roupas")
def listar_roupas():

    roupas = db.session.query(Roupa).all()
    roupa_em_json = [Roupa.json() for Roupa in roupas]
    
    return (jsonify(roupa_em_json))


app.run(debug=True)
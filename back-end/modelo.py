
from config import *

class Roupa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(254))
    tamanho = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    tecido = db.Column(db.String(254))    
    marca = db.Column(db.String(254))

    def __str__(self):
        return  str(self.id)+") " + str(self.modelo) + ", " +\
            str(self.tamanho) + " , " + str(self.cor) + " , " +\
                str(self.tecido) + " , " + str(self.marca)

    def json(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "tamanho": self.tamanho,
            "cor": self.cor,
            "tecido": self.tecido,
            "marca": self.marca,
        }

if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1= Roupa(modelo="camiseta", tamanho="P", cor="azul", tecido="jeans", marca="nike")
    p2= Roupa(modelo="camisa", tamanho="G", cor="rosa", tecido="algodao", marca="adidas")

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    print(p1.json())
    print(p2.json())
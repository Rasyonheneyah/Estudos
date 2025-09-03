class Espada:
    def __init__(material_lamina, material_empunhadura, encantamento):
        self.lamina = material_lamina
        self.empunhadura = material_empunhadura
        self.tipo = tipo
        self.encantamento = encantamento

    materiaisL = {
        pedra :10 , 
        ferro :45 , 
        diamante :95
        }
    materiaisE = [
        madeira :1.5, 
        borracha:3,
        titanio :7
        ]

    def enc_fogo():
        pass
    def enc_agua():
        pass
    def enc_terra():
        pass
    def enc_vento():
        pass
    def enc_nenhum():
        pass

    def ataque01(material_empunhadura, material):
        dano = materiaisL(material_lamina)*materiaisE(material_empunhadura)  
    def ataque02():
        pass



    encantamentos = [enc_fogo, enc_agua, enc_terra, enc_vento , enc_nenhum     ]


sword_of_artorias = (ferro, madeira, fogo)

sword_of_artorias.ataque01
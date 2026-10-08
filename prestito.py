class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice=codice
        self.data=data
        self.id_strumento=id_strumento
        self.cognome_allievo=cognome_allievo

    def __str__(self):
        return f"{self.codice}, {self.id_strumento}, {self.cognome_allievo}"

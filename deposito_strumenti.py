from csv import reader
from operator import attrgetter
from strumento import Strumento
from prestito import Prestito


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumento=[]
        self.prestito=[]

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            file=open(file_path, "r")
            dati=reader(file)
            for dato in dati:
                codice = str(dato[0])
                tipo = str(dato[1])
                marca = str(dato[2])
                anno_acquisto = int(dato[3])
                valore = float(dato[4])
                s=Strumento(codice, tipo, marca, anno_acquisto, valore)
                self.strumento.append(s)
            file.close()

        except FileNotFoundError:
            print("Errore nell'apertura del file!")
            return None

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        max_codice=0
        for elemento in self.strumento:
            codice=int(elemento.codice[1:])
            if codice > max_codice:
                max_codice=codice
        codice="S"+str(max_codice+1)
        s= Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumento.append(s)
        return s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        strumenti_ordinati=sorted(self.strumento, key=attrgetter('marca'))
        return strumenti_ordinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        for p in self.prestito:
            if p.id_strumento == id_strumento:
                print("Strumento già in prestito!")
                raise Exception

        for s in self.strumento:
           if s.codice == id_strumento:
                break
        else:
            print("Strumento non trovato!")
            raise Exception

        i = 1
        for p in self.prestito:
         numero = int(p.codice[1:])
         if numero >= i:
             i = numero + 1

        codice = "P" + str(i)

        pr = Prestito(codice, data, id_strumento, cognome_allievo)
        self.prestito.append(pr)
        return pr


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for p in self.prestito:
            if p.codice==id_prestito:
                self.prestito.remove(p)
                return p
        else:
            raise Exception("Prestito non trovato!")




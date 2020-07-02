from MusicClass import Music

class Service:
    def __init__(self):
        self._ListaMuzicala = []

    def rememorate(self):
        f = open("database","r")
        nrMuzici = int(f.readline())

        for muzici in range(nrMuzici):
            Titlu = f.readline().replace("\n", "")
            Autor = f.readline().replace("\n", "")
            Link = f.readline().replace("\n", "")
            self._ListaMuzicala.append(Music(Titlu,Autor,Link))

        f.close()

    def adaugare(self,titlu,autor,link):
        self._ListaMuzicala.append(Music(titlu,autor,link))

    def prezentare(self):
        i = 1
        for Muzica in self._ListaMuzicala:
            print(i,end="|")
            i += 1
            print(Muzica)

    def cautare_Link(self,Titlu):
        for muzica in self._ListaMuzicala:
            if (str(muzica.get_Titlu()) == Titlu):
                a = muzica.get_Link()
                return str(a)

    def cautare_Stergere(self,Titlu):
        for i,muzica in enumerate(self._ListaMuzicala):
            if (str(muzica.get_Titlu()) == Titlu):
                del self._ListaMuzicala[i]

    def get_nr_muzici(self):
        f = open("database", "r")
        nrMuzici = int(f.readline())

        f.close()
        return nrMuzici

    def scoatere_in_Memorie(self,NumarMuzici1):
        f = open("database","w")

        NumarMuzici = str(NumarMuzici1)

        f.writelines(NumarMuzici)
        f.writelines("\n")

        for muzica in self._ListaMuzicala:

            Titlu = muzica.get_Titlu()
            Autor = muzica.get_Trupa()
            Link = muzica.get_Link()

            f.writelines(Titlu)
            f.writelines("\n")

            f.writelines(Autor)
            f.writelines("\n")

            f.writelines(Link)
            f.writelines("\n")

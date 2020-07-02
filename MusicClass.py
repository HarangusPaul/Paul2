class Music:
    def __init__(self,Titlu,Trupa,Link):
        self._Titlu = Titlu
        self._Trupa = Trupa
        self._Link = Link

    def get_Titlu(self):
        return self._Titlu

    def set_Titlu(self,Titlu):
        self._Titlu = Titlu

    def get_Trupa(self):
        return self._Trupa

    def set_Trupa(self, Trupa):
        self._Trupa = Trupa

    def get_Link(self):
        return self._Link

    def set_Link(self, Link):
        self._Link = Link

    def __repr__(self):
        return "Titlu : {0} , Autor : {1}".format(self._Titlu,self._Trupa)

    def __str__(self):
        return "{0}".format(self._Titlu)

    def __eq__(self, other):
        return other.get_Titlu == self.get_Titlu()


from service import Service
from Interface import Interface

if __name__ == '__main__':
    serviciu = Service()
    interface = Interface(serviciu)
    interface.meniu()
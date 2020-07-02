from service import Service
from MusicClass import Music
import tkinter as tk
import re
import webbrowser

class Interface:
    def __init__(self,service):
        self.__service = service
        self.nrmuzici = self.__service.get_nr_muzici()

    def start(self):
        self.__service.rememorate()
        print("Program incarcat 100%")

    def stop(self):
        self.__service.scoatere_in_Memorie(self.nrmuzici)
        print("Program pregatit pentru inchidere!GoodBye")

    def Adaugare(self,Titlu,Autor,Link):
        if (Titlu != " " and Autor != " " and Link != " "):
            self.__service.adaugare(Titlu,Autor,Link)
        else:
            print("Err")

    def stergere(self,Titlu):
        if (Titlu != " "):
            self.__service.cautare_Stergere(Titlu)
            print("sters")

    def run_Link(self,Titlu):
        link = str(self.__service.cautare_Link(Titlu))

        link_Test = re.split('/',link)

        if (link_Test[0] == "https:"):
            webbrowser.open_new_tab(link)

    def Frame_de_Introducere(self):
        window2 = tk.Tk()
        window2.geometry("400x300")
        window2.title("Add")

        self.nrmuzici = self.nrmuzici + 1

        Titlu_Entry =  tk.Entry(window2,font=60)
        Titlu_Entry.place(x=100,y=0,width=300,height=40)

        T_label = tk.Label(window2,bg="yellow",text="Titlu")
        T_label.place(x=0,y=0,width=100,height=40)

        Autor_Entry = tk.Entry(window2, font=60)
        Autor_Entry.place(x=100, y=40, width=300, height=40)

        A_label = tk.Label(window2, bg="yellow", text="Autor")
        A_label.place(x=0, y=40, width=100, height=40)

        Link_Entry = tk.Entry(window2, font=60)
        Link_Entry.place(x=100, y=80, width=300, height=40)

        L_label = tk.Label(window2, bg="yellow", text="Link")
        L_label.place(x=0, y=80, width=100, height=40)

        Trimite_Info = tk.Button(window2,bg="red",text="Add",command=lambda: self.Adaugare(Titlu_Entry.get(),Autor_Entry.get(),Link_Entry.get()))
        Trimite_Info.place(x=125,y=180,width=150,height=80)

        window2.mainloop()

    def Frame_de_Stergere(self):
        window2 = tk.Tk()
        window2.geometry("250x150")
        window2.title("Stergere")

        self.nrmuzici = self.nrmuzici - 1

        T_Entry = tk.Entry(window2,font=60)
        T_Entry.place(x=50,y=0,width=200,height=50)

        T_label = tk.Label(window2, bg="yellow", text="Titlu")
        T_label.place(x=0, y=0, width=50, height=50)

        Stergere = tk.Button(window2,text="stergere",bg="red",command=lambda: self.stergere(T_Entry.get()))
        Stergere.place(x=100,y=75,width=50,height=50)

        window2.mainloop()

    def Frame_de_Run(self):
        window2 = tk.Tk()
        window2.geometry("250x150")
        window2.title("Run")

        T_Entry = tk.Entry(window2,font=60)
        T_Entry.place(x=50,y=0,width=200,height=50)

        T_label = tk.Label(window2, bg="yellow", text="Titlu")
        T_label.place(x=0, y=0, width=50, height=50)

        Run = tk.Button(window2,text="Run",bg="red",command=lambda: self.run_Link(T_Entry.get()))
        Run.place(x=100,y=75,width=50,height=50)

        window2.mainloop()

    def meniu(self):
        self.start()

        window1 = tk.Tk()
        window1.geometry("250x190")
        window1.title("Main")

        B_adaugare = tk.Button(window1,bg="red",text="Adaugare element",command=lambda: self.Frame_de_Introducere())
        B_adaugare.place(x=40,y=20,width=170,height=50)

        B_stergere = tk.Button(window1,bg="red",text="Stergere element",command=lambda: self.Frame_de_Stergere())
        B_stergere.place(x=40, y=70, width=170, height=50)

        B_run = tk.Button(window1, bg="red", text="Deschidere link/Informatii link", command=lambda: self.Frame_de_Run())
        B_run.place(x=40, y=120, width=170, height=50)

        window1.mainloop()

        self.stop()















# def printing(entry):
#     print(entry)
#
# def window2():
#     root = tk.Tk()
#
#     frame = tk.Frame(root,bg="blue")
#     frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
#
#     entry = tk.Entry(frame,font=60)
#     entry.place(relwidth=0.3,relheight=0.1)
#
#     button = tk.Button(frame,text="print",command=lambda: printing(entry.get()))
#     button.place(x=40, y=0, width=50, height=20)
#
#     root.mainloop()
#
# def main():
#     window = tk.Tk()
#
#     button = tk.Button(window, text="Press", command=window2)
#     button.pack()
#
#     window.mainloop()
#
# main()

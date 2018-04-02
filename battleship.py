import random
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, background="lightblue")
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Statki")
        self.pack(fill=BOTH, expand=1)
        writen = Label(self, text="Witaj w grze Statki", foreground="white", background="lightblue",
                       font=("Arial", 44, "italic"))
        writen.place(x=400, y=50, anchor=CENTER)
        # photo=PhotoImage(file="C:/Users/Adrian/Desktop/Missouri_post_refit.gif")
        # picture=Label(self, image=photo)
        # picture.place(x=400, y=400, anchor=CENTER)
        quitButton = Button(self, text="Wyjscie", width=15, font=("Arial", 24, "italic"), background="blue",
                            command=self.client_exit)
        quitButton.place(x=200, y=140, anchor=CENTER)
        openButton = Button(self, text="Rozpocznij gre", width=15, font=("Arial", 24, "italic"), background="blue",
                            command=self.game)
        openButton.place(x=570, y=140, anchor=CENTER)

    def client_exit(self):
        exit()

    def w(self, i, j, tablica, tablica1, wygrana, przegrana, s2, s3, s4, s41, s5, s6, s7, w2, w3, w4, w41, w5, w6, w7,
          event):

        if tablica[i][j] == 6 or tablica[i][j] == 5 or tablica[i][j] == 4 or tablica[i][j] == 3 or tablica[i][j] == 2 or \
                tablica[i][j] == 7 or tablica[i][j] == 41:
            c = Label(root, text="      ", bg="black")
            c.place(x=430 + (j * 30), y=250 + (i * 25))
            wygrana.append(1)
            if tablica[i][j] == 7:
                w7.append(1)
                if len(w7) == 7:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s7[a][b] == 1:
                                print("True")
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))
            if tablica[i][j] == 6:
                w6.append(1)
                if len(w6) == 6:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s6[a][b] == 1:
                                print("True")
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))
            if tablica[i][j] == 5:
                w5.append(1)
                if len(w5) == 5:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s5[a][b] == 1:
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))
            if tablica[i][j] == 4:
                w4.append(1)
                if len(w4) == 4:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s4[a][b] == 1:
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))
            if tablica[i][j] == 41:
                w41.append(1)
                if len(w41) == 4:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s41[a][b] == 1:
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))
            if tablica[i][j] == 3:
                w3.append(1)
                if len(w3) == 3:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s3[a][b] == 1:
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))
            if tablica[i][j] == 2:
                w2.append(1)
                if len(w2) == 2:
                    for a in range(0, 10):
                        for b in range(0, 10):
                            if s2[a][b] == 1:
                                d = Label(root, text="      ", bg="yellow")
                                d.place(x=430 + (b * 30), y=250 + (a * 25))

            if len(wygrana) == 31:
                writen1 = Label(self, text="WYGRAŁES!!!", foreground="red", background="lightblue",
                                font=("Arial", 32, "italic"))
                writen1.place(x=430, y=550, anchor=CENTER)

        else:
            d = Label(root, text="      ", bg="yellow")
            d.place(x=430 + (j * 30), y=250 + (i * 25))
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            while tablica1[a][b] == 2:
                a = random.randint(0, 9)
                b = random.randint(0, 9)
            while tablica1[a][b] == 1:
                tmp1 = a
                tmp2 = b
                d = Label(root, text="      ", bg="black")
                d.place(x=50 + (b * 30), y=250 + (a * 25))
                przegrana.append(1)
                if tmp1 > 1 and tmp1 < 9:
                    a = random.randint(tmp1 - 1, tmp1 + 1)
                if tmp2 > 1 and tmp2 < 9:
                    b = random.randint(tmp2 - 1, tmp2 + 1)
                while tablica1[a][b] == 2:
                    a = random.randint(0, 9)
                    b = random.randint(0, 9)
            d = Label(root, text="      ", bg="yellow")
            d.place(x=50 + (b * 30), y=250 + (a * 25))
            if len(przegrana) >= 31:
                writen5 = Label(self, text="PRZEGRAŁES ;(", foreground="red", background="lightblue",
                                font=("Arial", 32, "italic"))
                writen5.place(x=430, y=550, anchor=CENTER)

    def wstawianie(self, tablica1, i, j, event):
        tablica1[i][j] = 1
        d = Label(root, text="      ", bg="orange")
        d.place(x=50 + (j * 30), y=250 + (i * 25))

    def plansza(self, tablica1):
        writen3 = Label(self, text="TWOJA PLANSZA", foreground="red", background="lightblue",
                        font=("Arial", 24, "italic"))
        writen3.place(x=200, y=210, anchor=CENTER)
        writen5 = Label(self, text="Ustaw 1x7, 1x6, 1x5, 2x4, 1x3, 1x2 i przejdź do planszy przeciwnika",
                        foreground="black", background="lightblue", font=("Arial", 10, "italic"))
        writen5.place(x=200, y=510, anchor=CENTER)
        writen4 = Label(self, text="PLANSZA PRZECIWNIKA", foreground="red", background="lightblue",
                        font=("Arial", 24, "italic"))
        writen4.place(x=580, y=210, anchor=CENTER)
        for k in range(10):  # Rows
            for l in range(10):  # Columns
                g = Label(self, text="      ", bg="blue", )
                g.bind('<Button-1>', lambda e, tablica1=tablica1, k=k, l=l: self.wstawianie(tablica1, k, l, e))
                g.place(x=50 + (l * 30), y=250 + (k * 25))

    def game(self):
        tablica = [[0] * 10 for _ in range(10)]
        tablica1 = [[0] * 10 for _ in range(10)]

        def wstawianie(dlugosc, tablica, s, statek):
            p = random.randint(0, 1)
            if p == 1:
                r = 0
                while r != dlugosc:
                    r = 0
                    x = random.randint(0, 9 - dlugosc)
                    y = random.randint(0, 9)
                    for i in range(0, dlugosc):
                        if tablica[x + i][y] == 0:
                            r += 1
                for i in range(0, dlugosc):
                    tablica[x + i][y] = s
                if y > 0:
                    for i in range(0, dlugosc):
                        tablica[x + i][y - 1] = 1
                        statek[x + i][y - 1] = 1
                    if x > 0:
                        tablica[x - 1][y - 1] = 1
                        tablica[x - 1][y] = 1
                        statek[x - 1][y - 1] = 1
                        statek[x - 1][y] = 1
                    if x < 9:
                        tablica[x + dlugosc][y - 1] = 1
                        tablica[x + dlugosc][y] = 1
                        statek[x + dlugosc][y - 1] = 1
                        statek[x + dlugosc][y] = 1
                if y < 9:
                    for i in range(0, dlugosc):
                        tablica[x + i][y + 1] = 1
                        statek[x + i][y + 1] = 1
                    if x > 0:
                        tablica[x - 1][y + 1] = 1
                        tablica[x - 1][y] = 1
                        statek[x - 1][y + 1] = 1
                        statek[x - 1][y] = 1
                    if x < 9:
                        tablica[x + dlugosc][y + 1] = 1
                        tablica[x + dlugosc][y] = 1
                        statek[x + dlugosc][y + 1] = 1
                        statek[x + dlugosc][y] = 1

            else:
                r = 0
                while r != dlugosc:
                    r = 0
                    x = random.randint(0, 9)
                    y = random.randint(0, 9 - dlugosc)
                    for i in range(0, dlugosc):
                        if tablica[x][y + i] == 0:
                            r += 1
                for i in range(0, dlugosc):
                    tablica[x][y + i] = s
                if x > 0:
                    for i in range(0, dlugosc):
                        tablica[x - 1][y + i] = 1
                        statek[x - 1][y + i] = 1
                    if y > 0:
                        tablica[x - 1][y - 1] = 1
                        tablica[x][y - 1] = 1
                        statek[x - 1][y - 1] = 1
                        statek[x][y - 1] = 1
                    if y < 9:
                        tablica[x - 1][y + dlugosc] = 1
                        tablica[x][y + dlugosc] = 1
                        statek[x - 1][y + dlugosc] = 1
                        statek[x][y + dlugosc] = 1
                if x < 9:
                    for i in range(0, dlugosc):
                        tablica[x + 1][y + i] = 1
                        statek[x + 1][y + i] = 1
                    if y > 0:
                        tablica[x + 1][y - 1] = 1
                        tablica[x][y - 1] = 1
                        statek[x + 1][y - 1] = 1
                        statek[x][y - 1] = 1
                    if y < 9:
                        tablica[x + 1][y + dlugosc] = 1
                        tablica[x][y + dlugosc] = 1
                        statek[x + 1][y + dlugosc] = 1
                        statek[x][y + dlugosc] = 1

        s7 = [[0] * 10 for _ in range(10)]
        s6 = [[0] * 10 for _ in range(10)]
        s5 = [[0] * 10 for _ in range(10)]
        s4 = [[0] * 10 for _ in range(10)]
        s41 = [[0] * 10 for _ in range(10)]
        s3 = [[0] * 10 for _ in range(10)]
        s2 = [[0] * 10 for _ in range(10)]

        wstawianie(7, tablica, 7, s7)
        wstawianie(6, tablica, 6, s6)
        wstawianie(5, tablica, 5, s5)
        wstawianie(4, tablica, 4, s4)
        wstawianie(4, tablica, 41, s41)
        wstawianie(3, tablica, 3, s3)
        wstawianie(2, tablica, 2, s2)
        w7 = []
        w6 = []
        w5 = []
        w41 = []
        w4 = []
        w3 = []
        w2 = []

        self.plansza(tablica1)
        print(tablica1)
        wygrana = []
        przegrana = []
        i = 0
        for k in range(10):  # Rows
            for l in range(10):  # Columns
                b = Label(self, text="      ", bg="blue", )
                b.bind('<Button-1>',
                       lambda e, tablica=tablica, tablica1=tablica1, wygrana=wygrana, przegrana=przegrana, s2=s2, s3=s3,
                              s4=s4, s41=s41, s5=s5, s6=s6, s7=s7, w7=w7, w6=w6, w5=w5, w4=w4, w3=w3, w2=w2, w41=w41,
                              k=k, l=l: self.w(k, l, tablica, tablica1, wygrana, przegrana, s2, s3, s4, s41, s5, s6, s7,
                                               w2, w3, w4, w41, w5, w6, w7, e))
                b.place(x=430 + (l * 30), y=250 + (k * 25))
                i += 1


# class Window1(Frame):

root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()

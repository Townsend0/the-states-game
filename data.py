import turtle
import pandas
class Map:
    def __init__(self):
        self.a = turtle.Screen()
        self.a.title("GUESS US STATES GAME")
        self.a.addshape("blank_states_img.gif")
        self.a.setup(745,502)
        self.b = turtle.Turtle("blank_states_img.gif")
        self.c = turtle.Turtle()
        self.c.hideturtle()
        self.d = " "
        self.e = pandas.read_csv("50_states.csv")
        self.f = turtle.Turtle()
        self.g = 0
        self.h = turtle.Turtle()
        self.i = pandas.read_csv("50_states.csv")["state"].tolist()
        self.j = pandas.read_csv("50_states.csv")["state"].tolist()

    def win(self):
        self.h.clear()
        self.h.hideturtle()
        self.b.hideturtle()
        self.h.goto(0,0)
        self.h.write("YOU WON!",False,"center",("courier",20,"normal"))
        self.a.update()

    def writing_settings(self):
        self.f.penup()
        self.f.hideturtle()

    def answer(self):
        self.d = self.a.textinput(f"{self.g}/50".title(),"Enter a state's name: ").lower()
        return self.d

    def print_answer(self):
        for a in range(50):
            if self.i[a].lower() == self.d.lower():
                self.g +=1
                self.f.goto(self.e["x"][a],self.e["y"][a])
                self.f.write(f"{self.d}",False,"left")

    def check_answer(self):
        for a in range(50):
            if self.d == self.i[a].lower():
                self.j.remove(self.d.title())
                return True
            
    def missed_countries(self):
        if self.d =="exit":
            pandas.DataFrame(self.j).to_csv("missed_states.csv")
            
    
    

import pandas
import data
e = []
a = data.Map()
c = pandas.read_csv("50_states.csv")["state"].tolist()
g = pandas.read_csv("50_states.csv")["state"].tolist()
a.writing_settings()
while len(e) < 50:
    f = a.answer()
    if f not in e and a.check_answer():
        e.append(f)
        g.remove(f.title())
        a.print_answer()
    if f == "exit":
        a.missed_countries()
        break
if len(e) == 50:
    a.win()

a.mainloop()

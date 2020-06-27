from molmass import Formula, ELEMENTS
import tkinter as tk
import tkinter.ttk

# TODO: convert to *.exe file
# TODO: perform calculations for m and n

window = tk.Tk()
window.title("Stoichiometry Helper")

window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))


# ---- FUNCTIONS ----

def done():

    a = str(get_chemical1.get())
    b = str(get_chemical2.get())
    c = str(get_chemical3.get())
    d = str(get_chemical4.get())

    newMm = tk.Label(text="Molar Mass (g/mol):", font=("Courier New", 10))
    newMm.grid(row=7, column=0)

    c1 = tk.Text(master=window, height=1, width=15)
    c1.grid(row=7, column=1)
    c1.insert(tk.END, Formula(a).mass)
    c2 = tk.Text(master=window, height=1, width=15)
    c2.grid(row=7, column=3)
    c2.insert(tk.END, Formula(b).mass)
    c3 = tk.Text(master=window, height=1, width=15)
    c3.grid(row=7, column=5)
    c3.insert(tk.END, Formula(c).mass)
    c4 = tk.Text(master=window, height=1, width=15)
    c4.grid(row=7, column=7)
    c4.insert(tk.END, Formula(d).mass)

    p1 = tk.Text(master=window, height=5, width=42)
    p1.grid(row=0, column=9, padx=(90, 0))
    p1.insert(tk.END, str(Formula(a).composition()))
    p2 = tk.Text(master=window, height=5, width=42)
    p2.grid(row=1, column=9, padx=(90, 0))
    p2.insert(tk.END, str(Formula(b).composition()))
    p3 = tk.Text(master=window, height=5, width=42)
    p3.grid(row=2, column=9, padx=(90, 0))
    p3.insert(tk.END, str(Formula(c).composition()))
    p4 = tk.Text(master=window, height=5, width=42)
    p4.grid(row=3, column=9, padx=(90, 0))
    p4.insert(tk.END, str(Formula(d).composition()))

    data = [[getMR1.get(), getm1.get(), getn1.get(), Formula(a).mass],
            [getMR2.get(), getm2.get(), getn2.get(), Formula(b).mass],
            [getMR3.get(), getm3.get(), getn3.get(), Formula(c).mass],
            [getMR4.get(), getm4.get(), getn4.get(), Formula(d).mass]]

    for i in data:
        if i[1] == i[2] == 0.0:
            pass
        else:
            if i[1] != 0.0:
                i[2] = float(i[1]) / float(i[3])
            else:
                i[1] = float(i[2]) * float(i[3])

    


def description():

    a = ELEMENTS[str(getelement.get())]

    d = tk.Text(master=window, width=60, height=6)
    d.grid(row=6, column=9, padx=(60, 0), pady=(20, 20))
    d.insert(tk.END, a.description)


# ---- LABELS ----

chemical = tk.Label(text="Unbalanced Chemical Equation:", font=("Courier New", 10, 'bold'))
chemical.grid(row=0, column=0, pady=(30, 30))
MR = tk.Label(text="Molar Ratio/Coefficients (MR):", font=("Courier New", 10, 'bold'))
MR.grid(row=1, column=0, pady=(30, 30))
m = tk.Label(text="Mass (g):", font=("Courier New", 10, 'bold'))
m.grid(row=2, column=0, pady=(30, 30))
n = tk.Label(text="Moles (mol):", font=("Courier New", 10, 'bold'))
n.grid(row=3, column=0, pady=(30, 30))
Mm = tk.Label(text="Molar Mass (g/mol)", font=("Courier New", 10, 'bold'))
Mm.grid(row=4, column=0, pady=(30, 30))

plus1 = tk.Label(text="+", font=("Courier New", 10, 'bold'))
plus1.grid(row=0, column=2)
plus2 = tk.Label(text="+", font=("Courier New", 10, 'bold'))
plus2.grid(row=0, column=6)
equals = tk.Label(text="---->", font=("Courier New", 10, 'bold'))
equals.grid(row=0, column=4)

colon1 = tk.Label(text=":", font=("Courier New", 10, 'bold'))
colon1.grid(row=1, column=2)
colon2 = tk.Label(text=":", font=("Courier New", 10, 'bold'))
colon2.grid(row=1, column=4)
colon3 = tk.Label(text=":", font=("Courier New", 10, 'bold'))
colon3.grid(row=1, column=6)

# ---- ENTRY FIELDS ----

get_chemical1 = tk.Entry()
get_chemical1.grid(row=0, column=1)
get_chemical2 = tk.Entry()
get_chemical2.grid(row=0, column=3)
get_chemical3 = tk.Entry()
get_chemical3.grid(row=0, column=5)
get_chemical4 = tk.Entry()
get_chemical4.grid(row=0, column=7, padx=(0, 20))

getMR1 = tk.Entry()
getMR1.grid(row=1, column=1)
getMR2 = tk.Entry()
getMR2.grid(row=1, column=3)
getMR3 = tk.Entry()
getMR3.grid(row=1, column=5)
getMR4 = tk.Entry()
getMR4.grid(row=1, column=7, padx=(0, 20))

getm1 = tk.Entry()
getm1.insert(0, 0.0)
getm1.grid(row=2, column=1)
getm2 = tk.Entry()
getm2.insert(0, 0.0)
getm2.grid(row=2, column=3)
getm3 = tk.Entry()
getm3.insert(0, 0.0)
getm3.grid(row=2, column=5)
getm4 = tk.Entry()
getm4.insert(0, 0.0)
getm4.grid(row=2, column=7, padx=(0, 20))

getn1 = tk.Entry()
getn1.insert(0, 0.0)
getn1.grid(row=3, column=1)
getn2 = tk.Entry()
getn2.insert(0, 0.0)
getn2.grid(row=3, column=3)
getn3 = tk.Entry()
getn3.insert(0, 0.0)
getn3.grid(row=3, column=5)
getn4 = tk.Entry()
getn4.insert(0, 0.0)
getn4.grid(row=3, column=7, padx=(0, 20))

getMm1 = tk.Entry()
getMm1.insert(0, 0.0)
getMm1.grid(row=4, column=1)
getMm2 = tk.Entry()
getMm2.insert(0, 0.0)
getMm2.grid(row=4, column=3)
getMm3 = tk.Entry()
getMm3.insert(0, 0.0)
getMm3.grid(row=4, column=5)
getMm4 = tk.Entry()
getMm4.insert(0, 0.0)
getMm4.grid(row=4, column=7, padx=(0, 20))

getelement = tk.Entry(width=60)
getelement.grid(row=4, column=9, padx=(150, 50))

# ---- BUTTONS ----

submit = tk.Button(text="Submit", command=done, height=1, width=7, bg="#c8c8c8").grid(row=5, column=7, pady=(0, 20))

tkinter.ttk.Separator(window, orient='vertical').grid(column=8, row=0, rowspan=10, sticky='ns')

desc = tk.Button(text="^^^ Get description of the element entered above ^^^", command=description, bg="#c8c8c8")\
    .grid(row=5, column=9, padx=(150, 50))

window.mainloop()

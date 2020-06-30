from molmass import Formula, ELEMENTS
import tkinter as tk
import tkinter.ttk

window = tk.Tk()
window.title("Stoichiometry Helper")

# makes window size default to fullscreen
window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))


# ---- FUNCTIONS ----

def done():

    a = str(get_chemical1.get())
    b = str(get_chemical2.get())
    c = str(get_chemical3.get())
    d = str(get_chemical4.get())

    newMm = tk.Label(text="Molar Mass (g/mol):", font=("Segoe UI", 10))
    newMm.grid(row=7, column=0)

    computed_Mm_value1 = tk.Text(master=window, height=1, width=15)
    computed_Mm_value1.grid(row=7, column=1)
    computed_Mm_value1.insert(tk.END, Formula(a).mass)
    computed_Mm_value2 = tk.Text(master=window, height=1, width=15)
    computed_Mm_value2.grid(row=7, column=3)
    computed_Mm_value2.insert(tk.END, Formula(b).mass)
    computed_Mm_value3 = tk.Text(master=window, height=1, width=15)
    computed_Mm_value3.grid(row=7, column=5)
    computed_Mm_value3.insert(tk.END, Formula(c).mass)
    computed_Mm_value4 = tk.Text(master=window, height=1, width=15)
    computed_Mm_value4.grid(row=7, column=7)
    computed_Mm_value4.insert(tk.END, Formula(d).mass)

    percent_composition1 = tk.Text(master=window, height=5, width=42)
    percent_composition1.grid(row=0, column=9, padx=(90, 0))
    percent_composition1.insert(tk.END, str(Formula(a).composition()))
    percent_composition2 = tk.Text(master=window, height=5, width=42)
    percent_composition2.grid(row=1, column=9, padx=(90, 0))
    percent_composition2.insert(tk.END, str(Formula(b).composition()))
    percent_composition3 = tk.Text(master=window, height=5, width=42)
    percent_composition3.grid(row=2, column=9, padx=(90, 0))
    percent_composition3.insert(tk.END, str(Formula(c).composition()))
    percent_composition4 = tk.Text(master=window, height=5, width=42)
    percent_composition4.grid(row=3, column=9, padx=(90, 0))
    percent_composition4.insert(tk.END, str(Formula(d).composition()))

    data = [[getMR1.get(), getm1.get(), getn1.get(), Formula(a).mass],
            [getMR2.get(), getm2.get(), getn2.get(), Formula(b).mass],
            [getMR3.get(), getm3.get(), getn3.get(), Formula(c).mass],
            [getMR4.get(), getm4.get(), getn4.get(), Formula(d).mass]]

    # locate the sublist of data where values are filled in for mass and moles
    # if moles are given, find mass and vice versa
    # use equation (n = m / Mm) or (moles = mass / molar mass) or (mol = g / g/mol)
    for i in data:
        if i[1] == i[2] == 0.0:
            pass
        else:
            if i[1] != 0.0:
                i[2] = float(i[1]) / float(i[3])
            else:
                i[1] = float(i[2]) * float(i[3])

    # locate the lists where mass and moles have been calculated
    # calculate the number of moles of that compound as if molar ratio is 1 (k)
    # for instance, if n = 2.4 and MR = 2, k = 1.2
    for j in data:
        if j[1] != 0.0 and j[2] != 0.0:
            z = j

            k = float(z[2]) / float(z[0])

            # calculate the moles of the remaining compounds based on molar mass and #moles (n) adjusted for MR
            for q in data:
                q[2] = float(k) * float(q[0])

            # calculate the mass of the remaining compounds based on molar mass and #moles (n) adjusted for MR
            for r in data:
                r[1] = float(r[2]) * float(r[3])

            finished_mass_label = tk.Label(text="Moles (mol): ", font=("Segoe UI", 10))
            finished_mass_label.grid(row=8, column=0)

            finished_moles_label = tk.Label(text="Mass (g)", font=("Segoe UI", 10))
            finished_moles_label.grid(row=9, column=0)

            computed_n_value1 = tk.Text(master=window, height=1, width=15)
            computed_n_value1.grid(row=8, column=1)
            computed_n_value1.insert(tk.END, data[0][2])
            computed_n_value2 = tk.Text(master=window, height=1, width=15)
            computed_n_value2.grid(row=8, column=3)
            computed_n_value2.insert(tk.END, data[1][2])
            computed_n_value3 = tk.Text(master=window, height=1, width=15)
            computed_n_value3.grid(row=8, column=5)
            computed_n_value3.insert(tk.END, data[2][2])
            computed_n_value4 = tk.Text(master=window, height=1, width=15)
            computed_n_value4.grid(row=8, column=7)
            computed_n_value4.insert(tk.END, data[3][2])

            computed_m_value1 = tk.Text(master=window, height=1, width=15)
            computed_m_value1.grid(row=9, column=1)
            computed_m_value1.insert(tk.END, data[0][1])
            computed_m_value2 = tk.Text(master=window, height=1, width=15)
            computed_m_value2.grid(row=9, column=3)
            computed_m_value2.insert(tk.END, data[1][1])
            computed_m_value3 = tk.Text(master=window, height=1, width=15)
            computed_m_value3.grid(row=9, column=5)
            computed_m_value3.insert(tk.END, data[2][1])
            computed_m_value4 = tk.Text(master=window, height=1, width=15)
            computed_m_value4.grid(row=9, column=7)
            computed_m_value4.insert(tk.END, data[3][1])


def description():

    a = ELEMENTS[str(get_element.get())]

    d = tk.Text(master=window, width=50, height=7)
    d.grid(row=6, column=9, padx=(60, 0), pady=(20, 20))
    d.insert(tk.END, a.description)


# ---- LABELS ----

chemicals = tk.Label(text="Unbalanced Chemical Equation:", font=("Segoe UI", 10, 'bold'))
chemicals.grid(row=0, column=0, pady=(30, 30))
MR = tk.Label(text="Molar Ratio/Coefficients (MR):", font=("Segoe UI", 10, 'bold'))
MR.grid(row=1, column=0, pady=(30, 30))
m = tk.Label(text="Mass (g):", font=("Segoe UI", 10, 'bold'))
m.grid(row=2, column=0, pady=(30, 30))
n = tk.Label(text="Moles (mol):", font=("Segoe UI", 10, 'bold'))
n.grid(row=3, column=0, pady=(30, 30))
Mm = tk.Label(text="Molar Mass (g/mol)", font=("Segoe UI", 10, 'bold'))
Mm.grid(row=4, column=0, pady=(30, 30))

plus1 = tk.Label(text="+", font=("Segoe UI", 10, 'bold'))
plus1.grid(row=0, column=2)
plus2 = tk.Label(text="+", font=("Segoe UI", 10, 'bold'))
plus2.grid(row=0, column=6)
arrow = tk.Label(text="---->", font=("Segoe UI", 10, 'bold'))
arrow.grid(row=0, column=4)

colon1 = tk.Label(text=":", font=("Segoe UI", 10, 'bold'))
colon1.grid(row=1, column=2)
colon2 = tk.Label(text=":", font=("Segoe UI", 10, 'bold'))
colon2.grid(row=1, column=4)
colon3 = tk.Label(text=":", font=("Segoe UI", 10, 'bold'))
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

# .insert adds a default value to the entry field
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

get_element = tk.Entry(width=60)
get_element.grid(row=4, column=9, padx=(150, 50))

# ---- BUTTONS ----

submit = tk.Button(text="Calculate", command=done, height=1, width=8, bg="#c8c8c8", font=("Segoe UI", 10))\
    .grid(row=5, column=7, pady=(0, 20))

# vertical line
tkinter.ttk.Separator(window, orient='vertical').grid(column=8, row=0, rowspan=10, sticky='ns')

desc = tk.Button(text="^^^ Get description of the element entered above ^^^", command=description, bg="#c8c8c8",
                 font=("Segoe UI", 10)).grid(row=5, column=9, padx=(150, 50))

window.mainloop()

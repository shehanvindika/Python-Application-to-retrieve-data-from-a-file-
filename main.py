import pickle
from tkinter import *

def main():

    file = open("UNDict.dat", "rb")
    dict = pickle.load(file)
    countries = [k for k in dict.keys()]
    countries.sort()
    file.close()

    def selectedItem(event):
        item=countryList.get(countryList.curselection()[0])
        dataDict=dict[item]
        contienent=dataDict['cont']
        population=dataDict['popl']
        populationFinal = "{:,.0f}".format(population* 1000000)
        area = dataDict['area']
        areaFinal = "{:,.2f}".format(area)

        contienentVariable.configure(state="normal")
        contienentVariable.delete(0, END)
        contienentVariable.insert(0, contienent)
        contienentVariable.configure(state="readonly")

        populationVariable.configure(state="normal")
        populationVariable.delete(0, END)
        populationVariable.insert(0, populationFinal)
        populationVariable.configure(state="readonly")

        areaVariable.configure(state="normal")
        areaVariable.delete(0, END)
        areaVariable.insert(0, areaFinal)
        areaVariable.configure(state="readonly")


    window=Tk()
    window.title("United Nations")


    frame1=Frame(window)
    frame1.grid(row=0,column=0,rowspan=3)
    yscroll1 = Scrollbar(frame1)
    yscroll1.pack(side=RIGHT,fill=Y)

    countryList = Listbox(frame1,yscrollcommand=yscroll1.set,font=('Calibri 12'),width=40)
    countryList.pack(side=LEFT,fill=BOTH)
    for item in countries:
        countryList.insert(END, item)

    countryList.bind("<<ListboxSelect>>", selectedItem)
    yscroll1.config(command=countryList.yview)

    dataList=dict[countries[0]]
    contienent = dataList['cont']
    population = dataList['popl']
    populationFinal = "{:,.0f}".format(population* 1000000)

    area = dataList['area']
    areaFinal = "{:,.2f}".format(area)

    frame2=Frame(window)
    frame2.grid(row=0,column=1,rowspan=5,padx=5)

    contienentLabel = Label(frame2, text="Contienent:", font=('Calibri 14'))
    contienentLabel.grid(row=0, column=0, padx=10, pady=20, sticky=E)
    contienentVariable = Entry(frame2,state="readonly",font=('Calibri 14'),width=15)
    contienentVariable.configure(state="normal")
    contienentVariable.insert(0,contienent)
    contienentVariable.configure(state="readonly")
    contienentVariable.grid(row=0, column=1,pady=20,sticky=W)

    populationLabel = Label(frame2, text="Population:", font=('Calibri 14'))
    populationLabel.grid(row=2, column=0, padx=10, pady=20, sticky=E)
    populationVariable = Entry(frame2, state="readonly", font=('Calibri 14'),width=15)
    populationVariable.configure(state="normal")
    populationVariable.insert(0,populationFinal)
    populationVariable.configure(state="readonly")
    populationVariable.grid(row=2, column=1,pady=20,sticky=W)

    areaLabel = Label(frame2, text="Area (sq miles):", font=('Calibri 14'))
    areaLabel.grid(row=4, column=0, padx=10, pady=20, sticky=E)
    areaVariable = Entry(frame2,state="readonly", font=('Calibri 14'),width=15)
    areaVariable.configure(state="normal")
    areaVariable.insert(0,areaFinal)
    areaVariable.configure(state="readonly")
    areaVariable.grid(row=4, column=1,pady=20,sticky=SW)


    window.mainloop()


main()
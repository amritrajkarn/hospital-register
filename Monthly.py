import sqlite3
from sqlite3 import Error
from tkinter import *

# CONNECTION TO DATABASE
conn = sqlite3.connect("expense.db")

try:
    c = conn.cursor()
    # TABLE FOR DATA
    c.execute("""
    CREATE TABLE IF NOT EXISTS dailyReg (
    date text PRIMARY KEY,
    opdIncome integer,
    xrayIncome integer,
    ultrasoundIncome integer,
    dressingIncome integer,
    otIncome integer,
    otherIncome integer,
    doctorExpense integer,
    pertolExpense integer,
    DieselExpense integer,
    otherExpanse integer
    ); 
    """)

    # CLASS TO STORE DATA
    class Reg:
        date = opd = xray = ultrasound = dressing = ot = otherIncome = doctor = petrol = diesel = otherExp = ''

    # TO INSERT DATA
    def insert():

        regObj = Reg()
        regObj.date = date.get()
        regObj.opd = int(opd.get())
        regObj.xray = int(xray.get())
        regObj.ultrasound = int(ultrasound.get())
        regObj.dressing = int(dressing.get())
        regObj.ot = int(ot.get())
        regObj.otherIncome = int(otherIncome.get())
        regObj.doctor = int(doctor.get())
        regObj.petrol = int(petrol.get())
        regObj.diesel = int(diesel.get())
        regObj.otherExp = int(otherExp.get())
        with conn:
            c.execute("""INSERT INTO dailyReg Values (
                :date, :opd, :xray, :ultrasound, :dressing, :ot, :otherIncome,
                :doctor, :petrol, :diesel, :otherExp)
            """,{'date':regObj.date, 'opd':regObj.opd, 'xray':regObj.xray, 'ultrasound':regObj.ultrasound, 'dressing':regObj.dressing, 'ot':regObj.ot, 'otherIncome':regObj.otherIncome, 'doctor':regObj.doctor, 'petrol':regObj.petrol, 'diesel':regObj.diesel,'otherExp':regObj.otherExp })

    def searchScreen():
        Screen2 = Tk()
        Screen2.geometry('600x650')
        Screen2.title('Amrit Hospital Daily Register - Search 1.0')
        
        searchDate = StringVar()

        #with conn:
        #    c.execute("SELECT * FROM dailyReg WHERE date=?", (date,))
        #   print(c.fetchone())   

        titleSearchLabel = Label(Screen2, text="Search Daily Income and Expense", bg='RED', width=300 ,font=("Courier", 24)).pack()
    
        dateSearchLabel = Label(Screen2, text="Date", font=("Courier", 16)).place(x=40, y=70)
        dateSearchEntry = Entry(Screen2, textvariable = searchDate, font=("Ariel", 16)).place(x=230, y=70)
        searchBtn = Button(Screen2, text='Search', width=10, height=1, bg='grey', font=("Courier", 14), command = searchScreen).place(x=230, y=560)


        Screen2.mainloop(2)

    def mainScreen():
        insertScreen = Tk()
        insertScreen.geometry('525x650')
        insertScreen.title('Amrit Hospital Daily Register 1.0')

        # GLOBAL VARIABLES
        global date, opd, xray, ultrasound, dressing, ot, otherIncome, doctor, petrol, diesel, otherExp

        date = StringVar()
        opd = StringVar()
        xray = StringVar()
        ultrasound = StringVar()
        dressing = StringVar()
        ot = StringVar()
        otherIncome = StringVar()
        doctor = StringVar()
        petrol = StringVar()
        diesel = StringVar()
        otherExp = StringVar()

        titleLabel = Label(insertScreen, text="Daily Income and Expense", bg='grey', width=300 ,font=("Courier", 24)).pack()
    
        dateLabel = Label(insertScreen, text="Date", font=("Courier", 16)).place(x=40, y=70)
        dateEntry = Entry(insertScreen, textvariable = date, font=("Ariel", 16)).place(x=230, y=70)

        incomeLabel = Label(insertScreen, text="Income",bg='green', font=("Courier", 20)).place(x=210, y=120)
        
        OPDLabel = Label(insertScreen, text="OPD", font=("Courier", 16)).place(x=40, y=170)
        OPDEntry = Entry(insertScreen, textvariable = opd, font=("Ariel", 16)).place(x=230, y=170)

        xrayLabel = Label(insertScreen, text="X-Ray", font=("Courier", 16)).place(x=40, y=200)
        xrayEntry = Entry(insertScreen, textvariable = xray, font=("Ariel", 16)).place(x=230, y=200)
    
        dressingLabel = Label(insertScreen, text="Dressing", font=("Courier", 16)).place(x=40, y=230)
        dressingEntry = Entry(insertScreen, textvariable = dressing, font=("Ariel", 16)).place(x=230, y=230)

        otLabel = Label(insertScreen, text="OT", font=("Courier", 16)).place(x=40, y=260)
        otEntry = Entry(insertScreen, textvariable = ot, font=("Ariel", 16)).place(x=230, y=260)
    
        ultrasoundLabel = Label(insertScreen, text="Ulta Sound", font=("Courier", 16)).place(x=40, y=290)
        ultrasoundEntry = Entry(insertScreen, textvariable = ultrasound, font=("Ariel", 16)).place(x=230, y=290)

        otherIncLabel = Label(insertScreen, text="Others", font=("Courier", 16)).place(x=40, y=320)
        otherIncEntry = Entry(insertScreen, textvariable = otherIncome, font=("Ariel", 16)).place(x=230, y=320)

        expenseLabel = Label(insertScreen, text="Expenditure",bg='red', font=("Courier", 20)).place(x=170, y=370)
        
        doctorLabel = Label(insertScreen, text="Doctors", font=("Courier", 16)).place(x=40, y=420)
        DoctorEntry = Entry(insertScreen, textvariable = doctor, font=("Ariel", 16)).place(x=230, y=420)

        petrolLabel = Label(insertScreen, text="Petrol", font=("Courier", 16)).place(x=40, y=450)
        petrolEntry = Entry(insertScreen, textvariable = petrol, font=("Ariel", 16)).place(x=230, y=450)

        dieselLabel = Label(insertScreen, text="Diesel", font=("Courier", 16)).place(x=40, y=480)
        dieselEntry = Entry(insertScreen, textvariable = diesel, font=("Ariel", 16)).place(x=230, y=480)

        otherExpLabel = Label(insertScreen, text="Others", font=("Courier", 16)).place(x=40, y=510)
        otherExpEntry = Entry(insertScreen, textvariable = otherExp, font=("Ariel", 16)).place(x=230, y=510)

        submitBtn = Button(insertScreen, text='Submit', width=10, height=1, bg='grey', font=("Courier", 14), command = insert).place(x=70, y=560)
        searchBtn = Button(insertScreen, text='Search', width=10, height=1, bg='grey', font=("Courier", 14), command = searchScreen).place(x=320, y=560)

        insertScreen.mainloop()

    mainScreen()
except Error as e:
    print(e)
conn.close()
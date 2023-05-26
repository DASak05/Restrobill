from tkinter import *
import time
import random
import tkinter.messagebox

root =Tk()
root.geometry("1400x750+0+0")
root.title("Restaurant billing system")
root.configure(background='sky blue')

Tops = Frame(root, bg='dark blue', bd=25, pady=20, relief=GROOVE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 30, 'bold'), text='Welcome To Narulas Kitchen', bd=15, bg='sky blue',
                fg='dark blue', justify=CENTER)
lblTitle.grid(row=0)



ReceiptCal_Function = Frame(root, bg='dark blue', bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Calculator_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='dark blue', bd=32, relief=GROOVE)
MenuFrame.pack(side=RIGHT)
Total_Function = Frame(MenuFrame, bg='sky blue', bd=4)
Total_Function.pack(side=BOTTOM)
Drinks_Function = Frame(MenuFrame,bg='sky blue',bd=4)
Drinks_Function.pack(side=TOP)


Drinks_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Drinks_Function.pack(side=LEFT)
Food_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Food_Function.pack(side=RIGHT)
# variables

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Total_of_Food = StringVar()
Total_of_Drinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

virgin_mojito= StringVar()
cappuccino = StringVar()
hot_chocolate = StringVar()
smoothies = StringVar()
milkshakes = StringVar()
icedlemon_tea= StringVar()
coffee = StringVar()
coke = StringVar()

fried_chicken = StringVar()
english_breakfast = StringVar()
chicken_wings = StringVar()
manchow_soup = StringVar()
efu_noodles = StringVar()
alfredo_pasta= StringVar()
arrabiata_pasta = StringVar()
clasicchicken_burger = StringVar()

virgin_mojito.set("0")
cappuccino.set("0")
hot_chocolate.set("0")
smoothies.set("0")
milkshakes.set("0")
icedlemon_tea.set("0")
coffee.set("0")
coke.set("0")

fried_chicken.set("0")
english_breakfast.set("0")
chicken_wings.set("0")
manchow_soup.set("0")
efu_noodles.set("0")
alfredo_pasta.set("0")
arrabiata_pasta.set("0")
clasicchicken_burger.set("0")

Date_of_Order.set(time.strftime("%y/%m/%d"))

# Function Declaration

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Total_of_Food.set("")
    Total_of_Drinks.set("")
    ServiceCharge.set("")
    textReceipt.delete("1.0", END)


    virgin_mojito.set("0")
    cappuccino.set("0")
    hot_chocolate.set("0")
    smoothies.set("0")
    milkshakes.set("0")
    icedlemon_tea.set("0")
    coffee.set("0")
    coke.set("0")

    fried_chicken.set("0")
    english_breakfast.set("0")
    chicken_wings.set("0")
    manchow_soup.set("0")
    efu_noodles.set("0")
    alfredo_pasta.set("0")
    arrabiata_pasta.set("0")
    clasicchicken_burger.set("0")

    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)
    variable11 .set(0)
    variable12 .set(0)
    variable13 .set(0)
    variable14 .set(0)
    variable15 .set(0)
    variable16 .set(0)


    textVirginMojito.configure(state=DISABLED)
    textCappuccino.configure(state=DISABLED)
    textHotChocolate.configure(state=DISABLED)
    textSmoothies.configure(state=DISABLED)
    textMilkShake.configure(state=DISABLED)
    textIcedlemontea.configure(state=DISABLED)
    textCoffee.configure(state=DISABLED)
    textCoke.configure(state=DISABLED)
    textFriedChicken.configure(state=DISABLED)
    textEnglishBreakfast.configure(state=DISABLED)
    textChickenWings.configure(state=DISABLED)
    textManchowSoup.configure(state=DISABLED)
    textEfuNoodles.configure(state=DISABLED)
    textAlfredoPasta.configure(state=DISABLED)
    textArrabiataPasta.configure(state=DISABLED)
    textClassicchickenBurger.configure(state=DISABLED)

def TotalofUnit():
    Unit1 = float(virgin_mojito.get())
    Unit2 = float(cappuccino.get())
    Unit3 = float(hot_chocolate.get())
    Unit4 = float(smoothies.get())
    Unit5 = float(milkshakes.get())
    Unit6 = float(icedlemon_tea.get())
    Unit7 = float(coffee.get())
    Unit8 = float(coke.get())

    Unit9 = float(fried_chicken.get())
    Unit10 = float(english_breakfast.get())
    Unit11 = float(chicken_wings.get())
    Unit12 = float(manchow_soup.get())
    Unit13 = float(efu_noodles.get())
    Unit14 = float(alfredo_pasta.get())
    Unit15 = float(arrabiata_pasta.get())
    Unit16 = float(clasicchicken_burger.get())

    Prices_Drinks = (Unit1 * 100) + (Unit2 *110) + (Unit3 * 100) + (Unit4 * 155) + (Unit5 * 110) + (Unit6 * 80) + (Unit7 * 85) + (Unit8 * 65)

    Prices_Food = (Unit9 * 120) + (Unit10 * 220) + (Unit11 * 150) + (Unit12 * 110) + (Unit13 * 139) + (Unit14 * 189) + (Unit15 * 179) + (Unit16 * 119)



    DrinksPrices = "P" + str('%.2f' % Prices_Drinks)
    FoodsPrices = "P" + str('%.2f' % Prices_Food)
    Total_of_Food.set(FoodsPrices)
    Total_of_Drinks.set(DrinksPrices)
    SC = "P" + str('%.2f' % 1.59)
    ServiceCharge.set(SC)

    Sub_Total_of_Unit = "P" + str('%.2f'%(Prices_Drinks + Prices_Food + 1.59))
    SubTotal.set(Sub_Total_of_Unit)

    Tax = "P" + str('%.2f'%((Prices_Drinks + Prices_Food + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT = ((Prices_Drinks + Prices_Food + 1.59) * 0.15)
    TC = "P" + str('%.2f'%(Prices_Drinks + Prices_Food + 1.59 + TT))
    TotalCost.set(TC)


def drinksvirgin_mojito():
    if variable1.get() == 1:
        textVirginMojito.configure(state=NORMAL)
        textVirginMojito.focus()
        textVirginMojito.delete('0', END)
        virgin_mojito.set("")
    elif variable1.get() == 0:
        textVirginMojito.configure(state=DISABLED)
        virgin_mojito.set("0")

def drinkscappuccino():
    if variable2.get() == 1:
        textCappuccino.configure(state=NORMAL)
        textCappuccino.focus()
        textCappuccino.delete('0', END)
        cappuccino.set("")
    elif variable2.get() == 0:
        textCappuccino.configure(state=DISABLED)
        cappuccino.set("0")

def drinksHotChocolate():
    if variable3.get() == 1:
        textHotChocolate.configure(state=NORMAL)
        textHotChocolate.delete('0', END)
        textHotChocolate.focus()
    elif variable3.get() == 0:
        textHotChocolate.configure(state=DISABLED)
        hot_chocolate.set("0")

def drinkssmoothies():
    if variable4.get() == 1:
        textSmoothies.configure(state=NORMAL)
        textSmoothies.delete('0', END)
        textSmoothies.focus()
    elif variable4.get() == 0:
        textSmoothies.configure(state=DISABLED)
        smoothies.set("0")

def drinksMilkShakes():
    if variable5.get() == 1:
        textMilkShake.configure(state=NORMAL)
        textMilkShake.delete('0', END)
        textMilkShake.focus()
    elif variable5.get() == 0:
        textMilkShake.configure(state=DISABLED)
        milkshakes.set("0")

def drinksIcedlemontea():
    if variable6.get() == 1:
        textIcedlemontea.configure(state=NORMAL)
        textIcedlemontea.delete('0', END)
        textIcedlemontea.focus()
    elif variable6.get() == 0:
        textIcedlemontea.configure(state=DISABLED)
        icedlemon_tea.set("0")

def drinksCoffee():
    if variable7.get() == 1:
        textCoffee.configure(state=NORMAL)
        textCoffee.delete('0', END)
        textCoffee.focus()
    elif variable7.get() == 0:
        Coffee.configure(state=DISABLED)
        coffee.set("0")

def drinksCoke():
    if variable8.get() == 1:
        textCoke.configure(state=NORMAL)
        textCoke.delete('0', END)
        textCoke.focus()
    elif variable8.get() == 0:
        textCoke.configure(state=DISABLED)
        coke.set("0")

def foodsFriedChicken():
    if variable9.get() == 1:
        textFriedChicken.configure(state=NORMAL)
        textFriedChicken.delete('0', END)
        textFriedChicken.focus()
    elif variable9.get() == 0:
        textFriedChicken.configure(state=DISABLED)
        fried_chicken.set("0")

def foodsEnglishBreakfast():
    if variable10.get() == 1:
        textEnglishBreakfast.configure(state=NORMAL)
        textEnglishBreakfast.delete('0', END)
        textEnglishBreakfast.focus()
    elif variable10.get() == 0:
        textEnglishBreakfast.configure(state=DISABLED)
        english_breakfast.set("0")

def foodsChickenWings():
    if variable11.get() == 1:
        textChickenWings.configure(state=NORMAL)
        textChickenWings.delete('0', END)
        textChickenWings.focus()
    elif variable11.get() == 0:
        textChickenWings.configure(state=DISABLED)
        chicken_wings.set("0")

def foodsManchowSoup():
    if variable12.get() == 1:
        textManchowSoup.configure(state=NORMAL)
        textManchowSoup.delete('0', END)
        textManchowSoup.focus()
    elif variable12.get() == 0:
        textManchowSoup.configure(state=DISABLED)
        manchow_soup.set("0")

def foodsEfuNoodles():
    if variable13 .get() == 1:
        textEfuNoodles.configure(state=NORMAL)
        textEfuNoodles.delete('0',END)
        textEfuNoodles.focus()
    elif(variable13.get() == 0):
        textEfuNoodles.configure(state=DISABLED)
        efu_noodles.set("0")

def foodsAlfredoPasta():
    if variable14 .get() == 1:
        textAlfredoPasta.configure(state=NORMAL)
        textAlfredoPasta.delete('0', END)
        textAlfredoPasta.focus()
    elif variable14.get() == 0:
        textAlfredoPasta.configure(state=DISABLED)
        alfredo_pasta.set("0")

def foodsArrabiataPasta():
    if variable15.get() == 1:
        textArrabiataPasta.configure(state=NORMAL)
        textArrabiataPasta.delete('0', END)
        textArrabiataPasta.focus()
    elif variable15.get() == 0:
        textArrabiataPasta.configure(state=DISABLED)
        arrabiata_pasta.set("0")

def foodsClassicchickenBurger():
    if variable16 .get() == 1:
        textClassicchickenBurger.configure(state=NORMAL)
        textClassicchickenBurger.delete('0',END)
        textClassicchickenBurger.focus()
    elif(variable16.get() == 0):
        textClassicchickenBurger.configure(state=DISABLED)
        clasicchicken_burger.set("0")

def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)


    textReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
    textReceipt.insert(END, 'Virgin Mojito:\t\t\t\t\t' + virgin_mojito.get() + '\n')
    textReceipt.insert(END, 'Cappucino:\t\t\t\t\t' + cappuccino.get() + '\n')
    textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
    textReceipt.insert(END, 'Smoothies:\t\t\t\t\t' + smoothies.get() + '\n')
    textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshakes.get() + '\n')
    textReceipt.insert(END, 'Iced lemon tea:\t\t\t\t\t' + icedlemon_tea.get()+'\n')
    textReceipt.insert(END, 'Coffee:\t\t\t\t\t' + coffee.get()+'\n')
    textReceipt.insert(END, 'Coke:\t\t\t\t\t' + coke.get()+'\n')
    textReceipt.insert(END, 'Fried Chicken:\t\t\t\t\t' + fried_chicken.get()+'\n')
    textReceipt.insert(END, 'English Breakfast:\t\t\t\t\t' + english_breakfast.get() + '\n')
    textReceipt.insert(END, 'Chicken Wings:\t\t\t\t\t' + chicken_wings.get()+'\n')
    textReceipt.insert(END, 'Manchow Soup:\t\t\t\t\t' + manchow_soup.get() + '\n')
    textReceipt.insert(END, 'Efu Noodles:\t\t\t\t\t' + efu_noodles.get()+'\n')
    textReceipt.insert(END, 'Alfredo Pasta:\t\t\t\t\t' +alfredo_pasta.get()+'\n')
    textReceipt.insert(END, 'Arrabiata Pasta:\t\t\t\t\t' + arrabiata_pasta.get() + '\n')
    textReceipt.insert(END, 'Classic Chicken Burger:\t\t\t\t\t' + clasicchicken_burger.get() + '\n')
    textReceipt.insert(END, 'Total of Drinks:\t\t\t\t' + Total_of_Drinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    textReceipt.insert(END, 'Total of Foods:\t\t\t\t' + Total_of_Food.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


# Drinks
Virgin_Mojito = Checkbutton(Drinks_Function, text='Virgin Mojito', variable=variable1, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksvirgin_mojito).grid(row=0, sticky=W)
Cappuccino= Checkbutton(Drinks_Function, text='Cappucino', variable=variable2, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinkscappuccino).grid(row=1, sticky=W)
HotChocolate = Checkbutton(Drinks_Function, text='Hot Chocolate', variable=variable3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksHotChocolate).grid(row=2, sticky=W)
Smoothies = Checkbutton(Drinks_Function, text='Smoothies', variable=variable4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinkssmoothies).grid(row=3, sticky=W)
MilkShake = Checkbutton(Drinks_Function, text='Milk Shake', variable=variable5, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMilkShakes).grid(row=4, sticky=W)
Iced_lemontea = Checkbutton(Drinks_Function, text='Iced lemon Tea', variable=variable6, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                          bg='sky blue', command=drinksIcedlemontea).grid(row=5, sticky=W)
Coffee = Checkbutton(Drinks_Function, text='Coffee', variable=variable7, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksCoffee).grid(row=6, sticky=W)
Coke = Checkbutton(Drinks_Function, text='Coke', variable=variable8, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
bg='sky blue', command=drinksCoke).grid(row=7, sticky=W)
# Drink Entry

textVirginMojito = Entry(Drinks_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=virgin_mojito)
textVirginMojito.grid(row=0,column=1)

textCappuccino = Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=cappuccino)
textCappuccino.grid(row=1,column=1)

textHotChocolate = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=hot_chocolate)
textHotChocolate.grid(row=2,column=1)

textSmoothies= Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=smoothies)
textSmoothies.grid(row=3,column=1)

textMilkShake = Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=milkshakes)
textMilkShake.grid(row=4,column=1)

textIcedlemontea = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=icedlemon_tea)
textIcedlemontea.grid(row=5,column=1)

textCoffee= Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=Coffee)
textCoffee.grid(row=6,column=1)

textCoke = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=coke)
textCoke.grid(row=7,column=1)
# Foods

FriedChicken = Checkbutton(Food_Function,text="Fried Chicken\t\t\t ",variable=variable9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsFriedChicken).grid(row=0,sticky=W)
EnglishBreakfast = Checkbutton(Food_Function,text="English Breakfast",variable=variable10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsEnglishBreakfast).grid(row=1,sticky=W)
ChickenWings= Checkbutton(Food_Function, text="Chicken Wings ", variable=variable11, onvalue = 1, offvalue=0,
                         font=('arial',16,'bold'), bg='sky blue', command=foodsChickenWings).grid(row=2, sticky=W)
ManchowSoup = Checkbutton(Food_Function, text="Manchow Soup ", variable=variable12, onvalue = 1, offvalue=0,
                            font=('arial',16,'bold'), bg='sky blue', command=foodsManchowSoup).grid(row=3, sticky=W)
EfuNoodles= Checkbutton(Food_Function, text="Efu Noodles ", variable=variable13, onvalue = 1, offvalue=0,
                            font=('arial',16,'bold'), bg='sky blue', command=foodsEfuNoodles).grid(row=4, sticky=W)
AlfredoPasta = Checkbutton(Food_Function, text="Alfredo Pasta ", variable=variable14, onvalue = 1, offvalue=0,
                           font=('arial',16,'bold'), bg='sky blue', command=foodsAlfredoPasta).grid(row=5, sticky=W)
ArrabiataPasta = Checkbutton(Food_Function, text="Arrabiata Pasta ", variable=variable15, onvalue = 1, offvalue=0,
                            font=('arial',16,'bold'), bg='sky blue', command=foodsArrabiataPasta).grid(row=6, sticky=W)
ClassicchickenBurger = Checkbutton(Food_Function, text="Classicchicken Burger ", variable=variable16, onvalue = 1, offvalue=0,
                           font=('arial',16,'bold'), bg='sky blue', command=foodsClassicchickenBurger).grid(row=7, sticky=W)

textFriedChicken=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=fried_chicken)
textFriedChicken.grid(row=0,column=1)

textEnglishBreakfast=Entry(Food_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=english_breakfast)
textEnglishBreakfast.grid(row=1,column=1)

textChickenWings=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=chicken_wings)
textChickenWings.grid(row=2, column=1)

textManchowSoup=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=manchow_soup)
textManchowSoup.grid(row=3, column=1)

textEfuNoodles=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=efu_noodles)
textEfuNoodles.grid(row=4, column=1)

textAlfredoPasta=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=alfredo_pasta)
textAlfredoPasta.grid(row=5,column=1)

textArrabiataPasta=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=arrabiata_pasta)
textArrabiataPasta.grid(row=6, column=1)

textClassicchickenBurger=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=clasicchicken_burger)
textClassicchickenBurger.grid(row=7, column=1)

# ToTal Cost
lblTotalofDrinks=Label(Total_Function,font=('arial',14,'bold'),text='Total of Drinks\t',bg='sky blue',fg='black',justify=CENTER)
lblTotalofDrinks.grid(row=0,column=0,sticky=W)
textTotalofDrinks=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Drinks)
textTotalofDrinks.grid(row=0,column=1)

lblTotalofFood=Label(Total_Function,font=('arial',14,'bold'),text='Total of Foods  ',bg='sky blue',fg='black',justify=CENTER)
lblTotalofFood.grid(row=1,column=0,sticky=W)
textTotalofFood=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Food)
textTotalofFood.grid(row=1,column=1)

lblServiceCharge=Label(Total_Function,font=('arial',14,'bold'),text='Service Charge',bg='sky blue',fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
# Payment information

lblPaidTax=Label(Total_Function,font=('arial',14,'bold'),text='\tPaid Tax',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
textPaidTax=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
textPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Total_Function,font=('arial',14,'bold'),text='\tSub Total',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
textSubTotal=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'), insertwidth=2,justify=RIGHT,textvariable=SubTotal)
textSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Total_Function,font=('arial',14,'bold'),text='\tTotal',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
textTotalCost=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
textTotalCost.grid(row=2,column=3)

# RECEIPT
textReceipt=Text(Receipt_Function,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
textReceipt.grid(row=0,column=0)


# BUTTONS
buttonTotal=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Total',bg='black',command=TotalofUnit).grid(row=0,column=0)
buttonReceipt=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Receipt',bg='black',command=Receipt).grid(row=0,column=1)
buttonReset=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Reset',bg='black',command=Reset).grid(row=0,column=2)
buttonExit=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Exit',bg='black',command=iExit).grid(row=0,column=3)


# Calculator Display




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




# Calculator
txtDisplay = Entry(Calculator_Function, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

# CALCULATOR BUTTONS
button7=Button(Calculator_Function, padx=16, pady=1, bd=7, fg='gold', font=('arial', 12, 'bold'), width=4, text='7',bg='black',command=lambda:btnClick(7)).grid(row=2,column=0)
button8=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='8',bg='black',command=lambda:btnClick(8)).grid(row=2,column=1)
button9=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='9',bg='black',command=lambda:btnClick(9)).grid(row=2,column=2)
buttonAdd=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='+',bg='black',command=lambda:btnClick('+')).grid(row=2,column=3)

button4=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='4',bg='black',command=lambda:btnClick(4)).grid(row=3,column=0)
button5=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='5',bg='black',command=lambda:btnClick(5)).grid(row=3,column=1)
button6=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='6',bg='black',command=lambda:btnClick(6)).grid(row=3,column=2)
buttonSub=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='-',bg='black',command=lambda:btnClick('-')).grid(row=3,column=3)

button1=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='1',bg='black',command=lambda:btnClick(1)).grid(row=4,column=0)
button2=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='2',bg='black',command=lambda:btnClick(2)).grid(row=4,column=1)
button3=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='3',bg='black',command=lambda:btnClick(3)).grid(row=4,column=2)
buttonMulti=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='*',bg='black',command=lambda:btnClick('*')).grid(row=4,column=3)

button0=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='0',bg='black',command=lambda:btnClick(0)).grid(row=5,column=0)
buttonClear=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='C',bg='black',command=btnClear).grid(row=5,column=1)
buttonEqual=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='=',bg='black',command=btnEquals).grid(row=5,column=2)
buttonDiv=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='/',bg='black',command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()


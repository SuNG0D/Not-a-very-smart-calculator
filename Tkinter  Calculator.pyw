from tkinter import*
from math import*
from tkinter import messagebox

window = Tk()
window.title("Calculadora")
window.geometry("400x500+700+300")
window.configure(bg = "silver")

#Shows the numbers you entered, the variable called operadors is the one that stores the input (as a string), while text_pantalla is the one showing on the screen.
def numeros(num):
    global operadors
    operadors = operadors+str(num)
    text_pantalla.set(operadors)

#The variable operador is the one that calculates the answer, we use eval so that the string entered is seen as a function (by the program).
#We use try and except so that the program tries to run the operador variable, except if there's an error, then the program will show and ERROR text and the operadors variable will reset.
#The text_pantalla_ans variable is just to store the answer since I haven't figured out how to save the answer.
def resultat():
    global operadors
    try:
        operador=str(eval(operadors))
        text_pantalla.set(operador)
        text_pantalla_ans.set("ANS="+operador)
    except:
        text_pantalla.set("ERROR")
    operadors = ("")
    
#Resets the operadors variable and changes the text_pantalla variable to 0.
def clear():
    global operadors
    operadors = ("")
    text_pantalla.set("0")

#Size variable counts the lenght of the operadors variable.
#Then we tell the operadors variable to remove the last input entered.
#We set the text_pantalla to operadors, and if the operadors variable is blank, we set the text_pantalla variable back to 0.
def CE():
    global operadors
    size = len(operadors)
    operadors = operadors[:size - 1]
    text_pantalla.set(operadors)
    if operadors == (""):
        text_pantalla.set("0") 

#Does the same as clear function but instead we set text_pantalla_ans to 0.
def ClearANS():
    global operadors
    operadors = ("")
    text_pantalla_ans.set("0")

#This one is a little bit hard to explain (at least for me :-P)
#A messagebox with a ok or cancel buttons asks if we want to leave, if we click ok the program closes
def closing():
    if messagebox.askokcancel("Quit", "Are you sure you wanna leave? :("):
        window.destroy()


text_pantalla = StringVar()
text_pantalla_ans = StringVar()
operadors = ("")

text_numeros = Label(window, font=("arial", 20, "bold"), width=20, textvariable= text_pantalla, bd=20, bg="grey", relief= RIDGE, justify="right").place(x=10, y=75)
text_numeros_anteriors = Label(window, font=("arial", 15, "bold"), width=20, textvariable= text_pantalla_ans, bd=20, bg="grey", relief= RIDGE, justify="right").place(x=10, y=5)

width= 8
height= 3


button7 = Button(window, text = "7", width=width, height=height, command = lambda:numeros(7)).place(x=17, y=180)
button8 = Button(window, text = "8", width=width, height=height, command = lambda:numeros(8)).place(x=87, y=180)
button9 = Button(window, text = "9", width=width, height=height, command = lambda:numeros(9)).place(x=157, y=180)
button4 = Button(window, text = "4", width=width, height=height, command = lambda:numeros(4)).place(x=17, y=240)
button5 = Button(window, text = "5", width=width, height=height, command = lambda:numeros(5)).place(x=87, y=240)
button6 = Button(window, text = "6", width=width, height=height, command = lambda:numeros(6)).place(x=157, y=240)
button1 = Button(window, text = "1", width=width, height=height, command = lambda:numeros(1)).place(x=17, y=300)
button2 = Button(window, text = "2", width=width, height=height, command = lambda:numeros(2)).place(x=87, y=300)
button3 = Button(window, text = "3", width=width, height=height, command = lambda:numeros(3)).place(x=157, y=300)
button0 = Button(window, text = "0", width=width, height=height, command = lambda:numeros(0)).place(x=17, y=360)
button_coma = Button(window, text = ".", width=width, height=height, command = lambda:numeros(".")).place(x=87, y=360)
button_suma = Button(window, text = "+", width=width, height=height, command = lambda:numeros("+")).place(x=227, y=300)
button_resta = Button(window, text = "-", width=width, height=height, command = lambda:numeros("-")).place(x=297, y=300)
button_Parentesi1 = Button(window, text = "(", width=width, height=height, command = lambda:numeros("(")).place(x=157, y=360)
button_Parentesi2 = Button(window, text = ")", width=width, height=height, command = lambda:numeros(")")).place(x=227, y=360)
button_multiplicar = Button(window, text = "x", width=width, height=height, command = lambda:numeros("*")).place(x=227, y=240)
button_dividir = Button(window, text = "%", width=width, height=height, command = lambda:numeros("/")).place(x=297, y=240)
button_CE = Button(window, text = "CE", width=width, height=height, command = CE).place(x=227, y=180)
button_C = Button(window, text = "C", width=width, height=height, command = clear).place(x=297, y=180)
button_Resultat = Button(window, text = "=", width=width, height=height, command = resultat).place(x=297, y=360)
button_CE = Button(window, text = "ClearANS", width=width, height=height, command = ClearANS).place(x=227, y=420)
button_pi = Button(window, text = "π", width=width, height=height, command = lambda:numeros("pi")).place(x=297, y=420)
welcome_text = (messagebox.showinfo("Hello There! :D","Made by: SuNG0D"))

#The WM_DELETE_WINDOW is a wm protocol to close the window, for instance, when you click the X button in your program you send a WM_DELETE_WINDOW client message to the computer to tell him to kill the program.
#A wm protocol is a command used to manage window manager.
#When the X button is pressed, the closing function runs, if the answer is ok, the program closes.
window.protocol("WM_DELETE_WINDOW", closing)
window.mainloop()

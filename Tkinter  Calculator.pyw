from tkinter import*
from math import*
from tkinter import messagebox

window = Tk()
window.title("Calculadora")
window.geometry("400x500+700+300")
window.configure(bg = "silver")

def numeros(num):
    global operadors
    operadors = operadors+str(num)
    text_pantalla.set(operadors)
    
def resultat():
    global operadors
    try:
        operador=str(eval(operadors))
        text_pantalla.set(operador)
        text_pantalla_ans.set("ANS="+operador)
    except:
        text_pantalla.set("ERROR")
    operadors = ("")
    
def clear():
    global operadors
    operadors = ("")
    text_pantalla.set("0")

def CE():
    global operadors
    size = len(operadors)
    operadors = operadors[:size - 1]
    text_pantalla.set(operadors)
    if operadors == (""):
        text_pantalla.set("0") 

def ClearANS():
    global operadors
    operadors = ("")
    text_pantalla_ans.set("0")

def closing():
    if messagebox.askokcancel("Quit", "Are you sure you wanna leave? :("):
        window.destroy()


text_pantalla = StringVar()
text_pantalla_ans = StringVar()
operadors = ("")

text_numeros = Label(window, font=("arial", 20, "bold"), width=20, textvariable= text_pantalla, bd=20, bg="grey", relief= RIDGE, justify="right").place(x=10, y=75)
text_numeros_anteriors = Label(window, font=("arial", 15, "bold"), width=20, textvariable= text_pantalla_ans, bd=20, bg="grey", relief= RIDGE, justify="right").place(x=10, y=5)

button_width= 8
button_height= 3


button7 = Button(window, text = "7", width=button_width, height=button_height, command = lambda:numeros(7)).place(x=17, y=180)
button8 = Button(window, text = "8", width=button_width, height=button_height, command = lambda:numeros(8)).place(x=87, y=180)
button9 = Button(window, text = "9", width=button_width, height=button_height, command = lambda:numeros(9)).place(x=157, y=180)
button4 = Button(window, text = "4", width=button_width, height=button_height, command = lambda:numeros(4)).place(x=17, y=240)
button5 = Button(window, text = "5", width=button_width, height=button_height, command = lambda:numeros(5)).place(x=87, y=240)
button6 = Button(window, text = "6", width=button_width, height=button_height, command = lambda:numeros(6)).place(x=157, y=240)
button1 = Button(window, text = "1", width=button_width, height=button_height, command = lambda:numeros(1)).place(x=17, y=300)
button2 = Button(window, text = "2", width=button_width, height=button_height, command = lambda:numeros(2)).place(x=87, y=300)
button3 = Button(window, text = "3", width=button_width, height=button_height, command = lambda:numeros(3)).place(x=157, y=300)
button0 = Button(window, text = "0", width=button_width, height=button_height, command = lambda:numeros(0)).place(x=17, y=360)
button_coma = Button(window, text = ".", width=button_width, height=button_height, command = lambda:numeros(".")).place(x=87, y=360)
button_suma = Button(window, text = "+", width=button_width, height=button_height, command = lambda:numeros("+")).place(x=227, y=300)
button_resta = Button(window, text = "-", width=button_width, height=button_height, command = lambda:numeros("-")).place(x=297, y=300)
button_Parentesi1 = Button(window, text = "(", width=button_width, height=button_height, command = lambda:numeros("(")).place(x=157, y=360)
button_Parentesi2 = Button(window, text = ")", width=button_width, height=button_height, command = lambda:numeros(")")).place(x=227, y=360)
button_multiplicar = Button(window, text = "x", width=button_width, height=button_height, command = lambda:numeros("*")).place(x=227, y=240)
button_dividir = Button(window, text = "%", width=button_width, height=button_height, command = lambda:numeros("/")).place(x=297, y=240)
button_CE = Button(window, text = "CE", width=button_width, height=button_height, command = CE).place(x=227, y=180)
button_C = Button(window, text = "C", width=button_width, height=button_height, command = clear).place(x=297, y=180)
button_Resultat = Button(window, text = "=", width=button_width, height=button_height, command = resultat).place(x=297, y=360)
button_CE = Button(window, text = "ClearANS", width=button_width, height=button_height, command = ClearANS).place(x=227, y=420)
button_pi = Button(window, text = "π", width=button_width, height=button_height, command = lambda:numeros("pi")).place(x=297, y=420)
welcome_text = (messagebox.showinfo("Hello There! :D","Made by: SuNG0D"))

window.protocol("WM_DELETE_WINDOW", closing)
window.mainloop()

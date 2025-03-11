
import tkinter as recadro
### igual precisamos teclear no terminal: sudo apt-get install python3-tk

# 1. Fabricar a xanela
xanela = recadro.Tk()

# 2. Poñerlla ao noso gusto
xanela.title("A miña app") ###############
xanela.geometry("300×200") #####################

# 3. preguntamos
pregunta = recadro.Label(xanela, text="Cantos km levas percorrido?") ###############

# 4. Fabricamos un cadro de texto para que o usuario escriba
resposta = recadro.Entry()

# 5. Creamos un botón para que o usuario pulse e envíe a información
botoncito = recadro.Button(xanela, text="Envía  a túa resposta!", background="red") ###############

# 6. Necesitamos facer as contas para cando se preme o botón
def calculito():
    km = int(resposta.get())
    metros = km*1000 ###############
    resultado["text"] = "Daquela  "+ str(metros)+ " son os metros percorridos!" ############### \n
    
    
# 7. O usuario preme o  botón e faise a conta
botoncito["command"] = calculito   
resultado = recadro.Label(xanela, text="")

# 8. Mostramos a xanela
pregunta.pack()
resposta.pack()
botoncito.pack()
resultado.pack()   

xanela.mainloop()
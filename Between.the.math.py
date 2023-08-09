

#test
from tkinter import *
import random
import os
import sys


def languageScreen():
	lang = Tk()
	lang.title("Between The  Math & Science - The Game")

	windowWidth = lang.winfo_reqwidth()
	windowHeight = lang.winfo_reqheight()
	positionRight = int(lang.winfo_screenwidth()/7 - windowWidth/3)
	positionDown = int(lang.winfo_screenheight()/4 - windowHeight/2)
	
	lang.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

	titulo = Label(lang, width=30, text='LET us have a QUIZ',
			   font=('Gothic', '28', 'bold'))
	titulo.place(relx=0.5, rely=0, anchor=N)

	texto = Label(lang,
				text='For enter in the Quiz,\n Please,Press the enter Buttom',
				font=('Consolas', 18))
	texto.place(relx=0.5, rely=0.25, anchor=N)

	def getLangPT():
		global language
		language = 'pt'
		lang.destroy()
	
	def getLangEN():
		global language
		language = 'en'
		lang.destroy()

	
	en = Button(lang, text='ENTER', width=20, height=2, font=('Arial', 22), fg='red', command=getLangEN)

	
	en.place(relx=0.5, rely=0.65, anchor=S)


	lang.mainloop()
	
languageScreen()

##if language == "pt":
 ##from ptbr import *
language == "en"
from en import *

#Startup screen and Tab tittle
inicial = Tk()
inicial.title("lets Crack the Quiz")
# End of intialisation

pontos = 0
fechar = 1
dificuldade = ''

# Screen adjustment
windowWidth = inicial.winfo_reqwidth()
windowHeight = inicial.winfo_reqheight()
positionRight = int(inicial.winfo_screenwidth()/7 - windowWidth/3)
positionDown = int(inicial.winfo_screenheight()/4 - windowHeight/2)
# set the canvas dimension
inicial.geometry("900x700+{}+{}".format(positionRight+300, positionDown))
# end of screen adjustment

# randamization of question
lista_perguntas_inicial = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(lista_perguntas_inicial)
lista_perguntas = []
y = 0
z = 0

# Difficulty level
lista_perguntasFacil = [2,3,5,8,11,13,15]
random.shuffle(lista_perguntasFacil)
lista_perguntasMedio = [1,9,12,14,16,18,20]
random.shuffle(lista_perguntasMedio)
lista_perguntasDificil = [4,6,7,10,17,19]
random.shuffle(lista_perguntasDificil)


# concentrate list and choose difficulty
def concatenador(lista_dificuldade, lista_perguntas_inicial):
  for k in lista_perguntas_inicial:
    if k in lista_dificuldade:
        pass
    else:
        lista_dificuldade.append(k)
  global lista_perguntas
  lista_perguntas = lista_dificuldade


# feedback
lista_respostas = [1.4,2.1,3.1,4.1,5.4,6.3,7.4,8.3,9.5,10.2,11.1,12.3,13.4,14.5,15.2,16.5,17.2,18.3,19.5,20.2]

# initial function:identification,play,rules and exit

def identificação():
    identificar = Tk()
    identificar.title('User Profile '+ '- SUBJECT ARE Math & Science ')

    identificar.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

    def dados():
      global usuario
      usuario = nome.get()

      erroNome = Label(identificar, text='Type your name', font=('Arial', 14))
      erroNome.place(relx=0.5, rely=0.22, anchor=N)
      
      if usuario != '':
        erroNome['text'] = 'Name stored'
        erroNome['bg'] = 'green'

    def botaoFacil():
      global dificuldade
      dificuldade = 'facil'
      dificuldadeMedia['bg'] = 'white'
      dificuldadeDificil['bg'] = 'white'
      dificuldadeFacil['bg'] = 'green'

    def botaoMedio():
      global dificuldade
      dificuldade = 'medio'
      dificuldadeDificil['bg'] = 'white'
      dificuldadeFacil['bg'] = 'white'
      dificuldadeMedia['bg'] = 'orange'

    def botaoDificil():
      global dificuldade
      dificuldade = 'dificil'
      dificuldadeMedia['bg'] = 'white'
      dificuldadeFacil['bg'] = 'white'
      dificuldadeDificil['bg'] = 'red'

    def botaoJogar():
      if dificuldade != '' and usuario != '':
        identificar.destroy()
        if dificuldade == 'facil':
          concatenador(lista_perguntasFacil, lista_perguntas_inicial)
        elif dificuldade == 'medio':
          concatenador(lista_perguntasMedio, lista_perguntas_inicial)
        else:
          concatenador(lista_perguntasDificil, lista_perguntas_inicial)
      else:
        dados()
        erroDificuldade = Label(identificar, text='Choose the difficulty please.', font=('Arial, 14'))
        erroDificuldade.place(relx=0.5, rely=0.95, anchor=S)

    tituloUsuario = Label(identificar, text = 'Type your name below', font=('Gothic', 32, "bold"), fg = 'green')
    nome = Entry(identificar, width=30, font=('Arial', 20))
    confirmarNome = Button(identificar, width=15, text = 'Confirm', font=(16), command=dados)
    textDificuldade = Label(identificar, text =  'Select the difficulty', font=('Gothic', 32, "bold"), fg = 'black')

    dificuldadeFacil = Button(identificar, text = 'Easy', width=20, font=('Arial', 18), command=botaoFacil)
    dificuldadeMedia = Button(identificar, text = 'Normal', width=20, font=('Arial', 18), command=botaoMedio)
    dificuldadeDificil = Button(identificar, text = 'Hard', width=20, font=('Arial', 18), command=botaoDificil)
    comecarJogo = Button(identificar, text =  'PLAY', width=20, font=('Arial', 22, 'bold'), command=botaoJogar)

    tituloUsuario.place(relx=0.5, rely=0, anchor=N)
    nome.place(relx=0.5, rely=0.1, anchor=N)
    confirmarNome.place(relx=0.5, rely=0.16, anchor=N)
    textDificuldade.place(relx = 0.5, rely = 0.3, anchor=CENTER)

    dificuldadeFacil.place(relx=0.5, rely=0.5, anchor=S)
    dificuldadeMedia.place(relx=0.5, rely=0.58, anchor=S)
    dificuldadeDificil.place(relx=0.5, rely=0.66, anchor=S)
    comecarJogo.place(relx=0.5, rely=0.9, anchor=S)

    identificar.mainloop()


def getGame():
    global z, fechar

    # choose the intial screen or the previous question
    if fechar == 1:
      inicial.destroy()
      identificação()
      if dificuldade == '' or usuario == '':
        exit()

    # intialisation of the rules screen and tab titlle
    jogo = Tk()
    jogo.title("Perguntas" if language == 'pt' else 'Questions' + "- SUBJECT ARE Math & Science")
    # end of the intialisation

    # Screen adjustment
    jogo.geometry("900x700+{}+{}".format(positionRight+300, positionDown))
    # end screen snap

    def verificação(y,z):
      global pontos
      if (x+y) in lista_respostas:
        pontos += 1
        jogo.destroy()
        if pontos == 20:
          feedback(x)
        else:
          getGame()
      else:
        jogo.destroy()
        feedback(x)


    def y_alt1():
        y = 0.1
        verificação(y,z)


    def y_alt2():
        y = 0.2
        verificação(y,z)


    def y_alt3():
        y = 0.3
        verificação(y,z)

        
    def y_alt4():
        y = 0.4
        verificação(y,z)
    
    def y_alt5():
        y = 0.5
        verificação(y,z)
        


    # Alternativas
    x = lista_perguntas[z]
    y = 0.1
    z += 1

    # close only the game window onwards
    fechar += 1
    
    perguntaQ = Label(jogo, text=perguntas[x], fg = 'black', font=('Arial', 20))

    letraA = Label(jogo,
                  text='a)',
                  font=('Arial', 16, 'bold'))

    alt1 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command = y_alt1)

    y += 0.1

    letraB = Label(jogo,
                  text='b)',
                  font=('Arial', 16, 'bold'))

    alt2 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt2)

    y += 0.1

    letraC = Label(jogo,
                  text='c)',
                  font=('Arial', 16, 'bold'))

    alt3 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt3)

    y += 0.1

    letraD = Label(jogo,
                  text='d)',
                  font=('Arial', 16, 'bold'))

    alt4 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt4)

    y += 0.1

    letraE = Label(jogo,
                  text='e)',
                  font=('Arial', 16, 'bold'))

    alt5 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt5)

    
    pontuacao = Label(jogo, text='Points:', font=('Arial', 16))
    pontuacaonum = Label(jogo, text=pontos, font=('Arial', 16), fg='#006600')
    pontuacao.place(relx=0.9, rely=0.7, anchor=CENTER)
    pontuacaonum.place(relx=0.97, rely=0.7, anchor=CENTER)


    alt1.place(relx = 0.05, rely = 0.4, anchor = W)
    letraA.place(relx = 0, rely = 0.4, anchor = W)
    alt2.place(relx = 0.05, rely = 0.5, anchor = W)
    letraB.place(relx = 0, rely = 0.5, anchor = W)
    alt3.place(relx = 0.05, rely = 0.6, anchor = W)
    letraC.place(relx = 0, rely = 0.6, anchor = W)
    alt4.place(relx = 0.05, rely = 0.7, anchor = W)
    letraD.place(relx = 0, rely = 0.7, anchor = W)
    alt5.place(relx = 0.05, rely = 0.8, anchor = W)
    letraE.place(relx = 0, rely = 0.8, anchor = W)
    perguntaQ.place(relx = 0.5, rely = 0, anchor = N)


    # game window reply
    jogo.mainloop()


def getQuit():
    # close the splash screen
    inicial.destroy()
    # close the code
    exit()


def fbquit():
    fb.destroy()
    exit()


def fbrestart():
    os.execl(sys.executable, sys.executable, * sys.argv)
  
    

def feedback(x):
    global fb
    # Initialise the feedback window and rename it
    fb = Tk()
    fb.title("Feedback - ")
    
    # size the feedback window
    fb.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

    tituloFeed = Label(fb, text='YOU FAILED', font=('Gothic', 32, "bold"), fg = 'red')
    justificativa = Label(fb, text = 'Justificativa:' if language == 'pt' else 'Feedback:', font=('Arial', 23, "bold"), fg = 'black')
    resposta = Label(fb, text=explic[x], fg = 'black', font=('Arial', 18))
    tituloFeed.place(relx=0.5,rely=0,anchor=N)
    
    # Feedback text
    if pontos == 0:
      textofbprimario = "Noob"
      textofbsecundario =  'You have to improve your skills!'
    elif pontos > 0 and pontos < 6:
      textofbprimario = "Novice"
      textofbsecundario = 'You could have gone better...'
    elif pontos > 5 and pontos < 11:
      textofbprimario = "Median"
      textofbsecundario = 'Continue practing, you are growing!'
    elif pontos > 10 and pontos < 16:
      textofbprimario = "Expert!"
      textofbsecundario =  "That's good! Show me more!"
    elif pontos > 15 and pontos < 20:
      textofbprimario = "Professional!"
      textofbsecundario = 'Wow! Almost done!'
    elif pontos == 20:
      tituloFeed['text'] = 'YOU WON! CONGRATS!!'
      tituloFeed['fg'] = '#66ff66'
      tituloFeed['font'] = ('Gothic', 72, "bold")
      tituloFeed.place(relx=0.5, rely=0.18, anchor=N)
      resposta['text'] = ''
      justificativa['text'] = ''
      textofbprimario = "Masterpiece!"
      textofbsecundario = 'You got it all!'
    else:
      pass


    # Texts
    mensagemfb = Label(fb, text= 'your score was:', font=('Gothic', 20, "bold"))
    pontuacao = Label(fb, text=pontos, font=('Gothic', 42, "bold"), fg = "#330000")
    textosfeedbackpri = Label(fb, text=textofbprimario, font=('Gothic', 52, "bold"), fg = '#b30000')
    textosfeedbacksec = Label(fb, text=textofbsecundario, font=('Gothic', 18, "bold"))
    nada = Label(fb, text='', width= 0, height=8)
    sair = Button(fb, text= 'QUIT', width=20, font=('Arial', 18, 'bold'), fg = '#b30000', command=fbquit)
    again = Button(fb, text= 'PLAY AGAIN', width=20, font=('Arial', 18, 'bold'), fg = '#006600', command=fbrestart)


    # Positioning of labels
    justificativa.place(relx=0, rely=0.15, anchor=W)
    resposta.grid(row=30, column=0)
    nada.grid(row=0, column=0)
    mensagemfb.place(relx= 0.5, rely= 0.5, anchor=S)
    pontuacao.place(relx = 0.5, rely= 0.6, anchor=S)
    textosfeedbackpri.place(relx=0.5,rely=0.75, anchor=S)
    textosfeedbacksec.place(relx=0.5,rely=0.80, anchor=S)
    sair.place(relx=0.3, rely=0.95, anchor=S)
    again.place(relx=0.7, rely=0.95, anchor=S)
    
# end of function


# game tittle in splash window(add colors)
titulo = Label(inicial, width=30, text='Subjects Are, Math & Science ',
               font=('Gothic', '28', 'bold'))
titulo.place(relx=0.5, rely=0, anchor=N)


# Home screen Buttons
jogar = Button(inicial, text= 'START', width=20, height=2, font=('Arial', 22), fg='green', command=getGame)
sair = Button(inicial, text= 'QUIT', width=20, font=('Arial', 18, 'bold'), command=getQuit)
# end of Buttons

# text labels
preGame = Label(inicial,
                text='Read the rules below and\nstart when you are ready ',
                font=('Consolas', 12))

rules = Label(inicial,
              text=
			  'This Quiz is made by 20 (twenty) questions about mathematic, physics and chemistry,\n'
			  'you have to choose one out of five options for each question.\n'
			  'If you choose them wrong, the Quiz will end and the feedback window will show the explanation for the correct answer.\n'
			  'Beyond that, your classification score will be there as well with a nice text :)',
              width=800,
              bg = 'black',
              fg = '#FACA2F',
              font=('Times', 14))


# Button location
jogar.place(relx=0.5, rely=0.2, anchor=N)
preGame.place(relx=0.5, rely=0.38, anchor=N)
rules.place(relx=0.5, rely=0.55, anchor=CENTER)
sair.place(relx=0.5, rely=0.8, anchor=S)
# end of location


# intial window repeat
inicial.mainloop()

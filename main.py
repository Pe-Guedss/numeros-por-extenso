import tkinter as tk

import tkinter.font as tkFont

from PIL import ImageTk, Image

root = tk.Tk()

#Definição das bibliotecas para busca do resultado
unidades = {"0": "zero","1": "um", "2": "dois", "3": "três", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", 
            "8": "oito", "9": "nove"}

dezenas_dez = {"10": "dez", "11": "onze", "12": "doze", "13": "treze", "14": "quatorze", "15": "quinze", 
           "16": "dezesseis", "17": "dezessete", "18": "dezoito", "19": "dezenove"}

dezenas = {"1": "dez", "2": "vinte", "3": "trinta", "4": "quarenta", "5": "cinquenta", "6": "sessenta", "7": "setenta",
          "8": "oitenta", "9": "noventa"}

centenas = {"1": "cento", "2": "duzentos", "3": "trezentos", "4": "quatrocentos", "5": "quinhentos", "6": "seiscentos",
           "7": "setecentos", "8": "oitocentos", "9": "novecentos", "100": "cem"}

#Definição do texto de saída
texto_saida = "Ainda não foi digitado nenhum número :("
instrucoes = '''Bem vindo ao meu primeiro programa em Python!

Caso a visualização esteja ruim, clique no botão com a grande letra "A" em amarelo.
Ele faz com que o programa seja alterado para o modo alto contraste.

Esse programa tem uma funcionalidade bem simples.

Digite um número no campo em branco da janela principal, o número deve ser de 0 a 999.

Ao clicar no botão "Iniciar", ou pressionar a tecla "Enter", o número digitado será exibido por extenso!

Obrigado por executar meu programa! :)'''

#Atualiza a mensagem exibida de acordo com o valor digitado pelo usuário
def atualiza (texto_saida):
	msg.config(text = texto_saida)


#Função para imprimir números de um dígito
def imprime_um_digito (entrada):
	texto_saida = f"O número digitado foi: \n{unidades [entrada].capitalize()}"
	atualiza (texto_saida)
	return


#Função para imprimir números de dois dígitos
def imprime_dois_digitos (entrada):
	if entrada [0] == "1":
		texto_saida = f"O número digitado foi: \n{dezenas_dez [entrada].capitalize()}"
		atualiza (texto_saida)
		return

	elif entrada [1] == "0":
		texto_saida = f"O número digitado foi: \n{dezenas [entrada [0]].capitalize()}"
		atualiza (texto_saida)
		return

	else:
		texto_saida = f"O número digitado foi: \n{dezenas [entrada[0]].capitalize()} e {unidades [entrada[1:2]]}"
		atualiza (texto_saida)
		return


#Função para imprimir números de três dígitos
def imprime_tres_digitos (entrada):
	if entrada == "100":
		texto_saida = f"O número digitado foi: \n{centenas [entrada].capitalize()}"
		atualiza (texto_saida)
		return

	elif entrada [1:] == "00":
		texto_saida = f"O número digitado foi: \n{centenas [entrada[0]].capitalize()}"
		atualiza (texto_saida)
		return

	elif entrada [1] == '1':
		texto_saida = f"O número digitado foi: \n{centenas [entrada[0]].capitalize()} e {dezenas_dez [entrada[1:]]}"
		atualiza (texto_saida)
		return

	elif entrada [2] == "0":
		texto_saida = f"O número digitado foi: \n{centenas [entrada[0]].capitalize()} e {dezenas [entrada[1]]}"
		atualiza (texto_saida)
		return

	elif entrada [1] == "0":
		texto_saida = f"O número digitado foi: \n{centenas [entrada[0]].capitalize()} e {unidades [entrada[2]]}"
		atualiza (texto_saida)
		return

	else:
		texto_saida = f"O número digitado foi: \n{centenas [entrada [0]].capitalize()} e {dezenas [entrada[1]]} e {unidades [entrada[2]]}"
		atualiza (texto_saida)
		return



#Função base do programa, ela faz o tratamento da entrada do usuário
def program (event = None):

	entrada = user_input.get()

	#=*=*=*=*=*=*=*=*=*=*=*=Testando se o número é válido=*=*=*=*=*=*=*=*=*=*=*=
	if not entrada.isdigit():
		texto_saida = "Você precisa digitar um número natural!"
		atualiza (texto_saida)
		return
	        
	if int (entrada) > 999 or (len (entrada) > 1 and entrada [0] == "0"):
		texto_saida = "O número digitado não é válido!"
		atualiza (texto_saida)
		return

	digitos = len (entrada)
	    
	if digitos == 1:
		imprime_um_digito (entrada)
	        
	if digitos == 2:
		imprime_dois_digitos (entrada)
	            
	if digitos == 3:
		imprime_tres_digitos (entrada)



#Função para realizar a troca de modo de visualização (Alto Contraste ou Normal)
def modo_AC ():

	if msg ["fg"] == "white":
		fontStyle.config(size = 18, weight ='bold')
		msg.config(fg = "yellow")
		texto.config(fg = "yellow")
		run_Program.config (fg = "yellow", padx = 20)
	else:
		fontStyle.config(size = 14, weight = "normal")
		msg.config(fg = "white")
		texto.config(fg = "white")
		run_Program.config (fg = "white", padx = 10)


#Criando a janela de ajuda ao usuário
def nova_janela():

	janela_ajuda = tk.Toplevel(root)

	janela_ajuda.title ("Ajuda")
	janela_ajuda.iconbitmap ("resources/P_Logo.ico")
	janela_ajuda.grab_set ()
	janela_ajuda.focus_force()
	ajuda = tk.Label (janela_ajuda, text = instrucoes, fg = "white", bg = "black",
						font = fontStyle, wraplength = 600, padx = 50, pady = 70)
	janela_ajuda.resizable (False, False)

	if msg ["fg"] == "yellow":
		ajuda.config (fg = "yellow")

	ajuda.pack(anchor = "center", padx = 0.5, pady = 0.5)


#Definindo uma variável para facilitar a troca de estilos
fontStyle = tkFont.Font (size=14)

#Definindo as propriedades da janela
root.resizable (False, False)
root.title ("Números por extenso")
root.iconbitmap ("resources/P_Logo.ico")

#carregando as imagens necessárias
img_fundo = ImageTk.PhotoImage(Image.open("resources/bck.png"))
img_contrate = ImageTk.PhotoImage(Image.open('resources/alto_contraste.png'))
img_ajuda = ImageTk.PhotoImage(Image.open('resources/ajuda.png'))

#Criando a tela de fundo do programa
fundo = tk.Label(root, image = img_fundo)
fundo.pack ()

#Criando os textos exibidos pelo programa
texto = tk.Label (root, text = "Digite um número de 0 a 999:", bg = "#3B3A3A", 
					fg = "white", relief = "raised", font=fontStyle)
texto.place (anchor = "center", bordermode = "outside", rely = 0.25, relx = 0.5)

msg = tk.Label (root, text = texto_saida, bg = "#3B3A3A", fg = "white", wraplength = 300,
				font=fontStyle)
msg.place (anchor = "center", bordermode = "outside", rely = 0.65, relx = 0.5)

#Criando o campo de submissão dos números pelo usuário
user_input = tk.Entry (root, justify = "center")
user_input.place (anchor = "center", bordermode = "outside", rely = 0.45, relx = 0.5, 
					height = 30)

#Configurando o programa para aceitar "Enter" ao invés de clicar no botão "Iniciar"
root.bind('<Return>', program)

#Criando o botão de iniciar o programa
run_Program = tk.Button(root, text = "Iniciar", padx = 10, pady = 10,
						relief = "ridge", fg = "white", bg = "black", wraplength = 100,
						justify = "center", command = program, font = fontStyle)
run_Program.place(anchor = "center", bordermode = "outside", rely = 0.9, relx = 0.5)

#Criando o botão de modo "Alto-Contraste"
alto_contraste = tk.Button (root, image = img_contrate, command = modo_AC)
alto_contraste.place (anchor = "center", relx = 0.1, rely = 0.92)

#Criando o botão de ajuda ao usuário
ajuda = tk.Button(root, image = img_ajuda, command = nova_janela)
ajuda.place (anchor = "center", relx = 0.9, rely = 0.92)

root.mainloop()
import pyautogui
import pandas

pyautogui.PAUSE = 1
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 

#passo 1: entrar no sistema da empresa, navegador
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior p site carregar
time.sleep(3)


#passo 2: fazer login
#clicar no campo de email
pyautogui.press("tab" )
pyautogui.write("email@gmail.com")
pyautogui.press("tab") #prox campo
pyautogui.write("senha")
pyautogui.press("tab") #passar para o botao
pyautogui.press("enter")
time.sleep(3)#site carregar


#passo 3: abrir base de dados
#pip install pandas openpyxl
tabela = pandas.read_csv("produtos.csv")


#passo 4: cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=373, y=286)

    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")

    pyautogui.scroll(5000)


#passo 5: repetir o passo 4 até acabar a lista de produtos




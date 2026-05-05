import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=670, y=415)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=510, y=375)
pyautogui.write("emaillegal@yahoo.com")
pyautogui.press("tab")
pyautogui.write("Orwell#1984")
pyautogui.press("tab")
pyautogui.press("enter")

# barra de codigo do produto: Point(x=526, y=255)
tabela = pd.read_csv("produtos.csv")
time.sleep(5)

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=526, y=255)
    pyautogui.write(codigo)

    marca = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # obs = tabela.loc[linha, "obs"]
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.press("tab")
        pyautogui.write(tabela.loc[linha, "obs"])

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

import os
import shutil
import datetime

caminho = "C://caminho"
lista_arquivos = os.listdir(caminho)

lista_datas = []
for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        data = os.path.getmtime(f"{caminho}/{arquivo}")
        lista_datas.append((data, arquivo))

lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]

hoje = str(datetime.date.today())

shutil.move("caminho1/"+ultimo_arquivo[1], "caminho2/"+ hoje+" - " + ultimo_arquivo[1])

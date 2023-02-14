# Mover arquivos com Python

### Objetivo do projeto:
Copiar os LOGS do MiKrotik Syslog Daemon e colocar em uma pasta segura, utilizando Python

### Step by Step

O primeiro passo é importar as bibliotecas:
```python
import os # comandos no sistema operacional
import shutil # operações com arquivos\
import datetime # manipulação de datas
```
O segundo passo é descobrir qual é o arquivo mais recente da pasta:
```python
caminho = "caminho"
lista_arquivos = os.listdir(caminho)

lista_datas = []
for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        data = os.path.getmtime(f"{caminho}/{arquivo}")
        lista_datas.append((data, arquivo))

lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]
```
Terceiro passo: Obter a data de hoje, e criar uma variável que armazene isso:
```python
hoje = str(datetime.date.today()) # convertido p string
```
Por fim, bastar mover utilizando o shutil:
```python
shutil.move(\"C://caminho1/\"+ultimo_arquivo[1], \"C://caminho2/\"+ hoje+\" - \" + ultimo_arquivo[1])
```
No caso, se o arquivo se chamasse <em>teste.txt</em>, ele terminaria em outro caminho com o nome <em>14.02.2023 - teste.txt

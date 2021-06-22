import tabula
import pandas as pd
import csv
from tabulate import tabulate

df = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[119.42, 137.48, 212.69, 341.57], guess = False, pages = 79)

dados = pd.DataFrame([df])

dados.to_csv('quadro30.csv', sep = ';', index = False)
dados.to_csv('quadro31.csv', sep = ';', index = False)
dados.to_csv('quadro32.csv', sep = ';', index = False)

from zipfile import *

with ZipFile("teste.zip", "w") as myzip:
    myzip.write("quadro30.csv")
    myzip.write("quadro31.csv")
    myzip.write("quadro32.csv")
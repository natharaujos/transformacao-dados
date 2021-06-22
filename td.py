import tabula
import pandas as pd
import csv
# from tabulate import tabulate

quadro30 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[119.42, 137.48, 212.69, 341.57], guess = False, pages = 79)

quadro31_1 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[619.95, 137.96, 740.91, 498.30], guess = False, pages = 79)

quadro31_2 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[98.33, 137.24, 748.82, 497.96], guess = False, pages = 80)

quadro31_3 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[98.33, 137.24, 748.82, 497.96], guess = False, pages = 81)

quadro31_4 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[98.33, 137.24, 748.82, 497.96], guess = False, pages = 82)

quadro31_5 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[98.33, 137.24, 748.82, 497.96], guess = False, pages = 83)

quadro31_6 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[98.33, 137.24, 672.46, 497.96], guess = False, pages = 84)

quadro32 = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
        area=[133.48, 134.98, 198.68, 310.65], guess = False, pages = 85)

dados30 = pd.DataFrame([quadro30])
dados31 = pd.DataFrame([quadro31_1, quadro31_2, quadro31_3, quadro31_4, quadro31_5, quadro31_6])
dados32 = pd.DataFrame([quadro32])

dados30.to_csv('quadro30.csv', sep = ';', index = False)
dados31.to_csv('quadro31.csv', sep = ';', index = False)
dados32.to_csv('quadro32.csv', sep = ';', index = False)

from zipfile import *

with ZipFile("Teste_Intuitive_Care_{nathan_araujo}.zip", "w") as myzip:
    myzip.write("quadro30.csv")
    myzip.write("quadro31.csv")
    myzip.write("quadro32.csv")
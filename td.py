import tabula

from tabulate import tabulate

df = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", encoding = 'utf-8',
            area=[119.42, 137.48, 212.69, 341.57], guess = False, pages = 79)

print (tabulate(df))

df.to_csv('quadro30.csv', 'encoding='utf-8)


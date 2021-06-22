import tabula
import zipfile

arquivo = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", pages=30)

tabula.convert_into("Padrão_TISS_Componente_Organizacional_202103.pdf", "Padrão_TISS_Componente_Organizacional_202103.csv", output_format="csv", pages=30)


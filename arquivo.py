import tabula

arquivo = tabula.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", pages="30,31, 32")

tabula.convert_into("Padrão_TISS_Componente_Organizacional_202103.pdf", "Padrão_TISS_Componente_Organizacional_202103.csv", output_format="csv", pages="30,31,32")
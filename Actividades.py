import pandas as pd
import os

Archivos = os.listdir("Descarga")

Consolidado = pd.DataFrame()

for Archivo in Archivos:
    df = pd.read_csv(F"Descarga/{Archivo}" , sep=";")
    df["Archivo"] = Archivo
    Consolidado = pd.concat([Consolidado, df])

Consolidado.to_csv("Consolidado.csv", index=False)

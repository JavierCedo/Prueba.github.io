import pandas as pd
from pyscript import document


def Busqueda_año(event):
    input_text = document.querySelector("#nombre")
    nombre =  input_text.value
    datos = {"nombres":["Javier","Juan","Vieff","Carmencita"]}
    df = pd.DataFrame(datos)
    for i in range(df.shape[0]):
        for j in range(df.shape[0]):
            if nombre == df.iloc[nombre]:
                fila = df.index[i]
                columna = df.index[j]
    
    output_div = document.querySelector("#output")
    output_div.innerText = print("%s, %s"%(fila,columna))

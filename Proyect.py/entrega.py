
#importar libreria para leer archivos excel
#from re import A
from asyncio.windows_events import NULL
import openpyxl as excel
import pandas as pd
import json
import math

#book = openpyxl.load_workbook("./Data.xlsx", data_only=True)

#hoja = book.active

#lectura del archivo
path = "./Data.xlsx"

#lectura por columnas
articulos = pd.read_excel(path, engine="openpyxl", sheet_name="Inventario")
#almacenes = pd.read_excel(path, engine="openpyxl", sheet_name="Inventario", usecols=["ALMACEN"])
#tipos = pd.read_excel(path, engine="openpyxl", sheet_name="Inventario", usecols=["TIPO"])
#marca = pd.read_excel(path, engine="openpyxl", sheet_name="Inventario", usecols=["MARCA"])
#openFile = pd.read_excel(path, engine="openpyxl", sheet_name="Inventario", usecols=["CODIGO"])

#grardado de valores
articles = articulos.values
#warehouses = almacenes.values
#types = tipos.values
#brand = marca.values
#data = openFile.values

list = []


# Check whether some values are NaN or not
print ()

def isEmpty(val):
    x = math.isnan(val)
    print(x)
    """
    if x == True:
        return NULL
    else:
        return val
    """

for d in articles:
    jsn = {
        'code': d[0],
        'warehouse': d[1],
        'type': d[2],
        'brand': d[3],
        'name': d[4],
        'description': NULL,
        'sale_price': d[6],
        'shipping_price': d[7],
        'price': d[8],
        'manual_price': d[9],
        'quantity': d[10],
        'min_quantity':d[11],
        'active': d[12]
    }
    print(d[6])
    list.append(jsn)

data_json = json.dumps(list)
archivo_json = open("data.json","w")
archivo_json.write(data_json)
archivo_json.close()



#arreglos

#print(f'{warehouses}')
#print(f'{war}')
#almacenamiento de valores el arreglos
#for a in war:
    #print(a)

#for i in data:
    #print(i)





"""
todo = {}
todo['warehouses'] = []
todo['warehouses'].append({
    'alm' : [warehouses]})
with open ('TODO.json', 'w') as archivo:
    json.dump(todo, archivo)

prueba = []
datos = {}
prueba['almacen'] = warehouses
prueba.append(prueba)
prueba(f'{prueba}')


data_json = json.dumps(todo)
archivo_json = open("data.json","w")
archivo_json.write(data_json)
archivo_json.close()



"""


"""
#print(data['A2'].values)
for col in data.iter_cols(min_row=1, max_col=3,max_row=2):
    for cell in col:
        #cell_range = data['K2':'K255']
        print(cell)
"""

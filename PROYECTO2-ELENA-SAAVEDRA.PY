

#%%%%%importando pandas
import pandas as pd
#from sqlalchemy import false

#%%%%%
sldb= pd.read_csv ("synergy_logistics_database.csv")


#%%  TOTAL DE INGRESOS  EN LOGISTICA +++++CORRECTO++++++
TOTAL=sldb.groupby(["origin","destination","transport_mode","direction"])
toprutas=TOTAL.sum()["total_value"].sort_values(ascending=False)
toprutas=toprutas.reset_index()
total=toprutas["total_value"].sum()
toprutas["porcentaje"]=(toprutas["total_value"]/total)*100
toprutas.head(n=40)


#%% INFRESO TOTAL MODOS DE TRANSPORTE ++++++CORRECTO++++
modos_transporte=sldb.groupby("transport_mode").sum()
total=modos_transporte["total_value"].sum()
modos_transporte["porcentaje"]=(modos_transporte["total_value"]/total)*100




#%%%%total de operacioes realizadaspor medio de transporte
mododetransport=sldb.groupby("transport_mode").count()


#%%%%RUTAS POPULARES POR MEDIO DE TRASPORTE 
rutaspopulares=sldb.groupby(["origin","destination","transport_mode","direction"]).count()

#%%RUTAS MAS POPOLARES PARAEXPORTACION E IMPORTACION
rutasexport_import=sldb.groupby(["direction","origin","destination","transport_mode"]).count()
export=sldb[sldb["direction"]=="Exports"]
imports=sldb[sldb["direction"]=="Imports"]


#%%%RUTAS DE EXPORTACION POR CONTEO
export_populares=export.groupby(["origin","destination","transport_mode"]).count()


#%%%RUTAS DE EXPORTACION ORDENANDO PRIMEROS 10 POR CONTEO Y PORCENTAJE QUE APORTAN AL INGRESO TOTAL DE OPERACIONES REALIZ
export_populares=export.groupby(["origin","destination","transport_mode"])
top_rutasex=export_populares.count()["total_value"].sort_values(ascending=False)
top_rutasex=top_rutasex.reset_index()
total=top_rutasex["total_value"].sum()
top_rutasex["porcentaje"]=(top_rutasex["total_value"]/total)*100

#%%%RUTAS DE EXPORTACION ORDENANDO PRIMEROS 10 POR INGRESOS TOTALES Y PORCENTAJE QUE APORTAN AL INGRESO TOTAL
export_populares=export.groupby(["origin","destination","transport_mode"])
top_rutasex=export_populares.sum()["total_value"].sort_values(ascending=False)
top_rutasex=top_rutasex.reset_index()
total=top_rutasex["total_value"].sum()
top_rutasex["porcentaje"]=(top_rutasex["total_value"]/total)*100



#%%%RUTAS DE EXPORTACION ORDENANDO PRIMEROS 10 POR  CONTEO
export_populares=export.groupby(["origin","destination","transport_mode"])
top_rutasex=export_populares.count()["total_value"].sort_values(ascending=False).head(10)


#%%%RUTAS DE IMPORTACION POR CONTEO
import_populares=imports.groupby(["origin","destination","transport_mode"]).count()

#%%%RUTAS DE IMPORTACION  ORDENANDO PRIMEROS POR CONTEO Y PORCENTAJE QUE APORTAN  TOTAL DE OPERACIONES REALIZ
import_populares=imports.groupby(["origin","destination","transport_mode"])
top_rutasim=import_populares.count()["total_value"].sort_values(ascending=False)
top_rutasim=top_rutasim.reset_index()
total=top_rutasim["total_value"].sum()
top_rutasim["porcentaje"]=(top_rutasim["total_value"]/total)*100


#%%%RUTAS DE IMPORTACION ORDENANDO POR INGRESOS TOTALES Y PORCENTAJE QUE APORTA AL TOTAL
import_populares=imports.groupby(["origin","destination","transport_mode"])
top_rutasim=import_populares.sum()["total_value"].sort_values(ascending=False)
top_rutasim=top_rutasim.reset_index()
total=top_rutasim["total_value"].sum()
top_rutasim["porcentaje"]=(top_rutasim["total_value"]/total)*100


# %%

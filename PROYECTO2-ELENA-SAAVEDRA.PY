



#%%%%%importando pandas
import pandas as pd
#from sqlalchemy import false

#%%%%%
sldb= pd.read_csv ("synergy_logistics_database.csv")

#%% PROMEDIO TOTAL MODOS DE TRANSPORTE 
modos_transporte=sldb.groupby("transport_mode").mean()



#%%%%total de operacioes realizadaspor medio de transporte
mododetransport=sldb.groupby("transport_mode").count()


#%%%%RUTAS POPULARES POR MEDIO DE TRASPORTE
rutaspopulares=sldb.groupby(["origin","destination","transport_mode"]).count()

#%%RUTAS MAS POPOLARES PARAEXPORTACION E IMPORTACION

rutasexport_import=sldb.groupby(["direction","origin","destination","transport_mode"]).count()
export=sldb[sldb["direction"]=="Exports"]
imports=sldb[sldb["direction"]=="Imports"]


#%%%RUTAS DE EXPORTACION POR CONTEO
export_populares=export.groupby(["origin","destination","transport_mode"]).count()

#%%%RUTAS DE EXPORTACION ORDENANDO PRIMEROS 10
export_populares=export.groupby(["origin","destination","transport_mode"])
top_rutasex=export_populares.count()["total_value"].sort_values(ascending=False).head(10)
top_rutasex=top_rutasex.reset_index()
total=top_rutasex["total_value"].sum()
top_rutasex["porcentaje"]=(top_rutasex["total_value"]/total)*100


#%%%RUTAS DE IMPORTACION POR CONTEO
import_populares=imports.groupby(["origin","destination","transport_mode"]).count()

#%%%RUTAS DE IMPORTACION ORDENANDO PRIEMEROS 10
import_populares=imports.groupby(["origin","destination","transport_mode"])
top_rutasim=import_populares.count()["total_value"].sort_values(ascending=False).head(10)


# %%

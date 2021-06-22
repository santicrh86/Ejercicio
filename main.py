
from urllib.request import urlretrieve

import numpy as np
import pandas as pd

url = 'http://analytics.deacero.com/Api/GetApi/ApiHotelFull/ff7482d9-5203-5381-8d97-c769a4807328'

#urlretrieve(url, 'test2.json')
df = pd.read_json('test2.json')
df.to_csv("Datos.csv")
print("Fin de codigo")

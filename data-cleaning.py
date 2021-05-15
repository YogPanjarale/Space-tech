import pandas as pd
import csv

from pandas.core.frame import DataFrame

fcsv = pd.read_csv("data\\given.csv")

print(fcsv.shape)
cols_to_del = fcsv.columns.tolist()[5:]
col_not_to_remove = ["planet_type","planet_radius","orbital_radius","orbital_period","eccentricity","pl_hostname","pl_discmethod","pl_orbincl","pl_dens","st_mass","st_rad","st_teff","dec_str","ra_str"]
for r in col_not_to_remove:
    cols_to_del.remove(r)
# print(cols_to_del)
for d in cols_to_del:
    del fcsv[d]
print(fcsv.shape)
print(list(fcsv))
fcsv:DataFrame = fcsv.rename({
    "pl_hostname":"solar_system_name",
    "pl_discmethod":"planet_discovery_method",
    "pl_orbincl":"planet_orbital_inclination",
    "pl_dens":"planet_density",
    "ra_str":"right_ascension",
    "dec_str":"declination",
    "st_teff":"host_temprature",
    "st_mass":"host_mass",
    "st_rad":"host_radius"
},axis="columns")
print(list(fcsv))
fcsv.to_csv("data\\cleaned.csv")
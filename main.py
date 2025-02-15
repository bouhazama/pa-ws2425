import datetime
import os

import numpy as np

import project.functions as fn

file_path = "./project/data/data_GdD_Datensatz_WS2425.h5"
brewing = "brewing_0002" 
tank_id = "B001"
measured_quantities = ("level", "temperature", "timestamp")

def main():
    brewing_T_env = fn.read_metadata(file_path, brewing, "T_env")
    brewing_specific_heat_capacity_beer = fn.read_metadata(file_path, brewing, "specific_heat_capacity_beer")
    brewing_density_beer = fn.read_metadata(file_path, brewing, "density_beer")

    print(brewing_T_env)
    print(brewing_specific_heat_capacity_beer)
    print(brewing_density_beer)

if __name__ == "__main__":
    main()

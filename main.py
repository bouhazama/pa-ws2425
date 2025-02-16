import datetime
import os

import numpy as np

import project.functions as fn

file_path = "./project/data/data_GdD_Datensatz_WS2425.h5"
brewing = "brewing_0002" 
tank_id = "B001"
measured_quantities = ("level", "temperature", "timestamp")

def main():
    # brewing group metadata
    brewing_T_env = fn.read_metadata(file_path, brewing, "T_env")
    brewing_specific_heat_capacity_beer = fn.read_metadata(file_path, brewing, "specific_heat_capacity_beer")
    brewing_density_beer = fn.read_metadata(file_path, brewing, "density_beer")
    # tank group metadata
    tank_id_path = f"{brewing}/{tank_id}"
    mass_tank = fn.read_metadata(file_path, tank_id_path, "mass_tank")
    surface_area_tank = fn.read_metadata(file_path, tank_id_path, "surface_area_tank")
    footprint_tank = fn.read_metadata(file_path, tank_id_path, "footprint_tank")
    heat_transfer_coeff_tank = fn.read_metadata(file_path, tank_id_path, "heat_transfer_coeff_tank")
    specific_heat_capacity_tank = fn.read_metadata(file_path, tank_id_path, "specific_heat_capacity_tank")

    df_data = {}
    raw_data = {}

    for measured_quantity in measured_quantities:
        dataset_path = f"{tank_id_path}/{measured_quantity}"
        raw_data[measured_quantity] = fn.read_data(file_path, dataset_path)

    print(raw_data)    

if __name__ == "__main__":
    main()

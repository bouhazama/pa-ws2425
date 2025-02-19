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

    is_equal_lenght = fn.check_equal_length(raw_data["level"], raw_data["temperature"], raw_data["timestamp"])
    if not is_equal_lenght:
        raise ValueError("all measured datasets must have the same lenght")
    
    processed_data = {}
    filter_sizes = (4, 20, 41, 191)
    df_data["time"] = fn.process_time_data(raw_data["timestamp"])

    for filter_size in filter_sizes:
        key = f"temperature_k_{filter_size}"
        processed_data[key] = fn.filter_data(raw_data["temperature"], filter_size)


    fill_level_without_negatives = fn.remove_negatives(raw_data["level"])
    fill_level_nan_interpolated = fn.interpolate_nan_data(df_data["time"], fill_level_without_negatives)

    for filter_size in filter_sizes:
        key = f"level_k_{filter_size}"
        processed_data[key] = fn.filter_data(fill_level_nan_interpolated, filter_size)

    # TODO some level interpolated data has nans
    print(processed_data)



if __name__ == "__main__":
    main()

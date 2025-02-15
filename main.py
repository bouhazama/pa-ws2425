import datetime
import os

import numpy as np

import project.functions as fn

file_path = "./project/data/data_GdD_Datensatz_WS2425.h5"
brewing = "brewing_0002" 
tank_id = "B001"
measured_quantities = ("level", "temperature", "timestamp")

def main():
    unit_metadata = fn.read_metadata(file_path, "brewing_0002/B001/level", "unit")


if __name__ == "__main__":
    main()

from typing import Any

import h5py as h5
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from numpy.typing import NDArray
import pandas as pd
from plotid.publish import publish
from plotid.tagplot import tagplot


def read_metadata(file: str, path: str, attr_key: str) -> Any | None:
    """Die Funktion liest aus einer HDF5-Gruppe einen Metadatenwert aus. Falls das Metadatum, die HDF5-Gruppe oder der Datensatz nicht existieren
    ,werden die Pfade aller zur Verfuegung gestellten DataFrames gezeigt.
    
    Args:
        file (str): Pfad der HDF5-Datei
        path (str): Pfad zu einer HDF5-Gruppe oder eines Datensatzes innerhalb der HDF5-Datei
        attr_key (str): Name des Metadatums, das ausgelesen werden soll

    
    Returns:
        Union[Any | None]: Metadatenwert oder None, falls das Metadatum, die HDF5-Gruppe oder der Datensatz nicht vorhanden ist.
    """
    with h5.File(file, 'r') as f:
        try:
            metadata = f[path].attrs[attr_key]
        except KeyError:
            print("The given group path: '{}', or metadata key '{}' does not exist".format(path, attr_key))
            return None
    return metadata

def read_data(file: str, path: str) -> NDArray | None:
    pass


def check_equal_length(*arrays: NDArray) -> bool:
    pass


def process_time_data(data: NDArray) -> NDArray:
    pass


def remove_negatives(array: NDArray) -> NDArray:
    pass


def linear_interpolation(
    time: NDArray, start_time: float, end_time: float, start_y: float, end_y: float
) -> NDArray:
    pass


def interpolate_nan_data(time: NDArray, y_data: NDArray) -> NDArray:
    pass


def filter_data(data: NDArray, window_size: int) -> NDArray:
    """Filter data using a moving average approach.

    Args:
        data (NDArray): Data to be filtered
        window_size (int): Window size of the filter

    Returns:
        NDArray: Filtered data
    """
    output = []
    pad_width = window_size // 2
    padded_data = np.pad(array=data, pad_width=pad_width, mode="empty")
    for i in range(pad_width, padded_data.size - pad_width):
        # Implementieren Sie hier den SMA!
        sma = []
        output.append(sma)
    return np.array(output)



def calc_heater_heat_flux(P_heater: float, eta_heater: float) -> float:
    pass


def calc_convective_heat_flow(
    k_tank: float, area_tank: float, t_total: float, t_env: float
) -> float:
    pass


def calc_mass_flow(
    level_data: NDArray, tank_footprint: float, density: float
) -> NDArray:
    pass


def calc_transported_power(
    mass_flow: float, specific_heat_capacity: float, temperature: float
) -> float:
    pass


def store_plot_data(
    data: dict[str, NDArray], file_path: str, group_path: str, metadata: dict[str, Any]
) -> None:
    pass


def read_plot_data(
    file_path: str, group_path: str
) -> tuple[pd.DataFrame, dict[str, Any]]:
    pass


def plot_data(data: pd.DataFrame, formats: dict[str, str]) -> Figure:
    pass


def publish_plot(
    fig: Figure, source_paths: str | list[str], destination_path: str
) -> None:
    pass


if __name__ == "__main__":
    pass

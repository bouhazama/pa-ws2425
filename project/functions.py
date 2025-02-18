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
    """The function reads a metadata value from an HDF5 group. If the metadata, the HDF5 group, 
    or the dataset does not exist, a message is displayed.
    
    Args:
        file (str): Path to the HDF5 file
        path (str): Path to an HDF5 group or a dataset within the HDF5 file
        attr_key (str): Name of the metadata to be read

    Returns:
        Union[Any | None]: Metadata value or None if the metadata, the HDF5 group, or the dataset is not available.
    """
    with h5.File(file, 'r') as f:
        try:
            metadata = f[path].attrs[attr_key]
        except KeyError:
            print("The given group path: '{}', or metadata key '{}' does not exist".format(path, attr_key))
            return None
    return metadata


def read_data(file: str, path: str) -> NDArray | None:
    """The function reads a data value from an HDF5 group. If the path of the data does not exist, a warning is displayed
    
    Args:
        file (str): Path to the HDF5 file
        path (str): Path to an HDF5 group or a dataset within the HDF5 file

    Returns:
        Union[NDArray | None]: numpy array or None
    """
    # TODO IMPROV ERROR HANDLING
    with h5.File(file, 'r') as f:
        try:
            data = f[path]
            return data[()]
        except KeyError:
            print("The given path: '{}' does not exist".format(path))
            return None
  

def check_equal_length(*arrays: NDArray) -> bool:
    """Compare the lengths of multiple NDArrays passed as a tuple.

    Args:
        *arrays: Variable number of NDArrays to compare.

    Returns:
        bool: True if all arrays have the same length, False otherwise.
    """
    lengths = [len(arr) for arr in arrays]
    if all(length == lengths[0] for length in lengths):
        return True
    else:
        return False


def process_time_data(data: NDArray) -> NDArray:
    """Subtract the first value of the passed array from all other values and convert them to seconds.

    Args:
        data: NDArray of timestamps.

    Returns:
        NDArray: array of timestamp relativ to start of measurment in seconds.
    """
    start_timestamp = data[0]
    substract = lambda x: (x - start_timestamp)/1000
    return substract(data)


def remove_negatives(array: NDArray) -> NDArray:
    """Replace negativ values with np.nan.

    Args:
        array: NDArray of timestamps.

    Returns:
        NDArray: array of timestamp after replacing negativ values with np.nan.
    """
    return np.where(array < 0, np.nan, array)
    

def linear_interpolation(
    time: NDArray, start_time: float, end_time: float, start_y: float, end_y: float
) -> NDArray:
    """Apply linear interpolation based on start_y + (end_y - start_y)*((x - start_time)/(end_time - start_time)).

    Args:
        time: NDArray of timestamps.

    Returns:
        NDArray: array of interpolated values having the same lenght as time array passed as parameter.
    """
    interpolate = lambda x: start_y + (end_y - start_y)*((x - start_time)/(end_time - start_time))
    return interpolate(time)


def interpolate_nan_data(time: NDArray, y_data: NDArray) -> NDArray:
    """Interpolate gaps of np.nan that exist in y_data in time array.

    Args:
        time: NDArray of timestamps.
        y_data: NDArray of values.

    Returns:
        NDArray: array of interpolated values having the same lenght as time array passed as parameter.
    """
    first_y_value = y_data[0]
    last_y_value = y_data[-1]
    if first_y_value == np.nan or last_y_value == np.nan:
        raise ValueError("the first and last value in the y_data array must not contain np.nan.")
    active_gap = False
    interpolated_data = np.copy(y_data)
    for index, value in np.ndenumerate(y_data):
        if value == np.nan and active_gap == False:
            start_index = index 
            active_gap = True
        if value != np.nan and active_gap == True:
            end_index = index
            # TODO use time[start_index - 1] ?
            # Q: in 3.d.5 the array to pass to the previously implemented as first argument is the full time data or time data in the interval [start_index:end_index]
            # if time data in the interval [start_index:end_index] then why also we provide start_time, end_time
            gap_interpolation = linear_interpolation(time, time[start_index - 1], time[end_index], y_data[start_index - 1], y_data[end_index])
            # TODO How to populate interpolated _data, Q: in 3.d.7) After the loop ends, return the array interpolated_data. it was not mentioned how to populate interpolated_data
            interpolated_data = gap_interpolation
            active_gap = False


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

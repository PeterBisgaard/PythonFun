# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:39:08 2024

@author: Trine

Slize the file into months 

stride=10
lon_subset = lon[::stride,::stride]

make a meshgrid by splitting each line(lat) into an array then append them together
"""
#%% initialisation 
import os
import numpy as np 
import pandas as pd

#%% Function

def Split_files(file_path, output_directory, target): 

    data = []

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            data.append(columns)

    df = pd.DataFrame(data)

    # Convert DataFrame values to numeric, replacing non-numeric strings with NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Replace NaN values with 0 (or any other desired value)
    df = df.fillna('')

    matches = np.all(df.values == target, axis=1)

    matching_row_indices = np.where(matches)[0]

    start_index = 0
    array_count = 0

    for i in matching_row_indices:
        if start_index == i:
            continue
        
        segment = df.iloc[start_index-1:i]
        
        start_index = i + 1
        
        # Save the segment to a file
        file_name = f"month_{array_count}.gri"
        full_path = os.path.join(output_directory, file_name)
        np.savetxt(full_path, segment.values, fmt='%s')  # Save as strings
        array_count += 1  # Prepare for the next file name
   
#%% Run Function
file_path=r"C:\Users\Trine\Bachelor\Iceland_480.gri"
output_directory = r"C:\Users\Trine\OneDrive\DTU\Bachelorprojekt\Harmexpg\Iceland 480 km"
target=np.array([ 62.00, 69.00, -26.00, -12.00, 0.05, 0.1])

Split_files(file_path, output_directory, target)



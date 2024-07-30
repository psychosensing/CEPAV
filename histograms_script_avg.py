from glob import glob
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import re
import tqdm
import numpy as np
import pickle
import os

s_output_paths = sorted(glob("VU_AMS/s2_output/*.csv", recursive=True), key=lambda x: f'{int(re.search("p([0-9]+)", x).group(1)):03}')
avg_values_path = "s2_avg_values.pic"
histogram_save_plot_path = "s2_histograms.png"
use_columns = {"HR": [30,150], "DBP": [30, 150], "SBP": [60, 120], "CO": [0,15], "TPR": [0,10], "tl": [-9999], "tr": [-9999], "wr": [-9999]}
bins=20

pbar = tqdm.tqdm(s_output_paths)
participant_columns_avergage = {}
columns_avergage = {}
avg_loaded_paths = []

if os.path.exists(avg_values_path):    
    with open(avg_values_path, "rb") as file:
        participant_columns_avergage, columns_avergage, avg_loaded_paths = pickle.load(file)
        print(f"Loaded min max from file: {len(participant_columns_avergage)}, {len(columns_avergage)}, {len(avg_loaded_paths)}")

for participant_path in pbar:
    if participant_path in avg_loaded_paths:
        pbar.set_description("AVG skipping %s" % participant_path)
        continue
    pbar.set_description("AVG Processing %s" % participant_path)
    participant_name = os.path.basename(participant_path)
    if participant_name not in participant_columns_avergage:
        participant_columns_avergage[participant_name] = {}
    df = pd.read_csv(participant_path, header=0)
    # for column_name in df.columns.difference(['timestamp']):
    for column_name in use_columns:
        if len(use_columns[column_name]) > 1:
            df_between = df[column_name][df[column_name].between(use_columns[column_name][0], use_columns[column_name][1], inclusive="both")]
        else:
            df_between = df[column_name][df[column_name] != use_columns[column_name][0]]   
        average_value = df_between.mean()
        participant_columns_avergage[participant_name][column_name] =  average_value
        if column_name not in columns_avergage:
            columns_avergage[column_name] = []
        columns_avergage[column_name].append(average_value)    
        
    avg_loaded_paths.append(participant_path)
    if pbar.n % 5 == 0:
        pbar.set_description("Dump avg values, loaded paths")
        with open(avg_values_path, "wb") as file:
            pickle.dump((participant_columns_avergage, columns_avergage, avg_loaded_paths), file)
pbar.close()
print("Dump avg values, loaded paths")
with open(avg_values_path, "wb") as file:
    pickle.dump((participant_columns_avergage, columns_avergage, avg_loaded_paths), file)
    
pd.DataFrame(columns_avergage).hist(figsize=(23,10), bins=bins, layout=(2,4))
plt.savefig(histogram_save_plot_path) 
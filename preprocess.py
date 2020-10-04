import pandas as pd
from sklearn import preprocessing
import numpy as np

def preprocess(unprocessedData):
    processedData = unprocessedData

    # Get types of each column
    types = unprocessedData.dtypes
    indexOfFloats = list()
    names = unprocessedData.columns
    nameCounter = 0
    for x in types:
        if(x == float):
            indexOfFloats.append(names[nameCounter])
        nameCounter += 1

    # Get all columns that are floats
    df_num = unprocessedData.select_dtypes(include=[np.float])
    # Normalize column data
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(df_num)
    df_normalized = pd.DataFrame(x_scaled)

    # Replace columns in original dataset that were floats
    norm_count = 0
    for fl in indexOfFloats:
        processedData[fl] = df_normalized[norm_count]
        norm_count += 1

    return processedData
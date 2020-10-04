import numpy as np
import pandas as pd

def cleanData(dataFile, nameFile):
    raw_data = []
    names = []
    for line in nameFile:
        if '\n' in line:
            temp = line.split('\n')
            names.append(temp[0])
        else:
            names.append(line)

    for line in dataFile:
        vals = line.split(',')
        for i in range(len(vals)):
            if '\n' in vals[i]:
                temp = vals[i].split('\n')
                vals[i] = temp[0]
            try:
                vals[i] = float(vals[i])
            except:
                pass
        raw_data.append(np.array(vals))

    data = np.array(raw_data)

    dataset = pd.DataFrame(data=data, columns=names)

    # Make columns numeric if applicable
    for col in dataset.columns:
        try:
            dataset[col] = pd.to_numeric(dataset[col])
        except:
            pass

    return dataset
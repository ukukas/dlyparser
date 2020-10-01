import pandas as pd

colspecs = [(0, 11),
           (12, 20),
           (21, 30),
           (31, 37),
           (38, 40),
           (41, 71),
           (72, 75),
           (76, 79),
           (80, 85)]

names = ['ID', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'STATE', 'NAME',
            'GSN FLAG', 'HCN/CRN FLAG', 'WMO ID']

df = pd.read_fwf('ghcnd-stations.txt', colspecs = colspecs, header = None,
                 names = names, converters = {'WMO ID': str})

df.to_csv('ghcnd-stations.csv', index = False)
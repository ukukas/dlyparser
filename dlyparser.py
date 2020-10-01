import pandas as pd

FBASE = 'ABC12345678'

widths = [11, 4, 2, 4] + [5, 1, 1, 1] * 31

stubnames = ['VALUE', 'MFLAG', 'QFLAG', 'SFLAG']
corenames = ['ID', 'YEAR', 'MONTH', 'ELEMENT']

names = corenames.copy()

for i in range(1,32):
    for name in stubnames:
        names.append(name + str(i))

writeorder = ['ID', 'YEAR', 'MONTH', 'DAY', 'ISODATE', 'ELEMENT', 'VALUE',
                'MFLAG', 'QFLAG', 'SFLAG']

dtypes = {'ID': str, 'YEAR': int, 'MONTH': int, 'ELEMENT': str}

for i in range(1,32):
    dtypes['VALUE' + str(i)] = int
    for name in stubnames[1:]:
        dtypes[name + str(i)] = str

df = pd.read_fwf(FBASE + '.dly', widths = widths, header = None, names = names,
                 converters = dtypes)
df = pd.wide_to_long(df, stubnames = stubnames, i = corenames, j = 'DAY')
df.reset_index(inplace = True)
df['ISODATE'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']], errors = 'coerce')
df.dropna(subset = ['ISODATE'], inplace = True)
df = df[writeorder]
df.sort_values(by=['ISODATE', 'ELEMENT'], inplace = True)
df.to_csv(FBASE + '.csv', index = False)

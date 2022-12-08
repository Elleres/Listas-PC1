import pandas as pd

df = pd.read_excel('exercicio_pandas\\arquivo.xlsx', header=0)
csvPythonFT = list(df['language'] == 'Python')
csvPython = df.loc[csvPythonFT]
csvPython.drop_duplicates(keep='first', subset=['repo_name'], inplace=True)
srtd = csvPython.sort_values(by='stars', ascending=False)
srtd = srtd.head(50)
srtdforks = csvPython.sort_values(by='forks', ascending=False)
srtdforks = srtdforks.head(50)
srtd.to_csv('PythonOnlyStars50.csv')
csvPython.to_csv('PythonOnly.csv')
srtdforks.to_csv('PythonForksSorted.csv')

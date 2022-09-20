import imdb
import csv


colunas = ['imdbID', 'title', 'year', 'genres', 'kind']
linhas = []
linhas_2 = []
filmes_id = [20880628, 10872600, 3501632, 9419884, 7131622]
texto = str()
for code in filmes_id:
    ia = imdb.IMDb()
    series = ia.get_movie(code)
    imdbID = series.data['imdbID']
    title = series.data['title']
    year = series.data['year']
    genres = series.data['genres']
    kind = series.data['kind']
    linhas.append(imdbID)
    linhas.append(title)
    linhas.append(year)
    for i in genres:
        texto += i + ' '
    linhas.append(texto)
    texto = ''
    linhas.append(kind)
    linhas_2.append(list(linhas))
    linhas.clear()
with open('filmes.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(colunas)
    write.writerows(linhas_2)

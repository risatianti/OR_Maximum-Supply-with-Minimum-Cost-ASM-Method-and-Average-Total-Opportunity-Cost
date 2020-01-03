from prints import line, dfprint, alokasi, delete
import numpy as np, pandas as pd, os

files = [i for i in os.listdir() if i.endswith('.xlsx')]
print('PILIH DATA')
for i, file in enumerate(files):
    print('{}. {}'.format(i + 1, file))
indx = int(input('masukkan pilihan: '))
raws = pd.read_excel(files[indx - 1], sheet_name='RANK').values

sups = np.copy(raws[:, -1])
dems = np.copy(raws[-1])

data = np.copy(raws[:-1, :-1])
loop = np.copy(data)

rows = np.arange(len(data))
cols = np.arange(len(data[0]))

print('DATA AWAL')
dfprint(loop, rows, cols, sups, dems, '')

aloc, I = [], 1
while True:
    print('>> ITERASI {}'.format(I));
    line()
    dfprint(loop, rows, cols, sups, dems, '   ')

    r = np.argmax(sups)
    c = np.argmin(loop[r])
    aloc.append((min([sups[r], dems[c]]), data[rows[r], cols[c]]))
    loop, rows, cols, sups, dems = delete(loop, rows, cols, sups, dems, r, c, [], [])

    print('')
    dfprint(loop, rows, cols, sups, dems, '   ')

    if len(loop) == 0:
        print('   Matriks Habis')
        break
    I += 1

alokasi(aloc)

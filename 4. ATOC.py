from prints import line, dfprint, alokasi, delete
import numpy as np
import pandas as pd
import os

files = [i for i in os.listdir() if i.endswith('.xlsx')]
print('PILIH DATA')
for i, file in enumerate(files):
    print('{}. {}'.format(i + 1, file))
indx = int(input('masukkan pilihan: '))
raws = pd.read_excel(files[indx - 1], sheet_name='RANK').values

sups = np.copy(raws[:, -1])
dems = np.copy(raws[-1])

data = np.copy(raws[:-1, :-1])

rows = np.arange(len(data))
cols = np.arange(len(data[0]))

print('DATA AWAL')
dfprint(data, rows, cols, sups, dems, '')

print('Reduksi Baris:')
red_row = np.array([i - min(i) for i in data])
dfprint(red_row, rows, cols, sups, dems, '')

print('Reduksi Kolom:')
red_col = np.array([i - min(i) for i in data.T]).T
dfprint(red_col, rows, cols, sups, dems, '')

print('Reduksi Baris + Reduksi Kolom')
loop = red_row + red_col
dfprint(loop, rows, cols, sups, dems, '')

print('RATOC dan CATOC')
stoc = np.array([np.average(i) for i in loop])
dtoc = np.array([np.average(i) for i in loop.T]).T
print('>> RATOC:', np.round(stoc, 2).tolist())
print('>> CATOC:', np.round(dtoc, 2).tolist(), '\n')


def safe_max(arr):
    if len(arr) == 0:
        return 0
    return max(arr)


aloc, I = [], 1
while True:
    print('>> ITERASI {}'.format(I));
    line()
    dfprint(loop, rows, cols, sups, dems, '   ')
    print('   RATOC:', np.round(stoc, 2).tolist())
    print('   CATOC:', np.round(dtoc, 2).tolist(), '\n')

    if safe_max(stoc) >= safe_max(dtoc):
        r = np.argmax(stoc)
        c = np.argmin(loop[r])
        print('   Maksimum: RATOC {}'.format(rows[r] + 1))
        print('   Nilai Minimum pada R{}: C{}'.format(rows[r] + 1, cols[c] + 1))
    else:
        c = np.argmax(dtoc)
        r = np.argmin(loop[:, c])
        print('   Maksimum: CATOC {}'.format(cols[c] + 1))
        print('   Nilai Minimum pada C{}: R{}'.format(cols[c] + 1, rows[r] + 1))

    aloc.append((min([sups[r], dems[c]]), data[rows[r], cols[c]]))
    loop, rows, cols, sups, dems, stoc, dtoc = delete(loop, rows, cols, sups, dems, r, c, stoc, dtoc)

    print('')
    dfprint(loop, rows, cols, sups, dems, '   ')

    if loop.shape[0] == 0 or loop.shape[1] == 0:
        print('   Matriks Habis')
        break
    I += 1

alokasi(aloc)

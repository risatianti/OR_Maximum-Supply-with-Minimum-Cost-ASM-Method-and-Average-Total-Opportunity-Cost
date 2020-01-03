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

rows = np.arange(len(data))
cols = np.arange(len(data[0]))

print('DATA AWAL')
dfprint(data, rows, cols, sups, dems, '')

loop = np.copy(data)


def reduksibaris(ldata):
    return np.array([i - min(i) for i in ldata])


def reduksikolom(ldata):
    return np.array([i - min(i) for i in ldata.T]).T


aloc = []
I = 1
while True:
    print('>> ITERASI {}'.format(I))
    if not all([0 in i for i in loop]):
        print('   Reduksi Baris')
        loop = reduksibaris(loop)
        dfprint(loop, rows, cols, sups, dems, '   ')

    if not all([0 in i for i in loop.T]):
        print('   Reduksi Kolom')
        loop = reduksikolom(loop)
        dfprint(loop, rows, cols, sups, dems, '   ')

    R, C = np.where(loop == 0)
    R, C = R.tolist(), C.tolist()

    skor = [R.count(i) + C.count(j) for i, j in zip(R, C)]

    index = np.argmin(skor)
    r, c = R[index], C[index]

    aloc.append((min([sups[r], dems[c]]), data[rows[r], cols[c]]))
    loop, rows, cols, sups, dems = delete(loop, rows, cols, sups, dems, r, c, [], [])
    dfprint(loop, rows, cols, sups, dems, '   ')

    if len(loop) == 0:
        break
    I += 1

alokasi(aloc)
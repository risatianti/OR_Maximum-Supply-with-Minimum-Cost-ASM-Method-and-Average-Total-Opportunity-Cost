import numpy as np, pandas as pd


def line():
    print('-' * 70)


def dfprint(data, rows, cols, sups, dems, spc):
    temp = np.copy(data)
    temp = np.vstack((temp, dems[:-1]))
    temp = np.vstack((temp.T, sups)).T

    df = pd.DataFrame(temp)
    df.columns = ['C{}'.format(i + 1) for i in cols] + ['SUP']
    df.index = ['{}R{}'.format(spc, i + 1) for i in rows] + ['{}DEM'.format(spc)]
    print(df, '\n')


def alokasi(aloc):
    line()
    print('\nALOKASI')

    maxa = max([len(str(i)) for i, j in aloc])
    maxb = max([len(str(j)) for i, j in aloc])
    maxc = len(str(sum([i * j for i, j in aloc])))

    jmlh = 0
    for i, j in aloc:
        a = str(i) + ' ' * (maxa - len(str(i)))
        b = str(j) + ' ' * (maxb - len(str(j)))
        c = ' ' * (maxc - len(str(i * j))) + str(i * j)
        print('{} x {} = {}'.format(a, b, c))
        jmlh += i * j
    print('\nJUMLAH:', jmlh)


def delete(loop, rows, cols, sups, dems, r, c, stoc, dtoc):
    if sups[r] > dems[c]:
        print('   Hapus Kolom C{}, menjadi:'.format(cols[c] + 1))
        sups[r] = sups[r] - dems[c]
        loop = np.delete(loop, c, 1)
        dems = np.delete(dems, c)
        cols = np.delete(cols, c)
        if dtoc != []:
            dtoc = np.delete(dtoc, c)
    elif sups[r] < dems[c]:
        print('   Hapus Baris R{}, menjadi:'.format(rows[r] + 1))
        dems[c] = dems[c] - sups[r]
        loop = np.delete(loop, r, 0)
        sups = np.delete(sups, r)
        rows = np.delete(rows, r)
        if stoc != []:
            stoc = np.delete(stoc, r)
    else:
        print('   Hapus Kolom C{} dan Baris R{}, menjadi:'.format(cols[c] + 1, rows[r] + 1))
        dems = np.delete(dems, c)
        sups = np.delete(sups, r)
        loop = np.delete(loop, c, 1)
        loop = np.delete(loop, r, 0)
        cols = np.delete(cols, c)
        rows = np.delete(rows, r)
        if stoc != []:
            dtoc = np.delete(dtoc, c)
            stoc = np.delete(stoc, r)
    if stoc == []:
        return loop, rows, cols, sups, dems
    return loop, rows, cols, sups, dems, stoc, dtoc

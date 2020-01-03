import numpy as np
import pandas as pd

def line():
    print('-'*70)

def integrate(a,b,c,d):
    return (((1/2)*a)+b)+(c-((1/2)*d))

def dataframe(arr,sup,dem,lr,lc,prin):
    x = np.copy(arr).tolist()
    x.append(dem)
    
    x = (np.asarray(x).T).tolist()
    x.append(list(sup)+[0])

    x = np.asarray(x).T

    df = pd.DataFrame(x)
    df.columns = ['C'+str(i) for i in lr]+['Supply']
    df.index = ['   R'+str(i) for i in lc]+['   Demand']

    if prin:
        print(df,'\n')
    else:
        return df

print('\nMEMBUAT DATA RANDOM'); line()
x = int(input("Input Banyak Baris: "))
y = int(input("Input Banyak Kolom: "))

lc = np.arange(x)+1
lr = np.arange(y)+1

while True:
    sup = [np.random.randint(20,100) for i in range(x)]
    dem = [np.random.randint(20,100) for i in range(y)]
    if sum(sup) == sum(dem):
        break

fsup = []
for i in sup:
    dif1 = np.random.randint(2,10)
    dif2 = np.random.randint(2,6)
    m = i^2
    n = m+dif1
    a = n+dif2
    b = a+dif1
    fsup.append('{}'.format([m,n,a,b]))

fdem = []
for i in dem:
    dif1 = np.random.randint(2,10)
    dif2 = np.random.randint(2,6)
    m = i^2
    n = m+dif1
    a = n+dif2
    b = a+dif1
    fdem.append('{}'.format([m,n,a,b]))

writer = pd.ExcelWriter('data random.xlsx')
while True:
    print(''); line(); print('MEMBUAT DATA  RANDOM'); line()
        
    data = []
    rank = []
    for i in range(x):
        temp1,temp2 = [],[]
        for j in range(y):
            dif1 = np.random.randint(2,10)
            dif2 = np.random.randint(2,6)
            
            m = np.random.randint(50)
            n = m+dif1
            a = n+dif2
            b = a+dif1
            
            res = np.int(np.ceil(integrate((n-m),m,b,(b-a))*0.5))
            
            temp1.append([m,n,a,b])
            temp2.append(res)
        
        data.append(temp1)
        rank.append(temp2)

    data = np.asarray(data)
    rank = np.asarray(rank)

    print('\n>> DATA FUZZY:')
    dataframe(data,fsup,fdem,lr,lc,True)

    print('>> RANK DATA:')
    dataframe(rank,sup,dem,lr,lc,True)

    print('Simpan Data?')
    print('0. Buat Ulang Data')
    print('1. Simpan Data')

    ulang = ' '
    while ulang not in '01':
        ulang = input('input opsi: ')

    if ulang == '1':
        df1 = dataframe(data,fsup,fdem,lr,lc,False)
        df2 = dataframe(rank,sup,dem,lr,lc,False)
        df1.to_excel(writer,sheet_name='FUZZY')
        df2.to_excel(writer,sheet_name='RANK')
        writer.close()
        break

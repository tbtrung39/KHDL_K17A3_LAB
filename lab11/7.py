with open('lab11/m_nums.txt','r') as f:
    m=list(map(int,f.readline().split()))
with open('lab11/n_num.txt','r') as f:
    n=list(map(int,f.readline().split()))
a=[i for i in m if i in n]

with open('lab11/so_chung.txt','w') as f:
    f.write(' '.join(map(str,a)))
with open('lab11/so_chung.txt','r') as f:
    a=f.read()
    print('các số chung:',a)
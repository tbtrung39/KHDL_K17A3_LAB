n = int(input("Nhap vao so lan tung: "))
n_omega= 6**n
n_bien_co_doi = 5**n
P_n_bien_co_doi = n_bien_co_doi/n_omega
P_n = 1- P_n_bien_co_doi
print(P_n**3)
def tinh_xac_suat_it_nhat_mot_lan_sau_n_lan_tung(n,so_mat):
    xac_suat_khong_co_sau=((so_mat-1)/so_mat)**n
    xac_suat_it_nhat_mot_lan_sau_n_lan_tung=1-xac_suat_khong_co_sau
    return round(xac_suat_it_nhat_mot_lan_sau_n_lan_tung,2)
so_lan_tung=int(input("Nhap so lan tung xuc xac(n): "))
so_mat_xuc_xac=6
ket_qua=tinh_xac_suat_it_nhat_mot_lan_sau_n_lan_tung(so_lan_tung, so_mat_xuc_xac)
print(f"Xac suat co it nhat 1 lan ca 3 deu ra 6 sau {so_lan_tung} lan tung: {ket_qua} ") 
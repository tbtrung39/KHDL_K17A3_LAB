def read_data(file_name):
    data = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split()
            data[int(parts[0])] = ' '.join(parts[1:])
    return data

def merge_data(sbd_ph_file, sbd_ten_file, phieu_diem_file):
    sbd_ph_data = read_data(sbd_ph_file)
    sbd_ten_data = read_data(sbd_ten_file)
    phieu_diem_data = read_data(phieu_diem_file)

    result = {}
    for sbd, ph in sbd_ph_data.items():
        if sbd in sbd_ten_data and ph in phieu_diem_data:
            result[sbd] = (sbd_ten_data[sbd], phieu_diem_data[ph])

    return result

def write_result(result, output_file):
    with open(output_file, 'w') as file:
        for sbd, (name, score) in sorted(result.items(), key=lambda x: x[1][1], reverse=True):
            file.write(f"{sbd} {name} {score}\n")

sbd_ph_file = 'Sbd_Ph.dat'
sbd_ten_file = 'SBD_Ten.txt'
phieu_diem_file = 'PhieuDiem.txt'
output_file = 'Ketqua.txt'

merged_data = merge_data(sbd_ph_file, sbd_ten_file, phieu_diem_file)
write_result(merged_data, output_file)
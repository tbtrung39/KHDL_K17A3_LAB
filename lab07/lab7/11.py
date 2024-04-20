def ds_sv(n, a, b, c, sv_cpp, sv_java, sv_python):
    tat_ca_sv = set(range(1, n+1))

    cpp_set = set(sv_cpp)
    java_set = set(sv_java)
    python_set = set(sv_python)

    mot_ngon_ngu = tat_ca_sv - (cpp_set.union(java_set, python_set))

    hai_ngon_ngu = (cpp_set & java_set) | (java_set & python_set) | (cpp_set & python_set)

    ba_ngon_ngu = cpp_set & java_set & python_set

    return mot_ngon_ngu, hai_ngon_ngu, ba_ngon_ngu

if __name__ == '__main__':
    n = int(input("Nhập số lượng sinh viên: "))
    a = int(input("Nhập số lượng sinh viên tham gia thi C++: "))
    sv_cpp = list(map(int, input("Nhập danh sách sinh viên tham gia thi C++: ").split()))
    b = int(input("Nhập số lượng sinh viên tham gia thi Java: "))
    sv_java = list(map(int, input("Nhập danh sách sinh viên tham gia thi Java: ").split()))
    c = int(input("Nhập số lượng sinh viên tham gia thi Python: "))
    sv_python = list(map(int, input("Nhập danh sách sinh viên tham gia thi Python: ").split()))

    print(ds_sv(n, a, b, c, sv_cpp, sv_java, sv_python))

import streamlit as st
import matplotlib.pyplot as plt
import time
import sys

# Tingkatkan batas rekursi
sys.setrecursionlimit(100000000)

# Fungsi iteratif untuk menjumlahkan bilangan ganjil dari 1 hingga n
def sum_odd_iterative(n):
    result = 0
    for i in range(1, n + 1, 2):
        result += i
    return result

# Fungsi rekursif dengan teknik Tail Recursion
def sum_odd_recursive_tail(n, acc=0):
    if n <= 0:
        return acc
    if n % 2 == 0:
        return sum_odd_recursive_tail(n - 1, acc)
    return sum_odd_recursive_tail(n - 2, acc + n)

# Fungsi pembungkus agar lebih mudah dipanggil
def sum_odd_recursive(n):
    return sum_odd_recursive_tail(n, 0)

# Header aplikasi
st.title("Perbandingan Waktu Eksekusi Algoritma Iteratif dan Rekursif")
st.markdown("""
Website ini membandingkan **waktu eksekusi** algoritma iteratif dan rekursif untuk menghitung 
jumlah bilangan ganjil dari 1 hingga \( n \), di berbagai nilai \( n \).
""")

# Input dari user
max_n = st.number_input("Masukkan nilai maksimum n:", min_value=10, value=10, step=10)
interval = st.number_input("Masukkan interval perhitungan:", min_value=10, value=50, step=10)

# Tombol untuk memulai perhitungan
if st.button("Hitung dan Tampilkan Grafik"):
    # List untuk menyimpan data
    n_values = list(range(10, max_n + 1, interval))  # Nilai n dengan step sesuai interval
    iterative_times = []
    recursive_times = []
    iterative_sums = []
    recursive_sums = []

    # Setup grafik
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title("Perbandingan Waktu Eksekusi Iteratif vs Rekursif")
    ax.set_xlabel("Nilai n")
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.grid(True)

    # Placeholder untuk grafik di Streamlit
    plot_placeholder = st.empty()

    # Menghitung waktu eksekusi untuk setiap nilai n
    for n in n_values:
        # Iteratif
        start_time = time.time()
        iterative_sum = sum_odd_iterative(n)
        iterative_time = time.time() - start_time
        iterative_times.append(round(iterative_time, 6))  # Membulatkan waktu hingga 6 desimal
        iterative_sums.append(iterative_sum)

        # Rekursif
        start_time = time.time()
        recursive_sum = sum_odd_recursive(n)
        recursive_time = time.time() - start_time
        recursive_times.append(round(recursive_time, 6))  # Membulatkan waktu hingga 6 desimal
        recursive_sums.append(recursive_sum)

        # Update grafik
        ax.plot(n_values[:len(iterative_times)], iterative_times, label="Iteratif", color="b", linestyle="-", linewidth=2, marker='o')
        ax.plot(n_values[:len(recursive_times)], recursive_times, label="Rekursif", color="r", linestyle="-", linewidth=2, marker='o')

        # Menampilkan grafik sementara di Streamlit
        plot_placeholder.pyplot(fig)

    # Menampilkan hasil akhir perhitungan SUM
    st.write(f"### Hasil Akhir")
    st.write(f"Iteratif SUM (n = {max_n}) = {iterative_sums[-1]}")
    st.write(f"Rekursif SUM (n = {max_n}) = {recursive_sums[-1]}")
    st.write(f"Waktu Iteratif: {iterative_times[-1]} detik")
    st.write(f"Waktu Rekursif: {recursive_times[-1]} detik")

    # Menambahkan legenda hanya sekali
    ax.legend()

    # Kesimpulan
    st.write("### Kesimpulan")
    st.write("Grafik di atas menunjukkan perbandingan waktu eksekusi untuk berbagai nilai \( n \):")
    st.write("- Garis **biru** mewakili **algoritma iteratif**.")
    st.write("- Garis **merah** mewakili **algoritma rekursif**.")
    st.write("Perhatikan bahwa untuk nilai \( n \) besar, algoritma rekursif bisa memakan waktu lebih lama karena overhead pemanggilan fungsi rekursif.")

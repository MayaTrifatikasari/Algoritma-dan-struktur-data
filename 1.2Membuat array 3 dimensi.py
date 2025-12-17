import tkinter as tk

# Membuat array 3 dimensi
array_3d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

# Fungsi untuk menampilkan isi array
def tampilkan_array():
    text.delete("1.0", tk.END)
    for i in range(len(array_3d)):
        for j in range(len(array_3d[i])):
            for k in range(len(array_3d[i][j])):
                text.insert(tk.END, f"array[{i}][{j}][{k}] = {array_3d[i][j][k]}\n")

# Membuat window
root = tk.Tk()
root.title("Array 3 Dimensi - Tkinter")

# Tombol
btn = tk.Button(root, text="Tampilkan Array 3D", command=tampilkan_array)
btn.pack(pady=5)

# Textbox untuk output
text = tk.Text(root, height=8, width=30)
text.pack(pady=5)

root.mainloop()

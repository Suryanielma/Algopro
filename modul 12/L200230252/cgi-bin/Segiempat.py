def hitung_luas(s):
    "fungsi menghitung luas dari segiempat"
    luas = int(s * s)
    return luas

nama = "Segiempat"
dimensi = "2D"
rumus = "(s * s)"
sisi = "Sisi : 10"
hasil = hitung_luas(10)

html=f"""
<!DOCTYPE html>

<html>
<head><title>Bangun Geometri</title></head>
<body>
<h3>Bangun Geometri</h3>

<p>Nama Bangun : {nama}</p>
<p>Dimensi : {dimensi}</p>
<p>Rumus Luas : {rumus}</p>
<p>{sisi}cm</p>
<p>Luas : {hasil}</p>
</body>
</html>"""

print(html)
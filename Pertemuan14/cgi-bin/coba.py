#!/usr/bin/env python3
import datetime

def hitung_umur(lahir):
    "menentukan umur sejak tanggal lahir tertentu"
    hari_ini = datetime.date.today()
    tahun = hari_ini.year - lahir.year
    bulan = hari_ini.month - lahir.month
    if bulan < 0:
        tahun -= 1
        bulan += 12
    return tahun, bulan

lahir = datetime.date(2005, 2, 10) # Tanggal lahir 10 Februari 2005
thn, bln = hitung_umur(lahir)
nama = "Elma"  
htm = f"""<!DOCTYPE html>

<html>
<head>
<title>Server dengan konten dinamis</title>
</head>
<body>
<p>{nama} lahir pada tanggal {lahir}.</p>
<p>Hari ini adalah tanggal {datetime.date.today()}.</p>
<p>Karena itu Elma berumur {thn} tahun {bln} bulan.</p>
<p>Terima kasih</p>
</body>
</html>"""

print(htm)
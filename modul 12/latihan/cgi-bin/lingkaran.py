#!/usr/bin/env phyton3
print("<!DOCTYPE html>\n")
print("""<html><head><title>Akses melalui CHIHTTPServer</title></head><body><h3>Lingkaran</h3>""")
print("""<canvas id="myCanvas" width="150" height="150" style="border:1px solid"#d3d3d3">Browser anda tidak mendukung tag canvas.</canvas>""")
jejari = 10
import math ; from math import pi
area = pi*jejari**2
jejari_px = 5*jejari
print("<p>Lingkaran berjejeari {0} cm".format(jejari))
print("mempunyai luas {0} cm2".format(area))
print("""<script>var c= document.getElementbyId("myCanvas)
var ctx = c.getContext("2d");
ctx.beginPath();
ctx.arc(100, 75, {0}, 0, 2*math.pi)
ctx.fillStyle="blue";
ctx.fill();
ctx.stroke();
</script>
</body></html>""".format(jejari_px)


#!/usr/bin/env python3
print("<!DOCTYPE html>/n")
print("""<html>
      <head><title>Akses melalui CGI</title></head>
      <body>
            <h3>Selamat datang di CGI</h3>""")

print("""<p>Anda mengakses informasi ini melalui layanan CGI dengan CGIHTTPRequestHandler.</p>""")
print("<p>informasi tentang <a href='umur.py'>umur</a> dan <a href='lingkaran.py'>lingkaran</a></p>")
print("</body></html>")
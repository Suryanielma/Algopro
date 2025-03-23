# import urllib.request

# response = urllib.request.urlopen("https://www.ums.ac.id")
# html = response.read()
# print(html)



# import urllib.request

# response = urllib.request.urlopen("https://www.ums.ac.id")
# html = response.read()
# htm = str(html)  # byte dikonversi menjadi string
# awal = htm.find("<title>")
# akhir = htm.find("</title>")
# judul = htm[awal:akhir+8]
# print(judul)



# import html

# judul = '<title>UMS &#8211; Wacana Keilmuan dan Keislaman</title>'
# judul_ok = html.unescape(judul)
# print(judul_ok



import requests
response = requests.get("https://republika.co.id/")
htm = str(response.content)
kursor = 0
tag_awal = 0
while tag_awal != -1:
    tag_awal = htm.find('<img', kursor)
    tag_akhir = htm.find('>', tag_awal + 1)
    kursor = tag_akhir + 1
    print(htm[tag_awal:kursor])
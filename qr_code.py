import qrcode as qr

img = qr.make("https://zoro.to/watch/one-piece-100?ep=2142")
img.save("random_link.png")

#__________________________________________________________

# import segno as sg

# qrcode = sg.make("hello")
# qrcode = sg.make_qr("welcome")
# # qrcode.save('click_here.png',scale = 10,)#border = 100)
# qrcode.save('click_here.png',dark = "red",light = "white",scale = 100, border = 1)
# #_______________________________________________________________--

# from segno import helpers
# qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')
# qrcode.designator
# '3-M'
# qrcode.save('wifi-access.png', scale=10)
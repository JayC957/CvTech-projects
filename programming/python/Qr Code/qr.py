

import qrcode

features = qrcode.QR(version=1, box_size=40, border=3)
features.add_data('https://www.linkedin.com/in/aidan-roller-03b2a3279/')
features.make(fit=True)
image = features.make_image(fill_color="black", back_color="white")
image.save('image.png')
import inkyphat
from PIL import ImageFont, Image

font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 19)
font2 = ImageFont.truetype(inkyphat.fonts.FredokaOne, 20)
font3 = ImageFont.truetype(inkyphat.fonts.FredokaOne, 17)

message = "Wednesday 6th Feb"
w, h = font.getsize(message)
x = (inkyphat.WIDTH / 2) - (w / 2)
y = (inkyphat.HEIGHT / 6) - (h / 2)

message2 = "Organise Cupboards"
w, h = font.getsize(message2)
x2 = (inkyphat.WIDTH / 2) - (w / 2)
y2 = (inkyphat.HEIGHT / 2) - (h / 2)

message3 = "Rain (H26C, L-1C)"
w, h = font.getsize(message3)
x3 = (inkyphat.WIDTH / 2) - (w / 2)
y3 = (inkyphat.HEIGHT - 15) - (h / 2)

inkyphat.text((x, y), message, inkyphat.BLACK, font)
inkyphat.text((x2, y2), message2, inkyphat.RED, font2)
inkyphat.text((x3, y3), message3, inkyphat.BLACK, font3)
inkyphat.show()

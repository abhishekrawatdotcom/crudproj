import random
import qrcode


x = random.randint(100000,999999)
im = qrcode.make('otp'+ str(x))

im.show()

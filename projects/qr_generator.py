import pyqrcode
from pyqrcode import QRCode 

s = "https://www.amazon.in/s?k=rich+dad+poor+dad+english&i=stripbooks&crid=1PUOFQDE5OMJJ&sprefix=rich+dad+poor+%2Cstripbooks%2C382&ref=nb_sb_ss_ts-doa-p_1_14"

url = pyqrcode.create(s)

url.svg("booklist.svg", scale = 8)


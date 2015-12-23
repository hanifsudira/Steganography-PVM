# Final Project Jaringan Multimedia
# Steganography using pixel value modification
# Author : Usaid, Ghulam, Hanif

from PIL import Image
import sys

class PictureVM:
	def __init__(self,(filename,message)):
		self.filename = filename
		self.message = message

	def toascii(self,n):
		asci = [ord(c) for c in n]
		return asci
	
	def tobase3(self,n):
		a = []
		while n>=1:
			sisa = n % 3
			n /= 3
			a.append(sisa)
		if len(a) == 4:
			a.append(0)
		a.reverse()
		return a

	def pvm(self): 
		#load image
		im = Image.open(self.filename)
		widht,height = im.size
		pix = im.load()
		
		#process convert to base3 
		asci = self.toascii(self.message)
		b = []
		for x in asci:
			b.append(self.tobase3(x))
		data = []
		for x in b:
			for y in range(len(x)):
				data.append(x[y])

		#process to hiding data
		count  = 0
		flag = False
		for x in range(widht):
			for y in range(height):
				temp = []
				for z in range(3):
					if count == len(data):
						flag = True
						break
					else:
						if pix[x,y][z] > 250:
							pix[x,y][z] = 250
						pixels = pix[x,y][z]
						f = pixels % 3
						d = data[count]
						if f == d :
							temp.append(pixels)
						elif f-d ==-2:
							temp.append(pixels - 1)
						elif f < d or f-d == 2:
							temp.append(pixels + 1)
						elif f > d:
							temp.append(pixels - 1)
					count += 1
				if flag:
					break
				pix[x,y] = tuple(temp)

		im.save('coba.png')

def main():
	filename = str(sys.argv[1])
	message = str(sys.argv[2])
	message = message.replace("%20"," ")
	lenmessage = str(len(message))+" "
	message = lenmessage+message
	lenmessage = str(len(message))
	newmessage = lenmessage+" "
	for x in message.split()[1:]:
		newmessage +=x+" " 
	steg = PictureVM((filename,newmessage))
	steg.pvm()

if __name__ == '__main__':
	main()

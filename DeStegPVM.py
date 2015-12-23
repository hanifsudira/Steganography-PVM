# Final Project Jaringan Multimedia
# Steganography using pixel value modification
# Author : Usaid, Ghulam, Hanif

from PIL import Image
import sys

class PictureVM:
	def __init__(self,filename):
		self.filename = filename
	
	def tochar(self,n):
		char = [chr(c) for c in n]
		return char

	def revbase3(self,n):
		a = []
		itr=4
		hasil=0
		for x in range(len(n)):
			temp=pow(3,itr)*n[x]
			itr-=1
			hasil+=temp
			if itr==-1:
				a.append(hasil)
				temp=0
				itr=4
				hasil=0
		return a

	def findstop(self):
		im = Image.open(self.filename)
		pix = im.load()
		stop = 10 * 5
		data = []
		count = 0
		flag = False
		for x in range(im.size[0]):
			for y in range(im.size[1]):
				for z in range(3):
					if count == stop:
						flag = True
						break
					test = pix[x,y][z] % 3
					data.append(test)
					count+=1
				if flag:
					break

		decode=self.revbase3(data)
		char=self.tochar(decode)
		out=[]
		buff=[]
		for x in char:
			buff.append(x)
		else:
			if buff:
				out.append(''.join(buff))
		return out[0]

	def pvm(self):
		im = Image.open(self.filename)
		pix = im.load()
		temp = str(self.findstop()).split()[0]
		try:
			stop =  int(temp) * 5
			data = []
			count = 0
			flag = False
			for x in range(im.size[0]):
				for y in range(im.size[1]):
					for z in range(3):
						if count == stop:
							flag = True
							break
						test = pix[x,y][z] % 3
						data.append(test)
						count+=1
					if flag:
						break

			decode=self.revbase3(data)
			char=self.tochar(decode)
			out=[]
			buff=[]
			for x in char:
				buff.append(x)
			else:
				if buff:
					out.append(''.join(buff))
			temp+=" "
			print out[0].split(temp)[1]
		except Exception,e:
			print "Tidak ada pesan rahasia didalam gambar"


def main():
	filename = str(sys.argv[1])
	steg = PictureVM(filename)
	steg.pvm()

if __name__ == '__main__':
	main()
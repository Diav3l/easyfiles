from easyfiles import easyfile
#import easyfiles
def main():
	
	f = easyfile("output")
	print(f.extract("content here ","int"))
	f.fill("content here ",-500,500,1000,50)
	print(f.extract("content here ","int"))
	#f.print()
	#print(f.filter("this"))
	print(f.__dict__)

if __name__ == '__main__':
	#while True:
	main()
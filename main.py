from easyfiles import easyfile
#import easyfiles
def main():
	
	f = easyfile("output")
	f.append("this")
	f.print()
	print(f.filter("this"))
	
if __name__ == '__main__':
	#while True:
	main()
class easyfile:
	def __init__(self,file:str):
		if not '.' in file:
			file+='.txt'
		self.file = file
		try:
			open(self.file,'x')
		except FileExistsError:
			pass
		
	"""creates or appends fliles, intended to be user friendly"""
	def append(self, content):
			with open(self.file, 'a') as f:
				f.write(f"{content}\n")
				
	"""prints an entire file"""		
	def print(self):
		with open(self.file) as f:
			for line in f:
				line = line.rstrip()
				print(line)
	
	"""returns array full of requested lines"""
	def filter (self, content):
		lines=[]
		with open(self.file,'r') as f:
			for line in f:
				if not content in line:
					continue
				lines.append(line.rstrip())
		return(lines)

	"""fills the file with random numbers that are proceded by designated content"""
	def fill(self,content='',lower=0,upper=500,lines=100,seed=0):
		import random
		if seed:
			random.seed(seed)
		with open(self.file,"a") as f:
			i=0
			while i<lines:
				f.write(f"{content}{random.randrange(lower,upper)}\n")
				i+=1

	"""retruns array full of everything on a line after the specified content, can specify return datatype"""
	def extract(self, content:str,datatype='str'):
		lines=[]
		with open(self.file,'r') as f:
			for line in f:
				if not content in line:
					continue
					
				if datatype =='int' or datatype=='integer':
					lines.append(int(line[len(content):].rstrip()))
				elif datatype =='float':
					lines.append(float(line[len(content):].rstrip()))
				else:
					lines.append(line[len(content):].rstrip())
					
		return(lines)
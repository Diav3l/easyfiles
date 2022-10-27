class easyfile:
	def __init__(self,file:str):
		if not '.' in file:
			file+='.txt'
		self.file = file
		try:
			with open(self.file) as f:
				pass
		except (FileNotFoundError):
			with open(self.file,'w') as f:
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
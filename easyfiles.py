"""creates or appends fliles, intended to be user friendly"""
def easyapp(file: str, content):
	if not '.' in file:
		file+='.txt'
	try:
		with open(file, 'a') as f:
			f.write(f"{content}\n")
	except(FileNotFoundError):
		with open(file,'w') as f:
			f.write(f"{content}\n")
"""prints an entire file"""		
def easyprint(file: str):
	if not '.' in file:
		file+='.txt'
	try:
		with open(file) as f:
			for line in f:
				line = line.rstrip()
				print(line)
	except(FileNotFoundError):
		return(f"{file} does not exist")
	return
"""returns array full of requested lines"""
def easyfilter (file: str, content):
	lines=[]
	if not '.' in file:
		file+='.txt'
	try:
		with open(file,'r') as f:
			for line in f:
				if not content in line:
					continue
				lines.append(line.rstrip())
		return(lines)
	except(FileNotFoundError):
		return(f"{file} does not exist")
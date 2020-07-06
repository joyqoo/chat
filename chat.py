# 讀取檔案
def read_file(fileName):
	lines = []
	with open(fileName,'r' ,encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換TXT檔格式
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person ='Tom'
			continue
		new.append(person+': '+line)		
	print(new)	
	return new 

# 寫出新檔案格式
def write_file(fileName ,lines):
	with open(fileName,'w') as f:
		for line in lines:
			f.write(line+'\n')
# 主要執行
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt' ,lines)

main()
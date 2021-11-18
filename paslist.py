import os

f = open('chkfilepas.txt', 'w')

def fild_all_files(directory):
	for root, dirs, files in os.walk(directory):
		#yield root
		for file in files:
			if file.endswith('.pas'):
				yield os.path.join(root, file)
			if file.endswith('.inc'):
				yield os.path.join(root, file)
			if file.endswith('.dpr'):
				yield os.path.join(root, file)


def chkfilecsvout(f, pathnamedir):
	for file in fild_all_files(pathnamedir):
		#print(file)
		str = os.path.dirname(file)+','+os.path.basename(file)+'\n'
		f.write(str)

chkfilecsvout(f, "directory")

f.close()
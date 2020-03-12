import os

with open('largefile.txt', 'r', encoding='utf-8') as f1:
	lf_list = [line.strip() for line in f1.readlines()]

string1 = '/root/Anitama-Backup/'
string2 = 'large_files/'
	
for i in range(0, len(lf_list)):
	s1 = lf_list[i]
	before = string1 + s1[2:]
	after = string1 + string2 + s1[2:]
	
	m1 = os.path.dirname(after)
	
	if os.path.exists(m1):
		pass
	else:
		os.makedirs(m1)
	
	os.rename(before, after)
	#os.rename(after, before)
	
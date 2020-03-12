import subprocess
import datetime
import os


with open('new-CDN-folder.txt', 'r', encoding='utf-8') as f1:
	folder_list = [line.strip() for line in f1.readlines()]

folder_section = 25

block1 = 0
block2 = 1

range1 = block1 * folder_section
range2 = block2 * folder_section

while range2 <= len(folder_list):
	
	try:
		for k in range(range1, range2):
			media_folder = 'cdn/' + folder_list[k] + '/*'

			subprocess.call(["git", "add", media_folder])

		subprocess.call(["git", "commit", "-m", "Commit block " + str(block2)])
		subprocess.call(["git", "push", "origin", "master"])
		
		print('Success: Block ' + str(block2))
		
	except Exception as error_info:

		print('Reason: ', error_info)
		
		with open('error_commit_block.txt', 'a', encoding='utf-8') as f4:
			f4.write('Fail: Block: ' + str(block2) + error_info + '\n')
			
	block1 = block1 + 1
	block2 = block2 + 1
	range1 = block1 * folder_section
	range2 = block2 * folder_section
	

try:
	for p in range(range1, len(folder_list)):
		media_folder = 'cdn/' + folder_list[p] + '/*'

		subprocess.call(["git", "add", media_folder])

	subprocess.call(["git", "commit", "-m", "Commit block " + str(block2)])
	subprocess.call(["git", "push", "origin", "master"])
	
	print('Success: Block ' + str(block2))
	
except Exception as error_info:

	print('Reason: ', error_info)
	
	with open('error_commit_block.txt', 'a', encoding='utf-8') as f4:
		f4.write('Fail: Block: ' + str(block2) + error_info + '\n')

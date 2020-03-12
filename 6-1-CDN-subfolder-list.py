import os 

root='/root/Anitama-Backup/cdn/'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]

with open('CDN-subfolder-list.txt', 'w+', encoding='utf-8') as f4:
	f4.write('\n'.join(dirlist) + '\n')
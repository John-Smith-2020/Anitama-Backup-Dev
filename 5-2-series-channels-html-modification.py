import re
import os

######
from glob import glob
channel_folder = r'./series_o'
html_files = [y for x in os.walk(channel_folder) for y in glob(os.path.join(x[0], '*.html'))]
######


# channel_folder_new = r'./channel'
# if os.path.exists(channel_folder_new):
	# pass
# else:
	# os.makedirs(channel_folder_new)
	
	
counter = 1

o1 = 'http://cdn.animetamashi.cn/'
r1 = 'https://github.com/John-Smith-2020/Anitama-CDN-Backup/raw/master/cdn/'
#r1 = '/Anitama-Backup/cdn/'
o2 = '/static/'
r2 = '/Anitama-Backup/static/'
o3 = '/article/'
r3 = '/Anitama-Backup/article/'
o4 = '</head>'
r4 = '<link rel="stylesheet" type="text/css" href="/Anitama-Backup/static/index/style/require/comment.css"></head>'

o5 = '<div class="list-comment" id="comment"></div>'
rex5 = r"html\":[\S\s]+totalCount"

o6 = '\\"'
r6 = '"'

r7 = '<div class="list-comment" id="comment"><div class="area-pager"></div><div class="inner"> '
r7_2 = ' </div><div class="area-pager"></div></div>'

o8 = '/series/'
r8 = '/Anitama-Backup/series/'

o9 = '/channel/'
r9 = '/Anitama-Backup/channel/'

while counter <= len(html_files):

	file_name = html_files[counter - 1]
	
	try: 	
		with open(file_name, 'r', encoding='utf-8') as f2:
			html = f2.read()
			
		html = html.replace(o1, r1)
		html = html.replace(o2, r2)
		html = html.replace(o3, r3)
		html = html.replace(o4, r4)
		html = html.replace(o8, r8)
		html = html.replace(o9, r9)
		
		# c_file_path = r'./comment/%s.json' % (n1[-16:])
		
		# if os.path.exists(c_file_path):
			
			# with open(c_file_path, 'r', encoding='utf-8') as f3:
				# comment_json = f3.read()
			
			# comment_json = comment_json.replace(o6, r6)
			
			# comment_o = re.search(rex5, comment_json).group()
			# comment_div = comment_o[7:-13]
			# full_div = r7 + comment_div + r7_2
			
			# html = html.replace(o5, full_div)
			
		with open(file_name, 'w+', encoding='utf-8') as f4:
			f4.write(html)
		
	except Exception as error_info:

		print('Reason: ', error_info)
		
		with open('error_html_channel_file.txt', 'a', encoding='utf-8') as f5:
			f5.write(''.join(file_name) + '\n')
	
	print('Finished: Page ' + str(counter))
	counter = counter + 1		
	
			
			

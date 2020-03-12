import os

from glob import glob
channel_folder = r'./channel'
html_files = [y for x in os.walk(channel_folder) for y in glob(os.path.join(x[0], '*.html'))]


for k in range(0, len(html_files)):

	filename = os.path.basename(html_files[k])
	
	string1 = '1.html'
	string2 = 'index.html'

	if filename == string1:
	
		dirname = os.path.dirname(html_files[k])
		
		with open(html_files[k], 'r', encoding='utf-8') as g1:
			html = g1.read()
	
		with open('%s/%s' % (dirname, string2), 'w+', encoding='utf-8') as g2:
			g2.write(html)
		
	print('Finished: Page ' + str(k+1))


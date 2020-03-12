import os
import re

from glob import glob
channel_folder = r'./series'
html_files = [y for x in os.walk(channel_folder) for y in glob(os.path.join(x[0], '*.html'))]

rex1 = r"data-tid=\"\d+"
rex2 = r"data-title=\".+?\""

string1 = '1.html'
string2 = 'index.html'

div1 = '$(document).ready(function(){$("#b'
div2 = '").click(function(){$("#Tab-Content").load("https://john-smith-2020.github.io/Anitama-Backup/series/'
div3 = '/");});});'

div4 = '<button id="b'
div5 = '">'
div6 = '</button>'


for k in range(0, len(html_files)):

	filename = os.path.basename(html_files[k])
	
	if filename == string1:
	
		#dirname = os.path.dirname(html_files[k])
		
		with open(html_files[k], 'r', encoding='utf-8') as g1:
			html = g1.read()
			
		m1 = re.search(rex1, html).group()
		button_id = re.search(r"\d+", m1).group()
		
		m2 = re.search(rex2, html).group()
		button_text = m2[12:-1]
		
		content_js = div1 + button_id + div2 + button_id + div3 
		button_div = div4 + button_id + div5 + button_text + div6 
	
		with open('series_btn_name.txt', 'a', encoding='utf-8') as g2:
			g2.write(button_div + '\n')
			
		with open('series_js_content.txt', 'a', encoding='utf-8') as g3:
			g3.write(content_js + '\n')
		
	print('Finished: Page ' + str(k+1))


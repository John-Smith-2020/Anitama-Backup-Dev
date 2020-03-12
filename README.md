# Anitama-Backup-Dev
Resources for Project Anitama-Backup 

1. Raw Data
**XXX_o.7z * 3**: Original html from Anitama.cn (No _o 7z were the ones published on Github Page)
**static.7z**: js/css files used by Anitama. Also includes 1 custom js and 1 custom css used by index.html. 
**index.html**: a navigation page that lists all the channels and series articles. 
**comment.7z**: The comments under articles, stored in json format. Note that the json has been merged together for multi-page comments. 
 
2. Python script
**3-2-optional-move-large-files.py**
<Github has a 100M file size limit, this script moves the large video files to another folder.>
<Use the command below to generate the large file list>
< find . -type f -size +100M > large_files_100M.txt >
**5-1-html-modification.py**
<Modify the original html to enable loading js/css and media files locally or under another domain. (like the Github Page)>
<The comments stored in json format originally has also been extracted and inserted into the main html.>
**5-2-series-channels-html-modification.py**
<Same functions as above, but for channel and series pages. Note it directly modifies the original files>
**5-3-optional-add-sub-index.py**
<To improve Github Page viewing experience, add index.html under each channel/series folder, so that the user does not need to type /1.html when jumping from another page.>
**6-1-CDN-subfolder-list.py**
<Create a folder list for media files folder (/cdn)>
**6-2-github-push-CDN.py**
<Although the repo size limit is 100GB, Github does not accept single commit larger than 2GB (according to one reply in their support forum, and I also tested). Therefore it's nessceary to split the commit process when uploading all the media files in /cdn folder. The previous generated folder list will serve this time. The basic idea is uploading 25 folders each commit. I suggest using non-mainland-China VPS/Dedicated server with reliable connection (no GFW) to run this script.>
**7-index-page-generator.py**
<Generate buttons' html and the corresponding Javascript used by custom index.html. ("Click to load" function)>

3. Logs:
The following python code will remove duplicate rows from text.
```
with open('article_list_fs.txt', 'r', encoding='utf-8') as d1:
	url_list = [line.strip() for line in d1.readlines()]
	
url_list_no_dupe = list(dict.fromkeys(url_list))

url_list_no_dupe.reverse()

url_list_str = "\n".join(url_list_no_dupe)

with open('article_list_fs_no_dupe.txt', 'w+') as d2:
	d2.write(url_list_str + '\n')
```

I used **article_list_no_dupe.txt** to collect articles, **media_file_list_fa_no_dupe.txt** and **media_file_list_Accp.txt** to collect media files. The article list was generated from scanning each "channel". The fa means "from article", and fs means "from series". Accp stands for accompaniment. (The files missed in the initial download.)

4. Migrate the website
Assuming you still want to host the website via Github Page, you need to fork (or git clone) two repos: 
https://github.com/John-Smith-2020/Anitama-Backup
https://github.com/John-Smith-2020/Anitama-CDN-Backup
Then modify the html in Anitama-Backup, replace the previous media file links with the new links from your own repo. If you have Git LFS enabled, it should be feasible to upload the remaining 56 videos that exceed 100M from [Google Drive](https://drive.google.com/drive/folders/1Ong9-Ad5cAhhYa3-W1hXZ643TfARb-dN?usp=sharing) and make the entire Anitama backup self-sustaining on Github. 
Currently the search function is achieved by Google Custom Search, which takes long time to crawl all the pages under the article folder, even after submitting the sitemap to the GCS console. Adding a custom search function that can run under Github Jekyll environment will be a significant improvement to this project.  

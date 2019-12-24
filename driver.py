import comment_downloader as CD
import fancySentiment as FS
# import sys
# sys.path.append('E:/爬取utube评论/YouTube-Sentiment-Analysis/CommentSentiment/')
import sentimentYouTube as SYT
import requests
import json
def main():
	# EXAMPLE videoID = 'tCXGJQYZ9JA'
	# videoId = input("Enter the videoID : ")
	videoId_all = ['FWMIPukvdsQ','QHTnuI9IKBA','LTejJnrzGPM','_jUJrIWp2I4','OrXiXDUQia8','wUJ-57SAE5A','Yx4JnDez1sk','fhkE3e7lT_g','K92fPB3lKCc','xYmyNCzoCFI']
	# Fetch the number of comments   
	# if count = -1, fetch all comments
	# count = int(input("Enter the no. of comment to extract : "))
	count = 2000
	comments = []

	with open('verified_proxies.json', encoding='utf-8') as f:
		# for line in f:
		a = json.load(f)
	# final[a['type']] = a['host']+':'+a['port']

	for videoId in videoId_all:
		requests.adapters.DEFAULT_RETRIES = 20
		s = requests.session()
		flag = 0
		# s.proxies = {"http": "27.152.8.152:9999", "https": "117.57.91.131:24978"}
		s.keep_alive = False
		s.proxies = {a[flag]['type']:str(a[flag]['host'])+':'+str(a[flag]['port'])}
		flag = flag+1

		comments = comments + CD.commentExtract(videoId, count)
	# print(comments)
	with open('data1.txt','w',encoding='utf-8') as f:
		for i in comments:
			f.write(i+'\n')
	SYT.sentiment(comments)
	FS.fancySentiment(comments)



if __name__ == '__main__':
	main()

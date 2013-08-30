'''
My twitter retweet bot, stor the search results in array and retweet them
'''
from random import randint
import time 
import sys
import twitter

api = twitter.Api(consumer_key='xxxxxxxxxxxxxxxxxxxx',
                  consumer_secret='xxxxxxxxxxxxxxxxxxxx',
                  access_token_key='xxxxxxxxxxxxxxxxxxxx',
                  access_token_secret='xxxxxxxxxxxxxxxxxxxx')

# add any terms you want
find = ['arduino','rasberry pi','linux','ubuntu','android','automation','python','robotics','3d printer','open source']

#loop through all
for f in find:
		results = api.GetSearch(f)
		print "\tfound %s for %s" %(len(results),f)
		for statusObj in results:
			try:
				#retweet
				#ignore if contains a mention
				#print 'Posting in reply to @%s: %s' % (statusObj.user.screen_name.encode('ascii', 'replace'), statusObj.text.encode('ascii', 'replace'))
				s = statusObj.text.encode('ascii', 'replace')
				#s.find('$')==-1 # not found
				#s.find('$')!=-1 # found
				if s.find('@') == -1:
					print "NO mention retweeting..."
					print statusObj.id
					api.PostRetweet(statusObj.id)
					delay = randint(120,180)
					print delay
					time.sleep(delay) #prevent account suspension 
					continue
				else:
					print "has a mention" # if a tweet has a mention it will skip it and move to next
				
			except Exception:
				print "Unexpected error:", sys.exc_info()[0:2]

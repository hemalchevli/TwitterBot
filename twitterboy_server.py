
#######################################################################
'''
My twitter retweet bot, stor the search results in array and retweet them
'''
from random import randint
import time 
import sys
import twitter
'''
Wolfram alpha app id 	R9L5RY-KQ29A2846Y
Consumer key 	uNYcuQLQF9O8hzjSRHI2w
Consumer secret 	oE2PCNYSbjFVwQSyNukDVQbh7b5a0hE71MQWIDgg
Access token 	1679781624-a1wv7R4xUN88HaAjszMG49TAYSGC6lX0JZcn09F
Access token secret 	yxCZqypJlP7GfnRsz2Ds8tETES8HLXhPyYCEqFweP38'''

#user _hemalc app phitters
#api = twitter.Api(consumer_key='uNYcuQLQF9O8hzjSRHI2w',
#                  consumer_secret='oE2PCNYSbjFVwQSyNukDVQbh7b5a0hE71MQWIDgg',
#                  access_token_key='1679781624-a1wv7R4xUN88HaAjszMG49TAYSGC6lX0JZcn09F',
#                  access_token_secret='yxCZqypJlP7GfnRsz2Ds8tETES8HLXhPyYCEqFweP38')
                  
                  
'''
User hemalchevli app rettytter
Consumer key 	Ic7RsuNeHsCY6lS5N8pGw
Consumer secret 	RFhU13vFNlZhUFUtRDu1nesZTCdxkOpK94DePJ9AE
Access token 	33941337-tJRqLUzeI7QyyMpgQAwLN5MHAkh51VBGmicEx7PQ
Access token secret 	S4r5EiAjg9MMfILeq5ALp6Lfl58iVW6OSODj6pDag'''
api = twitter.Api(consumer_key='Ic7RsuNeHsCY6lS5N8pGw',
                  consumer_secret='RFhU13vFNlZhUFUtRDu1nesZTCdxkOpK94DePJ9AE',
                  access_token_key='33941337-tJRqLUzeI7QyyMpgQAwLN5MHAkh51VBGmicEx7PQ',
                  access_token_secret='S4r5EiAjg9MMfILeq5ALp6Lfl58iVW6OSODj6pDag')


find = ['arduino','rasberry pi','linux','ubuntu','android','automation','python','robotics','3d printer','open source']
#find = ['arduino']

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
					time.sleep(delay)
					continue
				else:
					print "has a mention"
				
			except Exception:
				print "Unexpected error:", sys.exc_info()[0:2]

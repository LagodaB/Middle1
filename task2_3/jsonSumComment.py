import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', 'comments_42.json'
data = open('comments_42.json', 'rU').read()
test = json.loads(data)
counts = test['comments']
result = sum([count['count'] for count in counts])
print 'Count: {}'.format(len(counts))
print result
#TODO
#Find sum of comments

#print results

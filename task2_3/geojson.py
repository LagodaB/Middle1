import urllib
import json
import sys

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    try:
        address = raw_input('Enter location: ')
    except:
        print "Wrong location"
        break
    
    if len(address) < 1 :
        print "Wrong location"
        break


    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    try: 
	    js = json.loads(str(data))
    except: 
	    js = None
    if 'status' not in js or js['status'] != 'OK':
	    sys.exit("Failure To Retrieve")
    location = js["results"][0]["geometry"]["location"]
    address = [js["results"][0]["address_components"][0]['long_name'], 
               js["results"][0]["address_components"][2]['long_name']]

    print 'lat {} lng {}'.format(location['lat'], location['lng'])
    print '{}, {}'.format(address[0], address[1])
    #TODO
    #Return lat,lng,adress

'''
print 'lat',lat,'lng',lng
print location
'''

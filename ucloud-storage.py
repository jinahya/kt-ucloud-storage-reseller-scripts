import http.client
#import httplib
import math
import sys
import urllib.request

def authenticate(authUrl, authUser, authKey):
    print("authUrl: " + authUrl);
    print("authUer: " + authUser)
    print("authKey: " + authKey)
    connection = http.client.HTTPConnection(authUrl)
    request_headers = {
        "X-Auth-User": authUser,
        "X-Auth-Key" : authKey
    }

    connection.connect()
    connection.putheader("X-Auth-User", authUser)
    connection.putheader("X-Auth-Key", authKey)
    connection.endheader()
    connection.request("GET")

        
    return

def pythagoras(a,b):
    value = math.sqrt(a *a + b*b)
    print(value)
    pythagoras(3,3)

authUrl = sys.argv[1]
authUser = sys.argv[2]
authKey = sys.argv[3]

authenticate(authUrl, authUser, authKey)

import urllib.request as rq
#import urllib.response as rsp
#import json as js


#import Requests
class JobApi:

    """

    """
    
    request = rq.Request(url='https://data.usajobs.gov/api/codelist/occupationalseries',
    headers={},origin_req_host='https://developer.usajobs.gov/Tutorials/Code-List', method='GET')
    
    response = rq.urlopen(request)

    #print(response.read())

    #with open('jobs.txt','wb') as n:
    #    n.write(response.read())

    #with open('jobs.txt') as n:
    #    print(n.read())

    # try to do this with curl and the Request library
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if __name__ == "__main__":
        import sys
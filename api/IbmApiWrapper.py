
import urllib, urllib2

class IbmApiWrapper:

	def __init__(self):
		self.apiKey = '76c11f01-f39f-458a-b402-3e126a5d43b5'
		self.baseUrls = {
			'speech': 'https://api.idolondemand.com/1/api/sync/recognizespeech/v1'
		}

	def executeApiCallWithUrl(self, apiCallType, postUrl):
		url = self.baseUrls[apiCallType] + "?apikey=" + self.apiKey
		data = {
			'apikey':self.apiKey,
			'url': postUrl
		}
		request = urllib2.Request(url, urllib.urlencode(data))
		resp = urllib2.urlopen(request)
		return resp.read()


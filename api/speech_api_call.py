from IbmApiWrapper import IbmApiWrapper

api = IbmApiWrapper()

videoUrl = 'https://www.idolondemand.com/sample-content/videos/hpnext.mp4'
resp = api.executeApiCallWithUrl('speech', videoUrl)
print resp



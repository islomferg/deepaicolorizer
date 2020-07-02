import requests

class Colorizer():

    def __init__(self, token):
        """Init colorizer"""
        token: str
        self.token = token

    def colorizeByFile(self, image):
        """Image file example: open('photo.png', 'rb')"""
        image: 'binare file'
        data = requests.post(
            url='https://api.deepai.org/api/colorizer',
            files={'image': image},
            headers={'api-key': self.token}
        ).json()
        return data['output_url']
    
    def colorizeByImageUrl(self, url):
        """Image url"""
        data = requests.post(
            url='https://api.deepai.org/api/colorizer',
            data={'image': url},
            headers={'api-key': self.token}
        ).json()
        return data['output_url']
    
    def saveImage(self, path, imageUrl):
        """Save output image"""
        path: str
        imageUrl: str
        imageOutput = requests.get(url=imageUrl)
        with open(path, 'wb') as imageFile:
            imageFile.write(imageOutput.content)
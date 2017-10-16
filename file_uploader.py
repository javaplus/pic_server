#import requests
import io


def uploadFile(fileData):
    # create temp file:
    #print("FileDate size=" + fileData.size())
    with io.FileIO('./test.jpg', 'w') as file:
        file.write(fileData)
    #imageFile = open('./test.jpg', 'wb').write(fileData)

    #res = requests.post(url='http://localhost:8080',
     #               data=fileData,
      #              headers={'Content-Type': 'application/octet-stream'})



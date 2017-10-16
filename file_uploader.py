import requests
import io


def uploadFile(fileData):
    # create temp file:
    #print("FileDate size=" + fileData.size())

    #myfile = file(None, 'rb', fileData)
    files = {'file': ('mypic.jpg',io.BytesIO(fileData), 'image/jpeg', {'Expires': '0'})}
    res = requests.post(url='http://localhost:8080/api/upload',files=files)



def writeToFile(fileData):
    with io.FileIO('./test.jpg', 'w') as file:
        file.write(fileData)
    
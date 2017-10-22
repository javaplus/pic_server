import requests
import io
import boto3

def uploadFile(fileData):
    # create temp file:
    #print("FileDate size=" + fileData.size())

    #myfile = file(None, 'rb', fileData)
    files = {'file': ('mypic.jpg',io.BytesIO(fileData), 'image/jpeg', {'Expires': '0'})}
    res = requests.post(url='http://localhost:8080/api/upload',files=files)



def writeToFile(fileData):
    with io.FileIO('./test.jpg', 'w') as file:
        file.write(fileData)
    

def uploadFileToS3(fileData, fileName):
    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)
    
    # Upload a new file
    data = io.BytesIO(fileData)
    s3.Bucket('pb-pics').put_object(Key=fileName, Body=data)
    
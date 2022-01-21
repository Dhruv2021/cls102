import cv2
import dropbox
import random
import time

startTime=time.time()

def takeSnapshot():
    number=random.randint(0,100)
    videoCapture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCapture.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("snapshot taken")
    videoCapture.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    token="sl.BAiYcxpkGODBjZT6wrrx76YPe3lVdYcuZhoCTatE0QklY51D2EB3IhmLohsXBKwsZPuU9TJomtWRqvN8jUhP2wMg4N3PkK6lJQ3o0_lTYevHWG-S3UxTCVpDihUeNlGeTnTo8ow"
    file=imageName
    fileFrom=file
    fileto="/testfolder/"+(imageName)
    dbx=dropbox.Dropbox(token)
    with open (fileFrom,"rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=1):
            name=takeSnapshot()
            uploadFile(name)
main()

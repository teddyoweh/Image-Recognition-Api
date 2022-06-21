
import os
import face_recognition
import cv2  
import imageio
import numpy as np
import random
import shutil

import requests
class iMatch:
    def __init__(self):
        pass
   
    # Check if picture is blurry python, start here
    def isimgblurry(image):
        img = cv2.imread(image)

        laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
        if laplacian_var < 5:
            return True
        else:return False
    # end here

    # Check if image is in light background.
    def imagetheme(image):
        f = imageio.imread(image, as_gray=True)

        def img_estim(img, thrshld):
            is_light = np.mean(img) > thrshld
            return 'light' if is_light else 'dark'

        print(img_estim(f, 127))
    def __addsuffix(name):
        return str(str(random.randint(99999, 999999999))+str(name))
     
    def downloadimg(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            with open(self.getfilename(url), 'wb') as f:
                f.write(response.content)
        return self.getfilename(url)
    def getimgrb(self,imgs):
        box = []
        for img in imgs:
            igm =  self.downloadimg(img)
            pixels =face_recognition.load_image_file(igm)
            oscmd = f'del {igm}'
            os.system(oscmd)
         

            box.append(pixels)
        return box
    def getfilename(self,url):
        d ='/'
        box = []
        for i in range(len(url)):
            if url[i] ==d:
                box.append(i)
        for k in range(len(box)):
            try:
                if box[k]>box[k+1]:
                    
                    box[k], box[k+1] = box[k+1],box[k]       
            except:
                pass
        index = box[len(box)-1]
        return url[index+1:]
    def ismatch(self,box):
        

        img1_encoding = face_recognition.face_encodings(box[0])[0]
        img2_encoding = face_recognition.face_encodings(box[1])[0]

        return face_recognition.compare_faces([img1_encoding], img2_encoding)
    
class iMatchApi(iMatch):
    def __init__(self,url1,url2):
        rgb =self.getimgrb([url1,url2])
        print(self.ismatch(rgb))

#iMatchApi('https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-06/220610-donald-trump-2020-ac-432p-5730d1.jpg','https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-06/220610-donald-trump-2020-ac-432p-5730d1.jpg')
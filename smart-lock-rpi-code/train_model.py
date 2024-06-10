# # #! /usr/bin/python
# # 
# # # import the necessary packages
# # from imutils import path
# # import face_recognition
# # #import argparse
# # import pickle
# # import cv2
# # import os
# # import time
# # 
# # 
# # def trainmodel():
# # # our images are located in the dataset folder
# #     print("[INFO] start processing faces...")
# #     imagePaths = list(paths.list_images("dataset"))
# # 
# #     # initialize the list of known encodings and known names
# #     knownEncodings = []
# #     knownNames = []
# #     times = time.time()
# #     # loop over the image paths
# #     for (i, imagePath) in enumerate(imagePaths):
# #         # extract the person name from the image path
# #         print("[INFO] processing image {}/{}".format(i + 1,
# #             len(imagePaths)))
# #         name = imagePath.split(os.path.sep)[-2]
# # 
# #         # load the input image and convert it from RGB (OpenCV ordering)
# #         # to dlib ordering (RGB)
# #         image = cv2.imread(imagePath)
# #         rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # 
# #         # detect the (x, y)-coordinates of the bounding boxes
# #         # corresponding to each face in the input image
# #         boxes = face_recognition.face_locations(rgb,
# #             model="hog")
# # 
# #         # compute the facial embedding for the face
# #         encodings = face_recognition.face_encodings(rgb, boxes)
# # 
# #         # loop over the encodings
# #         for encoding in encodings:
# #             # add each encoding + name to our set of known names and
# #             # encodings
# #             knownEncodings.append(encoding)
# #             knownNames.append(name)
# # 
# #     # dump the facial encodings + names to disk
# #     print("[INFO] serializing encodings...")
# #     data = {"encodings": knownEncodings, "names": knownNames}
# #     f = open("encodings.pickle", "wb")
# #     f.write(pickle.dumps(data))
# #     f.close()
# #     return True
# #     print(time.time()-times)
# # trainmodel()
# 
# #! /usr/bin/python
# 
# # import the necessary packages
# from imutils import paths
# import face_recognition
# #import argparse
# import pickle
# import cv2
# import os
# import time
# # 
# # 
# def trainmodel():
# # our images are located in the dataset folder
#     print("[INFO] start processing faces...")
#     imagePaths = list(paths.list_images("/home/pi/facial-recognition-main/dataset"))
# 
#     # initialize the list of known encodings and known names
#     knownEncodings = []
#     knownNames = []
#     times = time.time()
#     # loop over the image paths
#     for (i, imagePath) in enumerate(imagePaths):
#         # extract the person name from the image path
#         print("[INFO] processing image {}/{}".format(i + 1,
#             len(imagePaths)))
#         name = imagePath.split(os.path.sep)[-2]
# 
#         # load the input image and convert it from RGB (OpenCV ordering)
#         # to dlib ordering (RGB)
#         image = cv2.imread(imagePath)
#         rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 
#         # detect the (x, y)-coordinates of the bounding boxes
#         # corresponding to each face in the input image
#         boxes = face_recognition.face_locations(rgb,
#             model="hog")
# 
#         # compute the facial embedding for the face
#         encodings = face_recognition.face_encodings(rgb, boxes)
# 
#         # loop over the encodings
#         for encoding in encodings:
#             # add each encoding + name to our set of known names and
#             # encodings
#             knownEncodings.append(encoding)
#             knownNames.append(name)
# 
#     # dump the facial encodings + names to disk
#     print("[INFO] serializing encodings...")
#     data = {"encodings": knownEncodings, "names": knownNames}
#     f = open("encodings.pickle", "wb")
#     f.write(pickle.dumps(data))
#     f.close()
#     return True
#     print(time.time()-times)
#trainmodel()


# import the necessary packages
from imutils import paths
import face_recognition
#import argparse
import pickle
import cv2
import os
import time


f = pickle.load(open("encodings.pickle", "rb"))
length = len(f['encodings'])
# print('length of existing pickle file ', length)
encodings = f['encodings']
names = f['names']
#print(names)

def trainmodel(username):
# our images are located in the dataset folder
    print("[INFO] start processing faces...")
    parentdir = "/home/pi/facial-recognition-main/dataset"
    path = os.path.join(parentdir,username) 
    imagePaths = list(paths.list_images(path))
    times = time.time()
    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,
            len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]

        # load the input image and convert it from RGB (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,
            model="hog")

        # compute the facial embedding for the face
        faceencodings = face_recognition.face_encodings(rgb, boxes)

        # loop over the encodings
        for encoding in faceencodings:
            # add each encoding + name to our set of known names and
            # encodings
            encodings.append(encoding)
            names.append(name)

    # dump the facial encodings + names to disk
#     print("[INFO] serializing encodings...")
    data = {"encodings": encodings, "names": names}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()
    print(time.time()-times)
    return True
    

def delmodel(username):
    l = []
    l.append(username)
#     print(l)
    print(names)
#     print(len(encodings))
    for n in l:
    # taking 1 number found in the list
    # remove it from the list
        while n in names:
            index = names.index(n)
#             print(index)
            names.remove(n)
            encodings.pop(index)
    data = {"encodings": encodings, "names": names}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()
    print(len(encodings))
    print(names)
    
#trainmodel('MR Noor')
#delmodel('noor')
# print(names)
#print(names)
# f = pickle.load(open(r"C:\Users\mohd noor ahmed\Downloads\encodings-main\encodings-main\encodings.pickle", "rb"))
# print(len(f['names']))
# print(f)
# 
from os import getcwd
from sklearn.model_selection import train_test_split
import json
import glob
import cv2

wd = getcwd()
"labelme标注的json 数据集转为pytorch版yolov4的训练集"
classes = ['SealCover_R', 'Seal_R', 'ShieldSleeve_R', 'ShieldCrimpFerrule_R', 'ShieldCrimpFerrule_L', 'ShieldSleeve_L',
           'SealCover_L', 'Seal_L']

image_ids = glob.glob(r"C:\Users\AIMTTEST\Desktop\cable_dataset0403/*[jpg,bmp]")
print(image_ids)
train_list_file = open('data/train.txt', 'w')
val_list_file = open('data/val.txt', 'w')


def convert_annotation(image_id, list_file):
    print(image_id + ".jpg")
    img = cv2.imread("C:/Users/AIMTTEST/Desktop/cable_dataset0403/" + image_id )
    h, w = img.shape[:2]
    jsonfile = open('C:/Users/AIMTTEST/Desktop/cable_dataset0403/%s.json' % image_id[0:-4])
    in_file = json.load(jsonfile)
    print(h, w, "\n")
    for i in range(0, len(in_file["shapes"])):
        object = in_file["shapes"][i]
        cls = object["label"]
        points = object["points"]
        xmin = int(points[0][0])
        ymin = int(points[0][1])
        xmax = int(points[1][0])
        ymax = int(points[1][1])
        weight = (xmax - xmin) / w
        height = (ymax - ymin) / h
        x_center = ((points[0][0] + points[1][0]) / 2) / w
        y_center = ((points[0][1] + points[1][1]) / 2) / h

        if cls not in classes:
            print("cls not in classes")
            continue
        cls_id = classes.index(cls)
        b = (x_center, y_center, weight, height)
        list_file.write(str(cls_id) + " " + " ".join([str(a) for a in b]) + "\n")
    jsonfile.close()


def ChangeData2TXT(image_List, dataFile):
    for image_id in image_List:
        print("sss", image_id)
        dataFile.write(image_id)
        # convert_annotation(image_id.split('.')[0], dataFile)
        dataFile.write("\n")
    dataFile.close()


trainval_files, test_files = train_test_split(image_ids, test_size=0.2, random_state=55)
for id in image_ids:
    id = id.split('\\')[-1]
    # id = id.split('.')[-2:]
    id = id
    file = open(f"C:/Users/AIMTTEST/Desktop/cable_dataset0403/{id[0:-4]}.txt", "w")
    convert_annotation(id, file)
    file.close()

ChangeData2TXT(trainval_files, train_list_file)
ChangeData2TXT(test_files, val_list_file)

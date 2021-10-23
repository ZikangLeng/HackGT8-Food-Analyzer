"""
Recognize food: fruit, vegetable
"""
import io
import os
import json
from datetime import datetime

import cv2
from google.cloud import vision_v1p3beta1 as vision

class imageProcess:
    foodname = "unknown"


    def load_food_name(self,food_type):
        """
        Load all known food type name.
        :param food_type: Fruit or Vegetable
        :return:
        """
        names = [line.rstrip('\n').lower() for line in open(food_type + '.dict')]
        return names


    def recognize_food(self,img_path, list_foods):
        start_time = datetime.now()

        # Read image with opencv
        img = cv2.imread(img_path)

        # Get image size
        height, width = img.shape[:2]

        # Scale image
        img = cv2.resize(img, (800, int((height * 800) / width)))

        # Save the image to temp file
        cv2.imwrite("output.jpg", img)

        # Create new img path for google vision
        img_path ="output.jpg"

        # Create google vision client
        client = vision.ImageAnnotatorClient()

        # Read image file
        with io.open(img_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        label_detection_feature = vision.types.Feature(type_=vision.types.Feature.Type.LABEL_DETECTION)
        request_features = [label_detection_feature]
        response = client.annotate_image(
         {'image': image, 'features': request_features})
        labels = response.label_annotations
        
        for label in labels:
           
            desc = " "+label.description.lower()
            score = round(label.score, 2)
            print("label: ", desc, "  score: ", score)
            for food in list_foods:
                food = " " + food
                if (desc in food):
                    food= food[1:len(food)]
                    foodname = food
                    print(foodname)

                    # Get first fruit only
                    break

    def takeImage(self):
        
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()

        # Setup google authen client key
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'astral-petal-329903-0138510647da.json'

        FOOD_TYPE = 'Food'  # 'Vegetable'

        print('---------- Start FOOD Recognition --------')
        list_foods = self.load_food_name(FOOD_TYPE)
        self.recognize_food(img_name, list_foods)
        print('---------- End ----------')
        try: 
            os.remove(img_name)
        except: pass

test = imageProcess()

test.takeImage()
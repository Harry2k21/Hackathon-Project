from google.cloud import vision 
import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountToken.json"

def label_detector(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.logo_detection(image = image)
    logos = response.logo_annotations
   # print("Logos: ", logos)
    for logo in logos:
        print(logo.description)

    if response.error.message:
        raise Exception(
            '{}\nerror'.format(response.error.message)
        )
label_detector(path = "CokeCAn.jpg")
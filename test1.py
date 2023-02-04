from google.cloud import vision 
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountToken.json"

def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        #print('Normalized bounding polygon vertices: ')
       # for vertex in object_.bounding_poly.normalized_vertices:
           # print(' - ({}, {})'.format(vertex.x, vertex.y))

    
localize_objects(path = "banana2.JPG")

#namefield
#Confidence field

#error field not on database
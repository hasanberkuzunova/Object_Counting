from object_counting_v1 import ObjectCounting_v1 as oc

model_path = r'C:\Users\hasan.uzunova\Desktop\tf object detection\TFODCourse\Tensorflow\workspace\models\my_ssd_mobnet_diffcolorsvv22\export\saved_model'
label_map_path = r'C:\Users\hasan.uzunova\Desktop\tf object detection\TFODCourse\Tensorflow\workspace\annotations\label_map.pbtxt'
image_path = r'C:\Users\hasan.uzunova\Desktop\asil-test.jpg'
labels = "TREE"
image_resize_division = 2
small_object = 1
#small_object = True
#image_path = r'C:\Users\kaan.ornek\Desktop\tf object detection\TFODCourse\Tensorflow\workspace\images\test\WMSI6244_11zon.jpeg'

oc.count_objects(model_path, labels, label_map_path, image_path, small_object, image_resize_division)

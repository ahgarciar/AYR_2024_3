
#from keras.preprocessing.image import load_img, img_to_array  #deprecated en tf 2.9 #alternative 0
#from tensorflow.keras.utils import load_img  #alternative 1
from keras.utils import load_img, img_to_array #alternative 2

largo, alto = 1000, 1000
#file = './FIT V.jpg'
file = './gato.jpeg'
img = load_img(file, target_size = (largo, alto) # )
             ,color_mode = "grayscale")
print(img.size)
print(img.mode)

#opcion 1
img.show()

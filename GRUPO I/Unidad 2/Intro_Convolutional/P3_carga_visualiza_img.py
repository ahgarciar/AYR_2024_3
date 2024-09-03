
#from keras.preprocessing.image import load_img, img_to_array  #deprecated en tf 2.9 #alternative 0
#from tensorflow.keras.utils import load_img  #alternative 1
from keras.utils import load_img, img_to_array #alternative 2
#from keras.api.utils import load_img, img_to_array #alternative 3

largo, alto = 200, 200
#file = './FIT V.jpg'
file = './gato.jpeg'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

print(img.size)
print(img.mode)


imagen_en_array = img_to_array(img)  #filas, columnas, canales de colores
print(imagen_en_array.shape)

#print(imagen_en_array)

for i in imagen_en_array:
    for j in i:
        print(str(j[0]) + ",", end="")
    print()


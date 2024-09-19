import cv2

# logo = cv2.imread('3_1.jpg')
# print(logo[190,168])
# # [210,148,108]

# logo = cv2.imread('./3_1.jpg')
# blue=logo[198,168,0]
# green=[198,168,1]
# red=logo[198,168,2]
# print(blue,green,red)

zrn = cv2.imread("./3_1.jpg")
print("图片类型",type(zrn))
print(zrn.shape)



blue = zrn[190,168,0]
green = zrn[190,168,1]
red = zrn[190,168,2]
print(blue,green,red)
print(type(blue))









































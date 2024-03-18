import os
import cv2 as cv

image_path = 'D:\\yolo\\ultralytics-main\\datasets\\trafficsign_data\\valid\\images'    #&#x8BBE;&#x7F6E;&#x56FE;&#x7247;&#x8BFB;&#x53D6;&#x7684;&#x8DEF;&#x5F84;
save_path = 'D:\\yolo\\trafficsign_data\\valid\\images'    #&#x8BBE;&#x7F6E;&#x56FE;&#x7247;&#x4FDD;&#x5B58;&#x7684;&#x8DEF;&#x5F84;

if not os.path.exists(save_path):    #&#x5224;&#x65AD;&#x8DEF;&#x5F84;&#x662F;&#x5426;&#x6B63;&#x786E;&#xFF0C;&#x5982;&#x679C;&#x6B63;&#x786E;&#x5C31;&#x6253;&#x5F00;
    os.makedirs(save_path)

image_file = os.listdir(image_path)

for image in image_file:
    if image.split('.')[-1] in ['bmp', 'jpg', 'jpeg', 'png', 'JPG', 'PNG']:
        str = image.rsplit(".", 1)    #&#x4ECE;&#x53F3;&#x4FA7;&#x5224;&#x65AD;&#x662F;&#x5426;&#x6709;&#x7B26;&#x53F7;&#x201C;.&#x201D;&#xFF0C;&#x5E76;&#x5BF9;image&#x7684;&#x540D;&#x79F0;&#x505A;&#x4E00;&#x6B21;&#x5206;&#x5272;&#x3002;&#x5982;112345.jpeg&#x5206;&#x5272;&#x540E;&#x7684;str&#x4E3A;["112345","jpeg"]
        output_img_name = str[0] + ".jpg"    #&#x53D6;&#x5217;&#x8868;&#x4E2D;&#x7684;&#x7B2C;&#x4E00;&#x4E2A;&#x5B57;&#x7B26;&#x4E32;&#x4E0E;&#x201C;.jpg&#x201D;&#x653E;&#x5728;&#x4E00;&#x8D77;&#x3002;
        src = cv.imread(os.path.join(image_path, image))
        newimg = cv.imwrite(save_path + '/' + output_img_name, src)
print('FINISHED')
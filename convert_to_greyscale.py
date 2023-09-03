import os,cv2
path = r'D:\KULIAH\SEM_8\PROJECT\Dataset_kaggle_baru\training\Tuberculosis' # Source Folder
dstpath = r'D:\KULIAH\SEM_8\PROJECT\Dataset_kaggle_baru\Tuberculosis grey' # Destination Folder

try:
    os.makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in destination folder")

# Folder won't used
files = os.listdir(path)

for image in files:
    img = cv2.imread(os.path.join(path,image))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(dstpath,image),gray)
import os

img_dir = "downloads/pho-vn"
def main(): 
    i = 0
    for filename in os.listdir(img_dir): 
        dst ="pho_" + str(i) + ".jpg"
        src = f'{img_dir}/{filename}'
        dst = f'{img_dir}/{dst}'

        os.rename(src, dst) 
        i += 1
  
if __name__ == '__main__': 
      
    main() 
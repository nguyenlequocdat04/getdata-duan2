import os

# change dir before run script
img_dir = "data/banh-mi-vn"
anno_dir = "data/banh-mi-vn-annotations"

annos = os.listdir(anno_dir)


def main():
    # print((annos))
    i = 0
    for img_name in os.listdir(img_dir):
        anno_name = f'{img_name.split(".")[0]}.xml'
        if not anno_name in annos:
            print(f"Remove {img_name}")
            os.remove(f"{img_dir}/{img_name}")
            i += 1

    print(f"Delete {i} imgs")
  
if __name__ == '__main__': 
    main() 
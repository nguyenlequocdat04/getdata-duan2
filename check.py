import os
import xmltodict, json
import pprint
# change dir before run script
anno_dir = "./data/banh-mi-vn-annotations"

annos = os.listdir(anno_dir)
pp = pprint.PrettyPrinter(indent=4)

def main():
    for anno in annos:
        f = open(f"./data/banh-mi-vn-annotations/{anno}")
        content = f.read()
        if content:
            o = xmltodict.parse(content)
            width = int(o['annotation']['size']['width'])
            # print(width)
            if width <=0:
                print(f"{o['annotation']['filename']}: {width}")
                # remove it
                os.remove(f"{anno_dir}/{anno}")
        

if __name__ == '__main__': 
    main()
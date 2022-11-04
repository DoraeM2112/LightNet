import os
import json
from tqdm import tqdm
import argparse



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--json_file', default='test2all.json',
                        type=str, help="coco file path")
    parser.add_argument('--save_dir', default='labels', type=str,
                        help="where to save .txt labels")
    arg = parser.parse_args()

    data = json.load(open(arg.json_file, 'r'))

    # 如果存放txt文件夹不存在，则创建
    if not os.path.exists(arg.save_dir):
        os.makedirs(arg.save_dir)

    id_map = {}

    # 解析目标类别，也就是 categories 字段，并将类别写入文件 classes.txt 中

    for img in tqdm(data['images']):

        # 解析 images 字段，分别取出图片文件名、图片的宽和高、图片id
        filename = img["file_name"]

        head, tail = os.path.splitext(filename)

        # txt文件名，与对应图片名只有后缀名不一样
        # txt_name = head + ".txt"
        # txt_name = filename
        # f_txt = open(os.path.join(arg.save_dir, txt_name), 'w')
        f_txt = open('test_is.txt', 'a+')

        f_txt.write("%s\n" % filename)

        f_txt.close()

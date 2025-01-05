import os
import numpy as np
import cv2 as cv

def generate_trimap(alpha):
    fg = np.array(np.equal(alpha, 255).astype(np.float32))
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    unknown = np.array(np.not_equal(alpha, 0).astype(np.float32))
    iterations = np.random.randint(1, 20)
    unknown = cv.dilate(unknown, kernel, iterations=iterations)
    trimap = fg * 255 + (unknown - fg) * 128
    return trimap.astype(np.uint8)

def convert_alpha_to_trimap(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
            alpha_path = os.path.join(input_folder, filename)
            alpha = cv.imread(alpha_path, cv.IMREAD_GRAYSCALE)
            
            if alpha is not None:
                trimap = generate_trimap(alpha)
                trimap_filename = os.path.splitext(filename)[0] + '.png'
                trimap_path = os.path.join(output_folder, trimap_filename)
                cv.imwrite(trimap_path, trimap)
                print(f"Trimap saved: {trimap_path}")
            else:
                print(f"Could not read alpha image: {alpha_path}")

# 设置输入和输出文件夹路径
input_folder = 'autodl-fs/in-context-matting-main/datasets/ICM57/alpha'
output_folder = 'autodl-fs/in-context-matting-main/datasets/ICM57/trimap'

# 调用函数转换 alpha 图像为 trimap
convert_alpha_to_trimap(input_folder, output_folder)
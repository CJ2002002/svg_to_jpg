'''
Author: C2002002J 2826728609@qq.com
Date: 2023-12-24 18:53:01
LastEditors: C2002002J 2826728609@qq.com
LastEditTime: 2023-12-24 20:19:23
FilePath: \undefinede:\Git_project\svg_all_to_jpg.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import cairosvg

def convert_svg_to_jpg(svg_path, jpg_path, output_width=1920, output_height=1080):
    # 使用 cairosvg 将 SVG 转换为 JPEG，增加 output_width 和 output_height 参数
    # 这里图片参数可以设置为你想要的大小
    cairosvg.svg2png(url=svg_path, write_to=jpg_path, output_width=output_width, output_height=output_height)

def batch_convert_svg_to_jpg(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有 SVG 文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".svg"):
            svg_path = os.path.join(input_folder, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)
            
            # 转换并保存为 JPEG，可以根据需要调整 output_width 和 output_height
            convert_svg_to_jpg(svg_path, jpg_path, output_width=1920, output_height=1080)
            print(f"转换完成：{filename} -> {jpg_filename}")

# 指定输入和输出文件夹
input_folder = "svg文件输入路径"  # 替换为实际的 SVG 文件夹路径
output_folder = "jpg文件输出路径"    # 替换为实际的输出文件夹路径

# 执行批量转换
batch_convert_svg_to_jpg(input_folder, output_folder)

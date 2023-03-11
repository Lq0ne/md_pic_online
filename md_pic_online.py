# -*- coding: UTF-8 -*-

import os
import requests
import json

DIR_PATH = "C:\\WebSecurity\\hvv\\笔记\\hvv"# os.path.abspath(os.path.dirname(__file__)) 
L_cur = 2   
R_cur = 1   
image_local_add = 'C:'
image_remote_add = 'https://'
file_data_cache = ""
log_data_cache = "" #日志缓存

def file_update(file):
    os.chdir(DIR_PATH)
    with open(file, 'w', encoding='utf-8') as fw:
        fw.write(file_data_cache)
        fw.close

def image_upload():
    data = json.dumps({'list': [image_local_add]})
    response = requests.post(url='http://127.0.0.1:36677/upload', data = data)
    return response

if __name__ == '__main__':
    log_file = open("log.txt", "r+",encoding="utf-8")
    log_data_cache += log_file.read()
    files = os.listdir(DIR_PATH)
    os.chdir(DIR_PATH)
    file_num = 0
    for file in files:  #处理目录下每个文件

        if (not os.path.isdir(file) and file[-3:] == '.md'): 
            file_num += 1
            file_data_cache = ""
            with open(file,'r',encoding = 'utf-8') as f:
                line_num = 0
                for line in f: 
                    if (line.find('![image') != -1 and line.find("http") == -1):
                        L_cur = line.find('(') + 1
                        R_cur = line.find(')')
                        image_local_add = line[L_cur:R_cur]
                        # print(image_local_add)
                        line_num += 1
                        log_data_cache += "uploading：正在上传第" + str(file_num) + "个文件\'" + file + "\'的第" + str(line_num) + "张图片......"
                        print("uploading：正在上传第" + str(file_num) + "个文件\'" + file + "\'的第" + str(line_num) + "张图片......")
                        response = image_upload()   # 上传
                        # print(type(response.text))
                        # print(response.text)
                        if(response.text.find('false') != -1):  # 报错
                            log_data += "Upload fail! PicGo upload error!\nPlease check your PicGo setting and web connection!\n"
                            print("Upload fail! PicGo upload error!\nPlease check your PicGo setting and web connection!\n")
                            print(image_local_add)
                        else:
                            log_data += "Upload Success!"
                            print("Upload Success!")
                            image_remote_add = response.text[response.text.find('https://'):response.text.find("\"]}")]
                            # print(image_remote_add)
                            line = line.replace(image_local_add,image_remote_add)
                    file_data_cache += line
                f.close()
            file_update(file)   
    log_file.write(log_data_cache)
    log_file.close()
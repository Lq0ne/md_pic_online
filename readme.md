# Online .md Picture -readme

This python script will help you upload images that have not been uploaded.

**!!!!!!!!!!!!!!Before run the script, please backup your .md files in advance!!!!!!!!!!!!!!!**

## How To Use

Run the .py file with Python3.10 which has installed Requests package([How To Install](https://docs.python.org/3.10/installing/index.html)) and [PicGo](https://picgo.github.io/PicGo-Doc/en/).It will find your local images and upload them to your default Img with [PicGo](https://picgo.github.io/PicGo-Doc/en/) server. Then change the image url to the online url. You just need launch the PicGo , set the Img, change the global variable which named *DIR_PATH* to your .md file absolut path in the script such as "C:\\\\users\\\\Administrator\\\\documents\\\\". Then just waiting for it completing the work! 







# .md本地图片转线上

此脚本能够帮助你自动批量上传你的md文件里的本地图片至图床并自动修改其url。

**！！！！！！！！！！！！在此之前，请提前备份你的md文件以防造成无法挽回的损失！！！！！！！！！！！！！！！！**

## 如何使用此脚本

此脚本基于[PicGo](https://picgo.github.io/PicGo-Doc/en/)和python Requests库，使用前请提前预装([如何装requests库](https://docs.python.org/3.10/installing/index.html))。运行此脚本将自动抓取md文件内的本地图片，通过PicGo App开放的本地上传端口上传至默认图床并修改图片链接为在线链接。脚本内地全局变量 DIR_PATH 标识了md文件的绝对路径，请修改其为你的md文件全局路径如"C:\\\\users\\\\Administrator\\\\documents\\\\"。接下来只需要等待其完成工作。
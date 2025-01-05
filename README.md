使用autodl进行实验  

1.按照autodl教程配置好基础镜像后，点击进入终端  

2.输入source activate，进入base环境  

3.将environment.yml上传到主机所在地的存储空间内  

4.进入base环境以后，输入conda env create -f /root/autodl-fs/environment.yml创建环境  

5.通过xftp将程序上传至autodl-fs之中  

6.环境创建完毕后输入conda activate icm 进入虚拟环境  

7.输入pip install -r autodl-fs/colab_requirements.txt下载需要的库函数  

8.通过https://hf-mirror.com/网站下载stable-diffusion-2-1  

9.运行eval.py代码：  

进入eval.py所在的文件夹：cd /root/autodl-fs/in-context-matting-main  

输入python eval.py

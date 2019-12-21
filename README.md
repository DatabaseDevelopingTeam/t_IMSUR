# t_IMSUR
轻量级道路信息管理系统

1. mysql环境配置

推荐5.7版本，ubuntu系统可参考此文章

[https://www.jianshu.com/p/35e7af7db96a](https://www.jianshu.com/p/35e7af7db96a)

1. python环境配置
* 安装python3

推荐安装python3.5

* 安装python3-pip

ubuntu16.04及其以上系统使用下面的命令

```
sudo apt install python3-pip
```
1. django环境配置

推荐2.2版本

* 从github下载源码
```
git clone https://github.com/DatabaseDevelopingTeam/t_IMSUR.git
```
会下载下来一个文件夹,**t_IMSUR**
* 安装django
```
pip install django==2.2
```
如果下载速度慢，使用下面的命令指定豆瓣源进行下载
```
pip install django==2.2 -i https://pypi.douban.com/simple
```
* 配置数据库
  * 安装django需要的两个与mysql相关的模块
```
pip install pymysql
pip install mysqlclient
```
### 版本报错解决方案
[https://blog.csdn.net/lijing742180/article/details/91966031](https://blog.csdn.net/lijing742180/article/details/91966031)

(就是要把那两行代码注释掉)

  * 修改django数据库配置

打开项目目录下的IMSUR/settings.py文件,找到下列代码块

![图片](https://uploader.shimo.im/f/5dgGMkwOCg8BobCv.png!thumbnail)

将**PASSWORD**对应的值改为自己的mysql登录密码

* mysql数据库配置

在mysql中创建名为**imsur**的数据库。在mysql交互环境中的命令为:

```
create database imsur default character set utf8;
```
* 准备启动django项目
  * 首先进入项目目录。当前目录中应该要有manage.py文件
  * 收集静态文件
```
python manage.py collectstatic
```
  * 生成数据库迁移脚本
```
python manage.py makemigrations
```
  * 写入数据库
```
python manage.py migrate
```
* 启动项目!!
```
python manage.py runserver
```
* 访问网站

浏览器中键入 [http://localhost:8000](http://localhost:8000)

# 发布流程

> 注意，以下内容仅供参考，且需要配置自己的**token**，内容仅供本人使用。

## 安装依赖

```bash
pip install twine
```

## 生成二进制文件

```bash
 python setup.py sdist  
```

或者使用

```bash
python setup.py bdist_wheel sdist
```

* 其中bdist表示二进制的可执行文件格式.
* wheel是python很常见的打包后的二进制格式（包括pyd即python动态库和元数据）
* 其中sdist代表源码，打包后为.tar.gz格式。

## 上传到pypi

```bash
twine upload dist/*
```

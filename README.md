# Furry_tool
Furry_tool是一个个人工具集，本库旨在将个人总结的部分通用代码上传到pypi，实现随时调用。

# 发布流程
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
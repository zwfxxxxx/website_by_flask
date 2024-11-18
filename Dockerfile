FROM python:3.9-slim

# 设置工作目录
WORKDIR /app
# 将当前目录下的所有文件复制到工作目录
COPY . /app
# 安装依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["python", "app.py"]
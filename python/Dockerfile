
# 使用合适的基础镜像，例如官方的 Python 镜像
FROM python:3.10

# 设置时区
ENV TZ=Asia/Shanghai

# 更新软件包并安装 nmap、masscan 和 git
RUN apt-get update && \
    apt-get install -y nmap masscan git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装 dirsearch

# 将工作目录设置为应用程序目录
WORKDIR /app

# 将应用程序依赖项复制到容器中并安装
COPY requirements.txt ./
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# 将应用程序代码复制到容器中
COPY . .

# 在容器启动时运行命令
CMD ["python", "main.py", "runserver", "0.0.0.0:8000"]

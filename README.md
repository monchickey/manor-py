# manor-py Python 常用工具类库

manor （原 py3monchickey） 是一个基于 Python 3 的常用工具类库，提供了文件处理、数据库连接、网络通信、系统命令调用等实用功能。

## 主要功能模块

- **config_util**: YAML 配置文件读取工具
- **counter**: 线程安全的计数器类
- **daemon**: Unix/Linux 守护进程工具
- **data_process**: 数据处理工具（时间转换、编码解码、哈希计算等）
- **fileio_util**: 文件和目录操作工具
- **ftp_util**: FTP 文件操作工具
- **http_util**: HTTP 请求工具
- **lru_cache**: LRU 缓存工具类
- **mysql_util**: MySQL 数据库操作工具
- **network_util**: 网络工具（域名解析、Socket 通信等）
- **os_util**: 系统命令调用工具

## 安装

### 从源码安装

```bash
git clone https://github.com/monchickey/manor-py.git
cd manor-py
pip install .
```

## 使用示例

### 配置文件读取

```python
from manor import config_util

# 读取 YAML 配置文件
config = config_util.get_yaml_config('config.yaml')
print(config)
```

### 使用计数器

```python
from manor import Counter

counter = Counter()
counter.accumulate('requests')
counter.accumulate('requests')
print(counter.get('requests'))  # 输出: 2
```

### 文件操作

```python
from manor import fileio_util

# 创建目录
fileio_util.create_dirs('/tmp/test_dir')

# 计算文件 MD5
md5 = fileio_util.get_file_md5('/path/to/file')
print(md5)
```

### 数据库操作

```python
from manor import mysql_util

# 获取数据库连接
conn = mysql_util.get_connection('localhost', 3306, 'user', 'password', 'database')
if conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM table')
    results = cursor.fetchall()
    conn.close()
```

### HTTP 请求

```python
from manor import http_util

# 简单 GET 请求
content = http_util.simple_get('https://example.com')
print(content)
```

### 网络工具

```python
from manor import network_util

# 获取域名对应的 IP
ip = network_util.get_remotehost_ip('www.example.com')
print(ip)
```

## 依赖项

- PyMySQL >= 0.7.11
- PyYAML >= 3.11
- xxhash >= 1.2.0

## 许可证

本项目采用 Apache 2.0 许可证。详见 [LICENSE](LICENSE) 文件。


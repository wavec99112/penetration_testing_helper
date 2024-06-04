# 渗透测试助手

这是一个简单的渗透测试工具，用于生成有效载荷并启动 Metasploit 监听器。它支持生成不同平台的有效载荷，使得渗透测试变得更加便捷。

## 运行环境

- Python 3.x
- Metasploit Framework

确保你的系统已经安装了 Python 3.x 和 Metasploit Framework。

## 安装

将代码克隆到本地：

```bash
git clone https://github.com/your_username/penetration-testing-helper.git
```
## 使用方法
### 在终端中进入项目目录：
```
cd penetration-testing-helper
```
### 启动程序
```
python wave2k.py
```
根据菜单提示进行操作
选择生成有效载荷的类型
输入所需的信息，如 LHOST、LPORT、输出格式和输出文件名
程序将自动生成有效载荷并启动 Metasploit 监听器
将生成的有效载荷发送给目标主机，并等待其连接到监听器
一旦连接成功，你就可以在 Metasploit 控制台中与目标主机进行交互
## 免责协议
该软件仅用于教育和研究目的，任何未经授权的使用行为均与作者无关。用户需自行承担使用该软件可能造成的后果。

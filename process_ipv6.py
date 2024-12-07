import requests

# 定义输出文件路径（保存到当前目录）
output_file = "ipv6.txt"

# 请求数据的 URL
url = "https://addressesapi.090227.xyz/cmcc-ipv6"

try:
    # 获取地址数据
    print(f"正在请求 URL: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 如果状态码不是 200，会抛出异常
    raw_data = response.text

    # 处理数据
    print("处理返回的数据...")
    processed_data = []
    for line in raw_data.strip().split("\n"):
        if line.startswith("[") and "]" in line:
            # 提取 IP 地址和描述
            ip, desc = line.split("]", 1)
            ip_with_port = f"{ip}]:443"  # 在中括号外部添加 :443
            processed_line = f"{ip_with_port}{desc.strip()}"
            processed_data.append(processed_line)

    # 写入文件
    print("写入数据到文件...")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(processed_data))
    
    print(f"文件成功保存到: {output_file}")

except requests.exceptions.RequestException as e:
    print(f"请求 URL 时发生错误: {e}")
except Exception as e:
    print(f"处理或保存文件时发生错误: {e}")

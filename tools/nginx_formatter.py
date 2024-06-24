import tkinter as tk
from tkinter import ttk
import re

def format_nginx_conf(config):
    # 移除多余的空行
    config = re.sub(r'\n\s*\n', '\n', config)
    
    # 分割成行
    lines = config.split('\n')
    formatted_lines = []
    indent = 0
    
    for line in lines:
        line = line.strip()
        
        # 处理块的开始
        if line.endswith('{'):
            formatted_lines.append('    ' * indent + line)
            indent += 1
        # 处理块的结束
        elif line.startswith('}'):
            indent -= 1
            formatted_lines.append('    ' * indent + line)
        # 处理普通行
        else:
            formatted_lines.append('    ' * indent + line)
    
    return '\n'.join(formatted_lines)

def format_button_click():
    input_text = input_text_area.get("1.0", tk.END)
    formatted_text = format_nginx_conf(input_text)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, formatted_text)

# 创建主窗口
root = tk.Tk()
root.title("Nginx配置格式化工具")
root.geometry("800x600")

# 创建输入文本区
input_frame = ttk.LabelFrame(root, text="输入Nginx配置")
input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_text_area = tk.Text(input_frame, wrap=tk.WORD)
input_text_area.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# 创建格式化按钮
format_button = ttk.Button(root, text="格式化", command=format_button_click)
format_button.pack(pady=10)

# 创建输出文本区
output_frame = ttk.LabelFrame(root, text="格式化后的Nginx配置")
output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

output_text_area = tk.Text(output_frame, wrap=tk.WORD)
output_text_area.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# 运行主循环
root.mainloop()

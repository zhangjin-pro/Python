import re


def format_nginx_conf(file_path, output_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        lines = file.readlines()

    formatted_lines = []
    indent_level = 0
    indent_str = "    "  # 4 spaces for indentation

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith("#"):
            formatted_lines.append(indent_str * indent_level + stripped_line)
            continue

        if stripped_line.endswith("{"):
            formatted_lines.append(indent_str * indent_level + stripped_line)
            indent_level += 1
        elif stripped_line.endswith("}"):
            indent_level -= 1
            formatted_lines.append(indent_str * indent_level + stripped_line)
        else:
            formatted_lines.append(indent_str * indent_level + stripped_line)

    with open(output_path, 'w', encoding=encoding) as file:
        file.write("\n".join(formatted_lines) + "\n")

    print(f"Formatted configuration written to: {output_path}")
# Example usage
input_file = "C:/Users/zhang/Desktop/nginx.conf"
output_file = "C:/Users/zhang/Desktop/nginx.conf.2"
format_nginx_conf(input_file, output_file)

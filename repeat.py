def remove_duplicate_lines(file_path):
    lines = []
    seen = set()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line not in seen:
                seen.add(line)
                lines.append(line)
            else:
                print(f"重复字段: {line}")

    with open(file_path, 'w') as file:
        file.write('\n'.join(lines))

    print("重复字段已删除并文件已更新。")
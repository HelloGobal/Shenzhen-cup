from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import RtfFormatter

# 多行输入处理（支持空行保留）
print("请输入代码（输入end结束）:")
lines = []
while True:
    line = input()
    if line == "end":  # 自定义结束标记[9,10](@ref)
        break
    lines.append(line)
c = '\n'.join(lines)  # 保留原始空行[6,7](@ref)

# 生成RTF格式代码
rtf_code = highlight(c, PythonLexer(), RtfFormatter())

# 写入RTF文件（UTF-8编码保障兼容性）
with open("output.rtf", "w", encoding="utf-8") as f:  # 编码设置[1,3](@ref)
    f.write(rtf_code)
print("RTF文件已生成：output.rtf")

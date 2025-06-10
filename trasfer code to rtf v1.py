from docx import Document
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import RtfFormatter
c=input("请输入你准备转换为rtf文件的代码：")

doc = Document()
code = '''   '''#在这里添加代码
rtf_code = highlight(code, PythonLexer(), RtfFormatter())

# 创建临时RTF文件
with open("temp.rtf", "w") as f:
    f.write(rtf_code)
f.close()
##doc.add_picture("temp.rtf")  # 作为对象插入
##doc.save("output.docx")

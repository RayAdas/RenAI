import asyncio
from datetime import datetime

from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.document import Document

# 输出区域（只读）
output_field = TextArea(
    text="",
    scrollbar=True,
    wrap_lines=True,
    read_only=False,
)

# 输入区域（单行）
input_field = TextArea(
    height=1,
    prompt="> ",
    multiline=False,
)

# 追加日志
def log(msg: str):
    output_field.buffer.insert_text(msg + "\n", move_cursor=True)

# 回车处理
def accept(doc: Document):
    text = doc.text
    log(f"[输入] {text}")
    doc.text = ""  # 清空输入框

input_field.accept_handler = accept

# 布局：上下结构
root_container = HSplit([
    output_field,
    input_field,
])

layout = Layout(root_container, focused_element=input_field)

# 键绑定（可选）
kb = KeyBindings()

@kb.add("c-c")
def _(event):
    event.app.exit()

app = Application(
    layout=layout,
    key_bindings=kb,
    # full_screen=True,
)

# 后台任务
async def clock_task():
    while True:
        await asyncio.sleep(5)
        now = datetime.now().strftime("%H:%M:%S")
        log(f"[时间] {now}")

async def main():
    asyncio.create_task(clock_task())
    await app.run_async()

if __name__ == "__main__":
    asyncio.run(main())
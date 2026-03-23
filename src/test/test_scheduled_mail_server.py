import asyncio

from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.document import Document

from scheduled_mail_service.address import Address_CLI

# 输出区域
output_field = TextArea(
    text="",
    scrollbar=True,
    wrap_lines=True,
    read_only=False,
)

# 输入区域
input_field = TextArea(
    height=1,
    prompt="> ",
    multiline=False,
)

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

def accept(doc: Document):
    text = doc.text
    asyncio.create_task(add_cli.knock(text))
    doc.text = ""  # 清空输入框

input_field.accept_handler = accept

app = Application(
    layout=layout,
    key_bindings=kb,
    # full_screen=True,
)

def log(msg: str):
    output_field.buffer.insert_text(msg + "\n", move_cursor=True)

async def main():
    await app.run_async()

if __name__ == "__main__":
    add_cli = Address_CLI(log_func=log)
    asyncio.run(main())
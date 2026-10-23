from pathlib import Path
from store import load,save,find
path = Path(__file__).with_name('user_info.json')
def write_user_info():
        items=load()
        user={}
        user['id']=max((item["id"] for item in items), default=0) + 1
        user['content']=input('请输入content:')
        user['deadline']=(input('请输入deadline(iso格式,例:2026-10-21):'))
        user['status']=input('请输入status:')
        user['create_time']=(input('请输入create_time(iso格式,例:2026-10-21):'))
        items.append(user)
        save(items)
        print(f'已写入{path}')
def view():
        print(load())
def done():
    raw = input('要标记完成的 id: ').strip()
    if not raw.isdigit():
        print('请输入数字 id')
        return
    task_id = int(raw)
    items = load()
    task = find(items, task_id)
    if task is None:
        print(f'没有 id = {task_id} 的任务')
        return
    task['status'] = 'done'
    save(items)
    print(f'已标记完成：{task["content"]}')

while True:
        print('输入1编写清单,输入2读取清单,输入3完成未完成的清单,输入4结束')
        choice=input('输入你的选择,只能输入数字:').strip()
        if choice=='1':
                write_user_info()
        elif choice=='2':
               view()
        elif choice=='3':
               done()
        else:
                break


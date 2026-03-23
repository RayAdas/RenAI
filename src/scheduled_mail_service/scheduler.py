from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def job():
    """定时任务函数"""
    print(f"当前时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 定时任务执行中...")

# 创建调度器
scheduler = BlockingScheduler()

# 添加任务：每5秒执行一次
scheduler.add_job(job, 'interval', seconds=5)

print("定时任务已启动，每5秒执行一次...")
print("按 Ctrl+C 停止程序\n")

try:
    scheduler.start()
except KeyboardInterrupt:
    print("\n程序已停止")
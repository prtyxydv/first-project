import psutil
from datetime import datetime

cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

log_line = (
    f"{datetime.now()} | "
    f"CPU: {cpu_usage}% | "
    f"RAM: {memory.percent}% | "
    f"Disk: {disk.percent}%\n"
)

print(log_line)

with open("system_log.txt", "a") as f:
    f.write(log_line)

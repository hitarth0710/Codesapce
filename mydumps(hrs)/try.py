import psutil
import tkinter as tk


def update_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    network_info = psutil.net_io_counters()

    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    memory_total_label.config(text=f"Total Memory: {memory_info.total / (1024.0 ** 3):.2f} GB")
    memory_used_label.config(text=f"Used Memory: {memory_info.used / (1024.0 ** 3):.2f} GB")
    memory_free_label.config(text=f"Free Memory: {memory_info.free / (1024.0 ** 3):.2f} GB")
    disk_total_label.config(text=f"Total Disk Space: {disk_usage.total / (1024.0 ** 3):.2f} GB")
    disk_used_label.config(text=f"Used Disk Space: {disk_usage.used / (1024.0 ** 3):.2f} GB")
    disk_free_label.config(text=f"Free Disk Space: {disk_usage.free / (1024.0 ** 3):.2f} GB")
    network_label.config(text=f"Network Info: Bytes Sent: {network_info.bytes_sent / 125000:.2f} Mbps, Bytes Received: {network_info.bytes_recv / 125000:.2f} Mbps")
    root.after(1000, update_stats)

root = tk.Tk()

tk.Label(root, text="CPU").grid(row=0, column=0)
cpu_label = tk.Label(root)
cpu_label.grid(row=0, column=1)

tk.Label(root, text="Memory Total").grid(row=1, column=0)
memory_total_label = tk.Label(root)
memory_total_label.grid(row=1, column=1)

tk.Label(root, text="Memory Used").grid(row=2, column=0)
memory_used_label = tk.Label(root)
memory_used_label.grid(row=2, column=1)

tk.Label(root, text="Memory Free").grid(row=3, column=0)
memory_free_label = tk.Label(root)
memory_free_label.grid(row=3, column=1)

tk.Label(root, text="Disk Total").grid(row=4, column=0)
disk_total_label = tk.Label(root)
disk_total_label.grid(row=4, column=1)

tk.Label(root, text="Disk Used").grid(row=5, column=0)
disk_used_label = tk.Label(root)
disk_used_label.grid(row=5, column=1)

tk.Label(root, text="Disk Free").grid(row=6, column=0)
disk_free_label = tk.Label(root)
disk_free_label.grid(row=6, column=1)

tk.Label(root, text="Network").grid(row=7, column=0)
network_label = tk.Label(root)
network_label.grid(row=7, column=1)

update_stats()

root.mainloop()

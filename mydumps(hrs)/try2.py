import streamlit as st
import psutil
import time

def main():
    st.title("Real-Time System Resource Monitor")

    if st.button('Start Real Time Data'):
        placeholder_cpu = st.empty()
        placeholder_memory = st.empty()
        placeholder_disk = st.empty()
        placeholder_network = st.empty()

        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            network_info = psutil.net_io_counters()

            placeholder_cpu.text(f"CPU Usage: {cpu_usage}%")
            placeholder_memory.text(f"Total Memory: {memory_info.total / (1024.0 ** 3):.2f} GB\nUsed Memory: {memory_info.used / (1024.0 ** 3):.2f} GB\nFree Memory: {memory_info.free / (1024.0 ** 3):.2f} GB")
            placeholder_disk.text(f"Total Disk Space: {disk_usage.total / (1024.0 ** 3):.2f} GB\nUsed Disk Space: {disk_usage.used / (1024.0 ** 3):.2f} GB\nFree Disk Space: {disk_usage.free / (1024.0 ** 3):.2f} GB")
            placeholder_network.text(f"Network Info: Bytes Sent: {network_info.bytes_sent / 125000:.2f} Mbps, Bytes Received: {network_info.bytes_recv / 125000:.2f} Mbps")

            time.sleep(1)  # Refresh every second

if __name__ == "__main__":
    main()

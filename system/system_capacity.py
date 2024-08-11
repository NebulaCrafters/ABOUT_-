import psutil

def get_cpu_info():
    # Get CPU core info
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)

    print("CPU Capacity:")
    print(f"Physical cores: {cpu_cores}")
    print(f"Logical threads: {cpu_threads}")
    print()

def get_storage_info():
    # Get storage capacity
    partitions = psutil.disk_partitions()
    print("Storage Capacity:")
    for partition in partitions:
        print(f"Device: {partition.device}")
        usage = psutil.disk_usage(partition.mountpoint)
        total = usage.total / (1024 ** 3)  # Convert to GB

        print(f"Total size: {total:.2f} GB")
        print()

if __name__ == "__main__":
    get_cpu_info()
    get_storage_info()

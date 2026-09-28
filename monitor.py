#!/usr/bin/env python3

import platform
import os
import socket
import shutil
from datetime import datetime


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def get_system_info():
    print_header("SYSTEM INFORMATION")

    print(f"Hostname        : {socket.gethostname()}")
    print(f"Operating System : {platform.system()}")
    print(f"OS Version      : {platform.version()}")
    print(f"Architecture    : {platform.machine()}")
    print(f"Python Version  : {platform.python_version()}")


def get_disk_usage():
    print_header("DISK USAGE")

    total, used, free = shutil.disk_usage("/")

    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    print(f"Total Space : {total_gb:.2f} GB")
    print(f"Used Space  : {used_gb:.2f} GB")
    print(f"Free Space  : {free_gb:.2f} GB")

    usage_percent = (used / total) * 100

    print(f"Usage       : {usage_percent:.2f}%")

    if usage_percent > 90:
        print("WARNING: Disk usage is very high!")
    elif usage_percent > 75:
        print("WARNING: Disk usage is getting high.")
    else:
        print("Disk usage is normal.")


def get_environment():
    print_header("ENVIRONMENT")

    print(f"User        : {os.getenv('USER', 'Unknown')}")
    print(f"Home        : {os.getenv('HOME', 'Unknown')}")
    print(f"Current Dir : {os.getcwd()}")


def create_report():
    print_header("SYSTEM MONITOR REPORT")

    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    get_system_info()
    get_disk_usage()
    get_environment()

    print_header("REPORT COMPLETE")

    print("System monitoring completed successfully.")


if __name__ == "__main__":
    create_report()

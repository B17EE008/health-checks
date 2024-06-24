#!/usr/bin/binenv python3
(...)
def check_dick_full(disk,min_gb,min_percent):
    """Returns True isn't enough disk space, False otherwise."""
    du=shutil.dixk_usage(disk)
    #calculate the percentage of free space
    percentage_free=100*du.free/du.total
    #calculate how many free gigabytes
    gigabytes_free=du.free/2**30
    if percentage_free<min_percent or gigabytes_free<min_gb:
        return True
    return False

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys_exit(1)
    if check_disk_full(disk="/",min_gb=2,min_percent=10):
        print("Disk full")
        sys.exit(1)

    print("Everything ok")
    sys.exit(0)
main()

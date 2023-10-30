# program to delete temporary files
# clear files from windows prefetch directory
# launch disk cleanup utility (cleanmgr.exe)
# run at own risk


import os
import subprocess


def clear_temp_files():
    """Clear the Windows temporary files."""
    temp_folder = os.getenv('TEMP')
    if not temp_folder:
        print("Could not locate the TEMP folder.")
        return

    files_removed = 0
    for file_name in os.listdir(temp_folder):
        file_path = os.path.join(temp_folder, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                files_removed += 1
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
                files_removed += 1
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    print(f"Deleted {files_removed} items from TEMP folder.")


def clear_prefetch():
    """Clear the Windows prefetch files."""
    prefetch_path = r'C:\Windows\Prefetch'
    if os.path.exists(prefetch_path):
        for file_name in os.listdir(prefetch_path):
            file_path = os.path.join(prefetch_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print("Prefetch directory not found.")


def run_disk_cleanup():
    """Run the built-in Windows Disk Cleanup utility."""
    try:
        subprocess.run(['cleanmgr.exe'], check=True)
    except subprocess.CalledProcessError:
        print("Failed to run Disk Cleanup utility.")


if __name__ == "__main__":
    clear_temp_files()
    clear_prefetch()
    run_disk_cleanup()

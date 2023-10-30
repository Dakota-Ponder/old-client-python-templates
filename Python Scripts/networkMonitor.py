import subprocess
import platform


def ping(host):
    """
    Returns True if host responds to a ping request, otherwise False.
    Also returns the average ping time.
    """

    # Determine the ping command and arguments based on OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]

    try:
        output = subprocess.check_output(
            command, universal_newlines=True, stderr=subprocess.STDOUT)
        if "time=" in output:
            avg_time = output.split("time=")[-1].split(" ")[0]
            return True, avg_time
        else:
            return False, None
    except subprocess.CalledProcessError:
        return False, None


if __name__ == "__main__":
    hosts = ["google.com", "yahoo.com", "nonexistentwebsite.xyz"]

    for host in hosts:
        is_up, time = ping(host)
        if is_up:
            print(f"{host} is up with an average ping time of {time} ms")
        else:
            print(f"{host} is down")

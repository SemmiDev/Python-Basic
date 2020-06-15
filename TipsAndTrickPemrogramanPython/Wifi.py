import subprocess

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(('utf-8').split('\n'))
a = [a.split(":")[1][1:-1] for i in a if "All User Profiles"]

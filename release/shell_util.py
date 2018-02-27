import subprocess
import time

print(time.time())
obj = subprocess.Popen("git clone https://github.com/zyndev/python_lib.git e:/python_list6", stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(time.time())
print("stdout")
while True:
    cmd_out = obj.stdout.read()
    if cmd_out:
        print(cmd_out)
    else:
        break
obj.stdout.close()

print("stderr")
while True:
    cmd_error = obj.stderr.read()
    if cmd_error:
        print(cmd_error)
    else:
        break

obj.stderr.close()

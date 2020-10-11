import subprocess

# completed = subprocess.run(["ls", "-l"])
# print(type(completed))
# print("args", completed.args)
# print("code", completed.returncode) #alway 0 if 1 then error
# print("stderr", completed.stderr)
# print("stdout", completed.stdout)
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
# completed = subprocess.run(["ls", "-l"],
#                           capture_output=True,
#                           text=True)
completed = subprocess.run(["python3", "other.py"])
if completed.returncode != 0:
    print(completed.stderr)

import os
from subprocess import Popen, PIPE
if os.name=="nt":
    script = "battery.bat"
else:
    script = "battery.sh"
process = Popen(script, stdout=PIPE,shell=True)
(output, err) = process.communicate()
exit_code = process.wait()
output = output.decode("utf-8") 
for kv in output.split("\r\n"):
    keyval = kv.split("=")
    if len(keyval)==2:
        print(keyval[0]+"="+keyval[1])
#print(output.split("\r\n"))
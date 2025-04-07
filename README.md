# a PoC for the python language 

demonstrates the **insecure deserialization vulnerability** using the **pickle** module in Python

**Insecure Deserialization**:
Deserialization is the process of converting data from a byte stream back into a Python object. 
This is often done using serialization formats like pickle in Python.
Insecure deserialization occurs when data is deserialized from an untrusted source without proper validation, which can lead to arbitrary code execution,
data tampering, or other security vulnerabilities.

# Code eexplaination
The **Skid** class implements a custom __reduce__ method, which is invoked during deserialization when using the pickle module.
The __reduce__ method allows an attacker to define how the object should be serialized and later deserialized.
In this case, the __reduce__ method returns a tuple (open, (filename, 'a'), ()), which means when the object is deserialized,
the open function is called with the specified filename ('/tmp/skid') and the mode 'a' (append mode). This will open the file /tmp/skid for writing,
but more importantly, it could be used to execute malicious code by manipulating what gets deserialized.


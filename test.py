from iotdb.Session import Session

ip = "10.12.180.244"
port_ = "6667"
username_ = "root"
password_ = "root"
session = Session(ip, port_, username_, password_)
session.open(False)
print("successful")
session.close()
print("successful")
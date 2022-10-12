import requests

r = requests.get("http://192.168.100.3:8080/hello_world")
string = r.text
assert string == "Hello World", "The strings don't match"
print(string)

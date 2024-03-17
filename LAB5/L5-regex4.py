import re
pattern4 = re.compile("[A-Z]{1}[a-z]+")
print(pattern4.findall("Feel Good inc"))

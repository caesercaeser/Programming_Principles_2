import re
pattern3 = re.compile("[a-z]+_[a-z]+")
print(pattern3.findall("Feel_Good good_inc"))

name = "vishu"
nameshort = name[0:3]
print(nameshort)  # Output: vis

print(name.upper())  # Output: VISHU
print(name.lower())  # Output: vishu
print(name.capitalize())  # Output: Vishu
print(name.replace("v", "V"))  # Output: Vishu
print(name.find("shu"))  # Output: 2
print(len(name))  # Output: 5
print(name.split("s"))  # Output: ['vi', 'hu']
print(name.index("u"))  # Output: 4
print(name.count("i"))  # Output: 1
print(name.startswith("vi"))  # Output: True
print(name.endswith("hu"))  # Output: True
print(name.isalpha())  # Output: True
print(name.isdigit())  # Output: False
print(name.strip())  # Output: vishu (no leading/trailing spaces to remove)
print(name.center(10, "-"))  # Output: --vishu---
print(name.ljust(10, "*"))  # Output: vishu*****
print(name.rjust(10, "*"))  # Output: *****vishu
print(name.swapcase())  # Output: VISHU
print(name.title())  # Output: Vishu
print(name.encode())  # Output: b'vishu'
print(name.endswith("u"))  # Output: True
print(name.startswith("vi"))  # Output: True
print(name.islower())  # Output: True
print(name.isupper())  # Output: False
print(name.istitle())  # Output: False
print(name.isprintable())  # Output: True
print(name.zfill(10))  # Output: 00000vishu
print(name.partition("s"))  # Output: ('vi', 's', 'hu')
print(name.rpartition("s"))  # Output: ('vi', 's', 'hu
print(name.splitlines())  # Output: ['vishu']
print(name.expandtabs())  # Output: vishu (no tabs to expand)
print(name.translate(str.maketrans("vishu", "VISHU")))  # Output: VISHU
print(name.removeprefix("vi"))  # Output: shu
print(name.removesuffix("hu"))  # Output: vis

# formatting
name = int(input('Введите имя   '))
string = "Hello  %s" % name 
string = "Hello  {}".format(name)
string = f"Hello  {name}"

print(string)

# methods
example = 'aaa  aAaAaAaAaA bbb ccc'
print(example.lower())
print(example.upper())
print(example.capitalize())


print(f"count of ccc in example = {example.count('ccc')}")
print(f"first occurence of substring bbb = {example.find('bbb')}")

print(f"раньше я выглядел вот так: {example}, но потом меня replace на {example.replace('aA', '1')}")
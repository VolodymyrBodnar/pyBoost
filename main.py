name = int(input('Введите имя   '))
string = "Hello  %s" % name 
string = "Hello  {}".format(name)
string = f"Hello  {name}"

print(string)
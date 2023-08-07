#list comprehension
#x = [x ** 4 for x in range(5)]
#print(x)

#print([n for n in range(11) if n%2 ==1])

pessoas = ['ana', 'Thiago ', 'JOÃO', 'PedrO']

#Ana = ' anA'
#print(Ana.strip().capitalize())

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas]

print(pessoas_normalizadas)
def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return str(a) + str(b)

result = function(5, '10')
print(result)

result = function('5','10')
print(result)

result = function(5,10)
print(result)
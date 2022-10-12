fruits=['mango','apple','grapes']
print(sorted(fruits))

fruit1=('mango','apple','grapes')
# sort method is not available in tuple bcz tuple are immutable 

fruit2={'mango','apple','grapes'}

print(sorted(fruit2))

cars=[
    {
        'name':'hello',
        'price':50000,
    },
    {
        'name':'hello',
        'price':40000,
    },
    {
        'name':'hello',
        'price':30000,
    },
    {
        'name':'hello',
        'price':10000,
    },
]
# sab kam price sy isko order karna 
print(sorted(cars , key = lambda d:d['price']))
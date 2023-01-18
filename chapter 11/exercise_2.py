#  function that return the string and first character is capital case 

def name(l ,**kwargs):
    if kwargs.get("reverse_string")== True:
        return [names[::-1].title() for names in l]
    else:
        return [names.title() for names in l]
l=['abu bakar' ,'waheed']

print(name(l, reverse_string=True))
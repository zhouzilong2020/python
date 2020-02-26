spam = ['apples', 'bananas', 'tofu', 'cats', 'asdasd', 'gwfwe']

def function(list):
    a = ''
    for i in range(len(list)-1):
        a += (list[i] + ', ')
    a += ("and " + list[i+1] + ".")
    return a


print(function(spam))
    

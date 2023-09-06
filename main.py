# write your code here
person = {
    'name':'Badreya',
    'age': 17,
    "hobbies" : ['Drawing','Knitting','Reading','playing piano'],
    }

print(person.get('name'))
print(person.get('age'))

person['age']=1000
person['country']= 'kuwait'
print(person)
print(len(person))
person["hobbies"].append("watching anime")
def check_hobbies(person):
    if len(person["hobbies"])>3:
        print('WOW YOU ARE AMAZING😎')
check_hobbies(person)

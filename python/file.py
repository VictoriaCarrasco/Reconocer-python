num1 = 42 #variable declaration number 
num2 = 2.3 #variable declaration number
boolean = True #variable declaration boolean 
string = 'Hello World' #Svariable declaration string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize, los diccionarios van con llaves. 
fruit = ('blueberry', 'strawberry', 'banana') #tuples initialize TUPLES VAN CON () PARENTESIS REDONDOS, no son editables. 
print(type (fruit)) #type check, type para verificar el tipo de variable
print(pizza_toppings[1])  #list acces value 
pizza_toppings.append('Mushrooms') #list add value, appendes como el push lo coloca al final 
print(person['name']) #acces value dictionary.
person['name'] = 'George' #dictionary change value 
person['eye_color'] = 'blue' #dictionary add value 
print(fruit[2]) #print access value 

if num1 > 45: #conditional if 
    print("It's greater")
else:
    print("It's lower") #conditional else

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15: #conditional elseif 
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #tiene una sintaxis diferente los bucles for, en este caso empieza con 5.
    if (x%5==0)
    print("es divisible")
    #para imprimir los multiplos de algún número. 
    print(x)
for x in range(2,5): #empieza en 2 y termina en 5 
    print(x)
for x in range(2,10,3): #arranca en el 2, 3 seria el valor del salto.
    print(x)

x = 0 #while start loop 
while(x < 5): #while stop 
    print(x)
    x += 1 #while increment 

pizza_toppings.pop()
pizza_toppings.pop(1) # list delete value, quita un elemento de la lista. 

print(person)
person.pop('eye_color') #dictionary delete value. 
print(person)

for topping in pizza_toppings: #for loop start 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for loop break 

def print_hello_ten_times(): # definicion de variables, se hacen con def y no con function 
    for num in range(10):
        print('Hello')

print_hello_ten_times() #function

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #function parameter 

def print_hello_x_or_ten_times(x = 10): #variable con parametro con defecto, si no le doy valor asume por defecto el 10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

#coment 

# multiline
""" 
Bonus section # multiline
"""

# print(num3) #single line #NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'. No tiene el metodo POP 
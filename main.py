# print(abs(-7)) 
# print(bool(0))
# print(bool(-11))
# print(bool(127))
# print(bool(""))
# print(bool("AHMED"))



# my_silly_list=[]
# print(bool(my_silly_list))

# my_silly_list=['h','k','g']
# print(bool(my_silly_list))

# x=eval(input("Please enter your age: "))
# print(x)

# x="print('Hello world')"
# eval(x)

# my_small_program='''print('meat')
# print('sandwich')'''
# exec(my_small_program)



# print(float(3))
# print(float('5'))
# print(float('5.6'))

# print(int(12.345))
# print(int('5'))


# print(len('this is a test string'))
# fingers=['thumb','index','middle','ring','pinky']
# print(len(fingers))
# enemies_map={'Batman':'Joker','superman':'Lex Luthon',
#              'Spiderman':'Green Goblin'}
# print(len(enemies_map))


# numbers=[5,4,10,30,22]
# print(max(numbers))

# strings='s,t,r,i,n,g,S,T,R,I,N,G'
# print(max(strings))
# print(max(10,300,450,50,90))

# numbers=[5,4,10,30,22]
# print(min(numbers))


# list_of_numbers=[0,50,100,150,200,250,300,350,400,450]
# print(sum(list_of_numbers))


# sentence="Hello, how are you today?"
# words=sentence.split()
# print(words)


# numbers="1,2,3,4,5"
# number_list=numbers.split(',')
# print(number_list)


# test_file=open('myfle.txt','w')
# test_file.write('What is green and loud? A frog\n')
# test_file.write('What is green and loud? A frog')
# test_file.close()

# test_file=open('myfle.txt')
# text=test_file.read()
# test_file.close()
# print(text)

# test_file=open('myfle.txt')
# text=test_file.readlines()
# test_file.close()
# print(text)


file = open("points.txt")

lines = file.readlines()
print(lines)
for line in lines:
    a = line.split()
    x = int(a[0])
    y = int(a[1])
    distance = abs(y - x)
    print(f"Distance between {x} and {y} is {distance}")

file.close()
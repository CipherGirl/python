"""
| Generator function               | Coroutine use                     |
| -------------------------------- | --------------------------------- |
| `yield` used to produce sequence | `yield` used to receive/send data |
| `next(gen)` only                 | `.send()` used actively           |
| Iteration over values            | Interaction with external caller  |
"""

import random

def bad_service_chatbot():
    answers = ["We don't do that",
               "We will get back to you right away",
               "Your call is very important to us",
               "Sorry, my manager is unavailable"]
    yield "Can I help you?"
    s = ''
    while True:
        if s is None:
            break
        s = yield random.choice(answers)

def pl_sentence(sentence):
    output = []
    for one_word in sentence.split():
        if one_word[0] in 'aeiou':
            output.append(one_word + 'way')
        else:
            output.append(one_word[1:] + one_word[0] + 'ay')
    return ' '.join(output)

def pig_latin_translator():
    s = ''
    while True:
        s = yield pl_sentence(s)
        if s is None:
            break

def switchboard():
    while True:
        choice = yield "1 for PL, 2 for support, 3 to exit"
        if choice == 1:
            yield from pig_latin_translator()
        elif choice == 2:
            yield from bad_service_chatbot()
        elif choice == 3:
            return
        else:
            print('Bad choice; try again')
    
s = switchboard()


print(next(s))
print(s.send(1))
print(next(s))
print(s.send("Hello"))
# print(s.send(None))
# print(s.send(1))
# print(s.send("Hello"))
# print(s.send("World"))

# def gen1():
#     x = 10
#     print("Before send:", x)
#     x = yield x     
#     print("After send:", x)

# g1 = gen1()
# next(g1)   
# try:
#     g1.send(123)
# except StopIteration:
#     print("Coroutine finished, continuing main program")   



# def gen2():
#     x = yield        
#     print("Received:", x)

# g2 = gen2()
# next(g2) 
# try:
#     g2.send(99)
# except StopIteration:
#     print("Coroutine finished, continuing main program")
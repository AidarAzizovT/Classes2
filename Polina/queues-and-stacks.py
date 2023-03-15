#list
# q = []
# q.append('eat')
# q.append('sleep')
# q.append('code')
# print(q)
# print(q.pop(0))  # 'eat'
# print(q)


# from queue import Queue
#
# q = Queue()
#
# q.put('eat')
# q.put('sleep')
# q.put('code')
#
# print(q)
# # <queue.Queue object at 0x1070f5b38>
#
# print(q.get())  # 'eat'
# print(q.get())  # 'sleep'
# print(q.get())


# # Implementing stack using the queue module
# from queue import LifoQueue
#
# # Initializing a my_stack stack with maxsize
# my_stack = LifoQueue(maxsize=5)
#
# # qsize() display the number of elements
# # in the my_stack
# print(my_stack.qsize())
#
# # put() function is used to push
# # element in the my_stack
# my_stack.put('x')
# my_stack.put('y')
# my_stack.put('z')
#
# print("Stack is Full: ", my_stack.full())
# print("Size of Stack: ", my_stack.qsize())
#
# # To pop the element we used get() function
# # from my_stack in
# # LIFO order
# print('\nElements poped from the my_stack')
# print(my_stack.get())
# print(my_stack.get())
# print(my_stack.get())
#
# print("\nStack is Empty: ", my_stack.empty())
from queue import Queue
queue = Queue()

def input_value():
    number = int(input('Input value'))
    if number > 0:
        queue.put(number)
    elif number == 0: #Thus we want to delete element from queue
        if queue.not_empty:
            print(min(queue))
            queue.pop(0)
        else:
            print(-1)




# n = int(input('How many operations with queue do you want to do? '))
#
# for i in range(n):
#     input_value()
# print(queue)

def find_sum(integer: int):
    print(integer)
















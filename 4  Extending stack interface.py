def stack():
    stack=[]
    num_of_queries=int(input())
    for i in range(num_of_queries):
        querylist=[]
        query=input()
        l1=query.split(" ")
        if len(l1)==1:
            if l1[0]=="pop":
                pop(stack)
            else:
                max(stack)
        else:
            push(int(l1[1]),stack)


def pop(stack):
    del stack[-1]
    return stack

def max(stack):
    big=stack[0]
    for i in range(1,len(stack)):
        if stack[i]>big:
            big=stack[i]
    print(big)
    return stack
def push(num,stack):
    stack.append(num)
    return stack

stack()
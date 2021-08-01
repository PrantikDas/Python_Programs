pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list = []
p=int(input("Enter the length of the list \n"))
print("Enter the elements of the list below")
for i in range(p):
    a = int(input())
    list.append(a)
n=int(input("Enter the number you want to find out \n"))
list.sort()
print(list)
if search (list,n):
    print("The value is located at position index",pos,"at sorted list",list)
else:
    print("The value has not been found \n")
input("The program has ended ;) \n")

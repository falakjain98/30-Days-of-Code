act = list(map(int,input().strip().split(' ')))
exp = list(map(int,input().strip().split(' ')))
fine = 0
if act[2]>exp[2]:
    fine = 10000
elif act[2]==exp[2]:
    if act[1]>exp[1]:
        fine = 500 * (act[1]-exp[1])
    elif act[1]<=exp[1] and act[0]>exp[0]:
        fine = 15 * (act[0]-exp[0])
print(fine)

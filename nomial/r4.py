import random


res1 = random.randrange(1, 11)          # 1 - 10范围内的随机整数
res2 = random.randrange(1, 11, 2)       # 1 - 10范围内每两个的随机整数
res3 = random.choice(range(1, 11, 2))   # 1 - 10范围内每两个的随机整数
print(res1, res2, res3)


res4 = random.randint(1, 10)            # 1 - 10范围内的随机整数
res5 = random.randrange(1, 11)          # 1 - 10范围内的随机整数
print(res4, res5)


res6 = random.choice(range(1, 11))            # 1 - 10范围内的随机整数
res7 = random.choice(["张三", "李四", "王五", "罗翔", "Alex", "Jone"])
print(res6, res7)


print("\n")

out_list = []
for i in range(1,121):
    random_number = random.uniform(0,1)
    if random_number < 0.75:
        # Append uniform random number between 0 - 25 with probability .75
        out_list.append(random.randint(0,25))
    else:
        #Append uniform random number between 0-75 with probability 0.25
        out_list.append(random.randint(25,100))

print(out_list)
import statistics
print(statistics.mean(out_list))


print("#######")
Number_of_users = 10
Average_score = 25

index = Number_of_users / 2
result = []

while index:
    index -= 1
    random_number = random.randint(0,51)
    result.append(random_number)
    result.append(50-random_number)

print (result)
print (sum(result))
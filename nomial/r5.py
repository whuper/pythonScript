import scipy.stats as stats
a,b = 1,5
mu,sigma = 4,3
dist = stats.truncnorm((a - mu) / sigma,(b - mu) / sigma,loc=mu,scale=sigma)
values = dist.rvs(121)


def show_list (list):
    for i in list:
        print(i, end=' ')
    print();
    
    t_sum = 0   
    t_average = 0.0

    t_sum = sum(list)
    t_average = round(t_sum/121,4)

    print("列表的和：" + str(t_sum))
    print("数量："+ str(len(list)));
    print("列表的平均数：" + str(t_average))

show_list(values)
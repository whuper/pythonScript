import random
import string

###################产生2个以上随机整数###################
###################第一个数随机产生，第二个使用平均数求出###################
#count 数字的个数
#average 平均数
#begin 起始区间
#end 结束区间
def int_random (average, begin, end):

    #print "wzh_random"
    # numarr = [0 for x in range(2)];
    numarr = [];
    i = 0;
    # while (1):
 
    #   num_first = random.randrange(begin, end);
    num_first = random.randint(begin, end);

    #第二个数
    num_second = average * 2 - num_first;

    numarr.append(num_first);
  
   
    if (num_second >= begin and num_second <= end):  
        numarr.append(num_second);
    else:
        # 继续分配,分为三个数
        rest_val_temp = average * 3 - num_first

        restTwo = re_random(rest_val_temp, begin, end,average)
        numarr.extend(restTwo)

    return numarr;

def re_random (rest_val, begin, end,average):
    numarr = [];
    random_number = random.uniform(0,1)
    if rest_val <= 10:
        if random_number <= 0.5:
            # 大值与小值
            numarr.append(end)
            numarr.append(rest_val - end)
        else:
            # 平均分
            if (rest_val % 2) == 0:
                #偶数
                numarr.append(rest_val/2)
            else:
                #奇数
                numarr.append(rest_val//2)
                numarr.append(rest_val//2 + 1)
    else:
        rest_val2 = rest_val + average
        mean_temp =    rest_val2//3
        numarr.append(mean_temp)
        numarr.append(mean_temp)
        numarr.append(rest_val2-mean_temp*2)

    """     
    for i in range(len(numarr)):
        if numarr[i] > end: 
    """

            

    return numarr;





###################产生随机数###################
###################第一个数随机产生，第二个使用平均数求出###################
#count 数字的个数
#average 平均数
#begin 起始区间
#end 结束区间
def float_random (count, average, begin, end):

    #print "wzh_random"
    numarr = [0 for x in range(2)];
    i = 0;
    while (1):
 
      num = random.uniform(begin, end);
      #取两位小数
      num_first = round(num, 2);

      #第二个数
      num_second = average * 2 - num_first;

      if (num_second >= begin and num_second <= end):
          numarr[i] = num_first;
          i = i + 1;
          numarr[i] = num_second;
          break

    return numarr;



###################写文件###################
def write_file (filename, content):
    fo = open (filename, "rb+");
    fo.write(bytes(content,'utf-8'));
    # fo.write(content);
    fo.close();

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

###################主函数调用产生整形随机数###################

def test_random_int():
    count = 121;
    average = 4;
    begin = 1;
    end = 5;
    numarr_count = 0;
    numarr = [0 for x in range(count)];
    # for i in range (count // 2):
    while(numarr_count < count):
        templist = int_random (average, begin, end)
        j = 0;
        for j in range (len(templist)):
             numarr[numarr_count] = templist[j];
             numarr_count += 1;

    
    print("修正前 ######：")
    show_list (numarr)
    # 数据修正开始
    #if (count % 2) != 0:
     #   numarr[count-1] = random.randint(begin, end);

    t_average2 = round(sum(numarr)/count,4)
    if(  t_average2 < average):
        # 差了多少没有分配
        undistributed = round(count * round((average - t_average2),4),4)
        print("undistributed: " + str(undistributed))
        # if(undistributed <= end):
        # numarr[count-1] = int(undistributed)
        # else:


        
    


             
    content = '';
    #打乱排序
    print("修正后 ######：")
    print("数据未打乱：");
    show_list (numarr)
    """     
    random.shuffle(numarr);
        print("数据打乱：");
        show_list (numarr) 
    """
    for i in numarr:
        content = content + "\n" + str(i)
    #print content;
    #追加写入文件
    filename = "test3.txt";
    print("文件名称：",filename);
    write_file (filename, content)
    write_file (filename, "\n");

###################主函数调用产生实型随机数###################
#40个数字，平均数400，363 - 429 之间
def test_random_float():
    count = 40;
    average = 402;
    begin = 363;
    end = 429;
    numarr_count = 0;
    numarr = [0 for x in range(count)];
    for i in range (count // 2):
        list = float_random (40, 402, 363, 429)
        j = 0;
        for j in range (len(list)):
             numarr[numarr_count] = list[j];
             numarr_count += 1;
    content = '';
    #打乱排序
    print("数据未打乱：");
    show_list (numarr)
    random.shuffle(numarr);
    print("数据打乱：");
    show_list (numarr)
    for i in numarr:
        content = content + ' ' + str(i);
    #print content;
    #追加写入文件
    filename = "test2.txt";
    print("文件名称：",filename);
    write_file (filename, content)
    write_file (filename, "\n");

#调用测试产生整形随机数
test_random_int();
#调用测试产生实型随机数
# test_random_float();

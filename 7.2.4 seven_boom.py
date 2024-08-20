def seven_boom(end_num):
    num_list = []
    for num in range(0, int(end_num)):
        if num == 7 or '7' in str(num) or num % 7 == 0:
            num_list.append('boom')
        else:
            num_list.append(num)
    return num_list



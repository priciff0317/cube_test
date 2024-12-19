
# Task1
def change_list_num_digits(change_list):
    result = []
    for i in change_list:
        digit = str(int(i%10))
        ten_digit = str(int(i/10))
        if digit == '0':
            digit = ''
        exchange_digit = int(digit+ten_digit)
        result.append(exchange_digit)
    print("Task1")
    print(result)
    print("\n")

input_arr = []

change_list_num_digits([35, 46, 57, 91, 29])

# Task2

def calculate_text(text):
    split_text = text.split(' ')
    merge_test = ''
    #過濾空白
    for i in split_text:
        merge_test += i
    
    arr_calculate_result = []
    # 將小寫字元改成大寫
    merge_test=merge_test.upper()
    
    #找要計算的字元
    for i in merge_test:
        if i not in arr_calculate_result:
            arr_calculate_result.append(i)
        else:
            continue
    #計算字元
    for i in range(len(arr_calculate_result)):
        total_char = merge_test.count(arr_calculate_result[i])
        arr_calculate_result[i] += " "+str(total_char)
        print(arr_calculate_result[i])
print("Task2")       
calculate_text("Hello welcome to Cathay 60th year anniversary")
print("\n")

#Task3
def find_order(num):
    arr_order = [x for x in range(1,num+1)]
    while len(arr_order) > 1:
        for i in range(0,3):
            if i == 2:
                arr_order.pop(0)
            else:
                temp = arr_order.pop(0)
                arr_order.append(temp)
        print(arr_order)
    # if len(arr_order) == 1:
    #     print(arr_order)

    print(f'第{arr_order[0]}順位')
find_order(50)




def test_config():
    return True

def loop_string_w_while(str):
    i = 0
    
    while i < len(str):
        print(i, "i < len(str)", i < len(str) , str[i])
        i += 1  

def loop_string_w_for_range(str):
    for i in range(len(str)):
        print(i, "i in range ", len(str),  str[i])

def loop_string_w_for(str):
    for char in str:#magic loop
        print(char)

def get_x_char_cnt_of_string(str, x_char):
    cnt = 0

    for char in str:
        if char == x_char:
            cnt += 1
    
    return cnt

def string_concatenation(str1, str2):
    return str1 + str2 #a new string is created in memory
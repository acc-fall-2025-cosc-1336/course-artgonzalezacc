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
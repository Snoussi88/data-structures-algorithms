'''Huffman Coding'''
#inputs2 = {"a":5,"b":9,"c":12,"d":13,"e":16,"f":45}
#unordered dictionnary
# unordered inputs dict ==> ordered


def sort_dict(inputs):
    frequencies_list = list(inputs.keys())
    frequencies_list.sort()
    temp = []
    for  item in frequencies_list:
        temp.append(inputs[item])
    new_dict = dict(zip(frequencies_list,temp))
    return new_dict



def huffmanTree(inputs):
    temp = sort_dict(inputs)#temporary sorted dict
    condition_arg =  list(temp.keys())
    condition = len(condition_arg) > 1
    while condition:
        temp = sort_dict(temp)
        char = list(temp.values())
        freq = list(temp.keys())
        if len(char) > 1 and len(freq) > 1:
            freq0 = freq.pop(0)
            freq1 = freq.pop(0)
            value0 = char.pop(0)
            value1 = char.pop(0)
        else:
            break
        temp = {freq0+freq1:(value0,value1)}
        remain_temp = dict(zip(freq,char)) 
        temp.update(remain_temp)
    return temp


def huffman_encode(char,inputs):
    temp = huffmanTree(inputs)
    temp = list(temp.values())
    temp = temp[0]
    print(temp)
    search(temp,char,"")

def search(root,char,code):
    code = code
    if(len(root)>1):
        search(root[0],char,code+"0")
        search(root[1],char,code+"1")
    else:
        if (root == char):
            print(code)
            




inputs1 = {12:"c",16:"e",9:"b",13:"d",5:"a",16:"e",45:"f"}
input2 = {10:'a',15:'b',30:'c',16:'d',29:'e'}

huffman_encode('a',inputs1) #should print 010


'''
作业：根据词典，输出一段文本所有可能的切割方式
'''


#词典，每个词后方存储的是其词频，仅为示例，也可自行添加
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

sentence = "经常有意见分歧"

"""
预期输出
[['经常', '有意见', '分歧'], 
 ['经常', '有意见', '分', '歧'],
 ['经常', '有', '意见', '分歧'], 
 ['经常', '有', '意见', '分', '歧'], 
 ['经常', '有', '意', '见分歧'], 
 ['经常', '有', '意', '见', '分歧'], 
 ['经常', '有', '意', '见', '分', '歧'], 
 ['经', '常', '有意见', '分歧'], 
 ['经', '常', '有意见', '分', '歧'], 
 ['经', '常', '有', '意见', '分歧'], 
 ['经', '常', '有', '意见', '分', '歧'], 
 ['经', '常', '有', '意', '见分歧'], 
 ['经', '常', '有', '意', '见', '分歧'], 
 ['经', '常', '有', '意', '见', '分', '歧']]
"""

def sliceSentence(subSentence):
    global Dict
    ret = []
    for i in range(1, len(subSentence)+1):
        if subSentence[:i] in Dict:
            # 结束并有效的直接返回
            if i == len(subSentence):
                ret.append([subSentence[:i]])
                continue
            
            #没结束就把后面的字句作为参数
            r = sliceSentence(subSentence[i:])
            for n in r:
                n.insert(0, subSentence[:i])
            ret += r
    return ret
    
ret = sliceSentence(sentence)
for l in ret[::-1]:
    print(l)


    
    
                
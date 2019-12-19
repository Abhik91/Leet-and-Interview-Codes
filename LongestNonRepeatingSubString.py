#Program to find Length of Longest Substring
#@author - Abhik Dey

def lengthOfLongestSubstring(s):
    nonRepChar=[]
    lenRes=0
    for i in s:
        if i not in nonRepChar:
            nonRepChar.append(i)
            lenNew=len(nonRepChar)
        else:
            idx=nonRepChar.index(i)
            print (idx)
            print (nonRepChar[0:idx+1])
            del nonRepChar[0:idx+1]
            nonRepChar.append(i)
        lenRes=max(lenNew,lenRes)    
    return lenRes

print('Length of Longest Substring - ',lengthOfLongestSubstring('pwwkew'))
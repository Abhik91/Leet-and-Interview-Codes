def jumpingOnClouds(c):

    i = 0
    hop = 0
    while (i < len(c)):
        print (i)
        if (i+2 < len(c) and c[i+2] == 0):
            print ("inside if i", i)
            hop +=1
            i +=2
        else:
            print ("inside else i", i)
            hop +=1
            i +=1
    return hop

if __name__ == '__main__':
    c = [0,0,1,0,0,1,0]
    hp = jumpingOnClouds(c)
    print (hp)

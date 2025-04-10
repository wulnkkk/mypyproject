from process import a,b
_Constant=[a,b]
def key_generate(astr=str):
    '''
    astr:小写英文字母组成的字符串
    '''
    _alist='a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z'.split('、')
    n=0
    s=[]
    tstr=[]
    for i in astr:
        if n<len(astr)//2:
            s.append(i)
            n+=1
        else:
            tstr.append(s)
            s=[i]
            n=1
    else:
        if len(tstr)<2:
            tstr.append(s)
        else:
            tstr[1]=tstr[1]+s
    key1=tstr[0][0]+tstr[1][0]
    key2=[]
    key3=[]
    for x in range(2):
        num=0
        for i in tstr[x]:
            num+=_alist.index(i)
        key2.append(_alist[num//len(tstr[x])])
        key3.append(_Constant[x][num//len(tstr[x])])
    key=key1.capitalize()+"@"+key2[0].capitalize()+key2[1]+'#'+key3[0]+key3[1]
    return key

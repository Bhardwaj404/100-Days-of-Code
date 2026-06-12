class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        # d1=(sorted(d.items()))
        # return d1.values()
        l=[]
        while len(d)>0:
            max_key=max(d)
            l.append(d[max_key])
            del d[max_key]
        return l
        #array of strings names
        #array heights
        #both of len n

            
class Solution:
    def countAsterisks(self, s: str) -> int:
        s2=s.split("|")
        c=0
        for i in range(len(s2)):
            if i%2==0:
                c=c+s2[i].count("*")
        return c

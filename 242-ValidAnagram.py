class Solution(object):

    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        #s boyunca dön
        for i in range(len(s)):
            #birinci alan countS[] dizisine s nin i ninci karakterini ekliyor
            #eşittirden sonraki alan sa countS içerisinde s[i] si var mı diye bakılıyor 
            #ve bir artırılıp countS[s[i]] ye ekleniyor
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #countS nin içi dolaşılıyor ve countS içinde countT ile aynı olmayan bişey varsa false dönüyor
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
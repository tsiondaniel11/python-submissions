class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s.replace('10#','j').replace('11#','k').replace('12#','l').replace('13#','m').replace('14#','n').replace('15#','o')
        s = s.replace('16#','p').replace('17#','q').replace('18#','r').replace('19#','s').replace('20#','t').replace('21#','u')
        s = s.replace('22#','v').replace('23#','w').replace('24#','x').replace('25#','y').replace('26#','z')
        s = s.replace('1','a').replace('2','b').replace('3','c').replace('4','d').replace('5','e').replace('6','f').replace('7','g')
        s = s.replace('8','h').replace('9','i')
        return s     

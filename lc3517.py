    def smallestPalindrome(self, s):
        f=Counter(s)
        l=[]
        m=""
        for ch in sorted(f):
            l.append(ch*(f[ch]//2))
            if f[ch]%2==1:
                m=ch
        l="".join(l)
        return l+m+l[::-1]
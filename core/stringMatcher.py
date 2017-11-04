def stringMatcher(s, t):
        ''' From Wikipedia article; Iterative with two matrix rows. '''
        if s == t: return 100.0
        elif len(s) == 0: return len(t)
        elif len(t) == 0: return len(s)
        v0 = [None] * (len(t) + 1)
        v1 = [None] * (len(t) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(s)):
            v1[0] = i + 1
            for j in range(len(t)):
                cost = 0 if s[i] == t[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]
        flag = 0
        if (len(s) != len(t)):
            flag = 1
        value = v1[len(t)]
        return ((max(len(s), len(t)) - value)  * 100 / max(len(s), len(t)))

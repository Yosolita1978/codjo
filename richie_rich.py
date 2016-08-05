def make_palindrome(s, k):
    new_s = ""
    x = 0
    y = len(s)-1
    count = 0

    while x < y:
        new_s = new_s + s[x]


        if s[x] != s[y]:
            count = count + 1

            if s[x] < s[y]:
                new_s = new_s.replace(s[x],s[y])
            
                    

        x = x + 1
        y = y - 1

    if count > k:
        return -1
    
    return new_s + "".join(reversed(new_s))

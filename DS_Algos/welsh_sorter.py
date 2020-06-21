ABCD = ['a', 'b', 'c', 'ch', 'd', 'dd', 'e', 'f', 'ff', 'g',
        'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph',
        'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']

order = {ABCD[i]:i for i in range(len(ABCD))}

def welsh_sorter(data):
    from functools import cmp_to_key

    def helper(s1, s2):
        i, j = 0, 0

        while i < len(s1) and j < len(s2):
            s1_part = s1[i]
            i += 1

            if i < len(s1):
                if s1[i-1:i+1] in order:
                    s1_part = s1[i-1:i+1]
                    i += 1

            s2_part = s2[j]
            j += 1

            if j < len(s2):
                if s2[j-1:j+1] in order:
                    s2_part = s2[j-1:j+1]
                    j += 1
            
            if s1_part != s2_part:
                return order[s1_part] - order[s2_part]
        
        return (len(s1)-i) - (len(s2)-j)

    return sorted(data, key=cmp_to_key(helper))

assert welsh_sorter(['cudd', 'chde', 'cude']) == ['cude', 'cudd', 'chde']


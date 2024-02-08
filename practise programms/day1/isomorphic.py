def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping_s_to_t = {}
    mapping_t_to_s = set()

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            if char_t in mapping_t_to_s:
                return False
            mapping_s_to_t[char_s] = char_t
            mapping_t_to_s.add(char_t)

    return True


print(isIsomorphic("egg", "add"))      
print(isIsomorphic("foo", "bar"))      
print(isIsomorphic("paper", "title")) 
print(isIsomorphic("fry", "sky"))     
print(isIsomorphic("apples", "apple"))

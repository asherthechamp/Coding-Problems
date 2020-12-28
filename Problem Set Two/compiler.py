# Valid set of opening and closing braces

class Solution:
  def is_valid(self, s):
    open_brace_array = []
    close_brace_string = ""
    for i in range(0, len(s)):
        if (s[i] in "{[("):
            open_brace_array.append(s[i])
        if (s[i] in "}])" and len(open_brace_array) != 0 and s[i] == match(open_brace_array[-1])):
            open_brace_array.pop()
    if (len(open_brace_array) == 0 or s == ""):
        return True
    else:
        return False

def match(s):
    m = ""
    if(s == "{"):
        m = "}"
    if(s == "("):
        m = ")"
    if(s == "["):
        m = "]"
    return m

s = "([{}])()"
# should return True
print(Solution().is_valid(s))

s = "()(){(())"
# should return False
print(Solution().is_valid(s))

s = ""
# should return True
print(Solution().is_valid(s))


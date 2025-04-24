def solution(s):
    if not s:
        return ""
    
    return "".join(" " + c if c.isupper() else c for c in s)
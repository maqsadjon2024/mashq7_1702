#47
def kopaytir(lst, n):
    return lst * n

print(kopaytir([1,2],3))

#48
def ascii_kod(c):
    return ord(c)

print(ascii_kod("A"))

#49
def harf(kod):
    return chr(kod)

print(harf(65))

#50
def faqat_harf(text):
    return ''.join(c for c in text if c.isalpha())

print(faqat_harf("salom123!!!"))

#51
def manfiy_sanash(lst):
    return sum(1 for x in lst if x < 0)

print(manfiy_sanash([-1,2,-3,4,-5]))

LONGEST_KEY = 1

initials = {
    "ม": "ม",
    "ป": "ป",
    "พ": "พ",
    "ง": "ง",
    "ก": "ก",
    "ค": "ค",
    "มป": "จ",
    "ปพ": "บ",
    "มพ": "ฟ",
    "งก": "ย",
    "กค": "อ",
    "งค": "ห",
    "มง": "น",
    "ปก": "ต",
    "พค": "ท",
    "มงปก": "ช",
    "ปกพค": "ด",
    "มงพค": "ส"
}
clusters = {
    "ร": "ร",
    "ว": "ว",
    "รว": "ล"
}
vowels_f = {
    "ี": "iิf",      # นิก
    "ู": "iุf",      # นุก
    "ีู": "iึf",      # นึก
    "แ": "แi็f",    # แน็ก
    "อ": "i็อf",    # น็อก
    "แอ": "iัf",    # นัก
    "ีแ": "เi็f",    # เน็ก
    "ูอ": "if",     # นก
    "ีูแอ": "เiิf",   # เนิก
    "ีแอ": "เiียf",  # เนียก
    "ูแอ": "iวf",   # นวก
    "ีูแ": "เiือf",   # เนือก
    "ีูอ": "เiือf",
    "—": "",       # Long vowel marker
    "ี—": "iีf",     # นีก
    "ู—": "iูf",     # นูก
    "ีู—": "iืf",     # นืก
    "แ—": "แif",   # แนก
    "อ—": "iอf",   # นอก
    "แอ—": "iาf",  # นาก
    "ีแ—": "เif",   # เนก
    "ูอ—": "โif",   # โนก
    "ีูแอ—": "เiอf", # เนอก
    "ีแอ—": "เiียf", # เนียก
    "ูแอ—": "iวf",  # นวก
    "ีูแ—": "เiือf",  # เนือก
    "ีูอ—": "เiือf"
}
vowels_nf = {
    "ี": "iิ",      # นิ
    "ู": "iุ",      # นุ
    "ีู": "iึ",      # นึ
    "แ": "แiะ",   # แนะ
    "อ": "เiาะ",  # เนาะ
    "แอ": "iะ",   # นะ
    "ีแ": "เiะ",   # เนะ
    "ูอ": "โiะ",   # โนะ
    "ีูแอ": "เiอะ", # เนอะ
    "ีแอ": "เiียะ", # เนียะ
    "ูแอ": "iวะ",  # นัวะ
    "ีูแ": "เiือะ",  # เนือะ
    "ีูอ": "เiือะ",
    "—": "",      # Long vowel marker
    "ี—": "iี",     # นี
    "ู—": "iู",     # นู
    "ีู—": "iื",     # นื
    "แ—": "แi",   # แน
    "อ—": "iอ",   # นอ
    "แอ—": "iา",  # นา
    "ีแ—": "เi",   # เน
    "ูอ—": "โi",   # โน
    "ีูแอ—": "เiอ", # เนอ
    "ีแอ—": "เiีย", # เนีย
    "ูแอ—": "iัว",  # นัว
    "ีูแ—": "เiือ",  # เนือ
    "ีูอ—": "เiือ"
}
finals = {
    "ม": "ม",
    "ป": "ป",
    "พ": "พ",
    "ง": "ง",
    "ก": "ก",
    "ค": "ค",
    "ปม": "จ",
    "พป": "บ",
    "พม": "ฟ",
    "กง": "ย",
    "คก": "อ",
    "คง": "ห",
    "มง": "น",
    "ปก": "ต",
    "พค": "ท",
    "ปกมง": "ช",
    "พคปก": "ด",
    "พคมง": "ส"
}
vf_overrides = { # Exceptions for some irregularly written stuff
    "iัfย": "ไi", # ตัย -> ไต
    "iัfว": "เiา" # กัว* -> เกา
}

def translate(key, arr):
    if key == '':
        return ''
    elif key not in arr:
        #raise KeyError # Combination does not follow base theory and is a brief
        return key
    else:
        return arr[key]
        
def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY) 
    stroke = key[0]
    
    #print("custom lookup called with " + stroke)
    
    after_vowel = False
    initial  = ""
    icluster = ""
    vowel    = ""
    fcluster = ""
    final    = ""
    
    for ch in stroke:
        # Initial
        if ch in initials and after_vowel == False:
            #print(ch + "is initial")
            initial = initial + ch
        # icluster
        elif ch in clusters and after_vowel == False:
            #print(ch + "is icluster")
            icluster = icluster + ch
        # Vowel
        elif ch in vowels_f:
            #print(ch + "is vowel")
            after_vowel = True # Boo necessary imperative code
            vowel = vowel + ch
        # fcluster
        elif ch in clusters and after_vowel == True:
            #print(ch + "is fcluster")
            fcluster = fcluster + ch
        # Final
        elif ch in finals and after_vowel == True:
            #print(ch + "is final")
            final = final + ch
        else:
            print(ch + "is ghost")
            raise KeyError # Not a key I know about
    
    # Translate the strokes
    initial  = translate(initial,  initials)
    icluster = translate(icluster, clusters)
    fcluster = translate(fcluster, clusters)
    final    = translate(final,    finals)
    if (fcluster + final) == "":
        vowel = translate(vowel, vowels_nf)
    else:
        vowel = translate(vowel, vowels_f)
    
    # Form final string
    if (vowel+fcluster+final) in vf_overrides:
        output = vf_overrides[vowel+fcluster+final]
    else:
        output = vowel
    output = output.replace("i", initial + icluster, 1)
    output = output.replace("f", fcluster + final,   1)
    
    return output
    
# Test
# print(lookup(["ปรแอรพค—"])) # ปรารท

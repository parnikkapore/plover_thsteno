import re

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
    "นี": "นิ่บ",      # นิก
    "นู": "นุ่บ",      # นุก
    "นีู": "นึ่บ",      # นึก
    "นแ": "แน็่บ",    # แน็ก
    "นอ": "น็่อบ",    # น็อก
    "นแอ": "นั่บ",    # นัก
    "นีแ": "เน็่บ",    # เน็ก
    "นูอ": "น่บ",     # นก
    "นีูแอ": "เนิ่บ",   # เนิก
    "นีแอ": "เนี่ยบ",  # เนียก
    "นูแอ": "น่วบ",   # นวก
    "นีูแ": "เนื่อบ",   # เนือก
    "นีูอ": "เนื่อบ",
    # "ล": Long vowel marker
    "นีล": "นี่บ",     # นีก
    "นูล": "นู่บ",     # นูก
    "นีูล": "นื่บ",     # นืก
    "แล": "แน่บ",   # แนก
    "อล": "น่อบ",   # นอก
    "แอล": "น่าบ",  # นาก
    "นีแล": "เน่บ",   # เนก
    "นูอล": "โน่บ",   # โนก
    "นีูแอล": "เนิ่บ",  # เนิก
    "นีแอล": "เนี่ยบ", # เนียก
    "นูแอล": "น่วบ",  # นวก
    "นีูแล": "เนื่อบ",  # เนือก
    "นีูอล": "เนื่อบ"
}
vowels_nf = {
    "นี": "นิ่",      # นิ
    "นู": "นุ่",      # นุ
    "นีู": "นึ่",      # นึ
    "แ": "แน่ะ",   # แนะ
    "อ": "เน่าะ",  # เนาะ
    "แอ": "น่ะ",   # นะ
    "นีแ": "เน่ะ",   # เนะ
    "นูอ": "โน่ะ",   # โนะ
    "นีูแอ": "เน่อะ", # เนอะ
    "นีแอ": "เนี่ยะ", # เนียะ
    "นูแอ": "นั่วะ",  # นัวะ
    "นีูแ": "เนื่อะ",  # เนือะ
    "นีูอ": "เนื่อะ",
    # "ล": Long vowel marker
    "นีล": "นี่",     # นี
    "นูล": "นู่",     # นู
    "นีูล": "นื่อ",    # นือ
    "แล": "แน่",   # แน
    "อล": "น่อ",   # นอ
    "แอล": "น่า",  # นา
    "นีแล": "เน่",   # เน
    "นูอล": "โน่",   # โน
    "นีูแอล": "เน่อ", # เนอ
    "นีแอล": "เนี่ย", # เนีย
    "นูแอล": "นั่ว",  # นัว
    "นีูแล": "เนื่อ",  # เนือ
    "นีูอล": "เนื่อ"
}
finals = {
    "ง":    "ง",
    "มง":   "น",
    "ม":    "ม",
    "ย":    "ย",
    "ว":    "ว",
    "งย":   "ก",
    "มว":   "บ",
    "มงวย": "ด"
}
vf_overrides = { # Exceptions for some irregularly written stuff
    "นัtfย": "ไน่", # ตัย -> ไต
    "นัtfว": "เน่า", # กัว* -> เกา
    "นัtfม": "น่ำ"  # นัม -> นำ
}

tonekeys = {
    "": 0,
    "ส": 2,
#   "ข": 3,
    "ต": 1,
    "สข": 3,
    "ตข": 4,
#   "สต": 0,
#   "สตข": 3
}
# อ - 0
# อ่ ต 1
# อ้ ส 2
# อ๊ ข/สข 3
# อ๋ ขต 4

tones = {
    ("mid","live","short"): ['น', 'น่', 'น้', 'น๊', 'น๋'],
    ("mid","live","long"): ['น', 'น่', 'น้', 'น๊', 'น๋'],
    ("mid","dead","short"): ['น', 'น', 'น้', 'น๊', 'น๋'],
    ("mid","dead","long"): ['น', 'น', 'น้', 'น๊', 'น๋'],
    ("low_p","live","short"): ['น', 'ส่', 'น่', 'น้', 'ส'], # ต่ำคู่/สูง
    ("low_p","live","long"): ['น', 'ส่', 'น่', 'น้', 'ส'],
    ("low_p","dead","short"): ['น', 'ส', 'น่', 'น', 'น๋'],
    ("low_p","dead","long"): ['น', 'ส', 'น', 'น้', 'น๋'],
    ("low","live","short"): ['น', 'ห่', 'น่', 'น้', 'ห'], # เฉพาะต่ำเดี่ยว
    ("low","live","long"): ['น', 'ห่', 'น่', 'น้', 'ห'],
    ("low","dead","short"): ['น', 'ห', 'น่', 'น', 'น๋'],
    ("low","dead","long"): ['น', 'ห', 'น', 'น้', 'น๋'],
}
cons_class = {
    "ก": "mid", "จ": "mid", "ด": "mid", "ต": "mid",
    "บ": "mid", "ป": "mid", "อ": "mid",
    
    "ค": "low_p", "ช": "low_p", "ท": "low_p","พ": "low_p", "ฟ": "low_p",
    "ส": "high", "ห": "high",
    
    "ง": "low", "น": "low", "ย": "low", "ร": "low", "ว": "low",
    "ม": "low", "ล": "low"
}
lhpair = {
    "ค": "ข", "ช": "ฉ", "ท": "ถ","พ": "ผ",
    "ฟ": "ฝ","ซ": "ส",
    "ฮ": "ห"
}
hlpair = {h:l for (l,h) in lhpair.items()}

def isLong(longmkr):
    return True if longmkr=="ล" else False

def liveness(final, isLong):
    if final=="": return "live" if isLong else "dead"
    else:
        if final in "นมยวง": return "live"
        if final in "กบด":  return "dead"
        return "live"

def reformat_data_tables():
    # van Rossum is making all subroutine programmers sweat
    global vowels_f, vowels_nf, vf_overrides
    
    MAI_EK = "น่".replace("น","")
    def normalize(txt): return txt.replace("น","i").replace("บ","f").replace(MAI_EK, "t")
    
    vowels_f =     { k.replace("น","") : normalize(v) for (k,v) in vowels_f.items()}
    vowels_nf =    { k.replace("น","") : normalize(v) for (k,v) in vowels_nf.items()}
    vf_overrides = { k.replace("น","i"): normalize(v) for (k,v) in vf_overrides.items()}
reformat_data_tables()

def translate(key, arr, fallback=None):
    if key == '':
        return ''
    elif key not in arr:
        return fallback or key
    else:
        return arr[key]
        
def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    stroke = key[0]
    
    # print("custom lookup called with " + stroke)
    
    # normalise stroke from embedded number, to preceding hash format
    # src: Emily's Symbols
    if any(k in stroke for k in "1234506789"):  # if chord contains a number
        stroke = list(stroke)
        numbers = ["O", "S", "T", "P", "H", "A", "F", "P", "L", "T"] # TODO: Change this to Thai keys
        for key in range(len(stroke)):
            if stroke[key].isnumeric():
                stroke[key] = numbers[int(stroke[key])]  # set number key to letter
                numberFlag = True
        stroke = ["#"] + stroke
        stroke = "".join(stroke)
    
    # Zones in layout:
    # Initial     มงปกพค
    # Icluster          รว
    # Vowel               อีอูแอ
    # Tone                    สตขล
    # final                       มงวย
    # fext                            รฟ
    match = re.fullmatch(r'([มงปกพค]*)([รว]*)([ีูA\*#\-แอ]*)([สตข]*)(ล?)([มงวย]*)([รฟ]*)', stroke)
    (initial,icluster,vowel,tone,longmkr,final,fext) = match.groups()

    # Normalize everything
    shift = re.search(r'[\*#]+', vowel)                  # Fetch "shift keys" (*, #)
    shift = shift.group() if shift is not None else ""
    vowel = re.sub(r'[\*#\-]+', "", vowel, 1)            # Remove *-# from the vowel group
    vowel += longmkr                                     # Add long marker to vowel group
    
    # print("!a", initial,icluster,vowel,tone,final,fext,shift)
    
    # Translate the strokes
    initial  = translate(initial,  initials)
    icluster = translate(icluster, clusters)
    final    = translate(final,    finals)
    fext     = fext # This zone has no fixed meaning
    
    # Translate vowel (form depends on if a final exists)
    if vowel=="" or vowel=="ล": # No vowel
        vowel = f"it-{vowel}f"
    elif (final) == "":         # Has vowel, no final
        vowel = translate(vowel, vowels_nf, f"it{vowel}")
    else:                       # Has vowel, has final
        vowel = translate(vowel, vowels_f, f"it{vowel}f")
    
    # Normalize high characters into low-paired
    initial_class = translate((initial+icluster)[0:1], cons_class, "mid")
    if initial_class == "high":
        initial = hlpair[initial]
        initial_class = "low_p"
    
    # determine tone mark
    
    if tone in tonekeys:
        tone = tones[(initial_class,
                      liveness(final, isLong(longmkr)),
                      "long" if isLong(longmkr) else "short")
                    ][tonekeys[tone]]
    else:
        final = tone + final # Print the invalid tone strokes before the final
        tone = ""
    
    tone = tone.replace("น", "")
    
    # ต = transform initial into low variant
    if "ต" in tone:
        tone = tone.replace("ต", "")
        initial = hlpair[initial]
        
    # ส = transform initial into high variant
    if "ส" in tone:
        tone = tone.replace("ส", "")
        initial = lhpair[initial]
        
    # ห = add a ห before the initial (orthography rule)
    if "ห" in tone:
        tone = tone.replace("ห", "")
        initial = "ห" + initial
    
    # print("!b", initial,icluster,vowel,tone,final,fext,shift)
    
    # Form output string
    if (vowel+final) in vf_overrides:
        output = vf_overrides[vowel+final]
    else:
        output = vowel
    output = (output.replace("i", initial + icluster, 1)
                    .replace("f", final,              1)
                    .replace("t", tone,               1)
                    + (fext or "")
                    + (shift or "")
             )
    
    return output
    
# Test
# print(lookup(["กร*แอลมว"])) # กราบ*
# print(lookup(["พค-แอม"])) # ทำ
# print(lookup(["กคีแลมง"])) # เอน
# print(lookup(["กูแอล"])) # กัว
# print(lookup(["กแอว"])) # เกา
# print(lookup(["มงแอตลมว"])) # หนาบ
# print(lookup(["มงแอสขมง"])) # นั้น
# print(lookup(["มงูสล"])) # นู่
# print(lookup(["พคแอสตมว"])) # ทัสตบ

# Thsteno - Fingerspelling dictionary
# Strokes corresponding to keyboard keys, for manual typing

# Normalize key names (so the in-file format can be easier to render)
def N(key): return key.replace("ก","")

translations = {
# Consonants ##################################################################

"ม": "ม",

"ป": "ป",

"พ": "พ",
"พ*": "ภ",
"#พ": "ผ",

"ร": "ร",

"ง": "ง",

"ก": "ก",

"ค": "ค",
"ค*": "ข",
"#ค": "ฆ",

"ว": "ว",

"มป": "จ",

"ปพ": "บ",

"มพ": "ฟ",
"มพ*": "ฝ",

"งก": "ย",
"งก*": "ญ",

"กค": "อ",

"งค": "ห",
"งค*": "ฮ",

"รว": "ล",
"รว*": "ฬ",

"มง": "น",
"มง*": "ณ",

"ปก": "ต",
"ปก*": "ฏ",

"พค": "ท",
"พค*": "ถ",
"#พค*": "ธ",
"มปพ": "ฐ",
"มปพ*": "ฑ",
"#มปพ*": "ฒ",

"มงปก": "ช",
"มงปก*": "ฉ",
"#มงปก*": "ฌ",

"ปกพค": "ด",
"ปกพค*": "ฎ",

"มงพค": "ส",
"มงพค*": "ศ",
"#มงพค*": "ซ",
"งกค": "ษ",

# Vowels ######################################################################

N("แอ"): "ะ",
N("*แอ"): N("กั"),
N("แอล"): "า",
    
N("กี"): N("กิ"),
N("กีล"): N("กี"),
    
N("กีู"): N("กึ"),
N("กีูล"): N("กื"),

N("กู"): N("กุ"),
N("กูล"): N("กู"),

N("กีแ"): "เ",
"แ": "แ",
N("กูอ"): "โ",

"อ": N("ก็"), # It's assigned here just because there's a free stroke XD
"แอย": "ใ",
"แอลย": "ไ", # Using ล instead of * to free up briefing space
"แอม": N("กำ"),

N("กีู*"): "ฤ",
N("กีู*ล"): "ฤๅ",
N("กีู#"): "ฦ",
N("กีู#ล"): "ฦๅ",

# Tone marks ##################################################################

"-ต": N("ก่"),
"-ส": N("ก้"),
"-สข": N("ก๊"),
"-ตข": N("ก๋"),

# Punctuation #################################################################

"-ฟ": "\n",

"-งว": "/",
"-งย": "-",

# Plover workaround - https://discord.com/channels/136953735426473984/281185832637825025/866572760025399296
"-ง": "{mode:reset_space}{^ ^}{mode:set_space:}",
"-ย": ",",
"-ว": ".",
"-มวร": "…",
"-มย": "?",
"-มง": "!",
"-วย": "ๆ",
"-รฟ": "ฯ",
"-วรฟ": "ฯลฯ",

"-ม": "'",
"-มว": "\"",
"-มร": "(",
"-วร": ")",
"-มฟ": "[",
"-วฟ": "]",
"-มรฟ": "{",
"-วรฟ": "}"
}

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY, 'lookup() called with %d strokes, > max of %d' % (len(key), LONGEST_KEY)
    if key[0] in translations: return translations[key[0]]
    else: raise KeyError("Not found")

def reverse_lookup(text):
    return [k for (k,v) in translations.items() if v==text]

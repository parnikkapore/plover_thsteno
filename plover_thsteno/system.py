# English steno layout:
# # # # #     # # # # #
# X T P H  *  F P L T D
# S K W R     R B G S Z
# 
#      A O   E U

# Thai steno layout:
# # # # #     # # # # #
# ม ป พ ร  *  ส ข ม ว ร
# ง ก ค ว     ต ล ง ย ฟ
#
#       อี อู แ อ

# Normalize key names (so the in-file format can be easier to render)
def N(key): return key.replace("อ","")

KEYS = (
    'ม-', 'ง-', 'ป-', 'ก-', 'พ-', 'ค-', 'ร-', 'ว-',
    N('อี-'), N('อู-'), 'A', '*', '#', '-แ', '-อ',
    '-ส', '-ต', '-ข', '-ล',
    '-ม', '-ง', '-ว', '-ย', '-ร', '-ฟ'
)

K = { # Mapping Extended Plover keys to system's key names
    '#1': '#',
    '#4': '#',
    '#2': '#',
    '#3': 'A',
    'X-': 'ม-',
    'S-': 'ง-',
    'T-': 'ป-',
    'K-': 'ก-',
    'P-': 'พ-',
    'W-': 'ค-',
    'H-': 'ร-',
    'R-': 'ว-',
    'A' : N('อี-'),
    'O' : N('อู-'),
    '*1': 'A',
    '*2': '*',
    'E' : '-แ',
    'U' : '-อ',
    '-F': '-ส',
    '-R': '-ต',
    '-P': '-ข',
    '-B': '-ล',
    '-L': '-ม',
    '-G': '-ง',
    '-T': '-ว',
    '-S': '-ย',
    '-D': '-ร',
    '-Z': '-ฟ'
}

IMPLICIT_HYPHEN_KEYS = (N('อี-'), N('อู-'), '*', '-แ', '-อ')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {
#    '-ร': '1-',
#    '-พ': '2-',
#    '-ป': '3-',
#    '-ม': '4-',
#    '-แ': '5-',
#    '-อ': '0-',
#    '-ว': '-6',
#    '-ค': '-7',
#    '-ก': '-8',
#    '-ง': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        K['#1']     : ('#1', '#2', '#3', '#4', '#5', '#6', '#9', '#A', '#B', '#C'),
        K['#3']     : ('#7', '#8'),
        K['X-']     : 'S1-',
        K['S-']     : 'S2-',
        K['T-']     : 'T-',
        K['K-']     : 'K-',
        K['P-']     : 'P-',
        K['W-']     : 'W-',
        K['H-']     : 'H-',
        K['R-']     : 'R-',
        K['A']     : 'A-',
        K['O']     : 'O-',
        K['*2']     : ('*1', '*2', '*3', '*4'),
        K['E']      : '-E',
        K['U']      : '-U',
        K['-F']     : '-F',
        K['-R']     : '-R',
        K['-P']     : '-P',
        K['-B']     : '-B',
        K['-L']     : '-L',
        K['-G']     : '-G',
        K['-T']     : '-T',
        K['-S']     : '-S',
        K['-D']     : '-D',
        K['-Z']     : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        K['#1']     : ('1', '2', '3', '4', '8', '9', '0', '-', '='),
        K['#3']     : ('5', '6', '7'),
        K['X-']     : 'q',
        K['S-']     : 'a',
        K['T-']     : 'w',
        K['K-']     : 's',
        K['P-']     : 'e',
        K['W-']     : 'd',
        K['H-']     : 'r',
        K['R-']     : 'f',
        K['A']     : 'c',
        K['O']     : 'v',
        K['*1']     : ('t', 'g'),
        K['*2']     : ('y', 'h'),
        K['E']     : 'n',
        K['U']     : 'm',
        K['-F']     : 'u',
        K['-R']     : 'j',
        K['-P']     : 'i',
        K['-B']     : 'k',
        K['-L']     : 'o',
        K['-G']     : 'l',
        K['-T']     : 'p',
        K['-S']     : ';',
        K['-D']     : '[',
        K['-Z']     : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        K['X-']     : 'S',
        K['S-']     : 'C',
        K['T-']     : 'T',
        K['K-']     : 'K',
        K['P-']     : 'P',
        K['W-']     : 'W',
        K['H-']     : 'H',
        K['R-']     : 'R',
        K['A']     : 'A',
        K['O']     : 'O',
        K['*2']     : ('~', '*'),
        K['E']     : 'E',
        K['U']     : 'U',
        K['-F']     : 'F',
        K['-R']     : 'Q',
        K['-P']     : 'N',
        K['-B']     : 'B',
        K['-L']     : 'L',
        K['-G']     : 'G',
        K['-T']     : 'Y',
        K['-S']     : 'X',
        K['-D']     : 'D',
        K['-Z']     : 'Z',
        K['*1']     : ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        K['X-']     : '^',
        K['S-']     : 'S-',
        K['T-']     : 'T-',
        K['K-']     : 'K-',
        K['P-']     : 'P-',
        K['W-']     : 'W-',
        K['H-']     : 'H-',
        K['R-']     : 'R-',
        K['A']     : 'A-',
        K['O']     : 'O-',
        K['*2']     : '*',
        K['E']      : '-E',
        K['U']      : '-U',
        K['-F']     : '-F',
        K['-R']     : '-R',
        K['-P']     : '-P',
        K['-B']     : '-B',
        K['-L']     : '-L',
        K['-G']     : '-G',
        K['-T']     : '-T',
        K['-S']     : '-S',
        K['-D']     : '-D',
        K['-Z']     : '-Z',
    },
    'TX Bolt': {
        # Can we distinguish between upper and lower S for this machine?
        '#'    : '#',
        K['S-']     : 'S-',
        K['T-']     : 'T-',
        K['K-']     : 'K-',
        K['P-']     : 'P-',
        K['W-']     : 'W-',
        K['H-']     : 'H-',
        K['R-']     : 'R-',
        K['A']     : 'A-',
        K['O']     : 'O-',
        K['*2']     : '*',
        K['E']      : '-E',
        K['U']      : '-U',
        K['-F']     : '-F',
        K['-R']     : '-R',
        K['-P']     : '-P',
        K['-B']     : '-B',
        K['-L']     : '-L',
        K['-G']     : '-G',
        K['-T']     : '-T',
        K['-S']     : '-S',
        K['-D']     : '-D',
        K['-Z']     : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        K['X-']     : 'S1-',
        K['S-']     : 'S2-',
        K['T-']     : 'T-',
        K['K-']     : 'K-',
        K['P-']     : 'P-',
        K['W-']     : 'W-',
        K['H-']     : 'H-',
        K['R-']     : 'R-',
        K['A']     : 'A-',
        K['O']     : 'O-',
        K['*1']     : ('*1', 'X1-', 'X2-', 'X3'),
        K['*2']     : '*2',
        K['E']      : '-E',
        K['U']      : '-U',
        K['-F']     : '-F',
        K['-R']     : '-R',
        K['-P']     : '-P',
        K['-B']     : '-B',
        K['-L']     : '-L',
        K['-G']     : '-G',
        K['-T']     : '-T',
        K['-S']     : '-S',
        K['-D']     : '-D',
        K['-Z']     : '-Z'
    },
}

DICTIONARIES_ROOT = 'asset:plover_thsteno:dicts'
DEFAULT_DICTIONARIES = ('thsteno_main.json', 'thsteno_fingerspelling.py','thsteno_base.py')

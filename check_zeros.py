import re
import glob

vector_patterns = [
    r'\\vb(?:[*])?\{[^}]+\}',
    r'\\[a-zA-Z]+', # match macros like \vP, \vq
]

# Build a regex that matches:
# - one of the vector patterns
# - optionally followed by subscripts, superscripts, dots, etc (just simple characters)
# - optionally some spaces and operators
# - = 0

pattern = re.compile(r'(\\[a-zA-Z]+(?:(?:_|\^)[a-zA-Z0-9{}]+)*\s*(?:[+\-*/=><]\s*)*0(?![\.,]?[0-9]))')

for filepath in glob.glob('./Sections/*.tex'):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            # very simple check
            if '= 0' in line and '\\vb{0}' not in line:
                # heuristic: if there's \vb, \vP, \vq, \vp, \vv, \vF, \var{\vq} etc before '= 0'
                if any(x in line for x in ['\\vb', '\\vP', '\\vq', '\\vp', '\\vv', '\\vF', '\\var{\\vq}', '\\var{\\vO}']):
                    print(f"{filepath}:{i+1}: {line.strip()}")

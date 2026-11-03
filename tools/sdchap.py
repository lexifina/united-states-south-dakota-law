"""Split a whole-chapter answer of the South Dakota API (api/Statutes/Statute/<title>-<chapter>) into its sections and render
each one exactly as parse.py renders a per-section answer. The chapter's Html is its table of contents followed by every
section's own Html, each after an "<hr><br>"."""
import html as H
import re

import parse

SENU = re.compile(r'<span[^>]*class="[^"]*SENU"[^>]*>(.*?)</span>', re.S)
CL = re.compile(r'<span[^>]*class="[^"]*\bs[0-9a-f]+CL"[^>]*>(.*?)</span>', re.S)


def pieces(d):
    parts = d['Html'].split('<hr><br>')
    for p in parts[1:]:
        b = p[p.find('<body'):]
        nums = [parse.clean(x) for x in SENU.findall(b)]
        nums = [x for x in nums if re.match(r'^\d', x)]
        if not nums:   # older pieces (Wp2Html): the number follows the SENU comment as plain text
            m = re.search(r'(\d+[0-9A-Z]*-\d+[0-9A-Z]*-[0-9A-Za-z.]*[0-9A-Za-z])\.?', parse.clean(re.sub(r'<!--.*?-->', '', b, flags=re.S)))
            yield (m.group(1), '', p) if m else (None, None, p)
            continue
        num = nums[0].rstrip('.')
        cl = CL.search(b)
        yield num, parse.clean(cl.group(1)) if cl else '', p


def render(num, cl, piece):
    d = {'Html': piece, 'Statute': num, 'CatchLine': cl}
    lines = parse.body(d)
    label = f'SDCL {num}'
    head_, _, frac = num.partition('.')
    k = parse.key(head_) + ('x' + re.sub(r'[^0-9a-z]', '', frac.lower()) if frac else '')
    if cl.startswith(num):
        cl = ''
    lines = [re.sub(r'^(?:' + re.escape(num) + r'\.\s*)+', '', l) for l in lines]
    if lines and not lines[0]:
        lines = lines[1:]
    if not cl and lines:
        cl, lines = lines[0], lines[1:]
    text = '# ' + label + ('. ' + cl if cl else '') + '\n' + ''.join(l + '\n' for l in lines)
    return k, {'label': label, 'kind': 'section', 'text': text}

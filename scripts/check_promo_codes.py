#!/usr/bin/env python3
"""Discover candidates from a Plarium forum moderator thread; never assert active status."""
import json,re,datetime,urllib.request,html,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/'promo-codes.json'
URL='https://forum.plarium.com/mech-arena/702_game-discussion/1759149_active-promo-codes---10th-june--2026/'
req=urllib.request.Request(URL,headers={'User-Agent':'MechArenaTacticalHubPromoMonitor/1.0 (public-page checker)'})
with urllib.request.urlopen(req,timeout=25) as response:
    page=response.read(1_500_000).decode('utf-8','replace')
# Text only, avoid scripts and HTML attributes. Moderator thread can change markup.
page=re.sub(r'<(script|style)\b[^>]*>.*?</\1>',' ',page,flags=re.I|re.S)
page=html.unescape(re.sub(r'<[^>]+>',' ',page))
page=re.sub(r'\s+',' ',page)
# Conservative extraction: promo-looking uppercase token followed by a dash and descriptive text.
pattern=r'\b([A-Z][A-Z0-9]{5,27})\s*[-–—:]\s*(?=(?:Grants?|Rank|200|100|Five|5|1|a |an |credits|A-Coins|for |gives?|available))'
found=set(re.findall(pattern,page,flags=re.I))
found={x.upper() for x in found if x.upper()==x and not x.startswith(('HTTP','HTTPS'))}
data=json.loads(DATA.read_text(encoding='utf-8'))
known={x['code'].upper() for x in data['codes']}
new=sorted(found-known)
# Do not automatically publish claims from an unverified scrape. PR contains candidates for review.
if new:
    path=ROOT/'promo-candidates.json'
    previous=json.loads(path.read_text()) if path.exists() else {'candidates':[]}
    existing={x['code'] for x in previous['candidates']}
    for code in new:
        if code not in existing: previous['candidates'].append({'code':code,'source':URL,'status':'Unverified candidate — review before publishing'})
    path.write_text(json.dumps(previous,indent=2)+'\n',encoding='utf-8')
    print('Candidate codes for manual review:', ', '.join(new))
else: print('No new candidate codes found (does not mean no new codes exist).')

"""Patch i18n.js with daily fortune translation keys"""
import os, shutil

os.chdir('/tmp/fifafa-zodiac')

# Patch i18n.js
i18n = open('i18n.js', 'r', encoding='utf-8').read()
new_keys = '''
    'daily-0':{ zh:'宜积极进取', en:'Be proactive today', ja:'積極的に行動を' },
    'daily-1':{ zh:'宜柔韧应变', en:'Stay flexible', ja:'柔軟に対応を' },
    'daily-2':{ zh:'宜热情行动', en:'Act with passion', ja:'情熱を持って' },
    'daily-3':{ zh:'宜稳重踏实', en:'Be steady', ja:'着実に進もう' },
    'daily-4':{ zh:'宜诚信待人', en:'Be sincere', ja:'誠実であれ' },
    'daily-5':{ zh:'宜厚德载物', en:'Nurture virtue', ja:'徳を育もう' },
    'daily-6':{ zh:'宜果断决策', en:'Be decisive', ja:'果断に決断を' },
    'daily-7':{ zh:'宜精益求精', en:'Refine skills', ja:'技を磨こう' },
    'daily-8':{ zh:'宜深思远虑', en:'Think deeply', ja:'深く考えよう' },
    'daily-9':{ zh:'宜灵活变通', en:'Be adaptable', ja:'柔軟に適応を' },
    'dtip-0':{ zh:'诸事顺遂', en:'All favorable', ja:'全て順調' },
    'dtip-1':{ zh:'宜静不宜动', en:'Stillness over action', ja:'静を保て' },
    'dtip-2':{ zh:'贵人相助', en:'Benefactors near', ja:'贵人の助け' },
    'dtip-3':{ zh:'灵感迸发', en:'Inspiration strikes', ja:'ひらめきの日' },
    'dtip-4':{ zh:'稳扎稳打', en:'Steady progress', ja:'着実に進もう' },
'''
end = i18n.rfind('};')
if end > 0:
    i18n = i18n[:end] + new_keys + i18n[end:]
    open('i18n.js', 'w', encoding='utf-8').write(i18n)
    print('i18n.js: PATCHED with 15 new keys')
else:
    print('ERROR: could not find end of i18n dict')

# Sync to en/ja
for d in ['en', 'ja']:
    shutil.copy('index.html', f'{d}/index.html')
    shutil.copy('i18n.js', f'{d}/i18n.js')
    shutil.copy('api.js', f'{d}/api.js')
print('en/ and ja/: SYNCED')

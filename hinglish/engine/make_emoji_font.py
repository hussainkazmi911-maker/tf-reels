# Builds engine/fonts/noto-color-emoji-sub.woff2 (Noto Color Emoji, SIL OFL 1.1) containing only the emoji the reels use.
# Source font: `npm pack @fontsource/noto-color-emoji` -> package/files/noto-color-emoji-emoji-400-normal.woff2
# usage: python3 make_emoji_font.py /path/to/noto-color-emoji-emoji-400-normal.woff2
import sys, os
from fontTools import subset
from fontTools.ttLib import TTFont

# every emoji that episodes may reference (make_tips.py asserts against this)
EMOJI = ("👀😬💀💡✅🚀🎉⚡❤️💬🔥😍✨⭐😭🥲😮‍💨🫠🤦😵❌🚫💸📩🔔👇👆🎯💰🏆🥳🤯😤⏰🕒⏱️⏳🔎🔍🏢🧵📋📰📎❓🏦🏷️📦🧾🤝✍️📝🧲💼🧰🫡🧩📱"
         "🔁💵🆓👥🔧📌📨🛠️📊🌍💻📈🚩🧠🙌😅😳🔒🗓️🔖💯🙏😶💔🫶☑️✔️➕")

def chars():
    return ''.join(EMOJI) + '‍️'

if __name__ == '__main__':
    src = sys.argv[1]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts', 'noto-color-emoji-sub.woff2')
    opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['*']; opts.notdef_outline = True
    f = TTFont(src)
    s = subset.Subsetter(opts); s.populate(text=chars()); s.subset(f)
    f.flavor = 'woff2'; f.save(out)
    print(out, os.path.getsize(out), 'bytes')

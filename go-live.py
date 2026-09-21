#!/usr/bin/env python3
"""Flip the App Store badge from "Coming soon" to a live link, once the app is approved.

The badge ships UNLINKED and dimmed because https://apps.apple.com/app/id6812983236 returns
404 until the app is actually live on the App Store, and a store badge that leads to a dead
page looks worse than one that is honestly labelled.

Run this the day Hyper Bounce is approved:

    python go-live.py            # show what would change
    python go-live.py --apply    # rewrite index.html
    git commit -am "App Store badge is live" && git push

It is idempotent: once flipped, re-running reports that there is nothing to do.
"""
import re
import sys

APP_STORE_URL = "https://apps.apple.com/app/id6812983236"
PAGE = "index.html"

SOON = re.compile(
    r'[ \t]*<!-- ON APP STORE APPROVAL:.*?-->\s*'
    r'<span class="badge-soon">\s*'
    r'<span class="pill">Coming soon</span>\s*'
    r'<span class="badge-appstore">(?P<img><img[^>]*>)</span>\s*'
    r'</span>',
    re.S)

LIVE = ('    <a class="badge-appstore" href="%s">\n      %s\n    </a>')


def main():
    src = open(PAGE, encoding="utf-8").read()

    if 'class="badge-soon"' not in src:
        if APP_STORE_URL in src:
            print("Already live: the App Store badge links to %s" % APP_STORE_URL)
        else:
            print("Nothing to do: no 'badge-soon' block found, and no App Store link either. "
                  "Check %s by hand." % PAGE)
        return

    m = SOON.search(src)
    if not m:
        sys.exit("Found a 'badge-soon' block but it does not match the expected shape.\n"
                 "Edit %s by hand: replace the <span class=\"badge-soon\"> block with\n"
                 '  <a class="badge-appstore" href="%s"><img ...></a>' % (PAGE, APP_STORE_URL))

    out = src[:m.start()] + (LIVE % (APP_STORE_URL, m.group("img"))) + src[m.end():]

    if "--apply" not in sys.argv:
        print("Would replace the 'Coming soon' block with:\n")
        print(LIVE % (APP_STORE_URL, m.group("img")))
        print("\nDry run. Re-run with --apply to write %s." % PAGE)
        return

    open(PAGE, "w", encoding="utf-8", newline="").write(out)
    print("Updated %s: App Store badge now links to %s" % (PAGE, APP_STORE_URL))
    print("Next: git commit -am 'App Store badge is live' && git push")
    print("Then confirm the served page: the badge should no longer be dimmed and the "
          "'Coming soon' pill should be gone.")


main()

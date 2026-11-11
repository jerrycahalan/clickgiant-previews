#!/usr/bin/env python3
"""Assemble West & Ginos preview pages from shared partials.

Usage: python3 _build/build.py   (run from the repo root)
Each entry in PAGES: (body file, output path, page title, review-bar label).
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, '..', 'west-ginos')
PAGES = [
    ('home.html', 'index.html', 'West &amp; Ginos Homepage A', 'Homepage (approved)'),
    ('car-accidents.html', 'car-accidents/index.html', 'Car Accident Lawyers | West &amp; Ginos Preview', 'Car Accidents page (approved)'),
    ('truck-accidents.html', 'truck-accidents/index.html', 'Truck Accident Lawyers | West &amp; Ginos Preview', 'Truck Accidents page (draft 1)'),
    ('dog-bites.html', 'dog-bites/index.html', 'Dog Bite Lawyers | West &amp; Ginos Preview', 'Dog Bites page (draft 1)'),
    ('slip-trip-fall.html', 'slip-trip-fall/index.html', 'Slip, Trip &amp; Fall Lawyers | West &amp; Ginos Preview', 'Slip, Trip &amp; Fall page (draft 1)'),
    ('why-choose-us.html', 'why-choose-us/index.html', 'Why Choose Us | West &amp; Ginos Preview', 'Why Choose Us page (draft 1)'),
    ('trent-west.html', 'attorneys/trent-west/index.html', 'Trent S. West | West &amp; Ginos Preview', 'Trent West bio (draft 1)'),
    ('michael-ginos.html', 'attorneys/michael-ginos/index.html', 'Michael G. Ginos | West &amp; Ginos Preview', 'Michael Ginos bio (draft 1)'),
]
HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap">
<link rel="stylesheet" href="{{ROOT}}assets/site.css">
</head>
<body>
'''
def part(name):
    with open(os.path.join(HERE, 'partials', name + '.html')) as f:
        return f.read()
for body, out, title, label in PAGES:
    depth = out.count('/')
    root = '../' * depth
    with open(os.path.join(HERE, 'pages', body)) as f:
        content = f.read()
    html = (HEAD.replace("{title}", title) + part('icons') + part('review').replace('{{PAGE_LABEL}}', label)
            + '<div class="stage" id="stage">\n<div class="site">\n' + part('header') + content
            + part('footer') + '</div><!-- .site -->\n</div><!-- .stage -->\n' + part('script') + '</body>\n</html>\n')
    html = html.replace('{{ROOT}}', root)
    dest = os.path.join(SITE, out)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'w') as f:
        f.write(html)
    print('built', out, len(html) // 1024, 'KB')

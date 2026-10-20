"""Builds the blog pages, sitemap, RSS feed and robots.txt.

Add a post: write its body to _src/posts/<slug>.html, add an entry to POSTS
below (newest first), then run:  python3 _src/build.py
"""
import html
import os
from datetime import datetime
from urllib.parse import quote

SITE = "https://lalkgeorge.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src", "posts")

CATS = {
    "ai": ("AI & Claude", "c-ai", "#7c3aed"),
    "meta": ("Meta Ads", "c-meta", "#4f46e5"),
    "hubspot": ("HubSpot", "c-hubspot", "#f97316"),
    "tracking": ("Tracking & Attribution", "c-tracking", "#10b981"),
    "linkedin": ("LinkedIn Ads", "c-linkedin", "#0ea5e9"),
    "seo": ("SEO & AEO", "c-seo", "#c2410c"),
    "saas": ("SaaS Growth", "c-saas", "#334155"),
}

ICONS = {
    "ai": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "meta": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-6"/>',
    "hubspot": '<circle cx="12" cy="12" r="3"/><circle cx="12" cy="4" r="1.5"/><circle cx="19" cy="17" r="1.5"/><circle cx="5" cy="17" r="1.5"/><path d="M12 9V5.5M14.6 13.5l3.2 2.4M9.4 13.5l-3.2 2.4"/>',
    "tracking": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
    "seo": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "saas": '<path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/>',
}

# Newest first. The first post is featured on the blog page.
POSTS = [
    {
        "slug": "how-i-run-meta-ads-with-claude",
        "title": "How I run Meta Ads with Claude: my actual workflow",
        "dek": "Claude connected straight to the ad account turns hours of spreadsheet audits into a few questions. Here's the setup, the weekly prompts, and the rules I don't break.",
        "cat": "ai",
        "date": "2026-10-20",
        "read": 7,
    },
    {
        "slug": "hubspot-lifecycle-stages-b2b-saas",
        "title": "HubSpot lifecycle stages for B2B SaaS: the setup that ends lead-quality fights",
        "dek": "Clear stage definitions, fast routing and rejection reasons. The HubSpot setup that gets marketing and sales on the same page.",
        "cat": "hubspot",
        "date": "2026-10-20",
        "read": 6,
    },
    {
        "slug": "b2b-saas-tracking-checklist",
        "title": "The B2B SaaS tracking checklist: GA4, GTM & HubSpot",
        "dek": "UTM rules, the events that matter, getting source data into the CRM, and sending better conversions back to ad platforms.",
        "cat": "tracking",
        "date": "2026-10-20",
        "read": 7,
    },
    {
        "slug": "linkedin-ads-b2b-saas-mistakes",
        "title": "7 LinkedIn Ads mistakes that burn B2B SaaS budgets",
        "dek": "From hidden default settings to judging LinkedIn by Meta's rules. A 10-minute audit that catches most of the waste.",
        "cat": "linkedin",
        "date": "2026-10-20",
        "read": 5,
    },
]

TOPICS = [
    ("ai", "Claude, ChatGPT and ChatGPT Ads in real marketing workflows"),
    ("meta", "Campaign structure, creative testing, audits"),
    ("hubspot", "Lifecycle stages, workflows, lead routing, reporting"),
    ("tracking", "GA4, GTM, UTMs, offline conversions"),
    ("linkedin", "B2B targeting, lead gen forms, ABM"),
    ("seo", "Ranking on Google and getting cited by AI search"),
    ("saas", "Launches, events, funnels and GTM"),
]

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')
FAVICON = ("<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
           "<rect width='100' height='100' rx='22' fill='%234f46e5'/><text x='50' y='66' font-size='46' font-family='Arial' "
           "font-weight='800' fill='white' text-anchor='middle'>LG</text></svg>\">")


def esc(s):
    return html.escape(s, quote=True)


def nice_date(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%b %-d, %Y")


def icon(cat):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round">' + ICONS[cat] + "</svg>")


def head(title, desc, url, prefix):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<meta name="twitter:creator" content="@LALKGEORGE">
<link rel="alternate" type="application/rss+xml" title="Lal K George: SaaS marketing blog" href="{SITE}/feed.xml">
{FAVICON}
{FONT}
<link rel="stylesheet" href="{prefix}assets/blog.css">
<!-- analytics -->
</head>
<body>
<nav>
  <div class="wrap">
    <a class="logo" href="{prefix}">Lal K George<span>.</span></a>
    <div class="links">
      <a href="{prefix}#services">What I do</a>
      <a href="{prefix}#experience">Experience</a>
      <a href="{prefix}#toolkit">Toolkit</a>
      <a class="on" href="{prefix}blog/">Blog</a>
    </div>
    <a class="btn btn-primary" href="https://x.com/LALKGEORGE" target="_blank" rel="noopener">Follow on X</a>
  </div>
</nav>
"""


FOOT = """<footer>© 2026 Lal K George · SaaS &amp; B2B Marketing · <a href="{prefix}feed.xml">RSS</a></footer>
</body>
</html>
"""


def card(p, prefix):
    name, cls, _ = CATS[p["cat"]]
    return f"""<a class="post" data-cat="{p['cat']}" href="{prefix}blog/{p['slug']}/">
  <div class="art {cls}">{icon(p['cat'])}</div>
  <div class="body">
    <span class="cat">{esc(name)}</span>
    <h3>{esc(p['title'])}</h3>
    <p>{esc(p['dek'])}</p>
    <div class="meta">{nice_date(p['date'])} · {p['read']} min read</div>
  </div>
</a>"""


def build_index():
    prefix = "../"
    feat, rest = POSTS[0], POSTS[1:]
    fname, fcls, _ = CATS[feat["cat"]]
    used = [c for c in CATS if any(p["cat"] == c for p in POSTS)]
    filters = '<button class="filter on" data-f="all">All</button>' + "".join(
        f'<button class="filter" data-f="{c}">{esc(CATS[c][0])}</button>' for c in used)
    topics = "".join(
        f'<div class="topic"><i style="background:{CATS[c][2]}"></i><b>{esc(CATS[c][0])}</b><span>{esc(t)}</span></div>'
        for c, t in TOPICS)
    out = head("Blog | Lal K George: SaaS marketing lessons",
               "Practical lessons on Meta Ads, AI and Claude, HubSpot, tracking, LinkedIn Ads and SaaS growth.",
               f"{SITE}/blog/", prefix)
    out += f"""
<header class="bhero">
  <div class="blob b1"></div>
  <div class="wrap">
    <div class="label">Blog</div>
    <h1>Lessons from <em>the trenches</em> of SaaS marketing</h1>
    <p>Practical, no-fluff notes on paid ads, AI workflows, HubSpot and tracking. What works, and what quietly burns budget.</p>
    <div class="filters" role="group" aria-label="Filter posts by topic">{filters}</div>

    <a class="featured" data-cat="{feat['cat']}" href="{prefix}blog/{feat['slug']}/">
      <div class="art {fcls}">{icon(feat['cat'])}</div>
      <div class="body">
        <span class="cat">Featured · {esc(fname)}</span>
        <h2>{esc(feat['title'])}</h2>
        <p>{esc(feat['dek'])}</p>
        <div class="meta">{nice_date(feat['date'])} · {feat['read']} min read</div>
      </div>
    </a>

    <div class="posts">
      {''.join(card(p, prefix) for p in rest)}
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="label">Topics</div>
    <h2 class="sec">What I write about</h2>
    <div class="topics">{topics}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="strip">
      <div><h3>Get new posts first</h3><p>I share every new lesson on X and LinkedIn.</p></div>
      <div class="cta">
        <a class="btn btn-primary" href="https://x.com/LALKGEORGE" target="_blank" rel="noopener">Follow on X</a>
        <a class="btn btn-ghost" href="https://www.linkedin.com/in/lalkgeorge" target="_blank" rel="noopener">Connect on LinkedIn</a>
      </div>
    </div>
  </div>
</section>

<script>
(function(){{
  var btns=document.querySelectorAll('.filter'), items=document.querySelectorAll('[data-cat]');
  btns.forEach(function(b){{ b.addEventListener('click',function(){{
    btns.forEach(function(x){{x.classList.toggle('on',x===b)}});
    var f=b.getAttribute('data-f');
    items.forEach(function(el){{ el.style.display=(f==='all'||el.getAttribute('data-cat')===f)?'':'none'; }});
  }}); }});
}})();
</script>
"""
    out += FOOT.format(prefix=prefix)
    os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
    with open(os.path.join(ROOT, "blog", "index.html"), "w") as f:
        f.write(out)


def build_post(p):
    prefix = "../../"
    name, cls, _ = CATS[p["cat"]]
    url = f"{SITE}/blog/{p['slug']}/"
    with open(os.path.join(SRC, p["slug"] + ".html")) as f:
        body = f.read()
    share_url = quote(url + "?utm_source=share", safe="")
    share_text = quote(p["title"], safe="")
    others = [o for o in POSTS if o["slug"] != p["slug"]][:3]
    out = head(f"{p['title']} | Lal K George", p["dek"], url, prefix)
    out += f"""
<header class="ahead">
  <div class="wrap">
    <a class="back" href="{prefix}blog/">← All posts</a>
    <div style="margin-top:22px"><span class="cat">{esc(name)}</span></div>
    <h1>{esc(p['title'])}</h1>
    <p class="dek">{esc(p['dek'])}</p>
    <div class="byline"><div class="av">LG</div><div><b>Lal K George</b>{nice_date(p['date'])} · {p['read']} min read</div></div>
    <div class="art cover {cls}">{icon(p['cat'])}</div>
  </div>
</header>

<article class="article">
  <div class="wrap">
    <div class="prose">
{body}
    </div>
    <div class="share">
      <span>Share</span>
      <a href="https://x.com/intent/post?text={share_text}&url={share_url}" target="_blank" rel="noopener">Post on X</a>
      <a href="https://www.linkedin.com/sharing/share-offsite/?url={share_url}" target="_blank" rel="noopener">Share on LinkedIn</a>
    </div>
  </div>
</article>

<section class="more">
  <div class="wrap">
    <div class="label">Keep reading</div>
    <div class="posts">{''.join(card(o, prefix) for o in others)}</div>
  </div>
</section>
"""
    out += FOOT.format(prefix=prefix)
    d = os.path.join(ROOT, "blog", p["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(out)


def build_meta():
    urls = [f"{SITE}/", f"{SITE}/blog/"] + [f"{SITE}/blog/{p['slug']}/" for p in POSTS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(sm)
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    items = ""
    for p in POSTS:
        d = datetime.strptime(p["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 09:00:00 +0530")
        u = f"{SITE}/blog/{p['slug']}/"
        items += (f"  <item><title>{esc(p['title'])}</title><link>{u}</link><guid>{u}</guid>"
                  f"<pubDate>{d}</pubDate><description>{esc(p['dek'])}</description></item>\n")
    rss = ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n'
           f"  <title>Lal K George: SaaS marketing blog</title><link>{SITE}/blog/</link>\n"
           "  <description>Practical lessons on Meta Ads, AI, HubSpot, tracking and SaaS growth.</description>\n"
           + items + "</channel></rss>\n")
    with open(os.path.join(ROOT, "feed.xml"), "w") as f:
        f.write(rss)


if __name__ == "__main__":
    build_index()
    for p in POSTS:
        build_post(p)
    build_meta()
    print(f"Built blog index, {len(POSTS)} posts, sitemap.xml, feed.xml, robots.txt")

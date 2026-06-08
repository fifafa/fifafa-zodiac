#!/usr/bin/env python3
"""
lalalin.xyz Content Factory — AI-powered social media automation v2
Generates posts for Reddit, X/Twitter, Instagram, YouTube
Powered by DeepSeek API via backend client
"""
import os
import sys
import json
import random
import time
from datetime import datetime
from pathlib import Path

# Load .env from backend
from dotenv import load_dotenv
_backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backend')
load_dotenv(os.path.join(_backend_dir, '.env'))

sys.path.insert(0, _backend_dir)
from deepseek_client import DeepSeekClient

API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
client = DeepSeekClient(api_key=API_KEY)

# Rate limiting between API calls (seconds)
RATE_LIMIT = 3
MAX_RETRIES = 2


def _call_with_retry(fn, *args, **kwargs):
    """Call API with retry and rate limiting."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            time.sleep(RATE_LIMIT)
            return fn(*args, **kwargs)
        except Exception as e:
            if attempt < MAX_RETRIES:
                print(f"  ⚠️  Retry {attempt+1}/{MAX_RETRIES}: {e}")
                time.sleep(RATE_LIMIT * 2)
            else:
                print(f"  ❌ Failed after {MAX_RETRIES} retries: {e}")
                return None


# ============================================================
# REDDIT Bot
# ============================================================
REDDIT_SUBREDDITS = [
    "r/astrology", "r/tarot", "r/numerology", "r/psychic",
    "r/spirituality", "r/ChineseZodiac", "r/fortune",
]

def generate_reddit_post():
    module = random.choice(["bazi", "tarot", "zodiac", "ziwei"])
    topic = random.choice(["career", "love", "wealth", "health", "destiny"])

    system = """You are a Reddit power user helping promote lalalin.xyz — an AI Eastern fortune-telling website.
Write an engaging, authentic Reddit post (title + body) that naturally attracts interest.
Rules:
- Be genuine, NOT spammy. Offer real value first.
- Share a fun fact or insight about Eastern fortune-telling
- Subtly mention the website at the end with a natural call-to-action
- Keep it under 500 words
- Use casual Reddit tone (not corporate)
- Include at least 1 emoji"""

    prompt = f"""Write a Reddit post for r/astrology or similar subreddit about {module} ({topic} focus).
The post should feel like a real person sharing their experience, not an ad.
Title should be catchy and under 100 chars.
End with: "If you want to try {module} yourself, I found this free tool: lalalin.xyz"

Return JSON: {{"title": "...", "body": "..."}}"""

    result = _call_with_retry(client.chat_sync, system, prompt, max_tokens=500)
    if result is None:
        return "Error generating post", "API call failed"
    
    text, tokens = result
    try:
        data = json.loads(text)
        return data["title"], data["body"]
    except:
        lines = text.strip().split("\n")
        title = lines[0].strip("# ").strip()
        body = "\n".join(lines[1:]) if len(lines) > 1 else text
        return title[:100], body


# ============================================================
# X/TWITTER Scheduler
# ============================================================
X_POST_TYPES = [
    "daily_fortune", "build_in_public", "fun_fact", "user_story", "engagement"
]

TYPES_DESC = {
    "daily_fortune": "Write a daily fortune tweet. Be mysterious and intriguing. Include 1 zodiac animal.",
    "build_in_public": "Write a build-in-public tweet about building an AI fortune-telling SaaS. Mention a recent feature.",
    "fun_fact": "Share a fascinating fact about Eastern fortune-telling (bazi/tarot/zodiac).",
    "user_story": "Share a fictional but believable user success story about using the site.",
    "engagement": "Write an engagement tweet asking people to share their zodiac/tarot sign.",
}

def generate_x_post(post_type="daily_fortune"):
    system = """You write engaging X/Twitter posts for lalalin.xyz.
Rules:
- Under 280 characters
- 1-2 emojis max
- Natural, not salesy
- Use relevant hashtags (1-2 max)
- For "build_in_public": mention specific feature shipped
- For "daily_fortune": make it surprising and shareable"""

    prompt = TYPES_DESC.get(post_type, TYPES_DESC["daily_fortune"])
    prompt += "\n\nReturn just the tweet text (under 280 chars)."

    result = _call_with_retry(client.chat_sync, system, prompt, max_tokens=100)
    if result is None:
        return "[API Error]"
    text, _ = result
    return text.strip().strip('"')[:280]


# ============================================================
# Instagram Caption Generator
# ============================================================
def generate_ig_caption(module="tarot"):
    system = """You write Instagram captions for lalalin.xyz fortune-telling content.
Style: Mystical, aesthetic, engaging. Use line breaks. Include relevant hashtags."""

    prompt = f"""Write an Instagram caption for a {module} reading card image.
Include:
1. A mystical quote or insight
2. Brief explanation of the {module} method
3. Call to action (try your free reading)
4. 10-15 relevant hashtags (mix of English and #astrology #tarot #spirituality etc.)

Return just the caption text."""

    result = _call_with_retry(client.chat_sync, system, prompt, max_tokens=300)
    if result is None:
        return "[API Error]"
    text, _ = result
    return text.strip()


# ============================================================
# YouTube Script Generator
# ============================================================
def generate_yt_script(module="bazi", duration="10min"):
    mins = duration.replace("min", "")
    system = """You are a YouTube script writer specializing in spirituality and fortune-telling content.
Create engaging scripts that educate and entertain.
Structure: Hook → Introduction → Main Content → Call to Action."""

    prompt = f"""Write a {duration} YouTube script about "{module} fortune telling".
The video teaches viewers how {module} works and why it matters.

Structure:
1. HOOK (0:00-0:30): Surprising fact or question to grab attention
2. INTRO (0:30-1:30): What is {module}? Brief history
3. MAIN (1:30-{int(mins)-1}:30): Step-by-step walkthrough with examples
4. CTA (last 30s): Try it free at lalalin.xyz, like & subscribe

Format as: [TIMESTAMP] Speaker notes / visual cues
Include visual suggestions in [brackets]."""

    result = _call_with_retry(client.chat_sync, system, prompt, max_tokens=1000)
    if result is None:
        return "[API Error]"
    text, _ = result
    return text


# ============================================================
# Batch Generator
# ============================================================
def generate_weekly_content(quiet=False, reddit_count=3, x_count=5, ig_count=3, yt_count=2):
    """Generate a full week of content for all platforms."""
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)

    content = {
        "generated_at": datetime.now().isoformat(),
        "platforms": {}
    }

    def log(msg):
        if not quiet:
            print(msg)

    log("=" * 50)
    log("  lalalin.xyz Content Factory — Weekly Batch")
    log(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    log("=" * 50)

    # Reddit
    log(f"\n📱 Generating {reddit_count} Reddit posts...")
    reddit_posts = []
    for i in range(reddit_count):
        title, body = generate_reddit_post()
        reddit_posts.append({"title": title, "body": body})
        log(f"  ✅ Post {i+1}: {title[:60]}...")

    # X/Twitter
    log(f"\n🐦 Generating {x_count} X/Twitter posts...")
    x_posts = []
    for pt in X_POST_TYPES[:x_count]:
        tweet = generate_x_post(pt)
        x_posts.append({"type": pt, "text": tweet})
        log(f"  ✅ [{pt}]: {tweet[:60]}...")

    # Instagram
    log(f"\n📸 Generating {ig_count} Instagram captions...")
    ig_modules = ["tarot", "bazi", "zodiac"][:ig_count]
    ig_captions = []
    for m in ig_modules:
        cap = generate_ig_caption(m)
        ig_captions.append({"module": m, "caption": cap})
        log(f"  ✅ [{m}]: {cap[:60]}...")

    # YouTube
    log(f"\n🎬 Generating {yt_count} YouTube scripts...")
    yt_configs = [("bazi", "10min"), ("tarot", "8min"), ("zodiac", "6min")][:yt_count]
    yt_scripts = []
    for m, d in yt_configs:
        script = generate_yt_script(m, d)
        yt_scripts.append({"module": m, "duration": d, "script": script})
        log(f"  ✅ [{m}/{d}]: {len(script)} chars")

    content["platforms"] = {
        "reddit": reddit_posts,
        "x": x_posts,
        "instagram": ig_captions,
        "youtube": yt_scripts,
    }

    # Save to JSON
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    output_file = os.path.join(output_dir, f"content_{timestamp}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    log(f"\n📦 Saved to {output_file}")
    
    # Also save latest symlink
    latest = os.path.join(output_dir, "latest.json")
    if os.path.islink(latest) or os.path.exists(latest):
        os.remove(latest)
    os.symlink(os.path.basename(output_file), latest)
    
    return content


# ============================================================
# CLI
# ============================================================
if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="lalalin.xyz Content Factory v2")
    p.add_argument("--platform", choices=["reddit","x","instagram","youtube","all"], default="all")
    p.add_argument("--output", help="Output directory", default=None)
    p.add_argument("--quiet", "-q", action="store_true", help="Silent mode for cron")
    p.add_argument("--count", "-n", type=int, default=None, help="Number of items per platform")
    args = p.parse_args()

    if not API_KEY:
        print("❌ DEEPSEEK_API_KEY not configured. Set it in backend/.env")
        sys.exit(1)

    if args.platform == "all":
        n = args.count or 3
        generate_weekly_content(quiet=args.quiet, reddit_count=n, x_count=min(n+2, 5), ig_count=n, yt_count=2)
    elif args.platform == "reddit":
        for i in range(args.count or 1):
            title, body = generate_reddit_post()
            print(f"TITLE: {title}\n\n{body}\n---")
    elif args.platform == "x":
        for pt in X_POST_TYPES[:(args.count or 5)]:
            tweet = generate_x_post(pt)
            print(f"[{pt}] {tweet}\n")
    elif args.platform == "instagram":
        for m in ["tarot", "bazi", "zodiac"][:(args.count or 3)]:
            print(f"=== {m} ===\n{generate_ig_caption(m)}\n")
    elif args.platform == "youtube":
        for m, d in [("bazi", "10min"), ("tarot", "8min"), ("zodiac", "6min")][:(args.count or 2)]:
            print(f"=== {m} ({d}) ===\n{generate_yt_script(m, d)}\n")

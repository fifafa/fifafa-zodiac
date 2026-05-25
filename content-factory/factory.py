#!/usr/bin/env python3
"""
lalalin.xyz Content Factory — AI-powered social media automation
Generates posts for Reddit, X/Twitter, Instagram, YouTube
Powered by DeepSeek API
"""
import os
import sys
import json
import random
from datetime import datetime

# Add backend to path
_backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backend')
sys.path.insert(0, _backend_dir)
from deepseek_client import DeepSeekClient

API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-2311f0a9003e4fb7bdf8ad6bb46fd794")
client = DeepSeekClient(api_key=API_KEY)


# ============================================================
# REDDIT Bot
# ============================================================
REDDIT_SUBREDDITS = [
    "r/astrology", "r/tarot", "r/numerology", "r/psychic",
    "r/spirituality", "r/ChineseZodiac", "r/fortune",
]

REDDIT_POST_TEMPLATES = [
    "Just analyzed my {module} chart and wow... {detail} Anyone else had similar results?",
    "Free {module} reading for the first 5 comments! I'm practicing my skills. 🔮",
    "TIL about {topic} in {module}. Mind = blown. Here's what I learned:",
    "My grandmother was a fortune teller. She taught me {secret}. AMA!",
    "Hot take: {module} is more accurate than most people think. Here's why...",
]

def generate_reddit_post():
    """Generate a Reddit post with AI-powered content"""
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
- Include at least 1 emoji
"""

    prompt = f"""Write a Reddit post for r/astrology or similar subreddit about {module} ({topic} focus).
The post should feel like a real person sharing their experience, not an ad.
Title should be catchy and under 100 chars.
End with: "If you want to try {module} yourself, I found this free tool: lalalin.xyz"

Return JSON: {{"title": "...", "body": "..."}}"""

    text, tokens = client.chat_sync(system, prompt, max_tokens=500)
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

X_TEMPLATES = {
    "daily_fortune": "Today's {zodiac} fortune: {fortune} 🔮 #DailyFortune #EasternWisdom",
    "build_in_public": "Building lalalin.xyz Day {day}: Just shipped {feature}! 🚀 #BuildInPublic #IndieDev",
    "fun_fact": "Did you know? In {module}, {fun_fact} 🤯 #FunFact #FortuneTelling",
    "user_story": "A user told me they used our {module} reading and {story} ✨ Real magic happens when AI meets ancient wisdom.",
    "engagement": "Which {module} sign are you? Reply with your {sign_type} and I'll share a free reading! 🔮👇",
}

def generate_x_post(post_type="daily_fortune"):
    """Generate an X/Twitter post"""
    system = """You write engaging X/Twitter posts for lalalin.xyz.
Rules:
- Under 280 characters
- 1-2 emojis max
- Natural, not salesy
- Use relevant hashtags (1-2 max)
- For "build_in_public": mention specific feature shipped
- For "daily_fortune": make it surprising and shareable"""

    types_desc = {
        "daily_fortune": "Write a daily fortune tweet. Be mysterious and intriguing. Include 1 zodiac animal.",
        "build_in_public": "Write a build-in-public tweet about building an AI fortune-telling SaaS. Mention a recent feature.",
        "fun_fact": "Share a fascinating fact about Eastern fortune-telling (bazi/tarot/zodiac).",
        "user_story": "Share a fictional but believable user success story about using the site.",
        "engagement": "Write an engagement tweet asking people to share their zodiac/tarot sign.",
    }

    prompt = types_desc.get(post_type, types_desc["daily_fortune"])
    prompt += "\n\nReturn just the tweet text (under 280 chars)."

    text, _ = client.chat_sync(system, prompt, max_tokens=100)
    return text.strip().strip('"')[:280]


# ============================================================
# Instagram Card Generator
# ============================================================
def generate_ig_caption(module="tarot"):
    """Generate Instagram caption with hashtags"""
    system = """You write Instagram captions for lalalin.xyz fortune-telling content.
Style: Mystical, aesthetic, engaging. Use line breaks. Include relevant hashtags."""

    prompt = f"""Write an Instagram caption for a {module} reading card image.
Include:
1. A mystical quote or insight
2. Brief explanation of the {module} method
3. Call to action (try your free reading)
4. 10-15 relevant hashtags (mix of English and #astrology #tarot #spirituality etc.)

Return just the caption text."""

    text, _ = client.chat_sync(system, prompt, max_tokens=300)
    return text.strip()


# ============================================================
# YouTube Script Generator
# ============================================================
def generate_yt_script(module="bazi", duration="10min"):
    """Generate YouTube video script for fortune-telling content"""
    system = """You are a YouTube script writer specializing in spirituality and fortune-telling content.
Create engaging scripts that educate and entertain.
Structure: Hook → Introduction → Main Content → Call to Action."""

    prompt = f"""Write a {duration} YouTube script about "{module} fortune telling".
The video teaches viewers how {module} works and why it matters.

Structure:
1. HOOK (0:00-0:30): Surprising fact or question to grab attention
2. INTRO (0:30-1:30): What is {module}? Brief history
3. MAIN (1:30-{duration.replace('min','')}-1:30): Step-by-step walkthrough with examples
4. CTA (last 30s): Try it free at lalalin.xyz, like & subscribe

Format as: [TIMESTAMP] Speaker notes / visual cues

Include visual suggestions in [brackets]."""

    text, _ = client.chat_sync(system, prompt, max_tokens=1000)
    return text


# ============================================================
# Batch Generator
# ============================================================
def generate_weekly_content():
    """Generate a full week of content for all platforms"""
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)

    content = {
        "generated_at": datetime.now().isoformat(),
        "platforms": {}
    }

    print("=" * 50)
    print("  lalalin.xyz Content Factory — Weekly Batch")
    print("=" * 50)

    # Reddit: 3 posts
    print("\n📱 Generating Reddit posts...")
    reddit_posts = []
    for i in range(3):
        title, body = generate_reddit_post()
        reddit_posts.append({"title": title, "body": body})
        print(f"  ✅ Post {i+1}: {title[:60]}...")

    # X/Twitter: 7 posts (one per day)
    print("\n🐦 Generating X/Twitter posts...")
    x_posts = []
    for pt in X_POST_TYPES[:5]:
        tweet = generate_x_post(pt)
        x_posts.append({"type": pt, "text": tweet})
        print(f"  ✅ [{pt}]: {tweet[:60]}...")

    # Instagram: 3 captions
    print("\n📸 Generating Instagram captions...")
    ig_captions = []
    for m in ["tarot", "bazi", "zodiac"]:
        cap = generate_ig_caption(m)
        ig_captions.append({"module": m, "caption": cap})
        print(f"  ✅ [{m}]: {cap[:60]}...")

    # YouTube: 2 scripts
    print("\n🎬 Generating YouTube scripts...")
    yt_scripts = []
    for m, d in [("bazi", "10min"), ("tarot", "8min")]:
        script = generate_yt_script(m, d)
        yt_scripts.append({"module": m, "duration": d, "script": script})
        print(f"  ✅ [{m}/{d}]: {len(script)} chars")

    content["platforms"] = {
        "reddit": reddit_posts,
        "x": x_posts,
        "instagram": ig_captions,
        "youtube": yt_scripts,
    }

    # Save
    output_file = os.path.join(output_dir, f"content_{datetime.now().strftime('%Y%m%d_%H%M')}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    print(f"\n📦 Saved to {output_file}")
    return content


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="lalalin.xyz Content Factory")
    p.add_argument("--platform", choices=["reddit","x","instagram","youtube","all"], default="all")
    p.add_argument("--output", help="Output directory", default=None)
    args = p.parse_args()

    if args.platform == "all":
        generate_weekly_content()
    elif args.platform == "reddit":
        title, body = generate_reddit_post()
        print(f"TITLE: {title}\n\n{body}")
    elif args.platform == "x":
        for pt in X_POST_TYPES:
            tweet = generate_x_post(pt)
            print(f"[{pt}] {tweet}\n")
    elif args.platform == "instagram":
        for m in ["tarot", "bazi", "zodiac"]:
            print(f"=== {m} ===\n{generate_ig_caption(m)}\n")
    elif args.platform == "youtube":
        for m, d in [("bazi", "10min"), ("tarot", "8min")]:
            print(f"=== {m} ({d}) ===\n{generate_yt_script(m, d)}\n")

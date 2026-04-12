import random

# Your pools of pre-written 'fun' content blocks
intros = ["Ever dreamed of a passive income stream that actually works?", "The custom apparel world is exploding in 2026...", "Stop trading time for money. It's time to build..."]
bodies = ["When you look at [KEYWORD], the margins are insane...", "Designers are flocking to Printify for [KEYWORD] because..."]
closers = ["Don't wait. The best time to start was yesterday. The second best time is now.", "Join thousands of successful entrepreneurs today."]

def assemble_3000_words(target_keyword):
    # 1. Select and Shuffle
    content_blocks = [
        random.choice(intros),
        random.choice(bodies),
        # Add more logic here to reach 3,000 words
        f"Why {target_keyword} is the ultimate niche for 2026...",
        "### Pro Tips for Success",
        "* Focus on high-resolution graphics.",
        "* Use our [Printify Link](https://try.printify.com/r3xsnwqufe8t) for a bonus.",
        random.choice(closers)
    ]
    
    # 2. Key-Injection (The '10-into-1' Trick)
    full_text = "\n\n".join(content_blocks)
    full_text = full_text.replace("[KEYWORD]", target_keyword)
    
    return full_text

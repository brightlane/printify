import openai
import random
import schedule
import time
from datetime import datetime
import tweepy
import facebook

# Configure OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Twitter API credentials
twitter_consumer_key = 'YOUR_TWITTER_CONSUMER_KEY'
twitter_consumer_secret = 'YOUR_TWITTER_CONSUMER_SECRET'
twitter_access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
twitter_access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

# Facebook API credentials (for posting on your Facebook page)
facebook_access_token = 'YOUR_FACEBOOK_ACCESS_TOKEN'

# List of topics or keywords to base blogs on
topics = [
    "Printify Product Reviews",
    "Best Print on Demand Strategies with Printify",
    "How to Start a Printify Business",
    "Printify Affiliate Program Benefits",
    "Maximizing Profits with Printify",
    "Top Design Tips for Printify Success"
]

# Function to generate blog content
def generate_blog_content(topic):
    prompt = f"Write a 1000-1500 word blog post about '{topic}', focusing on how users can benefit from using Printify in their business. Include tips, real-world applications, and recommendations. Mention the affiliate program and encourage readers to join using your affiliate link."

    # OpenAI text generation call
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the most capable engine
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract generated content
    content = response.choices[0].text.strip()
    return content

# Function to post to Twitter
def post_to_twitter(content):
    # Set up Twitter API client
    auth = tweepy.OAuth1UserHandler(
        consumer_key=twitter_consumer_key,
        consumer_secret=twitter_consumer_secret,
        access_token=twitter_access_token,
        access_token_secret=twitter_access_token_secret
    )
    api = tweepy.API(auth)
    
    # Post tweet (Twitter has a 280-character limit, so we need to ensure the content fits)
    tweet = content[:280]  # Truncate the content to fit Twitter's character limit
    api.update_status(tweet)
    print(f"Tweet posted: {tweet}")

# Function to post to Facebook
def post_to_facebook(content):
    # Set up Facebook API client
    graph = facebook.GraphAPI(access_token=facebook_access_token, version="3.1")
    
    # Post content to your Facebook page (replace 'me' with your page's ID if posting to a page)
    graph.put_object(parent_object='me', connection_name='feed', message=content)
    print(f"Facebook post published.")

# Function to auto-generate and publish the blog
def generate_and_publish_blog():
    # Pick a random topic from the list
    topic = random.choice(topics)
    
    # Generate blog content
    content = generate_blog_content(topic)
    
    # Create blog title based on topic
    blog_title = f"Maximize Your Profits with {topic} - A Comprehensive Guide"
    
    # Date and timestamp for unique blog URLs
    date_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Print content to check (in real-life, it would be published via API to your website)
    print(f"Generated Blog Title: {blog_title}")
    print(f"Generated Content:\n{content}")
    
    # Optionally, publish the blog to a CMS like WordPress
    # Here you'd call your CMS API to publish the content
    # For example: publish_to_wordpress(blog_title, content, date_str)
    
    # Placeholder for publishing to your blog's platform
    print(f"Publishing blog at {date_str}...")
    
    # Post the generated content to Twitter and Facebook
    post_to_twitter(content)
    post_to_facebook(content)

# Function to run the scheduled task every 24 hours
def daily_blog_task():
    print(f"Generating new blog post... {datetime.now()}")
    generate_and_publish_blog()

# Schedule the task every day at a specific time (e.g., 9 AM)
schedule.every().day.at("09:00").do(daily_blog_task)

# Keep the script running to execute daily
while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for a minute before checking again

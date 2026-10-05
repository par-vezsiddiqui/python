# 3. Instagram Reel Engagement Tracker

# Store views (int), likes (int), and comments (int) for a viral reel. Calculate engagement rate percentage: ((likes + comments) / views) * 100. Print a performance audit report.

# Instagram Reel Engagement Tracker

# Step 1: Store views, likes, and comments as integers via user input
views = int(input("Enter total views: "))
likes = int(input("Enter total likes: "))
comments = int(input("Enter total comments: "))

# Step 2: Calculate total engagement and engagement rate percentage
total_engagement = likes + comments
engagement_rate = (total_engagement / views) * 100

# Step 3: Print performance audit report
print("\n" + "=" * 35)
print("   INSTAGRAM REEL PERFORMANCE AUDIT   ")
print("=" * 35)
print(f"Total Views     : {views:,}")
print(f"Total Likes     : {likes:,}")
print(f"Total Comments  : {comments:,}")
print("-" * 35)
print(f"Total Engagement: {total_engagement:,}")
print(f"Engagement Rate : {engagement_rate:.2f}%")
print("=" * 35)
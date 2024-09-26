"""
This script contains constants used across the project.
"""

# CONSTANTS FOR THE UTIL SCRIPT

from pathlib import Path


# Lists_filtering constants

script_path = Path(__file__).resolve()
project_root = script_path.parents[2]

# S3 Constants
BUCKET_NAME = "global-rct-users"
REGION_NAME = "us-west-1"

# Construct the path to the cleaned_data directory
RAW_DATA_PATH = project_root / "data" / "raw_data"
CLEAN_DATA_PATH = project_root / "data" / "cleaned_data"

# RELEVANT USER COLUMNS

USER_COLUMNS = [
    "user_id",
    "username",
    "name",
    "description",
    "user_url",
    "location",
    "search_location",
    "tweet_count",
    "followers_count",
    "following_count",
    "listed_count",
    "tweets",
    "token",
]

# NLP CONSTANTS

HUGGINGFACE_PIPELINE = "zero-shot-classification"
HUGGINGFACE_MODEL = "facebook/bart-large-mnli"
SCORE_THRESHOLD = 0.4
NUM_WORKERS = 8


# OTHER CONSTANTS

LIST_FIELDS = ["id", "name", "description"]
USER_FIELDS = [
    "created_at",
    "description",
    "entities",
    "id",
    "location",
    "most_recent_tweet_id",
    "name",
    "pinned_tweet_id",
    "profile_image_url",
    "protected",
    "public_metrics",
    "url",
    "username",
]

# TODO change the labels to more relevant stuff.
RELEVANT_LABELS = [
    "environment or pollution",
    "research",
    "politics",
    "policymaker",
    "nonprofit organization",
]
# CONSTANTS FOR SEARCH USERS AND GET LISTS SCRIPTS
# Dictionary mapping Indian state capitals to their respective states
STATE_CAPITALS = {
    "port blair": "andaman and nicobar islands",
    "hyderabad": ["andhra pradesh", "telangana"],
    "itanagar": "arunachal pradesh",
    "dispur": "assam",
    "patna": "bihar",
    "chandigarh": ["chandigarh", "punjab", "haryana"],
    "raipur": "chhattisgarh",
    "silvassa": "dadra and nagar haveli",
    "daman": "daman and diu",
    "delhi": ["uttar pradesh", "delhi", "haryana", "rajasthan"],
    "panaji": "goa",
    "gandhinagar": "gujarat",
    "shimla": "himachal pradesh",
    "srinagar": ["jammu and kashmir", "ladakh"],
    "ranchi": "jharkhand",
    "bengaluru": "karnataka",
    "thiruvananthapuram": "kerala",
    "leh": "ladakh",
    "kavaratti": "lakshadweep",
    "bhopal": "madhya pradesh",
    "mumbai": "maharashtra",
    "imphal": "manipur",
    "shillong": "meghalaya",
    "aizawl": "mizoram",
    "kohima": "nagaland",
    "bhubaneswar": "odisha",
    "puducherry": "puducherry",
    "jaipur": "rajasthan",
    "gangtok": "sikkim",
    "chennai": "tamil nadu",
    "agartala": "tripura",
    "lucknow": "uttar pradesh",
    "dehradun": "uttarakhand",
    "kolkata": "west bengal",
}


MAX_RESULTS = 99
MAX_TWEETS_FROM_USERS = 5
MAX_RESULTS_LISTS = 24
EXPANSIONS = ["author_id", "entities.mentions.username", "geo.place_id"]
TWEET_FIELDS = [
    "attachments",
    "author_id",
    "context_annotations",
    "conversation_id",
    "created_at",
    "edit_controls",
    "entities",
    "geo",
    "id",
    "in_reply_to_user_id",
    "lang",
    "public_metrics",
    "possibly_sensitive",
    "referenced_tweets",
    "reply_settings",
    "source",
    "text",
    "withheld",
]
USER_FIELDS = [
    "created_at",
    "description",
    "entities",
    "id",
    "location",
    "most_recent_tweet_id",
    "name",
    "pinned_tweet_id",
    "profile_image_url",
    "protected",
    "public_metrics",
    "url",
    "username",
]


# THRESHOLDS FOR GETTING LISTS
COUNT_THRESHOLD = 240
SLEEP_TIME = 120
GEOCODE_TIMEOUT = 5


# KEYWORD CONSTANTS

# Creating punctuations to be removed
PUNCTUATIONS = ["!" "," "." "," '"' "?" ":"]
PUNC = ""
for char in PUNCTUATIONS:
    PUNC += char

ACTIVIST_KEYWORDS = [
    "activist",
    "advocate",
    "campaigner",
    "crusader",
    "protester",
    "reformer",
    "champion",
    "fighter",
    "supporter",
    "defender",
    "militant",
    "social justice",
    "human rights",
    "equality",
    "protest",
    "demonstration",
    "advocacy",
    "grassroots",
    "change",
    "activism",
    "solidarity",
    "freedom",
    "empowerment",
    "justice",
    "civil rights",
    "rights",
    "equality",
    "liberty",
    "justice",
    "fairness",
]
POLITICS_KEYWORDS = [
    "politics",
    "political",
    "government",
    "policy",
    "election",
    "democracy",
    "governance",
    "legislation",
    "politician",
    "party",
    "candidate",
    "voting",
    "public office",
    "campaign",
    "administration",
    "constituency",
    "parliament",
    "congress",
    "senate",
    "diplomacy",
    "public policy",
    "lawmaker",
    "civic",
    "political science",
    "political party",
    "opposition",
    "congress",
    "administration",
    "governance",
    "public affairs",
    "legislation",
    "policy-making",
    "executive",
    "legislative",
    "judicial",
]
MEDIA_KEYWORDS = [
    "media",
    "journalism",
    "news",
    "reporting",
    "press",
    "broadcast",
    "communication",
    "journalist",
    "reporter",
    "editor",
    "publisher",
    "newsroom",
    "coverage",
    "broadcasting",
    "newscast",
    "information",
    "current affairs",
    "headline",
    "correspondent",
    "media outlet",
    "coverage",
    "editorial",
    "press release",
    "journalism",
    "media industry",
    "reporting",
    "newsroom",
    "headline",
    "current events",
    "broadcast",
]
ORGANIZATION_KEYWORDS = [
    "official",
    "company",
    "organization",
    "corporation",
    "collective",
    "group",
    "association",
    "enterprise",
    "foundation",
    "institute",
    "team",
    "society",
    "union",
    "network",
    "coalition",
    "syndicate",
    "consortium",
    "firm",
    "club",
    "guild",
    "committee",
    "bureau",
    "agency",
    "cooperative",
    "office",
    "sector",
    "service",
    "branch",
    "division",
    "subsidiary",
    "affiliate",
    "nonprofit",
    "charity",
    "NGO",
    "non-governmental organization",
    "advocacy",
    "humanitarian",
    "volunteer",
    "philanthropy",
    "community",
    "society",
    "coalition",
    "alliance",
    "initiative",
    "campaign",
    "movement",
    "project",
    "network",
    "consortium",
    "union",
    "association",
    "cooperative",
    "collective",
    "group",
    "committee",
    "team",
    "council",
    "partnership",
    "collaborative",
    "forum",
    "guild",
    "federation",
    "civic",
    "public service",
    "social impact",
    "sustainable",
    "environmental",
    "social responsibility",
    "community service",
    "global",
    "international",
    "worldwide",
    "multinational",
    "transnational",
    "globalized",
    "organization",
    "corporation",
    "business",
    "enterprise",
    "agency",
    "firm",
    "institute",
    "association",
    "group",
    "foundation",
    "committee",
    "nonprofit",
    "charity",
    "NGO",
    "collective",
    "coalition",
    "alliance",
    "initiative",
    "movement",
    "network",
    "union",
    "team",
    "council",
    "partnership",
    "collaborative",
    "forum",
    "service",
    "community",
    "sector",
]
GOVERNMENT_KEYWORDS = [
    "government",
    "govt",
    "gov",
    "public sector",
    "office of",
    "public administration",
    "public service",
    "public policy",
    "civil service",
    "governmental",
    "state",
    "federal",
    "local government",
    "administration",
    "governance",
    "public affairs",
    "regulation",
    "authority",
    "bureaucracy",
    "policy-making",
    "public office",
    "official",
    "public servant",
    "civil servant",
    "legislation",
    "executive",
    "legislative",
    "judicial",
    "government agency",
    "public institution",
    "government",
    "govt",
    "gov",
    "public sector",
    "office of",
    "administration",
    "regulation",
    "authority",
    "bureaucracy",
    "policy-making",
    "public office",
    "legislation",
    "executive",
    "legislative",
    "judicial",
    "government agency",
    "institution",
    "public service",
    "public sector",
    "civil service",
    "local government",
    "federal government",
    "state government",
    "public administration",
    "governmental",
    "administration",
    "president",
    "prime minister",
    "parliament",
]

CATEGORIES = {
    "Activist": ACTIVIST_KEYWORDS,
    "Politics": POLITICS_KEYWORDS,
    "Media": MEDIA_KEYWORDS,
    "Organization": ORGANIZATION_KEYWORDS,
    "Government": GOVERNMENT_KEYWORDS,
}

# words to be ignored in indexing
INDEX_IGNORE = (
    "a",
    "an",
    "and",
    "&",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "was",
    "were",
    "will",
    "with",
)


dict = {
    "TV Shows": 3,
    "TV Episodes": 4,
    "Sports Events": 6,
    "Person": 10,
    "Sport": 11,
    "Sports Team": 12,
    "Place": 13,
    "TV Genres": 22,
    "TV Channels": 23,
    "Sports League": 26,
    "American Football Game": 27,
    "NFL Football Game": 28,
    "Events": 29,
    "Community": 31,
    "Politicians": 35,
    "Political Race": 38,
    "Basketball Game": 39,
    "Sports Series": 40,
    "Soccer Match": 43,
    "Baseball Game": 44,
    "Brand Vertical": 45,
    "Brand Category": 46,
    "Brand": 47,
    "Product": 48,
    "Musician": 54,
    "Music Genre": 55,
    "Actor": 56,
    "Entertainment Personality": 58,
    "Athlete": 60,
    "Interests and Hobbies Vertical": 65,
    "Interests and Hobbies Category": 66,
    "Interests and Hobbies": 67,
    "Hockey Game": 68,
    "Video Game": 71,
    "Video Game Publisher": 78,
    "Video Game Hardware": 79,
    "Cricket Match": 83,
    "Book": 84,
    "Book Genre": 85,
    "Movie": 86,
    "Movie Genre": 87,
    "Political Body": 88,
    "Music Album": 89,
    "Radio Station": 90,
    "Podcast": 91,
    "Sports Personality": 92,
    "Coach": 93,
    "Journalist": 94,
    "TV Channel [Entity Service]": 95,
    "Reoccurring Trends": 109,
    "Viral Accounts": 110,
    "Concert": 114,
    "Video Game Conference": 115,
    "Video Game Tournament": 116,
    "Movie Festival": 117,
    "Award Show": 118,
    "Holiday": 119,
    "Digital Creator": 120,
    "Fictional Character": 122,
    "Multimedia Franchise": 130,
    "Unified Twitter Taxonomy": 131,
    "Video Game Personality": 136,
    "eSports Team": 137,
    "eSports Player": 138,
    "Fan Community": 139,
    "Esports League": 149,
    "Food": 152,
    "Weather": 155,
    "Cities": 156,
    "Colleges & Universities": 157,
    "Points of Interest": 158,
    "States": 159,
    "Countries": 160,
    "Exercise & fitness": 162,
    "Travel": 163,
    "Fields of study": 164,
    "Technology": 165,
    "Stocks": 166,
    "Animals": 167,
    "Local News": 171,
    "Global TV Show": 172,
    "Google Product Taxonomy": 173,
    "Digital Assets & Crypto": 174,
    "Emergency Events": 175,
}


category_dict = category_dict = {
    "media": [
        "tv shows",
        "tv episodes",
        "tv genres",
        "tv channels",
        "radio station",
        "podcast",
        "global tv show",
        "video game",
        "movie",
        "music album",
        "video game conference",
        "video game tournament",
        "movie festival",
        "concert",
        "award show",
        "holiday",
        "digital creator",
        "multimedia franchise",
        "digital assets & crypto",
        "local news",
        "journalist",
        "sports events",
        "basketball game",
        "sports series",
        "soccer match",
        "baseball game",
        "hockey game",
        "cricket match",
        "sports personality",
        "coach",
        "esports team",
        "esports player",
        "fan community",
        "esports league",
        "digital creator",
    ],
    "organizations": [
        "community",
        "brand vertical",
        "brand category",
        "brand",
        "product",
        "unified twitter taxonomy",
        "google product taxonomy",
        "digital assets & crypto",
        "colleges & universities",
        "points of interest",
    ],
    "policymaker": ["political race", "political body", "emergency events"],
    "politicians": ["politicians", "political race"],
    "researcher": ["Technology"],
    "environment": [
        "weather",
        "cities",
        "states",
        "countries",
        "emergency events",
    ],
}

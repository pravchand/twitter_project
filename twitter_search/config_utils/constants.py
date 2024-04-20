"""
This script contains constants used across the project.
"""

# CONSTANTS FOR THE UTIL SCRIPT

# NLP CONSTANTS

HUGGINGFACE_PIPELINE = "zero-shot-classification"

HUGGINGFACE_MODEL = "facebook/bart-large-mnli"

SCORE_THRESHOLD = 0.5

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

#TODO change the labels to more relevant stuff.
RELEVANT_LABELS = ["pollution", "environment", "public health", "climate"]
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


MAX_RESULTS = 25
MAX_RESULTS_LISTS = 100
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
COUNT_THRESHOLD = 24
SLEEP_TIME = 300


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

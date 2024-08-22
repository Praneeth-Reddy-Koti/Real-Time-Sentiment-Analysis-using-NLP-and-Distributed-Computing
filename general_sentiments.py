def analyze_general_sentiment(text):
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()

    # List of positive and negative keywords
    positive_keywords = [
        "love", "like", "awesome", "great", "happy", "amazing", "wonderful", "excellent", "fantastic", "joy",
        "pleasure", "delight", "good", "best", "beautiful", "superb", "adore", "enjoy", "glad", "satisfy",
        "fabulous", "lovely", "fantastic", "terrific", "thrilled", "grateful", "ecstatic", "wonderful", "perfect",
        "cheery", "blissful", "jubilant", "excited", "elated", "content", "radiant", "delighted", "overjoyed",
        "enthusiastic", "pleased", "positive", "sweet", "exhilarated", "blessed", "euphoric", "glorious",
        "appreciate", "satisfied", "charming", "fabulous", "marvelous", "admirable", "sensational", "charismatic",
        "vibrant", "sparkling", "splendid", "divine", "angelic", "serene", "ravishing", "uplifting", "exquisite",
        "majestic", "stunning", "bliss", "fascinating", "mesmerizing", "thrilling", "rapture", "paradise",
        "phenomenal", "wondrous", "idyllic", "gorgeous", "brilliant", "ecstasy", "radiance", "heavenly",
        "delirious", "exultant", "gleeful", "magnificent", "elevated", "ecstatic", "affectionate", "ardent",
        "affirmative", "ardor", "beneficial", "buoyant", "charitable", "cheerful", "chipper", "comforting",
        "compliment", "congratulate", "cute", "dazzling", "divine", "dream", "easy", "ebullient", "eclectic",
        "effervescent", "embrace", "encourage", "energetic", "enthusiastic", "euphoria", "exaltation", "fairy",
        "favorite", "fun", "glee", "gracious", "happy", "harmony", "healing", "healthy", "heartfelt", "heaven",
        "hooray", "hope", "illuminate", "inspiration", "jolly", "jovial", "kind", "lighthearted", "love", "lucky",
        "merry", "miracle", "noble", "optimism", "paradise", "passion", "peace", "playful", "pleasant", "precious",
        "pride", "pure", "rejoice", "relax", "relief", "reverent", "reward", "romantic", "savor", "smile", "soft",
        "soothing", "spirit", "splendid", "sublime", "sunshine", "sweet", "tender", "thankful", "thrill", "tranquil",
        "treasure", "upbeat", "valiant", "victorious", "vitality", "warm", "welcome", "wholesome", "wondrous",
        "worthy", "zeal", "zest", "attractive", "benevolent", "blithesome", "buoyant", "charismatic", "confident",
        "congratulatory", "dazzling", "dynamic", "ecstatic", "effusive", "empathy", "enchantment", "endearing",
        "energizing", "enthralling", "esteem", "festive", "forgiving", "gleeful", "gratifying", "heartwarming",
        "heavenly", "ideal", "inspiring", "jubilant", "kindness", "lively", "lovable", "luxurious", "magnetic",
        "mirthful", "opulent", "paragon", "perky", "proud", "radiant", "refreshing", "resplendent", "sanguine",
        "sensational", "sincere", "sprightly", "stellar", "stimulating", "sublime", "sunlit", "supportive",
        "thriving", "triumphant", "unforgettable", "vibrant", "victorious", "vivacious", "warmhearted", "whimsical",
        "winsome", "witty", "zealous"
    ]

    negative_keywords = [
        "hate", "dislike", "awful", "terrible", "horrible", "bad", "sad", "angry", "disgust", "unhappy",
        "disappoint", "miserable", "annoy", "frustrate", "regret", "fail", "pain", "upset", "depress", "lousy",
        "unfortunate", "inferior", "ugly", "problem", "worse", "dreadful", "abysmal", "repulsive", "vile", "despise",
        "loathe", "detest", "appalled", "displeased", "discontent", "abhor", "desperate", "disastrous", "wretched",
        "dismal", "gloomy", "dreary", "pessimistic", "melancholy", "grief", "despair", "sorrow", "heartbroken",
        "distraught", "agonizing", "mournful", "frustrating", "disheartened", "dejected", "morose", "dismayed",
        "anguish", "abominable", "atrocity", "betrayal", "bitter", "catastrophe", "corrupt", "cry", "damage",
        "deadly", "defective", "deplorable", "desolate", "destructive", "dire", "dirty", "discomfort", "disease",
        "disgusting", "dishonest", "dismaying", "distress", "dread", "evil", "fail", "fake", "fear", "filthy",
        "foolish", "foul", "frightful", "grieve", "gross", "guilt", "hardship", "harmful", "hate", "haunt",
        "heartbreaking", "hideous", "hostile", "hurt", "ignorant", "ill", "inferior", "injure", "insidious",
        "insult", "intolerable", "irritate", "lamentable", "lousy", "lying", "malicious", "miserable", "mourn",
        "nasty", "nauseate", "negative", "noxious", "objectionable", "offensive", "painful", "pathetic", "pitiful",
        "plague", "poor", "rage", "repellent", "resentment", "rotten", "ruin", "sad", "savage", "scare", "scorn",
        "scream", "selfish", "shameful", "shocking", "sick", "sinister", "sorrow", "sorry", "stink", "stress",
        "suffering", "torture", "toxic", "tragic", "trouble", "ugly", "unbearable", "unethical", "unfair", "unfit",
        "unfortunate", "unpleasant", "unsightly", "unwanted", "vicious", "vile", "villainous", "vulgar", "wicked",
        "woeful", "worse", "worthless", "wrong", "yucky", 'disappointed'
    ]

    # List of negation words
    negations = [
        "not", "no", "none", "cannot", "isn't", "wasn't", "shouldn't", "wouldn't", "couldn't", "don't", "doesn't",
        "didn't", "won't", "haven't", "hasn't", "hadn't", "never", "nothing", "nowhere", "noone", "neither",
        "nor", "barely", "hardly", "scarcely", "rarely", "few", "little"
    ]

    # Split text into words
    words = text_lower.split()

    # Initialize sentiment counters
    positive_count = 0
    negative_count = 0

    for i, word in enumerate(words):
        for positive_keyword in positive_keywords:
            if positive_keyword in word:
                # Check if the word is preceded by a negation within the previous three words
                if any(words[j] in negations for j in range(max(0, i - 3), i)):
                    negative_count += 1
                else:
                    positive_count += 1
                break

        for negative_keyword in negative_keywords:
            if negative_keyword in word:
                # Check if the word is preceded by a negation within the previous three words
                if any(words[j] in negations for j in range(max(0, i - 3), i)):
                    positive_count += 1
                else:
                    negative_count += 1
                break

    # Determine overall sentiment
    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

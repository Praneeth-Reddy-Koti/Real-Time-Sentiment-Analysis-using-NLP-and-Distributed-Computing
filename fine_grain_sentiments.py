def analyze_fine_grain_sentiment(text):
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()

    # List of fine-grain emotions
    fine_grain_emotions = {
      "excited": ["excited", "thrilled", "enthusiastic", "eager", "ecstatic", "elated", "overjoyed", "pumped", "gleeful", "animated", "thrilled", "delighted", "joyous", "radiant", "vibrant"],
      "depressed": ["depressed", "sad", "down", "despondent", "melancholy", "gloomy", "despairing", "miserable", "disheartened", "blue", "sorrowful", "weepy", "desolate", "forlorn", "brokenhearted"],
      "happy": ["happy", "joyful", "cheerful", "content", "pleased", "delighted", "satisfied", "glad", "joyous", "elated", "blissful", "ecstatic", "euphoric", "radiant", "jubilant"],
      "angry": ["angry", "irritated", "frustrated", "outraged", "furious", "resentful", "aggravated", "infuriated", "livid", "incensed", "fuming", "enraged", "wrathful", "indignant", "irate"],
      "confused": ["confused", "puzzled", "baffled", "bewildered", "perplexed", "mystified", "disoriented", "lost", "flustered", "dazed", "stumped", "foggy", "befuddled", "discombobulated", "nonplussed"],
      "anxious": ["anxious", "nervous", "worried", "apprehensive", "uneasy", "tense", "fearful", "panicked", "agitated", "jittery", "trepidatious", "edgy", "fretful", "petrified", "paranoid"],
      "surprised": ["surprised", "shocked", "amazed", "astonished", "astounded", "startled", "dumbfounded", "stunned", "flabbergasted", "awe-struck", "boggled", "gobsmacked", "taken aback", "speechless", "mind-blown"],
      "disgusted": ["disgusted", "revolted", "repulsed", "nauseated", "sickened", "appalled", "abhorrent", "horrified", "offended", "repelled", "vomit-inducing", "loathe", "odious", "detestable", "grotesque"],
      "hopeful": ["hopeful", "optimistic", "confident", "encouraged", "inspired", "expectant", "upbeat", "reassured", "buoyant", "positive", "heartened", "assured", "sanguine", "cheery", "promising"],
      "nostalgic": ["nostalgic", "sentimental", "wistful", "longing", "yearning", "homesick", "remorseful", "pensive", "reflective", "melancholic", "bittersweet", "yearning", "reminiscent", "wistful", "regretful"],
      "amused": ["amused", "entertained", "charmed", "tickled", "delighted", "gleeful", "humored", "jovial", "merry", "lighthearted", "hilarious", "uproarious", "comical", "jocular", "festive"],
      "fearful": ["fearful", "scared", "terrified", "petrified", "panicked", "horrified", "dreadful", "frightened", "anxious", "worried", "nervous", "apprehensive", "timid", "tense", "cowardly"],
      "curious": ["curious", "inquisitive", "interested", "intrigued", "inquiring", "nosy", "eager", "engrossed", "fascinated", "exploratory", "probing", "questioning", "analytical", "adventurous", "open-minded"],
      "relieved": ["relieved", "calm", "soothed", "rested", "reassured", "comforted", "content", "serene", "placid", "pacified", "unburdened", "easygoing", "trouble-free", "at ease", "light-hearted"],
      "disappointed": ["disappointed", "let down", "unhappy", "dismayed", "crestfallen", "chagrined", "regretful", "displeased", "deflated", "saddened", "frustrated", "unsatisfied", "underwhelmed", "disheartened", "bitter"],
      "hopeless": ["hopeless", "desperate", "despondent", "pessimistic", "resigned", "dismal", "forlorn", "dejected", "discouraged", "defeated", "melancholic", "downhearted", "wretched", "gloomy", "bleak"],
      "nostalgic": ["nostalgic", "sentimental", "wistful", "longing", "yearning", "homesick", "remorseful", "pensive", "reflective", "melancholic", "bittersweet", "yearning", "reminiscent", "wistful", "regretful"],
      "grateful": ["grateful", "thankful", "appreciative", "indebted", "obliged", "gracious", "acknowledging", "blessed", "privileged", "favored", "graceful", "humble", "charitable", "reverent", "adoring"],
      "proud": ["proud", "self-satisfied", "smug", "conceited", "arrogant", "vain", "boastful", "haughty", "egotistical", "cocky", "snooty", "swaggering", "imperious", "pompous", "supercilious"],
      "jealous": ["jealous", "envious", "covetous", "possessive", "suspicious", "resentful", "green-eyed", "competitive", "zealous", "insecure", "guarded", "watchful", "paranoid", "territorial", "protective"],
    }


    # Initialize sentiment
    sentiment = "neutral"

    # Check for each fine-grain emotion
    for emotion, keywords in fine_grain_emotions.items():
        for keyword in keywords:
            if keyword in text_lower:
                sentiment = emotion
                break  # Exit loop if emotion keyword is found

    return sentiment
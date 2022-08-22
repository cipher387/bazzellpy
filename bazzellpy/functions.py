# All Bazzell tools available here: https://inteltechniques.com/tools/

# Search engines tool: https://inteltechniques.com/tools/Search.html

def searchengines(query: str) -> dict:
    """
    Output a dict containing the URLs for your query across all search engines.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    SEdict = {
        "Surface web": {
            "Google": f"http://google.com/search?q={query}",
            "Google Date": f"http://google.com/search?q={query}&tbs=cdr:1,cd_min:1/1/0,sbd:1",
            "Google News": f"http://www.google.com/search?tbm=nws&q={query}",
            "Google Blogs": f"https://www.google.com/search?q={query}&tbm=nws&tbs=nrt:b",
            "Google FTP": f"https://www.google.com/search?q=inurl%3Aftp%20-inurl%3A(http|https)%20{query}",
            "Google Index": f"https://www.google.com/search?q=intitle%3Aindex.of+{query}",
            "Google Scholar": f"http://scholar.google.com/scholar?&q={query}",
            "Google Patents": f"https://patents.google.com/?q={query}",
            "Bing": f"http://bing.com/search?q={query}",
            "Bing News": f"http://bing.com/news/search?q={query}",
            "Yahoo": f"http://search.yahoo.com/search?p={query}",
            "Yandex": f"http://www.yandex.com/yandsearch?text={query}",
            "Baidu": f"http://baidu.com/s?wd={query}",
            "Searx": f"https://searx.be/?q={query}",
            "Exalead": f"http://www.exalead.com/search/web/results/?q={query}",
            "DuckDuckGo": f"https://duckduckgo.com/?q={query}",
            "StartPage": f"https://startpage.com/do/search?q={query}",
            "Qwant": f"https://www.qwant.com/?q={query}",
            "Brave": f"https://search.brave.com/search?q={query}",
            "Wayback": f"https://web.archive.org/web/*/{query}",
            "Ahmia": f"https://ahmia.fi/search/?q={query}",
            "Onionland": f"https://onionlandsearchengine.com/search?q={query}"
        },
        "Dark web": {
            "Torch": f"http://torch4st4l57l2u2vr5wqwvwyueucvnrao4xajqr2klmcmicrv7ccaad.onion/search?query={query}&action=search",
            "Tor66": f"http://www.tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/search?q={query}",
            "Haystack": f"http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q={query}",
            "Ahmia": f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={query}",
            "SearchDemon": f"http://srcdemonm74icqjvejew6fprssuolyoc2usjdwflevbdpqoetw4x3ead.onion/search?q={query}",
            "Excavator": f"http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion/search/{query}",
            "GDark": f"http://zb2jtkhnbvhkya3d46twv3g7lkobi4s62tjffqmafjibixk6pmq75did.onion/gdark/search.php?query={query}",
            "Hidden Reviews": f"http://u5lyidiw4lpkonoctpqzxgyk6xop7w7w3oho4dzzsi272rwnjhyx7ayd.onion/?s={query}",
            "OnionLand": f"http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/search?q={query}",
            "Phobos": f"http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query={query}",
            "Submarine": f"http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term={query}",
            "DeepSearch": f"http://searchgf7gdtauh7bhnbyed4ivxqmuoat3nm6zfrg3ymkq6mtnpye3ad.onion/search?q={query}",
            "OnionCenter": f"http://5qqrlc7hw3tsgokkqifb33p3mrlpnleka2bjg7n46vih2synghb6ycid.onion/index.php?a=search&q={query}",
            "FreshOnion": f"http://freshonifyfe4rmuh6qwpsexfhdrww7wnt5qmkoertwxmcuvm4woo4ad.onion/?query={query}"
        }
    }

    return SEdict

# Segmented Facebook tool into separate functions
# Tools available here: https://inteltechniques.com/tools/Facebook.html

def facebook_user(username: str, userno: str) -> dict:
    """
    Output a dict containing links to different parts of a user's Facebook profile.

    :param username: the username to search - input "" if not available
    :param userno: the user number to search - input "" if not available
    :return: dict containing links to various parts of user profile
    """

    if username=="":
        FBdict_username = {"Username search": "Nothing returned - no username supplied to search"}
    else:
        FBdict_username = {
            "Timeline": f"https://www.facebook.com/{username}",
            "About": f"https://www.facebook.com/{username}/about",
            "Employment": f"https://www.facebook.com/{username}/about?section=work",
            "Education": f"https://www.facebook.com/{username}/about?section=education",
            "Locations": f"https://www.facebook.com/{username}/about?section=living",
            "Contact Info": f"https://www.facebook.com/{username}/about?section=contact-info",
            "Basic Info": f"https://www.facebook.com/{username}/about?section=basic-info",
            "Relationship": f"https://www.facebook.com/{username}/about?section=relationship",
            "Family": f"https://www.facebook.com/{username}/about?section=family",
            "Biography": f"https://www.facebook.com/{username}/about?section=bio",
            "Life Events": f"https://www.facebook.com/{username}/about?section=year-overviews",
            "Friends": f"https://www.facebook.com/{username}/friends",
            "Photos": f"https://www.facebook.com/{username}/photos",
            "Photo Albums": f"https://www.facebook.com/{username}/photos_albums",
            "Videos": f"https://www.facebook.com/{username}/videos",
            "Check-ins": f"https://www.facebook.com/{username}/places_visited",
            "Recent check-ins": f"https://www.facebook.com/{username}/places_recent",
            "Sports": f"https://www.facebook.com/{username}/sports",
            "Music": f"https://www.facebook.com/{username}/music",
            "Movies": f"https://www.facebook.com/{username}/movies",
            "TV": f"https://www.facebook.com/{username}/tv",
            "Books": f"https://www.facebook.com/{username}/books",
            "Apps & Games": f"https://www.facebook.com/{username}/games",
            "Likes": f"https://www.facebook.com/{username}/likes",
            "Events": f"https://www.facebook.com/{username}/events",
            "Facts": f"https://www.facebook.com/{username}/did_you_know",
            "Reviews": f"https://www.facebook.com/{username}/reviews",
            "Notes": f"https://www.facebook.com/{username}/notes"
        }
    
    if userno=="":
        FBdict_userno = {"User number search": "Nothing returned - no user number supplied to search"}
    else:
        FBdict_userno = {
            "Profile":f"https://www.facebook.com/{userno}"
        }

    FBdict = {
        "Username": FBdict_username,
        "User number": FBdict_userno
    }

    return FBdict

def facebook_search(query: str) -> dict:
    """
    Output a dict containing links to various engines to search terms across facebook.

    :param query: the term you want to search
    :return: dict containing links to the search results for your query
    """

    FBdict = {
        "All": f"https://www.facebook.com/search/top/?q={query}",
        "Posts": f"https://www.facebook.com/search/posts/?q={query}",
        "People": f"https://www.facebook.com/search/people/?q={query}",
        "Photos": f"https://www.facebook.com/search/photos/?q={query}",
        "Videos": f"https://www.facebook.com/search/videos/?q={query}",
        "Marketplace": f"https://www.facebook.com/search/marketplace/?q={query}",
        "Pages": f"https://www.facebook.com/search/pages/?q={query}",
        "Places": f"https://www.facebook.com/search/places/?q={query}",
        "Groups": f"https://www.facebook.com/search/groups/?q={query}",
        "Apps": f"https://www.facebook.com/search/apps/?q={query}",
        "Events": f"https://www.facebook.com/search/events/?q={query}",
        "Links": f"https://www.facebook.com/search/links/?q={query}"
    }

    return FBdict

def facebook_mutuality(UID1: str, UID2: str) -> str:
    """
    Output a string containing a URL showing common friends between two user IDs.

    :param UID1: the first User ID
    :param UID2: the second User ID
    :return: common friends result URL as string
    """

    FBstr = f"https://facebook.com/browse/mutual_friends/?uid={UID1}&node={UID2}",
    
    return FBstr

# Segmented Twitter tool into separate functions
# Twitter tool: https://inteltechniques.com/tools/Twitter.html

def twitter_user(query: str) -> dict:
    """
    Takes Twitter username as string and returns dict of URLs to aspects of profile and third-party analysis tools
    
    :param query: the Twitter username you want to query
    :return: dictionary of URLs - Twitter profile & third-party analysis
    """

    Twitdict = {
        "Twitter Profile": f"https://twitter.com/{query}",
        "Outgoing Tweets": f"https://twitter.com/search?q=from%3A{query}&f=live",
        "Incoming Tweets": f"https://twitter.com/search?q=to%3A{query}&f=live",
        "Media Tweets": f"https://twitter.com/{query}/media/",
        "Liked Tweets": f"https://twitter.com/{query}/likes/"
        "Lists Created": f"https://twitter.com/{query}/lists/",
        "Lists Included": f"https://twitter.com/{query}/lists/memberships",
        "Moments": f"https://twitter.com/{query}/moments",
        "Topics": f"https://twitter.com/{query}/topics",
        "Followers": f"https://twitter.com/{query}/followers",
        "Following": f"https://twitter.com/{query}/following",
        "Social Bearing": f"https://socialbearing.com/search/user/{query}",
        "FollerMe": f"https://foller.me/{query}",
        "Google Archives": f"http://google.com/search?q=site%3Atwitter.com%2F{query}",
        "Google Tweets": f"https://www.google.com/search?q=site%3Atwitter.com%2F{query}%2Fstatus%2F",
        "Bing Archives": f"http://www.bing.com/search?q=twitter.com/{query}",
        "Yandex Archives": f"https://www.yandex.com/search/?text=https%3A%2F%2Ftwitter.com%2F{query}",
        "Google Cache": f"https://webcache.googleusercontent.com/search?q=cache:https://twitter.com/{query}",
        "Wayback Machine": f"http://web.archive.org/web/*/twitter.com/{query}",
        "Historical": f"https://memory.lol/tw/{query}",
        "Spoonbill": f"https://spoonbill.io/data/{query}",
        "Friend Analysis": f"https://followerwonk.com/analyze/{query}",
        "Follower Analysis": f"https://followerwonk.com/analyze/{query}?op=fl",
        "Twitter Audit": f"https://www.twitteraudit.com/{query}",
        "Twitonomy": f"https://www.twitonomy.com/profile.php?sn={query}"
    }
    
    return Twitdict

def twitter_user_year(query: str, year: str) -> dict:
    """
    See a Twitter user's activity during a specific year

    :param query: the user's username
    :param year: the year you are interested in
    :return: dict of URLs that chops up activity in various ways to be selected from for further analysis 
    """

    Twitdict = {
        "Outgoing by Year": f"https://twitter.com/search?q=from%3A{query}}%20since%3A{year}-01-01%20until%3A{year}-12-31&src=typd&f=live",
        "Incoming by Year": f"https://twitter.com/search?q=to%3A{query}%20since%3A{year}-01-01%20until%3A{year}-12-31&src=typd&f=live",
        "Media by Year": f"https://twitter.com/search?q=from%3A{query}%20since%3A{year}-01-01%20until%3A{year}-12-31%20filter%3Amedia&src=typd&f=live",
        "No Replies": f"https://twitter.com/search?q=from%3A{query}%20since%3A{year}-01-01%20until%3A{year}-12-31%20-filter%3Areplies&src=typd&f=live",
        "Only Replies": f"https://twitter.com/search?q=from%3A{query}%20since%3A{year}-01-01%20until%3A{year}-12-31%20filter%3Areplies&src=typd&f=live"
    }
    
    return Twitdict

def twitter_query_year(query: str, year: str) -> str:
    """
    Returns a URL giving activity for a specific term for a particular year

    :param query: search term(s)
    :param year: the year you are interested in
    :return: string of URL to page displaying activity
    """

    Twitstr = f"https://twitter.com/search?q={query}%20since%3A{year}-01-01%20until%3A{year}-12-31&src=typd&f=live"
    
    return Twitstr

def twitter_real_name(forename: str, surname: str) -> dict:
    """
    Identify Twitter Profiles using an individual's real name.

    :param forename: the individual's real first name
    :param surname: the individual's real surname
    :return: dict containing two URLs of search results
    """

    Twitdict = {
        "Profile Search I": f"https://twitter.com/search?q={forename}%20{surname}&f=user",
        "Profile Search II": f"http://followerwonk.com/bio/?q_type=all&n={forename}%20{surname}"
    }
    
    return Twitdict

def twitter_lists(list_number: str) -> dict:
    """
    Return URLs with details about Twitter lists (members and followers).

    :param list_number: the ID number of the list
    :return: dict containing the URLs
    """

    Twitdict = {
        "List": f"https://twitter.com/i/lists/{query}",
        "List Members": f"https://twitter.com/i/lists/{query}/members",
        "List Followers": f"https://twitter.com/i/lists/{query}/followers"
    }
    
    return Twitdict

# Segmented Insta tool into separate functions
# Insta tool: https://inteltechniques.com/tools/Instagram.html

def instagram_user(query: str) -> dict:
    """
    Various basic queries if all you have to go on is an Instagram username

    :param query: individual's username
    :return: dict containing URLs of results
    """

    Instadict = {
        "IG Profile": f"http://instagram.com/{query}",
        "IG Channel": f"http://instagram.com/{query}/channel/",
        "IG Tagged": f"https://instagram.com/{query}/tagged/",
        "Outgoing Search": f'https://www.google.com/search?q=site%3Ainstagram.com+"{query}%22"',
        "Incoming Search": f'https://www.google.com/search?q=site%3Ainstagram.com+"@{query}"',
        "Bing Search": f'https://www.bing.com/search?q=site%3Ainstagram.com+"{query}"',
        "Yandex Search": f'https://yandex.com/search/?text=site%3Ainstagram.com+"{query}"',
        "Twitter Posts": f'https://www.google.com/search?q=site%3Atwitter.com+“{query}”+“instagram.com%2Fp”',
        "Dumpor Profile": f"https://dumpor.com/v/{query}"
    }
    
    return Instadict

def instagram_follow(query: str) -> dict:
    """
    Directs to webpages containing a user's followers and who they follow

    :param query: the individual's username
    :return: dict containing the URLs of the followers and following webpages
    """

    Instadict = {
        "Followers": 'https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={%22id%22:%22%{que}%22,%22include_reel%22:true,%22fetch_mutual%22:true,%22first%22:50}'.format(que=query),
        "Following": 'https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={%22id%22:%22{que}%22,%22include_reel%22:true,%22fetch_mutual%22:false,%22first%22:50}'.format(que=query)
    }
    
    return Instadict

def instagram_user_term(user: str, search_term: str) -> str:
    """
    Searches out a user plus a search term

    :param user: individual's username
    :param search_term: self-explanatory
    :return: string URL for search results
    """

    Instastr = f'https://www.google.com/search?&q=site%3Ainstagram.com+“{user}”+“{search_term}”'
    
    return Instastr

def instagram_association(user1: str, user2: str) -> str:
    """
    Identifies associations between two Instagram users

    :param user1: first individual's username
    :param user2: second individual's username
    :return: string URL for search results
    """

    Instastr = f'https://www.google.com/search?&q=site%3Ainstagram.com+“{user1}”+“{user2}”'
    
    return Instastr

def instagram_search_or_tag(query: str) -> dict:
    """
    Results of search term or tag queries on Instagram

    :param query: the search term
    :return: dict of search result URLs
    """

    Instadict = {
        "Tags": f'https://www.instagram.com/explore/tags/{query}',
        "Search": f'https://www.google.com/search?&q=site%3Ainstagram.com+{query}',
        "Dumpor Tag": f'https://dumpor.com/t/{query}'
    }
    
    return Instadict

# Segmented LinkedIn tool into separate functions
# LinkedIn tool: https://inteltechniques.com/tools/Linkedin.html 

def linkedin_person_search(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> str:
    """
    Search result of profile matching a given forename, surname, title, company, school and keyword

    :param forename: self-explanatory
    :param surname: self-explanatory
    :param keyword: self-explanatory
    :param title: individual's job title
    :param company: self-explanatory
    :param school: self-explanatory
    :return: string containing URL of search result
    """

    Linkstr = f'https://www.linkedin.com/search/results/people/?keywords={keyword}&firstName={forename}&lastName={surname}&title={title}&company={company}&school={school}'
    
    return Linkstr

def linkedin_post_search(keyword: str, title: str) -> str:
    """
    Searches posts given one or more keywords and the poster's job title

    :param keyword: self-explanatory
    :param title: poster's job title
    :return: string containing URL of search result
    """

    Linkstr = f'https://www.linkedin.com/search/results/content/?authorJobTitle=%22{title}%22&keywords={keyword}'
    
    return Linkstr

def linkedin_google_bing_yandex(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> dict:
    """
    Search engine results for LinkedIn profiles matching a given forename, surname, title, company, school and keyword

    :param forename: self-explanatory
    :param surname: self-explanatory
    :param keyword: self-explanatory
    :param title: individual's job title
    :param company: self-explanatory
    :param school: self-explanatory
    :return: dict containing URLs of search results
    """

    Linkdict = {
        "Google": f"https://www.google.com/search?q=site%3Awww.linkedin.com+{keyword}+{forename}+{surname}+{title}+{company}+{school}",
        "Bing": f"https://www.bing.com/search?q=site%3Alinkedin.com+{keyword}+{forename}+{surname}+{title}+{company}+{school}",
        "Yandex": f"https://www.yandex.com/search/?text=site%3Alinkedin.com+{keyword}+{forename}+{surname}+{title}+{company}+{school}"
    }

    return Linkdict

# Communities tool: https://inteltechniques.com/tools/Communities.html
#       Only implementing this tool in part because some parts seem redundant

def community_query(query: str) -> dict:
    """
    Username and profile searches on Reddit, Hacker News, TikTok, Meetup, Ebay, Pintrest, Discord, Telegram, Parler and Gab

    :param query: username to search
    :return: dict of URLs of search results
    """

    Commdict = {
        "Reddit": {
            "User Profile": f"https://old.reddit.com/user/{query}",
            "User Posts": f"https://old.reddit.com/user/{query}/posts/",
            "User Comments": f"https://old.reddit.com/user/{query}/comments/",
            "Reddit Archive I": f"https://web.archive.org/web/*/https://www.reddit.com/user/{query}",
            "Reddit Archive II": f"https://webcache.googleusercontent.com/search?q=cache:https://www.reddit.com/user/{query}",
            "Pushshift": {
                "I": f"https://api.pushshift.io/reddit/search/comment/?author={query}&sort=asc&size=1000",
                "II": f"https://api.pushshift.io/reddit/search/comment/?author={query}",
                "III": f"https://api.pushshift.io/reddit/search/comment/?q={query}",
                "IV": f"https://api.pushshift.io/reddit/search/submission/?q={query}"
            }
        },
        "Hacker News": {
            "User Search": f"https://news.ycombinator.com/user?id={query}",
            "User Posts": f"https://news.ycombinator.com/submitted?id={query}",
            "User Comments": f"https://news.ycombinator.com/threads?id={query}",
            "Favorites": f"https://news.ycombinator.com/favorites?id={query}"
        },
        "TikTok": {
            "User Profile": f"https://www.tiktok.com/@{query}",
            "User Profile Search": f"https://www.tiktok.com/search/user?q={query}",
            "TikTok Analytics I": f"https://tokcount.com/tiktok-analytics/{query}",
            "TikTok Analytics II": f"https://exolyt.com/user/{query}",
            "TikTok Analytics III": f"https://tokcounter.com/tiktok-analytics/{query}"
        },
        "Meetup": {
            "Member Search": f"https://www.google.com/search?q=site:meetup.com+inurl:member+{query}"
        },
        "Ebay": {
            "User Account": f"https://www.ebay.com/usr/{query}",
            "User Feedback": f"https://feedback.ebay.com/ws/eBayISAPI.dll?ViewFeedback2&userid={user}",
            "User Items": f"https://www.ebay.com/sch/{user}",
            "Google Search": f"https://www.google.com/search?q=site%3Ahttps%3A%2F%2Fwww.ebay.com%2Fusr+%22{query}%22"
        },
        "Pintrest": {
            "User Search": f"https://www.pinterest.com/{query}",
            "User Pins": f"https://www.pinterest.com/{query}/pins/",
            "User Boards": f"https://www.pinterest.com/{query}/boards/"
        },
        "Discord": {
            "Server Invite Check": f"https://discord.gg/{query}"
        },
        "Telegram": {
            "t.me": f"https://t.me/{query}",
            "telegram.me/s": f"https://telegram.me/s/{query}",
            "telesco.pe": f"https://telesco.pe/{query}"
        },
        "Other": {
            "Parler User": f"https://parler.com/{query}",
            "Gab User": f"https://gab.com/{query}"
        }
    }

    return Commdict

def community_term_query(query: str) -> dict:
    """
    Terms and tags search across Reddit, 4chan, TikTok, Meetup, Discord and Telegram

    :param query: the term or tag to search
    :return: a dict containing URLs of search results
    """

    commdict = {
        "Reddit": {
            "Search": f"https://old.reddit.com/search?q={query}",
            "Title": f"https://old.reddit.com/search?q=title:{query}"
        },
        "4chan": {
            "Keyword Search": f"http://4chansearch.com/?q={query}&s=4",
            "Archive Search I": f"http://4chansearch.com/?q={query}&s=7",
            "Archive Search II": f"https://archive.4plebs.org/_/search/text/{query}/order/asc/",
            "Google Search": f"https://www.google.com/search?q=site:4chan.org {query}"
        },
        "TikTok": {
            "Tags": f"https://www.tiktok.com/tag/{query}",
            "Term Search": f"https://www.tiktok.com/search?q={query}",
            "Video Search": f"https://www.tiktok.com/search/video?q={query}",
            "Google Search": f"https://www.google.com/search?q=site:tiktok.com+{query}"
        },
        "Meetup": {
            "Event Search": f"https://www.google.com/search?q=site:meetup.com+inurl:events+{query}",
            "Post Search": f"https://www.google.com/search?q=site:meetup.com+inurl:discussions+{query}",
            "Google Search": f"https://www.google.com/search?q=site:meetup.com+{query}"
        },
        "Discord": {
            "Disboard": f"https://disboard.org/search?keyword={query}",
            "Top.gg": f"https://top.gg/servers/search?q={query}",
            "Discord.me": f"https://discord.me/servers?search={query}",
            "Discord Servers": f"https://discordservers.com/search/{query}",
            "Discordbee": f"https://discordbee.com/servers?q={query}",
            "Google Search": f"https://www.google.com/search?q=site:discord.com+{query}"
        },
        "Telegram": {
            "Group Search": f"https://www.telegram-group.com/en?s={query}",
            "Channel Search I": f"https://telegramchannels.me/search?type=all&search={query}",
            "Channel Searcg II": f"https://telemetr.io/en/channels?channel={query}"
        }
    }

    return commdict

# Email address tool: https://inteltechniques.com/tools/Email.html

def email_query(email: str) -> dict:
    """
    Returns URLs for search results on querying a specific email address

    :param email: the email you want to search
    :return: dict containing the search result URLs
    """

    Emaildict = {
        "Google": f'http://google.com/search?q="{email}"',
        "Bing": f'http://bing.com/search?q="{email}"',
        "Yandex": f'https://yandex.com/search/?text="{email}"',
        "Emailrep": f"https://emailrep.io/query/{email}",
        "Gravatar": f"https://en.gravatar.com/site/check/{email}",
        "HIBP": f"https://haveibeenpwned.com/unifiedsearch/{email}",
        "Dehashed": f'https://dehashed.com/search?query="{email}"',
        "Spycloud": f"https://portal.spycloud.com/endpoint/enriched-stats/{email}",
        "HudsonRock": f"https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email={email}",
        "CyberNews": f"https://check.cybernews.com/chk/?lang=en_US&e={email}",
        "PSBDMP": f"https://psbdmp.ws/api/search/{email}",
        "IntelX": f"https://intelx.io/?s={email}",
        "Hunter.io": f"https://hunter.io/email-verifier/{email}",
        "OCCRP": f"https://data.occrp.org/search?q={email}",
        "SpyTox": f"https://www.spytox.com/people/search?email={email}",
        "ThatsThem": f"https://thatsthem.com/email/{email}",
        "Protonmail": f"https://api.protonmail.ch/pks/lookup?op=get&search={email}",
        "DomainData": f"http://domainbigdata.com/email/{email}",
        "Whoisology": f"https://whoisology.com/email/{email}",
        "AnalyzeID": f"http://analyzeid.com/?email={email}",
        "Whoxy": f"https://www.whoxy.com/search.php?email={email}",
        "ScamSearch": f"https://scamsearch.io/search_report?searchoption=all&search={email}",
        "MySpace": f"https://myspace.com/search/people?q={email}",
        "Flickr": f"https://www.flickr.com/search/people/?q={email}",
        "Google psbdmp.ws": f'http://google.com/search?q=site:psbdmp.ws+"{email}"'
    }

    return Emaildict

# Username tool: https://inteltechniques.com/tools/Username.html

###############################################################
###############################################################
###############################################################
########## CTRL + D = MULTIPLE LINE SELECT IN VSCODE ##########
###############################################################
###############################################################
###############################################################

def username_query(query: str) -> dict:
    """
    Search for an individual given their username

    :param query: the individual's username
    :return: dict of URLs to search the username
    """

    Userdict = {
        "Google": f'https://www.google.com/search?q=%22{query}%22',
        "Bing": f'https://www.bing.com/search?q=%22{query}%22',
        "Yandex": f'https://yandex.com/search/?text="{query}"',
        "KnowEm Basic": f'https://knowem.com/checkusernames.php?u={query}',
        "KnowEm Adv": f'https://knowem.com/checksocialnames.php?u={query}',
        "UserSearch": [
            f'https://usersearch.org/results_normal.php?URL_username={query}',
            f'https://usersearch.org/results_advanced.php?URL_username={query}',
            f'https://usersearch.org/results_advanced1.php?URL_username={query}',
            f'https://usersearch.org/results_advanced2.php?URL_username={query}',
            f'https://usersearch.org/results_advanced4.php?URL_username={query}',
            f'https://usersearch.org/results_advanced5.php?URL_username={query}',
            f'https://usersearch.org/results_advanced6.php?URL_username={query}',
            f'https://usersearch.org/results_advanced7.php?URL_username={query}',
            f'https://usersearch.org/results_dating.php?URL_username={query}',
            f'https://usersearch.org/results_forums.php?URL_username={query}',
            f'https://usersearch.org/results_crypto.php?URL_username={query}'
        ],
        "NameVine": f'https://namevine.com/#/{query}',
        "SocialSearcher": f'https://www.social-searcher.com/search-users/?ntw=&q6={query}',
        "HaveIBeenPwned": f'https://haveibeenpwned.com/unifiedsearch/{query}',
        "Dehashed": f'https://dehashed.com/search?query="{query}"',
        "PSBDMP": f'https://psbdmp.ws/api/search/{query}',
        "Gravatar": f'https://en.gravatar.com/{query}',
        "LinkTree": f'https://linktr.ee/{query}',
        "InstagramBio": f'https://www.searchmy.bio/search?q={query}',
        "Twitter": f'http://twitter.com/{query}',
        "Facebook": f'https://facebook.com/{query}',
        "Instagram": f'http://instagram.com/{query}',
        "TikTok": f'https://www.tiktok.com/@{query}',
        "Tinder": f'https://tinder.com/@{query}',
        "Tumblr": f'https://{query}.tumblr.com',
        "Snapchat": f'https://www.snapchat.com/s/{query}',
        "Medium": f'https://medium.com/@{query}',
        "YouTube": f'http://youtube.com/{query}',
        "Reddit": f'https://www.reddit.com/user/{query}',
        "HIBP Emails": [
            f"https://haveibeenpwned.com/unifiedsearch/{query}@gmail.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@yahoo.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@hotmail.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@protonmail.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@live.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@outlook.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@icloud.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@yandex.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@gmx.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@mail.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@mac.com?truncateResponse=true",
            f"https://haveibeenpwned.com/unifiedsearch/{query}@me.com?truncateResponse=true"
        ],
        "Dehashed Emails": [
            f"https://dehashed.com/search?query=%22{query}@gmail.com%22",
            f"https://dehashed.com/search?query=%22{query}@yahoo.com%22",
            f"https://dehashed.com/search?query=%22{query}@hotmail.com%22",
            f"https://dehashed.com/search?query=%22{query}@protonmail.com%22",
            f"https://dehashed.com/search?query=%22{query}@live.com%22",
            f"https://dehashed.com/search?query=%22{query}@outlook.com%22",
            f"https://dehashed.com/search?query=%22{query}@icloud.com%22",
            f"https://dehashed.com/search?query=%22{query}@yandex.com%22",
            f"https://dehashed.com/search?query=%22{query}@gmx.com%22",
            f"https://dehashed.com/search?query=%22{query}@mail.com%22",
            f"https://dehashed.com/search?query=%22{query}@mac.com%22",
            f"https://dehashed.com/search?query=%22{query}@me.com%22"
        ],
        "Email Search": f'https://www.google.com/search?q=%22{query}@gmail.com%22OR%22{query}@yahoo.com%22OR%22{query}@hotmail.com%22OR%22{query}@protonmail.com%22OR%22{query}@live.com%22OR%22{query}@icloud.com%22OR%22{query}@yandex.com%22OR%22{query}@gmx.com%22OR%22{query}@mail.com%22OR%22{query}@mac.com%22OR%22{query}@me.com%22'
    }

    return Userdict

# Name tool: https://inteltechniques.com/tools/Name.html

def name_query(forename: str, surname: str) -> dict:
    """
    Returns URLs to query a given real forename and surname.

    :param forename: self-explanatory
    :param surname: self-explanatory
    :return: dict of URLs for querying an individual's real name against public databases
    """

    Namedict = {
        "TruePeopleSearch": f'https://www.truepeoplesearch.com/results?name={forename}%20{surname}',
        "FastPeopleSearch": f'https://www.fastpeoplesearch.com/name/{forename}-{surname}',
        "Nuwber": f'https://nuwber.com/search?name={forneame}%20{surname}',
        "Xlek": f'https://xlek.com/search_results.php?fname={forename}&lname={surname}&locations:all',
        "FamilyTreeNow": f'https://www.familytreenow.com/search/genealogy/results?first={forename}&last={surname}',
        "Intelius People Search": f'https://www.intelius.com/people-search/{forename}-{surname}',
        "Radaris": f'https://radaris.com/p/{forename}/{surname}',
        "Cyber Background Checks": f'https://www.cyberbackgroundchecks.com/people/{forename}-{surname}',
        "Spytox": f'https://www.spytox.com/people/search?name={forename}+{surname}',
        "SearchPeopleFree": f'https://www.searchpeoplefree.com/find/{forename}-{surname}',
        "Spokeo": f'https://www.spokeo.com/{forename}-{surname}?loaded=1',
        "Advanced Background Checks": f'https://www.advancedbackgroundchecks.com/names/{forename}-{surname}',
        "Yasni": f'http://www.yasni.com/{forename}+{surname}/check+people?sh',
        "Zaba Search": f'https://www.zabasearch.com/people/{forename}+{surname}',
        "PeopleSearchNow": f'https://www.peoplesearchnow.com/person/{forename}-{surname}',
        "Webmii": f'http://webmii.com/people?n=%22{forename}%20{surname}%22',
        "Social Searcher": f'https://www.social-searcher.com/search-users/?q6={forename}+{surname}',
        "Truthfinder": f'https://www.truthfinder.com/results/?firstName={forename}&lastName={surname}&state=ALL',
        "PeopleByName": f'http://www.peoplebyname.com/people/{forename}/{surname}',
        "Whitepages": f'https://www.whitepages.com/name/{forename}-{surname}',
        "That's Them": f'https://thatsthem.com/name/{forename}-{surname}',
        "Clustrmaps": f'https://clustrmaps.com/persons/{forename}-{surname}',
        "Rocketreach": f'http://google.com/search?q=site:rocketreach.co+"{forename} {surname}"',
        "OfficialUSA": f'https://www.officialusa.com/names/{forename}-{surname}',
        "Addresses.com": f'https://www.addresses.com/people/{forename}-{surname}',
        "Classmates.com": f'https://www.classmates.com/siteui/ybsearch/results?q={forename} {surname}',
        "Cubib": f'https://cubib.com/search_results.php?fname={forename}&lname={surname}&locations:all'
    }

    return Namedict

# Documents tool: https://inteltechniques.com/tools/Documents.html

def doc_query(query: str) -> dict:
    """
    Return search engine queries for online documents containing a particular term

    :param query: your search term
    :return: query URLs in dict
    """

    Docdict = {
        "PDF": f"https://www.google.com/search?q=ext%3Apdf+{query}",
        "DOC/DOCX": f"https://www.google.com/search?q=ext%3Adoc+OR+ext%3Adocx+{query}",
        "XLS/XLSX/CSV": f"https://www.google.com/search?q=ext%3Axls+OR+ext%3Axlsx+OR+ext%3Acsv+{query}",
        "PPT/PPTX/KEY": f"https://www.google.com/search?q=ext%3Appt+OR+ext%3Apptx+OR+ext%3Akey+{query}",
        "TXT/RTF/XML": f"https://www.google.com/search?q=ext%3Atxt+OR+ext%3Artf+OR+ext%3Axml+{query}",
        "ODT/ODS/ODP": f"https://www.google.com/search?q=ext%3Aodt+OR+ext%3Aods+OR+ext%3Aodp+{query}",
        "ZIP/RAR/7Z": f"https://www.google.com/search?q=ext%3Azip+OR+ext%3Arar+OR+ext%3A7z+{query}",
        "JPG/JPEG/PNG": f"https://www.google.com/search?q=ext%3Ajpg+OR+ext%3Ajpeg+OR+ext%3Apng+{query}&tbm=isch",
        "MPG/MP4": f"https://www.google.com/search?q=ext%3Ampg+OR+ext%3Ampeg+OR+ext%3Amp4+{query}",
        "MP3/WAV": f"https://www.google.com/search?q=ext%3Amp3+OR+ext%3Awav+OR+ext%3Aflac+{query}",
        "Google Docs": f"https://www.google.com/search?q=site%3Adocs.google.com+{query}",
        "Google Drive": f"https://www.google.com/search?q=site%3Adrive.google.com+{query}",
        "Google API": f"https://www.google.com/search?q=site%3Astorage.googleapis.com+{query}",
        "MS Docs": f"https://www.google.com/search?q=site%3Adocs.microsoft.com+{query}",
        "Amazon AWS": f"https://www.google.com/search?q=site%3As3.amazonaws.com+{query}",
        "Cloudfront": f"https://www.google.com/search?q=site%3Acloudfront.net+{query}",
        "GrayHatWarfare": f"https://buckets.grayhatwarfare.com/results/{query}",
        "SlideShare": f"https://www.google.com/search?q=site%3Aslideshare.net+{query}",
        "Prezi": f"https://www.google.com/search?q=site%3Aprezi.com+{query}",
        "ISSUU": f"https://www.google.com/search?q=site%3Aissuu.com+{query}",
        "Powershow": f"https://www.powershow.com/search/presentations/ppt/{query}",
        "Slide Bean": f"https://www.google.com/search?q=site%3Aslidebean.com+{query}",
        "Author Stream": f"https://www.google.com/search?q=site%3Aauthorstream.com+{query}",
        "Scribd": f"https://www.google.com/search?q=site%3Ascribd.com+{query}",
        "PDF Drive": f"https://www.pdfdrive.net/search?q={query}",
        "Wikileaks": f"https://search.wikileaks.org/?query={query}&exact_phrase=&any_of=&exclude_words=&document_date_start=&document_date_end=&released_date_start=&released_date_end=&new_search=True&order_by=most_relevant#results",
        "Archive.org": f"https://archive.org/search.php?query={query}&sin=TXT",
        "Google Books": f"https://www.google.com/search?tbm=bks&q={query}"  
    }

    return Docdict

# Images tool: https://inteltechniques.com/tools/Images.html

def img_query_url(query: str) -> dict:
    """
    Reverse search using an image

    :param query: url of image
    :return: results of image reverse search on various search engines
    """

    Imgdict = {
        "Google Search by Image": f"https://www.google.com/searchbyimage?site=search&sa=X&image_url={query}",
        "Bing Search by Image": f"https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:{query}",
        "Tineye": f"http://www.tineye.com/search/?url={query}",
        "Yandex Search by Image": f"https://yandex.com/images/search?rpt=imageview&url={query}",
        "Baidu": f"https://graph.baidu.com/upload?image={query}",
        "Karma Decay": f"https://karmadecay.com/search?q={query}"
    }

    return Imgdict

def img_query_text(query: str) -> dict:
    """
    Search for an image given a specific text query

    :param query: search term / textual description of what you are looking for
    :return: dict of URLs of results for the query
    """

    Imgdict = {
        "Google Images": f"https://www.google.com/search?q={query}&tbm=isch",
        "Bing Images": f"https://www.bing.com/images/search?q={query}",
        "Yandex Images": f"https://yandex.com/images/search?text={query}",
        "Twitter": f"https://twitter.com/search?f=image&q={query}",
        "Facebook": f"https://www.facebook.com/search/photos/?q={query}",
        "Instagram": f"https://www.google.com/search?tbm=isch&q=site%3Ainstagram.com+{query}",
        "LinkedIn": f"https://www.google.com/search?tbm=isch&q=site%3Alinkedin.com+{query}",
        "Flickr": f"https://www.flickr.com/search/?text={query}",
        "Tumblr": f"https://www.tumblr.com/search/{query}"
    }

    return Imgdict

# Videos tool: https://inteltechniques.com/tools/Videos.html

def YT_vid_ID_query(query: str) -> dict:
    """
    Various tools for use with Youtube (e.g., age-restriction bypass, view metadata, etc.)

    :param query: video ID of interest
    :return: dict of resultant URLs
    """

    Vidict = {
        "Age Bypass": f"https://keepvid.works/?url=https://www.youtube.com/watch/v={query}",
        "Full Screen": f"https://www.youtube.com/embed/{query}",
        "Thumbnail HQ": f"https://i.ytimg.com/vi/{query}/maxresdefault.jpg",
        "Thumbnail 2": f"https://img.youtube.com/vi/{query}/1.jpg",
        "Thumbnail 3": f"https://img.youtube.com/vi/{query}/2.jpg",
        "Thumbnail 4": f"https://img.youtube.com/vi/{query}/3.jpg",
        "Google Reverse": f"https://www.google.com/searchbyimage?site=search&sa=X&image_url=https://i.ytimg.com/vi/{query}/maxresdefault.jpg",
        "Bing Reverse": f"https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:https://i.ytimg.com/vi/{query}/maxresdefault.jpg",
        "Yandex Reverse": f"https://yandex.com/images/search?rpt=imageview&url=https://i.ytimg.com/vi/{query}/maxresdefault.jpg",
        "Tineye Reverse": f"http://www.tineye.com/search/?url=https://i.ytimg.com/vi/{query}/maxresdefault.jpg",
        "Restrictions I": f"http://polsy.org.uk/stuff/ytrestrict.cgi?ytid={query}",
        "Restrictions II": f"https://watannetwork.com/tools/blocked/#url={query}",
        "Metadata": f"https://www.googleapis.com/youtube/v3/videos?id={query}&part=snippet,statistics,recordingDetails&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw",
        "Download": f"http://www.pwnyoutube.com/watch?v={query}",
        "Web Archive": f"https://web.archive.org/web/https://www.youtube.com/watch?v={query}"
    }

    return Vidict

def YT_vid_comments(video_id: str, search_term: str) -> str:
    """
    Return the URL of comments on a given Youtube Video

    :param video_id: the ID number of the video
    :param search_term: key terms you are looking for in comments
    :return: URL (single string) of query result webpage
    """

    Vidstr = f"https://www.googleapis.com/youtube/v3/commentThreads?part=id,snippet&videoId={video_id}&pageToken=&order=Relevance&maxResults=100&searchTerms={search_term}&textFormat=plainText&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw"

    return Vidstr

def YT_user_query(query: str) -> dict:
    """
    Query a YouTube user given their username

    :param query: Youtube username
    :return: links to profile and account details for the given username
    """

    Vidict = {
        "Profile": f"https://www.youtube.com/user/{query}",
        "Account": f"https://www.youtube.com/feeds/videos.xml?user={query}"
    }

    return Vidict

def YT_channel_metadata(channel_id: str) -> str:
    """
    Get Youtube Channel metadata given a channel ID

    :param query: channel ID of interest
    :return: URL to metadata
    """

    Vidstr = f"https://youtube.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw"
    
    return Vidstr

def vid_search_term(query: str) -> dict:
    """
    Search for videos across the web by term or tag

    :param query: search term or tag of interest
    :return: dict containing URLs of results on various video sharing sites and search engines
    """

    Vidict = {
        "Google Videos": f"https://www.google.com/search?tbm=vid&q={query}",
        "Bing Videos": f"https://www.bing.com/videos/search?q={query}",
        "Yandex Videos": f"https://yandex.ru/video/search?text={query}&rpt=imageview",
        "Youtube": f"https://www.youtube.com/results?search_query={query}",
        "Twitter Videos": f"https://twitter.com/search?q={query}&f=video",
        "Facebook Videos": f"https://www.facebook.com/search/videos/?q={query}",
        "Reddit Videos": f"https://www.reddit.com/search?q=site:v.redd.it%20AND%20{query}",
        "TikTok": f"https://www.tiktok.com/tag/{query}",
        "PeteyVid": f"https://www.peteyvid.com/index.php?q={query}",
        "Archives I": f"https://archive.org/details/movies?and[]={query}",
        "Archives II": f"https://archive.org/details/opensource_movies?and%5B%5D={query}"
    }
    
    return Vidict

# Domains tool: https://inteltechniques.com/tools/Domain.html

def domain_query(query: str) -> dict:
    """
    Returns URLs of various sites to lookup information about a domain

    :param query: the domain you want to query
    :return: dict containg the URLs to lookup info
    """

    Domdict = {
        "ViewDNS": [
            f"http://viewdns.info/whois/?domain={query}",
            f"http://viewdns.info/reverseip/?host={query}&t=1",
            f"http://viewdns.info/reversewhois/?q={query}&t=1",
            f"http://viewdns.info/portscan/?host={query}",
            f"http://viewdns.info/iphistory/?domain={query}",
            f"http://viewdns.info/dnsreport/?domain={query}",
            f"http://viewdns.info/traceroute/?domain={query}"
        ],
        "Who.is": [
            f"http://who.is/whois/{query}",
            f"http://who.is/dns/{query}",
            f"http://who.is/domain-history/{query}"
        ],
        "Other Whois": [
            f"https://dmns.app/domains?q={query}",
            f"https://www.whoxy.com/{query}",
            f"https://whoisology.com/{query}",
        ],
        "Whois Archive": [
            f"https://web.archive.org/web/http://www.who.is/whois/{query}",
            f"https://web.archive.org/web/https://whois.domaintools.com/{query}",
            f"https://web.archive.org/web/https://www.whoxy.com/{query}",
            f"https://web.archive.org/web/https://domainbigdata.com/{query}",
            f"https://web.archive.org/web/https://whoisology.com/{query}",
            f"http://web.archive.org/web/*/{query}",
            f"http://archive.md/{query}",
            f"http://timetravel.mementoweb.org/list/19991212110000/http://{query}",
            f"https://webarchive.loc.gov/all/*/http://{query}",
            f"https://arquivo.pt/page/search?hitsPerPage=100&query=site%3A{query}",
            f"http://carbondate.cs.odu.edu/#{query}"
        ],
        "Google": [
            f"http://google.com/search?q=site%3A{query}",
            f"http://webcache.googleusercontent.com/search?q=cache:{query}"
        ],
        "Analytics": [
            f"https://website.informer.com/{query}#tab_stats",
            f"http://spyonweb.com/{query}",
            f"http://analyzeid.com/?domain={query}",
            f"https://dnslytics.com/reverse-analytics/{query}",
            f"https://dnslytics.com/reverse-adsense/{query}",
            f"https://www.domainiq.com/snapshot_history?data={query}#{query}",
            f"http://moonsearch.com/report/{query}.html", 
            f"https://www.nerdydata.com/reports/new?search=%7B%22all%22%3A%5B%7B%22type%22%3A%22code%22,%22value%22%3A%22{query}%22%7D%5D,%22any%22%3A%5B%5D,%22none%22%3A%5B%5D%7D",
            f"https://builtwith.com/{query}",
            f"https://dnsdumpster.com/static/map/{query}.png",
            f"http://{query}/robots.txt",
            f"https://host.io/{query}",
            f"https://host.io/backlinks/{query}",
            f"https://host.io/redirects/{query}",
            f"https://dnslytics.com/domain/{query}",
            f"https://www.wmtips.com/tools/info/{query}",
            f"https://www.robtex.com/dns-lookup/{query}",
            f"https://www.domaincodex.com/search.php?q={query}"
        ],
        "Network": [
            f"http://www.similarweb.com/website/{query}",
            f"https://moz.com/domain-analysis?site={query}",
            f"https://www.spyfu.com/overview/domain?query={query}",
            f"https://api.sharedcount.com/v1.0/?url=https%3A%2F%2F{query}&apikey=1934f519a63e142e0d3c893e59cc37fe0172e98a",
            f"https://www.reddit.com/search?q=site:{query}",
            f"http://bc.linkody.com/en/seo-tools/free-backlink-checker/{query}",
            f"https://www.copyscape.com/?q=http://{query}",
            f"http://www.visualsitemapper.com/map/{query}"
        ],
        "Threat detection": [
            f"https://www.virustotal.com/#/domain/{query}",
            f"https://threatintelligenceplatform.com/report/{query}",
            f"https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=100&virtual_hosts=INCLUDE&q={query}",
            f"https://securitytrails.com/list/apex_domain/{query}",
            f"https://www.threatcrowd.org/domain.php?domain={query}",
            f"https://themarkup.org/blacklight?url={query}",
            f"https://crt.sh/?q={query}"
        ],
        "Leaks/Compromised Data": [
            f"https://dehashed.com/search?query=%22{query}%22",
            f"https://www.hudsonrock.com/search?domain={query}",
            f"https://intelx.io/?s={query}",
            f"https://www.skymem.info/srch?q={query}"
        ]
    }

    return Domdict

# IP Addresses tool: https://inteltechniques.com/tools/IP.html

def IP_query(query: str) -> dict:
    """
    Output a dict containing the URLs for your IP query across all IP lookup providers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    IPdict = {
        "VD ReverseIP": f"http://viewdns.info/reverseip/?host={query}&t=1",
        "VD LocateIP": f"http://viewdns.info/iplocation/?ip={query}",
        "VD PortScan": f"http://viewdns.info/portscan/?host={query}",
        "VD Whois": f"http://viewdns.info/whois/?domain={query}",
        "VD TraceRoute": f"http://viewdns.info/traceroute/?ip={query}",
        "VD ReverseDNS": f"http://viewdns.info/reversedns/?domain={query}",
        "IPAddress.com": f"https://www.ipaddress.com/ipv4/{query}",
        "DNSChcker": f"https://dnschecker.org/ip-whois-lookup.php?query={query}",
        "IPLookup": f"https://www.ip-lookup.org/location/{query}",
        "MXTool": f"ttps://mxtoolbox.com/SuperTool.aspx?action=arin%3a{query}&run=toolpage",
        "MXBlacklist": f"https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a{query}&run=toolpage",
        "MXBlocklist": f"https://mxtoolbox.com/SuperTool.aspx?action=blocklist%3a{query}&run=networktools",
        "Bing IP": f"http://www.bing.com/search?q=ip%3A{query}",
        "IPLocation": f"https://www.iplocation.net/ip-lookup?query={query}&submit=IP+Lookup",
        "That's Them": f"https://thatsthem.com/ip/{query}",
        "Torrents": f"http://iknowwhatyoudownload.com/en/peer/?ip={query}",
        "Wigle SSID": f"https://wigle.net/search?ssid={query}",
        "Wigle Postal": f"https://wigle.net/search#fullSearch?postalCode={query}",
        "Shodan": f"https://www.shodan.io/search?query={query}",
        "Shodan Beta": f"https://beta.shodan.io/host/{query}",
        "Shodan Raw": f"https://beta.shodan.io/host/{query}/raw",
        "ThreatCrowd": f"https://www.threatcrowd.org/ip.php?ip={query}",
        "Censys": f"https://search.censys.io/hosts/{query}",
        "Dehashed": f"https://dehashed.com/search?query=%22{query}%22"
    }

    return IPdict

# Virtual currencies searches: https://inteltechniques.com/tools/Currencies.html
#   Out of virtual/crypto currency - will mostly be bitcoin
#   Would be nice to be able to search Eth and Doge, but I can't see many cases where bad actors will be circulating money in Doge

def bitcoin_query(query: str) -> dict:
    """
    Output a dict containing the URLs for your Bitcoin address query across a number of services.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    currdict = {
        "BTC Validation": f"https://thomas.vanhoutte.be/tools/validate-bitcoin-address.php?address={query}",
        "Satoshi Receive": f"https://blockchain.info/q/getreceivedbyaddress/{query}",
        "Satoshi Sent": f"https://blockchain.info/q/getsentbyaddress/{query}",
        "Satoshi Balance": f"https://blockchain.info/q/addressbalance/{query}",
        "Summary": f"https://chain.api.btc.com/v3/address/{query}",
        "Creation Date": f"https://blockchain.info/q/addressfirstseen/{query}",
        "Blockchain": f"https://www.blockchain.com/btc/address/{query}",
        "BitcoinAbuse": f"https://www.bitcoinabuse.com/reports/{query}",
        "WhosWho": f"https://bitcoinwhoswho.com/address/{query}",
        "OXT": f"https://oxt.me/address/{query}",
        "WalletExplorer": f"https://www.walletexplorer.com/address/{query}",
        "BTC": f"https://btc.com/{query}",
        "BC BTC": f"https://blockchair.com/bitcoin/address/{query}"
    }

    return currdict

# Breach searches: https://inteltechniques.com/tools/Breaches.html
#   Partial implementation of breach stuff
#   Dehashing etc is done far better with other tools
#       No point reinventing the wheel...
#   Finding breaches is the real use-case here
#   Also some of the fns Bazzell has online seem edge cases for most OSINT

def breachQ_email(query: str) -> dict:
    """
    Output a dict containing the URLs for your email address query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    Breachdict = {
        "HIBP": f"https://haveibeenpwned.com/unifiedsearch/{query}",
        "Dehashed": f'https://dehashed.com/search?query="{query}"',
        "IntelX": f"https://intelx.io/?s={query}",
        "PSDMP": f"https://psbdmp.ws/api/search/{query}",
        "CyberNews": f"https://check.cybernews.com/chk/?lang=en_US&e={query}",
        "Spycloud": f"https://portal.spycloud.com/endpoint/enriched-stats/{query}",
        "HudsonRock": f"https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email={query}"
    }

    return Breachdict

def breachQ_username(query: str) -> dict:
    """
    Output a dict containing the URLs for your username query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    Breachdict = {
        "HIBP": f"https://haveibeenpwned.com/unifiedsearch/{query}",
        "Dehashed": f'https://dehashed.com/search?query="{query}"',
        "PSBDMP": f"https://psbdmp.ws/api/search/{query}"
    }

    return Breachdict

def breachQ_domain(query: str) -> dict:
    """
    Output a dict containing the URLs for your domain query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    Breachdict = {
        "Dehashed": f'https://dehashed.com/search?query="{query}"',
        "PSBDMP": f"https://psbdmp.ws/api/search/{query}",
        "IntelX": f"https://intelx.io/?s={query}",
        "HudsonRock": f"https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email={query}"
    }

    return Breachdict

def breachQ_telephone(query: str) -> dict:
    """
    Output a dict containing the URLs for your telephone number query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

    Breachdict = {
        "Dehashed": f'https://dehashed.com/search?query="{query}"',
        "PSBDMP": f"https://psbdmp.ws/api/search/{query}"
    }

    return Breachdict

def breachQ_IP(query: str) -> dict:
    """
    Output a dict containing the URLs for your IP address query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """
    
    Breachdict = {
        "Dehashed": f'https://dehashed.com/search?query="{query}"',
        "PSBDMP": f"https://psbdmp.ws/api/search/{query}",
        "IntelX": f"https://intelx.io/?s={query}"
    }

    return Breachdict

# Master query function for breaches below
#       I know that chaining 5 if statements together below to make this is awful
#       I just don't have time to write something better

def breach_query(email: str, username: str, domain: str, telephone: str, IP_add: str) -> dict:
    """
    Output a dict containing the URLs for your IP query across all breach registers.

    :param email: email address to query - input "" to skip
    :param username: username to query - input "" to skip
    :param domain: domain to query - input "" to skip
    :param telephone: telephone number to query - input "" to skip
    :param IP_add: IP address to query - input "" to skip
    :return: dict of dicts containing URLs for your query
    """

    if email=="":
        s1 = {"Email": "Email to query not specified"}
    else:
        s1 = breachQ_email(email)

    if username=="":
        s2 = {"Username": "Username to query not specified"}
    else:
        s2 = breachQ_username(username)

    if domain=="":
        s3 = {"Domain": "Domain to query not specified"}
    else:
        s3 = breachQ_domain(domain)

    if telephone=="":
        s4 = {"Telephone": "Number to query not specified"}
    else:
        s4 = breachQ_telephone(telephone)

    if IP_add=="":
        s5 = {"IP": "Address to query not specified"}
    else:
        s5 = breachQ_IP(IP_add)

    Breachdict = {
        "Email": s1,
        "Username": s2,
        "Domain": s3,
        "Telephone": s4,
        "IP Address": s5
    }

    return Breachdict

##################################
#### FUTURE DEVELOPMENT TASKS ####
##################################
# 
# RE: API keys
# TODO: Contacted Michael Bazzell after Github auto-flagging API keys in certain tool redirect URLs as exposed secret keys. Michael explained that the Flickr key is a public test key. The Google key - as explained in his book - is a free key that anyone with a Google account can generate, he notes that this might be blocked from abuse. The Sharedcount key we did not discuss but is likely one of the free, 500 requests allowed keys.
#       Need to add comments to relevant functions firstly to underscore these aren't secret keys, secondly to make it easier to edit when/if these are blocked or stop working, and thirdly for people forking/cloning who want to input their own keys instead to avoid loss of service due to key blocking/expiration.
# 
# TODO: Error handling for all methods
# TODO: If there is time at some point, add in RegEx to check queries valid for each arg in methods
# TODO: Possibly add in master queries of multiple methods at once
# TODO: look into adding other crypto searching functionality, especially if Bitcoin becomes no longer the favoured coin
# TODO: these could be stuck in other tools:
#   https://api.flickr.com/services/rest/?method=flickr.people.findByEmail&api_key=27c196593dad58382fc4912b00cf1194&find_email=' + flemail
#   https://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key=27c196593dad58382fc4912b00cf1194&username=' + fluser
#   https://api.flickr.com/services/rest/?method=flickr.people.getInfo&api_key=27c196593dad58382fc4912b00cf1194&user_id=' + flnumber + '&format=rest
#
# def addressQ(query: str) -> dict:
#   TODO: Possibly implement address querying; Limited application outside United States - not implemented (yet)
#   Tool is here: https://inteltechniques.com/tools/Address.html
#
# def telephoneNo(query: str) -> dict:
#   TODO: Possibly implement telephone No tool; Limited application outside United States - not implemented (yet)
#   Tool is here: https://inteltechniques.com/tools/Telephone.html
#
# Maps tool: https://inteltechniques.com/tools/Location.html
# TODO: Possibly add Maps tool in the future
#       I really don't see this tool as necessary - why would you
#       need to search lat and long from multiple sources?
#
# def map_query(lat: str, long: str) -> dict:
#    """
#    """
#
#    Mapdict = {
#        
#    }
#
#    return Mapdict
#
# Business/Government searches: https://inteltechniques.com/tools/Business.html
# def bizgovQ(query: str) -> dict:
#   This is heavily US-centric
#   Seems little point implementing right now
#   TODO: implement Business/Government searches if demand appears
#
# Vehicle searches: https://inteltechniques.com/tools/Vehicle.html 
# def vehiQl(query: str) -> dict:
#   Only useful in the United States - not implemented
#   TODO: Implement vehicle searches if this becomes/is a desired feature
#
#
# Not implementing these in v1.0.0
# TODO: Implement the remainder of the Facebook tools when get time
#       There are JavaScript routines for querying
#
#def facebook_UID(UID: str, qual: str) -> dict:
#    """
#    """
#
#    FBdict = {
#
#    }
#
#    return FBdict
#
#def facebook_LOCID(LOCID: str, qualifier: str) -> dict:
#    """
#    """
#
#    FBdict = {
#
#    }
#    
#   return FBdict
#
# def facebook_UID_query(UID: str, qual:str, query: str) -> dict:
#    """
#    """
#
#    FBdict = {
#
#    }
#    
#   return FBdict
#
#def facebook_events_by_loc(LOCID: str, query: str) -> dict:
#    """
#    """
#
#    FBdict = {
#
#    }
#    
#   return FBdict
#
#def facebook_profiles_by_institution(IID: str, name: str) -> dict:
#    """
#    Employer, city or school
#    """
#
#    FBdict = {
#
#    }
#    
#   return FBdict
#
#
#def facebook_content_by_date(keyword: str, start: str, end: str) -> dict:
#    """
#    Return posts, photos, videos by keyword within a specific timeframe
#    """
#    FBdict = {
#
#    }
#    
#   return FBdict
#
# Some LinkedIn tools seem non-essential for locating individuals
# TODO: add when have time, would be useful for people using OSINT for Recruitment
#def linkedin_keyword(keyword: str) -> dict:
#    """
#       'https://www.linkedin.com/search/results/companies/?keywords=' + keyword
#       'https://www.linkedin.com/search/results/groups/?keywords=' + keyword
#       'https://www.linkedin.com/search/results/schools/?keywords=' + keyword
#       'https://www.linkedin.com/search/results/events/?keywords=' + keyword
#       'https://www.linkedin.com/jobs/index/?keywords=' + keyword
#    """
#
#    Linkdict = {
#    }
#
#    return Linkdict
#
# def linkedin_web_mob_profile(...)
#   function not implemented - use case seems redundant
#   TODO: only if requested
#   'https://search.google.com/test/mobile-friendly?url=http://linkedin.com/in/' + Search12
#
# def linkedin_photos_videos(...)
#   function not implemented - use case seems redundant
#   TODO: only if requested
#   'https://www.google.com/search?q=site:linkedin.com+' + Search13 + '&source=lnms&tbm=isch'
#   'https://www.bing.com/images/search?q=site%3alinkedin.com+' + Search14 + '&scenario=ImageBasicHover'
#   'https://www.google.com/search?q=site:linkedin.com+' + Search15 + '&tbm=vid'
#
# TODO: implement other aspects of Bazzell Communities tool if requested
#
# TODO: Pastes tool: https://inteltechniques.com/tools/Pastes.html
# Not doing right now
#def paste_query(query: str) -> dict:
#    """
#    """
#
#    Pastedict = {
#        
#    }
#
#    return Pastedict
#
# def live_audio_video(...)
#   Function not implemented
#   TODO: possibly implement the Live Audio and Live Video streams tools
#   However, bear in mind that those streaming service tools aren't as useful outside US.
#   Therefore, not a priority.
#   Live Audio searches: https://inteltechniques.com/tools/Radio.html
#   Live Video searches: https://inteltechniques.com/tools/Video.html
#
# def API_search(...)
#   This function seems a bit pointless and possibly a security flaw
#   TODO: possibly implement API search in future (see: https://inteltechniques.com/tools/API.html).
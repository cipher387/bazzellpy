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

def facebook_mutuality(UID1: str, UID2: str) -> str:
    """
    Output a string containing a URL showing common friends between two user IDs.

    :param UID1: the first User ID
    :param UID2: the second User ID
    :return: common friends result URL as string
    """

    FBstr = f"https://facebook.com/browse/mutual_friends/?uid={UID1}&node={UID2}",
    
    return FBstr

#def facebook_content_by_date(keyword: str, start: str, end: str) -> dict:
#    """
#    Return posts, photos, videos by keyword within a specific timeframe
#    """
#    FBdict = {
#
#    }
#    
#   return FBdict

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

# Utility seems non-essential for locating individuals
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

# Communities tool: https://inteltechniques.com/tools/Communities.html
#       Only implementing this tool in part because some parts seem redundant
#       TODO: implement other aspects of tool if requested

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

#####################
#####################
######################
# CTRL + D = MULTIPLE LINE SELECT IN VSCODE
# WILL MAKE FINISHING FROM HERE ON A LOT QUICKER
#####################
#####################
#####################

def username_query(query: str) -> dict:
    """
https://www.google.com/search?q=%22{query}%22
https://www.bing.com/search?q=%22{query}%22
'https://yandex.com/search/?text="{query}"'
https://knowem.com/checkusernames.php?u={query}
https://knowem.com/checksocialnames.php?u={query}
https://usersearch.org/results_normal.php?URL_username={query}
https://usersearch.org/results_advanced.php?URL_username={query}
https://usersearch.org/results_advanced1.php?URL_username={query}
https://usersearch.org/results_advanced2.php?URL_username={query}
https://usersearch.org/results_advanced4.php?URL_username={query}
https://usersearch.org/results_advanced5.php?URL_username={query}
https://usersearch.org/results_advanced6.php?URL_username={query}
https://usersearch.org/results_advanced7.php?URL_username={query}
https://usersearch.org/results_dating.php?URL_username={query}
https://usersearch.org/results_forums.php?URL_username={query}
https://usersearch.org/results_crypto.php?URL_username={query}
https://namevine.com/#/' + Search07
https://www.social-searcher.com/search-users/?ntw=&q6=' + Search08
https://haveibeenpwned.com/unifiedsearch/' + Search09
https://dehashed.com/search?query="' + Search10 + '"'
https://psbdmp.ws/api/search/' + Search11
https://en.gravatar.com/' + Search12
https://linktr.ee/' + Search13
https://www.searchmy.bio/search?q=' + Search14
http://twitter.com/' + Search15
https://facebook.com/' + Search16
http://instagram.com/' + Search17
https://www.tiktok.com/@' + Search18
https://tinder.com/@' + Search19
https://' + Search20 + '.tumblr.com'
https://www.snapchat.com/s/' + Search21
https://medium.com/@' + Search22
http://youtube.com/' + Search23
https://www.reddit.com/user/' + Search24
https://haveibeenpwned.com/unifiedsearch/{query}@gmail.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@yahoo.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@hotmail.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@protonmail.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@live.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@outlook.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@icloud.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@yandex.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@gmx.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@mail.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@mac.com?truncateResponse=true
https://haveibeenpwned.com/unifiedsearch/{query}@me.com?truncateResponse=true
https://dehashed.com/search?query=%22{query}@gmail.com%22
https://dehashed.com/search?query=%22{query}@yahoo.com%22
https://dehashed.com/search?query=%22{query}@hotmail.com%22
https://dehashed.com/search?query=%22{query}@protonmail.com%22
https://dehashed.com/search?query=%22{query}@live.com%22
https://dehashed.com/search?query=%22{query}@outlook.com%22
https://dehashed.com/search?query=%22{query}@icloud.com%22
https://dehashed.com/search?query=%22{query}@yandex.com%22
https://dehashed.com/search?query=%22{query}@gmx.com%22
https://dehashed.com/search?query=%22{query}@mail.com%22
https://dehashed.com/search?query=%22{query}@mac.com%22
https://dehashed.com/search?query=%22{query}@me.com%22
https://www.google.com/search?q=%22{query}@gmail.com%22OR%22{query}@yahoo.com%22OR%22{query}@hotmail.com%22OR%22{query}@protonmail.com%22OR%22{query}@live.com%22OR%22{query}@icloud.com%22OR%22{query}@yandex.com%22OR%22{query}@gmx.com%22OR%22{query}@mail.com%22OR%22{query}@mac.com%22OR%22{query}@me.com%22
    """

    Userdict = {
        "Google": f"",
        "Bing": f"",
        "Yandex": f"",
        "KnowEm Basic": f"",
        "KnowEm Adv": f"",
        "UserSearch": {},
        "NameVine": f"",
        "SocialSearcher": f"",
        "HaveIBeenPwned": f"",
        "Dehashed": f"",
        "PSBDMP": f"",
        "Gravatar": f"",
        "LinkTree": f"",
        "InstagramBio": f"",
        "Twitter": f"",
        "Facebook": f"",
        "Instagram": f"",
        "TikTok": f"",
        "Tinder": f"",
        "Tumblr": f"",
        "Snapchat": f"",
        "Medium": f"",
        "YouTube": f"",
        "Reddit": f"",
        "HIBP Emails": {},
        "Dehashed Emails": {},
        "Email Search": f""
    }

    return Userdict

# Name tool: https://inteltechniques.com/tools/Name.html

def name_query(forename: str, surname: str) -> dict:
    """
https://www.truepeoplesearch.com/results?name=' + Search01a + '%20' + Search01b, 'Search01window');}
https://www.fastpeoplesearch.com/name/' + Search02a + '-' + Search02b, 'Search02window');}
https://nuwber.com/search?name=' + Search03a + '%20' + Search03b, 'Search03window');}
https://xlek.com/search_results.php?fname=' + Search04a + '&lname=' + Search04b + '&locations:all', 'Search04window');}
https://www.familytreenow.com/search/genealogy/results?first=' + Search05a + '&last=' + Search05b, 'Search05window');}
https://www.intelius.com/people-search/' + Search06a + '-' + Search06b, 'Search06window');}
https://radaris.com/p/' + Search07a + '/' + Search07b, 'Search07window');}
https://www.cyberbackgroundchecks.com/people/' + Search08a + '-' + Search08b, 'Search08window');}
https://www.spytox.com/people/search?name=' + Search09a +'+' + Search09b, 'Search09window');}
https://www.searchpeoplefree.com/find/' + Search10a + '-' + Search10b, 'Search10window');}
https://www.spokeo.com/' + Search11a + '-' + Search11b +'?loaded=1', 'Search11window');}
https://www.advancedbackgroundchecks.com/names/' + Search12a + '-' + Search12b, 'Search12window');}
http://www.yasni.com/' + Search13a + '+' + Search13b + '/check+people?sh', 'Search13window');}
https://www.zabasearch.com/people/' + Search14a + '+' + Search14b, 'Search14window');}
https://www.peoplesearchnow.com/person/' + Search15a + '-' + Search15b, 'Search15window');}
http://webmii.com/people?n=%22' + Search16a + '%20' + Search16b + '%22', 'Search16window');}
https://www.social-searcher.com/search-users/?q6=' + Search17a + '+' + Search17b, 'Search17window');}
https://www.truthfinder.com/results/?firstName=' + Search18a + '&lastName=' + Search18b + '&state=ALL', 'Search18window');}
http://www.peoplebyname.com/people/' + Search19b + '/' + Search19a, 'Search19window');}
https://www.whitepages.com/name/' + Search20a + '-' + Search20b, 'Search20window');}
https://thatsthem.com/name/' + Search21a + '-' + Search21b, 'Search21window');}
https://clustrmaps.com/persons/' + Search22a + '-' + Search22b, 'Search22window');}
http://google.com/search?q=site:rocketreach.co+"' + Search23a + ' ' + Search23b + '"', 'Search23window');}
https://www.officialusa.com/names/' + Search24a + '-' + Search24b, 'Search24window');}
https://www.addresses.com/people/' + Search25a + '-' + Search25b, 'Search25window');}
https://www.classmates.com/siteui/ybsearch/results?q=' + Search26a + ' ' + Search26b, 'Search26window');}
https://cubib.com/search_results.php?fname=' + all1 + '&lname=' + all2 + '&locations:all', 'a4window');
    """

    Namedict = {
        
    }

    return Namedict

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

# Documents tool: https://inteltechniques.com/tools/Documents.html

def doc_query(query: str) -> dict:
    """
https://www.google.com/search?q=ext%3Apdf+{query}
https://www.google.com/search?q=ext%3Adoc+OR+ext%3Adocx+{query}
https://www.google.com/search?q=ext%3Axls+OR+ext%3Axlsx+OR+ext%3Acsv+{query}
https://www.google.com/search?q=ext%3Appt+OR+ext%3Apptx+OR+ext%3Akey+{query}
https://www.google.com/search?q=ext%3Atxt+OR+ext%3Artf+OR+ext%3Axml+{query}
https://www.google.com/search?q=ext%3Aodt+OR+ext%3Aods+OR+ext%3Aodp+{query}
https://www.google.com/search?q=ext%3Azip+OR+ext%3Arar+OR+ext%3A7z+{query}
https://www.google.com/search?q=ext%3Ajpg+OR+ext%3Ajpeg+OR+ext%3Apng+{query}&tbm=isch
https://www.google.com/search?q=ext%3Ampg+OR+ext%3Ampeg+OR+ext%3Amp4+{query}
https://www.google.com/search?q=ext%3Amp3+OR+ext%3Awav+OR+ext%3Aflac+{query}
https://www.google.com/search?q=site%3Adocs.google.com+{query}
https://www.google.com/search?q=site%3Adrive.google.com+{query}
https://www.google.com/search?q=site%3Astorage.googleapis.com+{query}
https://www.google.com/search?q=site%3Adocs.microsoft.com+{query}
https://www.google.com/search?q=site%3As3.amazonaws.com+{query}
https://www.google.com/search?q=site%3Acloudfront.net+{query}
https://buckets.grayhatwarfare.com/results/{query}
https://www.google.com/search?q=site%3Aslideshare.net+{query}
https://www.google.com/search?q=site%3Aprezi.com+{query}
https://www.google.com/search?q=site%3Aissuu.com+{query}
https://www.powershow.com/search/presentations/ppt/{query}
https://www.google.com/search?q=site%3Aslidebean.com+{query}
https://www.google.com/search?q=site%3Aauthorstream.com+{query}
https://www.google.com/search?q=site%3Ascribd.com+{query}
https://www.pdfdrive.net/search?q={query}
https://search.wikileaks.org/?query={query}&exact_phrase=&any_of=&exclude_words=&document_date_start=&document_date_end=&released_date_start=&released_date_end=&new_search=True&order_by=most_relevant#results
https://archive.org/search.php?query={query}&sin=TXT
https://www.google.com/search?tbm=bks&q={query}
    """

    Docdict = {
        
    }

    return Docdict

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

# Images tool: https://inteltechniques.com/tools/Images.html

def img_query_url(query: str) -> dict:
    """
https://www.google.com/searchbyimage?site=search&sa=X&image_url={query}
https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:{query}
http://www.tineye.com/search/?url={query}
https://yandex.com/images/search?rpt=imageview&url={query}
https://graph.baidu.com/upload?image={query}
https://karmadecay.com/search?q={query}
    """

    Imgdict = {
        
    }

    return Imgdict

def img_query_text(query: str) -> dict:
    """
https://www.google.com/search?q={query}&tbm=isch
https://www.bing.com/images/search?q={query}
https://yandex.com/images/search?text={query}
https://twitter.com/search?f=image&q={query}
https://www.facebook.com/search/photos/?q={query}
https://www.google.com/search?tbm=isch&q=site%3Ainstagram.com+{query}
https://www.google.com/search?tbm=isch&q=site%3Alinkedin.com+{query}
https://www.flickr.com/search/?text={query}
https://www.tumblr.com/search/{query}
    """

    Imgdict = {
        
    }

    return Imgdict

# These could be stuck in other tools:
#   https://api.flickr.com/services/rest/?method=flickr.people.findByEmail&api_key=27c196593dad58382fc4912b00cf1194&find_email=' + flemail
#   https://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key=27c196593dad58382fc4912b00cf1194&username=' + fluser
#   https://api.flickr.com/services/rest/?method=flickr.people.getInfo&api_key=27c196593dad58382fc4912b00cf1194&user_id=' + flnumber + '&format=rest

# Videos tool: https://inteltechniques.com/tools/Videos.html

def vid_query(query: str) -> dict:
    """
https://keepvid.works/?url=https://www.youtube.com/watch/v=' + Search01, 'Search01window');}
https://www.youtube.com/embed/' + Search02, 'Search02window');}
https://i.ytimg.com/vi/' + Search03 + '/maxresdefault.jpg', 'Search03window');}
https://img.youtube.com/vi/' + Search04 + '/1.jpg', 'Search04window');}
https://img.youtube.com/vi/' + Search05 + '/2.jpg', 'Search05window');}
https://img.youtube.com/vi/' + Search06 + '/3.jpg', 'Search06window');}
https://www.google.com/searchbyimage?site=search&sa=X&image_url=https://i.ytimg.com/vi/' + Search07 + '/maxresdefault.jpg', 'Search07window');}
https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:https://i.ytimg.com/vi/' + Search08 + '/maxresdefault.jpg', 'Search08window');}
https://yandex.com/images/search?rpt=imageview&url=https://i.ytimg.com/vi/' + Search09 + '/maxresdefault.jpg', 'Search09window');}
http://www.tineye.com/search/?url=https://i.ytimg.com/vi/' + Search10 + '/maxresdefault.jpg', 'Search10window');}
http://polsy.org.uk/stuff/ytrestrict.cgi?ytid=' + Search11, 'Search11window');}
https://watannetwork.com/tools/blocked/#url=' + Search12, 'Search12window');}
https://www.googleapis.com/youtube/v3/videos?id=' + Search13 + '&part=snippet,statistics,recordingDetails&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw', 'Search13window');}
http://www.pwnyoutube.com/watch?v=' + Search14, 'Search14window');}
https://web.archive.org/web/https://www.youtube.com/watch?v=' + Search15, 'Search15window');}
https://www.google.com/search?tbm=vid&q=' + Search16, 'Search16window');}
https://www.bing.com/videos/search?q=' + Search17, 'Search17window');}
https://yandex.ru/video/search?text=' + Search18 + '&rpt=imageview', 'Search18window');}
https://www.youtube.com/results?search_query=' + Search19, 'Search19window');}
https://twitter.com/search?q=' + Search20 + '&f=video', 'Search20window');}
https://www.facebook.com/search/videos/?q=' + Search21, 'Search21window');}
https://www.reddit.com/search?q=site:v.redd.it%20AND%20' + Search22, 'Search22window');}
https://www.tiktok.com/tag/' + Search23, 'Search23window');}
https://www.peteyvid.com/index.php?q=' + Search24, 'Search24window');}
https://archive.org/details/movies?and[]=' + Search25, 'Search25window');}
https://archive.org/details/opensource_movies?and%5B%5D=' + Search26, 'Search26window');}
https://archive.org/details/tv?q=' + Search27, 'Search27window');}
https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/0.jpg', 'rev13window');
https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/1.jpg', 'rev14window');
https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/2.jpg', 'rev15window');
https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/3.jpg', 'rev16window');
http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/0.jpg', 'revt5window');
http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/1.jpg', 'revt6window');
http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/2.jpg', 'revt7window');
http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/3.jpg', 'revt8window');
https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/0.jpg&rpt=imageview', 'rev17window');
https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/1.jpg&rpt=imageview', 'rev18window');
https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/2.jpg&rpt=imageview', 'rev19window');
https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/3.jpg&rpt=imageview', 'rev20window');
http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/0.jpg', 'rev21window');
http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/1.jpg', 'rev22window');
http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/2.jpg', 'rev23window');
http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/3.jpg', 'rev24window');}
https://www.google.com/searchbyimage?site=search&sa=X&image_url=https://i.vimeocdn.com/video/' + Search29, 'rev1window');
http://www.tineye.com/search/?url=https://i.vimeocdn.com/video/' + Search29, 'revt1window');
https://www.yandex.com/images/search?img_url=https://i.vimeocdn.com/video/' + Search29, 'rev5window');
http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=https://i.vimeocdn.com/video/' + Search29, 'rev9window');}
https://www.google.com/searchbyimage?site=search&sa=X&image_url=' + Search30, 'image1window');
http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=' + Search30, 'image4window');
http://www.tineye.com/search/?url=' + Search30, 'image2window');
https://yandex.com/images/search?url=' + Search30 + '&rpt=imageview', 'image3window');
https://image.baidu.com/pcdutu?queryImageUrl=' + Search30, 'image5window');}
https://www.youtube.com/user/' + Search31, 'Search31window');}
https://www.youtube.com/feeds/videos.xml?user=' + Search32, 'Search32window');}
https://youtube.googleapis.com/youtube/v3/channels?part=snippet&id=' + Search33 + '&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw', 'Search33window');}
https://www.googleapis.com/youtube/v3/commentThreads?part=id,snippet&videoId=' + Search34 + '&pageToken=&order=Relevance&maxResults=100&searchTerms=' + term + '&textFormat=plainText&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw', 'Search34window');}
    """

    Vidict = {
        
    }

    return Vidict

# Domains tool: https://inteltechniques.com/tools/Domain.html

def domain_query(query: str) -> dict:
    """
http://viewdns.info/whois/?domain=' + Search01, 'Search01window');}
http://viewdns.info/reverseip/?host=' + Search02 + '&t=1', 'Search02window');}
http://viewdns.info/reversewhois/?q=' + Search03 + '&t=1', 'Search03window');}
http://viewdns.info/portscan/?host=' + Search04, 'Search04window');}
http://viewdns.info/iphistory/?domain=' + Search05, 'Search05window');}
http://viewdns.info/dnsreport/?domain=' + Search06, 'Search06window');}
http://viewdns.info/traceroute/?domain=' + Search07, 'Search07window');}
http://who.is/whois/' + Search08, 'Search08window');}
http://who.is/dns/' + Search09, 'Search09window');}
http://who.is/domain-history/' + Search10, 'Search10window');}
https://dmns.app/domains?q=' + Search11, 'Search11window');}
https://www.whoxy.com/' + Search12, 'Search12window');}
https://whoisology.com/' + Search13, 'Search13window');}
https://web.archive.org/web/http://www.who.is/whois/' + Search15, 'Search15window');}
https://web.archive.org/web/https://whois.domaintools.com/' + Search16, 'Search16window');}
https://web.archive.org/web/https://www.whoxy.com/' + Search17, 'Search17window');}
https://web.archive.org/web/https://domainbigdata.com/' + Search18, 'Search18window');}
https://web.archive.org/web/https://whoisology.com/' + Search19, 'Search19window');}
http://web.archive.org/web/*/' + Search20, 'Search20window');}
http://archive.md/' + Search21, 'Search21window');}
http://timetravel.mementoweb.org/list/19991212110000/http://' + Search22, 'Search22window');}
https://webarchive.loc.gov/all/*/http://' + Search23, 'Search23window');}
https://arquivo.pt/page/search?hitsPerPage=100&query=site%3A' + Search24, 'Search24window');}
http://carbondate.cs.odu.edu/#' + Search25, 'Search25window');}
http://google.com/search?q=site%3A' + Search26, 'Search26window');}
http://webcache.googleusercontent.com/search?q=cache:' + Search27, 'Search27window');}
https://website.informer.com/' + Search28 + '#tab_stats', 'Search28window');}
https://urlscan.io/domain/' + Search29, 'Search29window');}
https://www.easycounter.com/report/' + Search30, 'Search30window');}
https://whois.domaintools.com/' + Search31, 'Search31window');}
https://www.domainiq.com/snapshot_history#' + Search32, 'Search32window');}
https://files.dmns.app/screenshots/' + Search33 + '.jpg', 'Search33window');}
http://spyonweb.com/' + Search34, 'Search34window');}
http://analyzeid.com/?domain=' + Search35, 'Search35window');}
https://dnslytics.com/reverse-analytics/' + Search36, 'Search36window');}
https://dnslytics.com/reverse-adsense/' + Search37, 'Search37window');}
https://www.domainiq.com/snapshot_history?data=' + Search38 + '#' + Search38, 'Search38window');}
http://moonsearch.com/report/' + Search39 + '.html', 'Search39awindow');}
https://www.nerdydata.com/reports/new?search=%7B%22all%22%3A%5B%7B%22type%22%3A%22code%22,%22value%22%3A%22' + Search40 + '%22%7D%5D,%22any%22%3A%5B%5D,%22none%22%3A%5B%5D%7D', 'Search40window');}
https://builtwith.com/' + Search41, 'Search41window');}
https://dnsdumpster.com/static/map/' + Search42 + '.png', 'Search42window');}
http://' + Search43 + '/robots.txt', 'Search43window');}
https://host.io/' + Search44, 'Search44window');}
https://host.io/backlinks/' + Search45, 'Search45window');}
https://host.io/redirects/' + Search46, 'Search46window');}
https://dnslytics.com/domain/' + Search47, 'Search47window');}
https://www.wmtips.com/tools/info/' + Search48, 'Search48window');}
https://www.robtex.com/dns-lookup/' + Search49, 'Search49window');}
https://www.domaincodex.com/search.php?q=' + Search50, 'Search50window');}
http://www.similarweb.com/website/' + Search51, 'Search51window');}
https://moz.com/domain-analysis?site=' + Search52, 'Search52window');}
https://www.spyfu.com/overview/domain?query=' + Search53, 'Search53window');}
https://api.sharedcount.com/v1.0/?url=https%3A%2F%2F' + Search54 + '&apikey=1934f519a63e142e0d3c893e59cc37fe0172e98a', 'Search54window');}
https://www.reddit.com/search?q=site:' + Search55, 'Search55window');}
http://bc.linkody.com/en/seo-tools/free-backlink-checker/' + Search56, 'Search56window');}
https://www.copyscape.com/?q=http://' + Search57, 'Search57window');}
http://www.visualsitemapper.com/map/' + Search58, 'Search58window');}
https://www.virustotal.com/#/domain/' + Search14, 'Search14window');}
https://threatintelligenceplatform.com/report/' + Search59, 'Search59window');}
https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=100&virtual_hosts=INCLUDE&q=' + Search60, 'Search60window');}
https://securitytrails.com/list/apex_domain/' + Search61, 'Search61window');}
https://www.threatcrowd.org/domain.php?domain=' + Search62, 'Search62window');}
https://themarkup.org/blacklight?url=' + Search63, 'Search63window');}
https://crt.sh/?q=' + Search64, 'Search64window');}
https://dehashed.com/search?query=%22' + Search65 + '%22', 'Search65window');}
https://www.hudsonrock.com/search?domain=' + Search66, 'Search66window');}
https://intelx.io/?s=' + Search67, 'Search67window');}
https://www.skymem.info/srch?q=' + Search68, 'Search68window');}
https://' + Search69 + '+', 'Search69window');}
https://' + Search71 + '~', 'Search71window');}
http://' + Search72 + '-', 'Search72window');}
http://checkshorturl.com/expand.php?u=' + Search73, 'Search73window');}
http://moonsearch.com/adsense/' + Search74 + '.html', 'Search74window');}
https://analyzeid.com/id/ca-pub-' + Search75, 'Search75window');}
https://dnslytics.com/reverse-adsense/pub-' + Search76, 'Search76window');}
https://api.hackertarget.com/analyticslookup/?q=pub-' + Search77, 'Search77window');}
http://moonsearch.com/analytics/' + Search78 + '.html', 'Search78window');}
https://analyzeid.com/id/ua-' + Search79, 'Search79window');}
https://dnslytics.com/reverse-analytics/ua-' + Search80, 'Search80window');}
https://publicwww.com/websites/%22ua-' + Search81 + '%22/', 'Search81window');}
https://api.hackertarget.com/analyticslookup/?q=UA-' + Search82, 'Search82window');}
    """

    Domdict = {
        
    }

    return Domdict

#####################
#####################
######################
# ALL METHODS AFTER THIS POINT HAVE ALREADY BEEN COMPLETED
# CONGRATULATIONS - V1.0.0 IS COMPLETE PENDING A FEW OUTSTANDING ISSUES (SEE GITHUB REPO ISSUES TAB)
# ALSO - MAKE SOME ADDITIONAL TESTS TO RUN BEFORE COMPLETING THOSE ISSUES
# CAN JUST PUMP THE CODE THROUGH A JUPYTER NOTEBOOK AND GET PYTEST TO COMPARE THE RESULTS IN TEST_FUNCTIONS.py
#####################
#####################
#####################

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

# Business/Government searches: https://inteltechniques.com/tools/Business.html
# def bizgovQ(query: str) -> dict:
#   This is heavily US-centric
#   Seems little point implementing right now
#   TODO: implement Business/Government searches if demand appears

# Vehicle searches: https://inteltechniques.com/tools/Vehicle.html 
# def vehiQl(query: str) -> dict:
#   Only useful in the United States - not implemented
#   TODO: Implement vehicle searches if this becomes/is a desired feature

# Virtual currencies searches: https://inteltechniques.com/tools/Currencies.html
# Out of virtual/crypto currency - will mostly be bitcoin
# Would be nice to be able to search Eth and Doge, but I can't see many cases where bad actors will be circulating money in Doge
# TODO: look into adding other crypto searching functionality, especially if Bitcoin becomes no longer the favoured coin

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
# Recommend only partial implementation of breach stuff
# Dehashing etc is done far better with other tools
# No point reinventing the wheel...
# Finding breaches is the real use-case here
# Also some of the fns Bazzell has online seem edge cases for most OSINT

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
# Also - I know that chaining 5 if statements together below to make this is awful
#       I just don't have time to write something better
# TODO: Breach master tool should really have error handling
#       Hell, so should the rest of this library probably
# TODO: If there is time at some point, add in RegEx to check queries valid for each arg in breach query master
# TODO: Possibly add in master queries for other tools
#       However, does seem like the master query is most useful for this tool at this stage
#       Worth waiting to see if there is any demand for this

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

# def live_audio_video(...)
#   Function not implemented
#   TODO: possibly implement the Live Audio and Live Video streams tools
#   However, bear in mind that those streaming service tools aren't as useful outside US.
#   Therefore, not a priority.
#   Live Audio searches: https://inteltechniques.com/tools/Radio.html
#   Live Video searches: https://inteltechniques.com/tools/Video.html

# def API_search(...)
#   This function seems a bit pointless and possibly a security flaw
#   TODO: possibly implement API search in future (see: https://inteltechniques.com/tools/API.html).
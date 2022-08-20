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
#    FBdict = {
#
#    }
#    return FBdict
#
#def facebook_LOCID(LOCID: str, qualifier: str) -> dict:
#    """
#    """
#    FBdict = {
#
#    }
#    return FBdict
#
# def facebook_UID_query(UID: str, qual:str, query: str) -> dict:
#    """
#    """
#    FBdict = {
#
#    }
#    return FBdict
#
#def facebook_events_by_loc(LOCID: str, query: str) -> dict:
#    """
#    """
#    FBdict = {
#
#    }
#    return FBdict
#
#def facebook_profiles_by_institution(IID: str, name: str) -> dict:
#    """
#    Employer, city or school
#    """
#    FBdict = {
#
#    }
#    return FBdict

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
#    return FBdict

# Segmented Twitter tool into separate functions
# TODO: Twitter tool: https://inteltechniques.com/tools/Twitter.html

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
    """
    Instadict = {
        "IG Profile": f"",
        "IG Channel": f"",
        "IG Tagged": f"",
        "Outgoing Search": f"",
        "Incoming Search": f"",
        "Bing Search": f"",
        "Yandex Search": f"",
        "Twitter Posts": f"",
        "Dumpor Profile": f""
    }
    return Instadict

def instagram_follow(query: str) -> dict:
    """
    """
    Instadict = {
        "Followers": f"",
        "Following": f""
    }
    return Instadict

def instagram_user_term(user: str, search_term: str) -> str:
    """
    """
    Instastr = f""
    return Instastr

def instagram_association(user1: str, user2: str) -> str:
    """
    """
    Instastr = f""
    return Instastr

# Almost certain there is no purpose for these two methods
# TODO: implement these when get an opportunity to
#def instagram_search_term(query: str) -> dict:
#    """
#    """
#    Instadict = {
#        
#    }
#    return Instadict
#def instagram_dumpor_tag(query: str) -> str:
#    """
#    """
#    Instadict = {
#        
#    }
#    return Instadict

# Segmented LinkedIn tool into separate functions
# TODO: LinkedIn tool: https://inteltechniques.com/tools/Linkedin.html 

def linkedin_person_search(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> str:
    """
    """
    Linkstr = f""
    return Linkstr

def linkedin_post_search(keyword: str, title: str) -> str:
    """
    """
    Linkstr = f""
    return Linkstr

def linkedin_google_bing_yandex(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> dict:
    """
    """
    Linkdict = {
        "Google": f"",
        "Bing": f"",
        "Yandex": f""
    }
    return Linkdict

# Utility seems non-essential for locating individuals
# TODO: add when have time, would be useful for people using OSINT for Recruitment
#def linkedin_keyword(keyword: str) -> dict:
#    """
#    """
#    Linkdict = {
#    }
#    return Linkdict

# def linkedin_web_mob_profile(...)
#   function not implemented - use case seems redundant
#   TODO: only if requested

# def linkedin_photos_videos(...)
#   function not implemented - use case seems redundant
#   TODO: only if requested

# TODO: Communities tool: https://inteltechniques.com/tools/Communities.html
#       Only implementing the username searches part of this tool, the rest seems quite redundant
#       TODO: implement other aspects of tool if requested
#       Actually, scratch only usernames policy (at least for the following exceptions):
#       4chan tool would be quite useful - implementing in separate tool
#       ... likewise with Tiktok, Telegram, Discord and Meetup subtools

def community_query(query: str) -> dict:
    """
    """
    Commdict = {
        "Reddit": {
            "User Profile": f"",
            "User Posts": f"",
            "User Comments": f"",
            "Reddit Archive I": f"",
            "Reddit Archive II": f""
            "Pushshift User I": f"",
            "Pushshift User II": f""
        },
        "Hacker News": {
            "User Search": f"",
            "User Posts": f"",
            "User Comments": f"",
            "Favorites": f""
        },
        "TikTok": {
            "User Profile": f"",
            "User Profile Search": f"",
            "TikTok Analytics I": f"",
            "TikTok Analytics II": f"",
            "TikTok Analytics III": f""
        },
        "Meetup": {
            "Member Search": f""
        },
        "Ebay": {
            "User Account": f"",
            "User Feedback": f"",
            "User Items": f""
        },
        "Pintrest": {
            "User Search": f"",
            "User Pins": f"",
            "User Boards": f""
        },
        "Discord": {
            "Server Invite Check": f""
        },
        "Other": {
            "Parler User": f"",
            "Gab User": f"",
            "Telegram User/Channel": f"",
            "Telegram User Videos": f""
        }
    }
    return Commdict

def community_term_query(query: str) -> dict:
    """
    """
    commdict = {
        "4chan": {
            "Keyword Search": f"",
            "Archive Search I": f"",
            "Archive Search II": f"",
            "Google Search": f""
        },
        "TikTok": {
            "Tags": f"",
            "Term Search": f"",
            "Video Search": f"",
            "Google Search": f""
        },
        "Meetup": {
            "Event Search": f"",
            "Post Search": f"",
            "Google Search": f""
        },
        "Discord": {
            "Disboard": f"",
            "Top.gg": f"",
            "Discord.me": f"",
            "Servers": f"",
            "Discordbee": f"",
            "Google Search": f""
        },
        "Telegram": {
            "Group Search": f"",
            "Channel Search I": f"",
            "Channel Searcg II": f""
        }
    }
    return commdict

# TODO: Email address tool: https://inteltechniques.com/tools/Email.html

def email_query(email: str) -> dict:
    """
    """
    # Implementation of this tool: https://inteltechniques.com/tools/Email.html
    Emaildict = {
        "Google": f"",
        "Bing": f"",
        "Yandex": f"",
        "Emailrep": f"",
        "Gravatar": f"",
        "HIBP": f"",
        "Dehashed": f"",
        "Spycloud": f"",
        "HudsonRock": f"",
        "CyberNews": f"",
        "PSBDMP": f"",
        "IntelX": f"",
        "LeakedSource": f"",
        "HunterVerify": f"",
        "OCCRP": f"",
        "SpyTox": f"",
        "ThatsThem": f"",
        "Protonmail": f"",
        "DomainData": f"",
        "Whoisology": f"",
        "AnalyzeID": f"",
        "Whoxy": f"",
        "ScamSearch": f"",
        "MySpace": f"",
        "Flickr": f""
    }
    return Emaildict

# TODO: Username tool: https://inteltechniques.com/tools/Username.html

def username_query(query: str) -> dict:
    """
    """
    Userdict = {
        "Google": f"",
        "Bing": f"",
        "Yandex": f"",
        "KnowEm Basic": f"",
        "KnowEm Adv": f"",
        "UserSearch": f"",
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
        "HIBP Emails": f"",
        "Dehashed Emails": f"",
        "Email Search": f""
    }
    return Userdict

# TODO: Name tool: https://inteltechniques.com/tools/Name.html

def name_query(forename: str, surname: str) -> dict:
    """
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
#    Mapdict = {
#        
#    }
#    return Mapdict

# TODO: Documents tool: https://inteltechniques.com/tools/Documents.html

def doc_query(query: str) -> dict:
    """
    """
    Docdict = {
        
    }
    return Docdict

# TODO: Pastes tool: https://inteltechniques.com/tools/Pastes.html

def paste_query(query: str) -> dict:
    """
    """
    Pastedict = {
        
    }
    return Pastedict

# TODO: #12 Images tool: https://inteltechniques.com/tools/Images.html

def img_query(query: str) -> dict:
    """
    """
    Imgdict = {
        
    }
    return Imgdict

# TODO: Videos tool: https://inteltechniques.com/tools/Videos.html

def vid_query(query: str) -> dict:
    """
    """
    Vidict = {
        
    }
    return Vidict

# TODO: Domains tool: https://inteltechniques.com/tools/Domain.html

def domain_query(query: str) -> dict:
    """
    """
    Domdict = {
        
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
#       Hell, probably should the rest of this library
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
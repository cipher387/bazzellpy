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
# TODO: #1 All tools available here: https://inteltechniques.com/tools/Facebook.html

def facebook_username(query: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def facebook_search(query: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def facebook_UID(UID: str, qual: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def facebook_LOCID(LOCID: str, qualifier: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def facebook_UID_query(UID: str, qual:str, query: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def facebook_events_by_loc(LOCID: str, query: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict


def facebook_profiles_by_institution(IID: str, name: str) -> dict:
    """
    Employer, city or school
    """
    FBdict = {

    }
    return FBdict

def facebook_mutuality(UID1: str, UID2: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def facebook_content_by_date(keyword: str, start: str, end: str) -> dict:
    """
    Return posts, photos, videos by keyword within a specific timeframe
    """
    FBdict = {

    }
    return FBdict

# TODO: #2 Twitter tool: https://inteltechniques.com/tools/Twitter.html

def twitter_user(query: str) -> dict:
    """
    """
    Twitdict = {
        
    }
    return Twitdict

def twitter_user_year(query: str, year: str) -> dict:
    """
    """
    Twitdict = {
        
    }
    return Twitdict

def search_term_year(query: str, year: str) -> dict:
    """
    """
    Twitdict = {
        
    }
    return Twitdict

def twitter_real_name(real_name: str) -> dict:
    """
    """
    Twitdict = {
        
    }
    return Twitdict

def twitter_lists(list_number: str) -> dict:
    """
    """
    Twitdict = {
        
    }
    return Twitdict

# TODO: #3 Insta tool: https://inteltechniques.com/tools/Instagram.html

def instagram_user(query: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

def instagram_follow(query: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

def instagram_user_term(query: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

def instagram_association(user1: str, user2: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

def instagram_search_term(query: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

def instagram_dumpor_tag(query: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

# TODO: #4 LinkedIn tool: https://inteltechniques.com/tools/Linkedin.html 

def linkedin_person_search(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> dict:
    """
    """
    Linkdict = {
        
    }
    return Linkdict

def linkedin_post_search(keyword: str, title: str) -> dict:
    """
    """
    Linkdict = {
        
    }
    return Linkdict

def linkedin_google_bing_yandex(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> dict:
    """
    """
    Linkdict = {
        
    }
    return Linkdict

def linkedin_keyword(keyword: str) -> dict:
    """
    """
    Linkdict = {
        
    }
    return Linkdict

# def linkedin_web_mob_profile(...)
#   function not implemented - use case seems redundant

# def linkedin_photos_videos(...)
#   function not implemented - use case seems redundant

# TODO: #5 Communities tool: https://inteltechniques.com/tools/Communities.html

def communities(query: str) -> dict:
    """
    """
    Commdict = {
        
    }
    return Commdict

# TODO: #6 Email address tool: https://inteltechniques.com/tools/Email.html

def email_address(email: str) -> dict:
    """
    """
    # Implementation of this tool: https://inteltechniques.com/tools/Email.html
    Emaildict = {
        "Google": "",
        "Bing": "",
        "Yandex": "",
        "Emailrep": "",
        "Gravatar": "",
        "HIBP": "",
        
    }
    return Emaildict

# TODO: #7 Username tool: https://inteltechniques.com/tools/Username.html

def usernameQ(query: str) -> dict:
    """
    """
    Userdict = {
        
    }
    return Userdict

# TODO: #8 Name tool: https://inteltechniques.com/tools/Name.html

def nameQ(forename: str, surname: str) -> dict:
    """
    """
    Namedict = {
        
    }
    return Namedict

# def addressQ(query: str) -> dict:
#   TODO: #23 Possibly implement address querying; Limited application outside United States - not implemented (yet)
#   Tool is here: https://inteltechniques.com/tools/Address.html

# def telephoneNo(query: str) -> dict:
#   TODO: #22 Possibly implement telephone No tool; Limited application outside United States - not implemented (yet)
#   Tool is here: https://inteltechniques.com/tools/Telephone.html

# TODO: #9 Maps tool: https://inteltechniques.com/tools/Location.html

def mapQu(query: str) -> dict:
    """
    """
    Mapdict = {
        
    }
    return Mapdict

# TODO: #10 Documents tool: https://inteltechniques.com/tools/Documents.html

def doQment(query: str) -> dict:
    """
    """
    Docdict = {
        
    }
    return Docdict

# TODO: #11 Pastes tool: https://inteltechniques.com/tools/Pastes.html

def pastes_query(query: str) -> dict:
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

# TODO: #13 Videos tool: https://inteltechniques.com/tools/Videos.html

def vid_query(query: str) -> dict:
    """
    """
    Vidict = {
        
    }
    return Vidict

# TODO: #14 Domains tool: https://inteltechniques.com/tools/Domain.html

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
#   TODO: #21 implement Business/Government searches if demand appears

# Vehicle searches: https://inteltechniques.com/tools/Vehicle.html 
# def vehiQl(query: str) -> dict:
#   Only useful in the United States - not implemented
#   TODO: #20 Implement vehicle searches if this becomes/is a desired feature

# TODO: #15 Virtual currencies searches: https://inteltechniques.com/tools/Currencies.html
# Out of virtual/crypto currency - will mostly be bitcoin
# Would be nice to be able to search Eth and Doge, but I can't see many cases where bad actors will be circulating money in Doge
# TODO: #19 look into adding other crypto searching functionality, especially if Bitcoin becomes no longer the favoured coin

def bitcoin_address(query: str) -> dict:
    """
    """
    currdict = {
        
    }
    return currdict

# TODO: #16 Breach searches: https://inteltechniques.com/tools/Breaches.html
# Recommend only partial implementation of breach stuff
# Dehashing etc is done far better with other tools
# No point reinventing the wheel...
# Finding breaches is the real use-case here
# Also some of the fns Bazzell has online seem edge cases for most OSINT

def breachQ_email(query: str) -> dict:
    """
    """
    Breachdict = {
        
    }
    return Breachdict

def breachQ_username(query: str) -> dict:
    """
    """
    Breachdict = {
        
    }
    return Breachdict

def breachQ_domain(query: str) -> dict:
    """
    """
    Breachdict = {
        
    }
    return Breachdict

def breachQ_telephone(query: str) -> dict:
    """
    """
    Breachdict = {
        
    }
    return Breachdict

def breachQ_IP(query: str) -> dict:
    """
    """
    Breachdict = {
        
    }
    return Breachdict

# def live_audio_video(...)
#   Function not implemented
#   TODO: #17 possibly implement the Live Audio and Live Video streams tools
#   However, bear in mind that those streaming service tools aren't as useful outside US.
#   Therefore, not a priority.
#   Live Audio searches: https://inteltechniques.com/tools/Radio.html
#   Live Video searches: https://inteltechniques.com/tools/Video.html

# def API_search(...)
#   This function seems a bit pointless and possibly a security flaw
#   TODO: #18 possibly implement API search in future (see: https://inteltechniques.com/tools/API.html).
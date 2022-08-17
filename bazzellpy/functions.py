def searchengi(query: str) -> dict:
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
            "Bing": f'http://bing.com/search?q="{query}"',
            "Bing News": f'http://bing.com/news/search?q="{query}"',
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
            "Torch": "",
            "Tor66": "",
            "Haystack": "",
            "Ahmia": "",
            "SearchDemon": "",
            "Excavator": "",
            "GDark": "",
            "Hidden Reviews": "",
            "OnionLand": "",
            "Phobos": "",
            "Submarine": "",
            "DeepSearch": "",
            "OnionCenter": "",
            "FreshOnion": ""
        }
    }

    return SEdict

def facebook(query: str) -> dict:
    """
    """
    FBdict = {

    }
    return FBdict

def twitter(query: str) -> dict:
    """
    """
    Twitdict = {
        
    }
    return Twitdict

def instagram(query: str) -> dict:
    """
    """
    Instadict = {
        
    }
    return Instadict

def linkedin(query: str) -> dict:
    """
    """
    Linkdict = {
        
    }
    return Linkdict

def communities(query: str) -> dict:
    """
    """
    Commdict = {
        
    }
    return Commdict

def emailaddr(query: str) -> dict:
    """
    """
    Emaildict = {
        
    }
    return Emaildict

def usernameQ(query: str) -> dict:
    """
    """
    Userdict = {
        
    }
    return Userdict

def nameQ(query: str) -> dict:
    """
    """
    Namedict = {
        
    }
    return Namedict

def addressQ(query: str) -> dict:
    """
    """
    Adddict = {
        
    }
    return Adddict

def telephoneNo(query: str) -> dict:
    """
    """
    Nodict = {
        
    }
    return Nodict

def mapQu(query: str) -> dict:
    """
    """
    Mapdict = {
        
    }
    return Mapdict

def doQment(query: str) -> dict:
    """
    """
    Docdict = {
        
    }
    return Docdict

def pastesQ(query: str) -> dict:
    """
    """
    Pastedict = {
        
    }
    return Pastedict

def imgQ(query: str) -> dict:
    """
    """
    Imgdict = {
        
    }
    return Imgdict

def vidQ(query: str) -> dict:
    """
    """
    Vidict = {
        
    }
    return Vidict

def domQ(query: str) -> dict:
    """
    """
    Domdict = {
        
    }
    return Domdict

def IPaddQ(query: str) -> dict:
    """
    """
    IPdict = {
        
    }
    return IPdict

def bizgovQ(query: str) -> dict:
    """
    """
    Instdict = {
        
    }
    return Instdict

def vehiQl(query: str) -> dict:
    """
    """
    Vehdict = {
        
    }
    return Vehdict

def Qrypto(query: str) -> dict:
    """
    """
    currdict = {
        
    }
    return currdict

def breachQ(query: str) -> dict:
    """
    """
    Breachdict = {
        
    }
    return Breachdict

def liveAud(query: str) -> dict:
    """
    """
    Audict = {
        
    }
    return Audict

def liveVid(query: str) -> dict:
    """
    """
    Vidict = {
        
    }
    return Vidict

# TODO: possible future implementation of API search tool
# see: https://inteltechniques.com/tools/API.html
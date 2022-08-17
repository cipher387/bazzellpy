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
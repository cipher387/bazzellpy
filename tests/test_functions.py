from bazzellpy import functions

def test_searchengi():
    assert functions.searchengi("google") == {
        "Surface web": {
            "Google": "http://google.com/search?q=google",
            "Google Date": "http://google.com/search?q=google&tbs=cdr:1,cd_min:1/1/0,sbd:1",
            "Google News": "http://www.google.com/search?tbm=nws&q=google",
            "Google Blogs": "https://www.google.com/search?q=google&tbm=nws&tbs=nrt:b",
            "Google FTP": "https://www.google.com/search?q=inurl%3Aftp%20-inurl%3A(http|https)%20google",
            "Google Index": "https://www.google.com/search?q=intitle%3Aindex.of+google",
            "Google Scholar": "http://scholar.google.com/scholar?&q=google",
            "Google Patents": "https://patents.google.com/?q=google",
            "Bing": 'http://bing.com/search?q="google"',
            "Bing News": 'http://bing.com/news/search?q="google"',
            "Yahoo": "http://search.yahoo.com/search?p=google",
            "Yandex": "http://www.yandex.com/yandsearch?text=google",
            "Baidu": "http://baidu.com/s?wd=google",
            "Searx": "https://searx.be/?q=google",
            "Exalead": "http://www.exalead.com/search/web/results/?q=google",
            "DuckDuckGo": "https://duckduckgo.com/?q=google",
            "StartPage": "https://startpage.com/do/search?q=google",
            "Qwant": "https://www.qwant.com/?q=google",
            "Brave": "https://search.brave.com/search?q=google",
            "Wayback": "https://web.archive.org/web/*/google",
            "Ahmia": "https://ahmia.fi/search/?q=google",
            "Onionland": "https://onionlandsearchengine.com/search?q=google"
        },
        # TODO need to add in the below once have added to functions.py to test against "google" query
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
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

# JS for Insta tool to adapt:::
"""
function doSearch01(Search01)
{window.open('http://instagram.com/' + Search01, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.Search01.value); return false;">
<input type="text" id="Search01" name="Search01" size="30" placeholder="Username" />
<input type="submit" style="width:140px" value="IG Profile" /><br></form>
<script type="text/javascript">
function doSearch02(Search02)
{window.open('http://instagram.com/' + Search02 + '/channel/', 'Search02window');}
</script>
<form onsubmit="doSearch02(this.Search02.value); return false;">
<input type="text" id="Search02" name="Search02" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="IG Channel" /><br></form>
<script type="text/javascript">
function doSearch03(Search03)
{window.open('https://instagram.com/' + Search03 + '/tagged/', 'Search03window');}
</script>
<form onsubmit="doSearch03(this.Search03.value); return false;">
<input type="text" id="Search03" name="Search03" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="IG Tagged" /><br></form>
<script type="text/javascript">
function doSearch04(Search04)
{window.open('https://www.google.com/search?q=site%3Ainstagram.com+"' + Search04 + '%22', 'Search04window');}
</script>
<form onsubmit="doSearch04(this.Search04.value); return false;">
<input type="text" id="Search04" name="Search04" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Outgoing Search" /><br></form>
<script type="text/javascript">
function doSearch05(Search05)
{window.open('https://www.google.com/search?q=site%3Ainstagram.com+"@' + Search05 + '"', 'Search05window');}
</script>
<form onsubmit="doSearch05(this.Search05.value); return false;">
<input type="text" id="Search05" name="Search05" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Incoming Search" /><br></form>
<script type="text/javascript">
function doSearch06(Search06)
{window.open('https://www.bing.com/search?q=site%3Ainstagram.com+"' + Search06 + '"', 'Search06window');}
</script>
<form onsubmit="doSearch06(this.Search06.value); return false;">
<input type="text" id="Search06" name="Search06" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Bing Search" /><br></form>
<script type="text/javascript">
function doSearch07(Search07)
{window.open('https://yandex.com/search/?text=site%3Ainstagram.com+"' + Search07 + '"', 'Search07window');}
</script>
<form onsubmit="doSearch07(this.Search07.value); return false;">
<input type="text" id="Search07" name="Search07" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Yandex Search" /><br></form>
<script type="text/javascript">
function doSearch08(Search08)
{window.open('https://www.google.com/search?q=site%3Atwitter.com+“' + Search08 + '”+“instagram.com%2Fp”', 'Search08window');}
</script>
<form onsubmit="doSearch08(this.Search08.value); return false;">
<input type="text" id="Search08" name="Search08" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Twitter Posts" /><br></form>
<script type="text/javascript">
function doSearch09(Search09)
{window.open('https://dumpor.com/v/' + Search09, 'Search09window');}
</script>
<form onsubmit="doSearch09(this.Search09.value); return false;">
<input type="text" id="Search09" name="Search09" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Dumpor Profile" /><br></form>
<script type="text/javascript">
function doSearch10(Search10)
{window.open('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={%22id%22:%22' + Search10 + '%22,%22include_reel%22:true,%22fetch_mutual%22:true,%22first%22:50}', 'Search10window');}
</script>
<form onsubmit="doSearch10(this.Search10.value); return false;">
<input type="text" id="Search10" name="Search10" size="30" placeholder="IG User ID" value="" />
<input type="submit" style="width:140px" value="Followers" /><br></form>
<script type="text/javascript">
function doSearch11(Search11)
{window.open('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={%22id%22:%22' + Search11 + '%22,%22include_reel%22:true,%22fetch_mutual%22:false,%22first%22:50}', 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11.value); return false;">
<input type="text" id="Search11" name="Search11" size="30" placeholder="IG User ID" value="" />
<input type="submit" style="width:140px" value="Following" /><br></form>
<br>
<script type="text/javascript">
function doSearch12(Search12,Search12b)
{window.open('https://www.google.com/search?&q=site%3Ainstagram.com+“' + Search12 + '”+“' + Search12b + '”', 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12.value,this.Search12b.value); return false;">
<input type="text" id="Search12" name="Search12" size="15" placeholder="Username" value="" />
<input type="text" name="Search12b" size="15" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="User + Term" /><br></form>
<script type="text/javascript">
function doSearch13(Search13,Search13b)
{window.open('https://www.google.com/search?&q=site%3Ainstagram.com+“' + Search13 + '”+“' + Search13b + '”', 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13.value,this.Search13b.value); return false;">
<input type="text" id="Search13" name="Search13" size="15" placeholder="Username" value="" />
<input type="text" name="Search13b" size="15" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Associations" /><br></form>
<br>
<script type="text/javascript">
function doSearch14(Search14)
{window.open('https://www.instagram.com/explore/tags/' + Search14, 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14.value); return false;">
<input type="text" name="Search14" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="IG Hashtags" /><br></form>
<script type="text/javascript">
function doSearch15(Search15)
{window.open('https://www.google.com/search?&q=site%3Ainstagram.com+' + Search15, 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15.value); return false;">
<input type="text" name="Search15" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="IG Terms" /><br></form>
<script type="text/javascript">
function doSearch16(Search16)
{window.open('https://dumpor.com/t/' + Search16, 'Search16window');}
</script>
<form onsubmit="doSearch16(this.Search16.value); return false;">
<input type="text" name="Search16" size="30" placeholder="Hashtag" value="" />
<input type="submit" style="width:140px" value="Dumpor Tag" /><br></form>
</p>
"""

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

# LinkedIn JS to adapt:::
"""
function doSearch01(keyword, fname, lname, title, company, school)
{window.open('https://www.linkedin.com/search/results/people/?keywords=' + keyword + '&firstName=' + fname + '&lastName=' + lname + '&title=' + title + '&company=' + company + '&school=' + school, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.keyword.value, this.fname.value, this.lname.value, this.title.value, this.company.value, this.school.value); return false;">
<input type="text" name="fname" size="20" placeholder="First Name" />
<input type="text" name="lname" size="20" placeholder="Last Name" /><br>
<input type="text" name="keyword" size="20" placeholder="Keyword" />
<input type="text" name="title" size="20" placeholder="Title" /><br>
<input type="text" name="company" size="20" placeholder="Company" />
<input type="text" name="school" size="20" placeholder="School" /><br>
<input type="submit" style="width:140px" Value="Person Search" />
</form><br>
<script type="text/javascript">
function doSearch02(keyword, title)
{window.open('https://www.linkedin.com/search/results/content/?authorJobTitle=%22' + title + '%22&keywords=' + keyword, 'Search02window');}
</script>
<form onsubmit="doSearch02(this.keyword.value, this.title.value); return false;">
<input type="text" name="keyword" size="20" placeholder="Keyword" />
<input type="text" name="title" size="20" placeholder="Title" /><br>
<input type="submit" style="width:140px" Value="Post Search" />
</form><br>
<script type="text/javascript">
function doSearch03(keyword, fname, lname, title, school, company)
{window.open('https://www.google.com/search?q=site%3Awww.linkedin.com+' + keyword + '+' + fname + '+' + lname + '+' + title + '+' + company + '+' + school, 'Search03window');}
</script>
<form onsubmit="doSearch03(this.keyword.value, this.fname.value, this.lname.value, this.title.value, this.company.value, this.school.value); return false;">
<input type="text" name="fname" size="20" placeholder="First Name" />
<input type="text" name="lname" size="20" placeholder="Last Name" /><br>
<input type="text" name="keyword" size="20" placeholder="Keyword" />
<input type="text" name="title" size="20" placeholder="Title" /><br>
<input type="text" name="company" size="20" placeholder="Company" />
<input type="text" name="school" size="20" placeholder="School" /><br>
<input type="submit" style="width:140px" Value="Google Search" />
</form><br>
<script type="text/javascript">
function doSearch04(keyword, fname, lname, title, school, company)
{window.open('https://www.bing.com/search?q=site%3Alinkedin.com+' + keyword + '+' + fname + '+' + lname + '+' + title + '+' + company + '+' + school, 'Search04window');}
</script>
<form onsubmit="doSearch04(this.keyword.value, this.fname.value, this.lname.value, this.title.value, this.company.value, this.school.value); return false;">
<input type="text" name="fname" size="20" placeholder="First Name" />
<input type="text" name="lname" size="20" placeholder="Last Name" /><br>
<input type="text" name="keyword" size="20" placeholder="Keyword" />
<input type="text" name="title" size="20" placeholder="Title" /><br>
<input type="text" name="company" size="20" placeholder="Company" />
<input type="text" name="school" size="20" placeholder="School" /><br>
<input type="submit" style="width:140px" Value="Bing Search" />
</form><br>
<script type="text/javascript">
function doSearch05(keyword, fname, lname, title, school, company)
{window.open('https://www.yandex.com/search/?text=site%3Alinkedin.com' + '+' keyword + '+' + fname + '+' + lname + '+' + title + '+' + company + '+' + school, 'Search05window');}
</script>
<form onsubmit="doSearch05(this.keyword.value, this.fname.value, this.lname.value, this.title.value, this.company.value, this.school.value); return false;">
<input type="text" name="fname" size="20" placeholder="First Name" />
<input type="text" name="lname" size="20" placeholder="Last Name" /><br>
<input type="text" name="keyword" size="20" placeholder="Keyword" />
<input type="text" name="title" size="20" placeholder="Title" /><br>
<input type="text" name="company" size="20" placeholder="Company" />
<input type="text" name="school" size="20" placeholder="School" /><br>
<input type="submit" style="width:140px" Value="Yandex Search" />
</form><br>
<script type="text/javascript">
function doSearch06(keyword)
{window.open('https://www.linkedin.com/search/results/companies/?keywords=' + keyword, 'Search06window');}
</script>
<form onsubmit="doSearch06(this.keyword.value); return false;">
<input type="text" name="keyword" size="30" placeholder="Keyword" />
<input type="submit" style="width:140px" Value="Company Search" />
</form>
<script type="text/javascript">
function doSearch07(keyword)
{window.open('https://www.linkedin.com/search/results/groups/?keywords=' + keyword, 'Search07window');}
</script>
<form onsubmit="doSearch07(this.keyword.value); return false;">
<input type="text" name="keyword" size="30" placeholder="Keyword" />
<input type="submit" style="width:140px" Value="Group Search" />
</form>
<script type="text/javascript">
function doSearch08(keyword)
{window.open('https://www.linkedin.com/search/results/schools/?keywords=' + keyword, 'Search08window');}
</script>
<form onsubmit="doSearch08(this.keyword.value); return false;">
<input type="text" name="keyword" size="30" placeholder="Keyword" />
<input type="submit" style="width:140px" Value="School Search" />
</form>
<script type="text/javascript">
function doSearch09(keyword)
{window.open('https://www.linkedin.com/search/results/events/?keywords=' + keyword, 'Search09window');}
</script>
<form onsubmit="doSearch09(this.keyword.value); return false;">
<input type="text" name="keyword" size="30" placeholder="Keyword" />
<input type="submit" style="width:140px" Value="Event Search" />
</form>
<script type="text/javascript">
function doSearch10(keyword)
{window.open('https://www.linkedin.com/jobs/index/?keywords=' + keyword, 'Search10window');}
</script>
<form onsubmit="doSearch10(this.keyword.value); return false;">
<input type="text" name="keyword" size="30" placeholder="Keyword" />
<input type="submit" style="width:140px" Value="Job Search" />
</form><br>
<script type="text/javascript">
function doSearch11(Search11)
{window.open('http://www.linkedin.com/in/' + Search11, 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11.value); return false;">
<input type="text" name="Search11" size="30" placeholder="Username" />
<input type="submit" style="width:140px" value="Profile" /><br></form>
<script type="text/javascript">
function doSearch12(Search12)
{window.open('https://search.google.com/test/mobile-friendly?url=http://linkedin.com/in/' + Search12, 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12.value); return false;">
<input type="text" name="Search12" size="30" placeholder="Username" />
<input type="submit" style="width:140px" value="Mobile Profile" /><br></form>
<script type="text/javascript">
function doSearch13(Search13)
{window.open('https://www.google.com/search?q=site:linkedin.com+' + Search13 + '&source=lnms&tbm=isch', 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13.value); return false;">
<input type="text" name="Search13" size="30" placeholder="Username or Real Name" value="" />
<input type="submit" style="width:140px" value="Google Photos" /><br></form>
<script type="text/javascript">
function doSearch14(Search14)
{window.open('https://www.bing.com/images/search?q=site%3alinkedin.com+' + Search14 + '&scenario=ImageBasicHover', 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14.value); return false;">
<input type="text" name="Search14" size="30" placeholder="Username or Real Name" value="" />
<input type="submit" style="width:140px" value="Bing Photos" /><br></form>
<script type="text/javascript">
function doSearch15(Search15)
{window.open('https://www.google.com/search?q=site:linkedin.com+' + Search15 + '&tbm=vid', 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15.value); return false;">
<input type="text" name="Search15" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Videos" /><br></form>
</p>
</div>
"""

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

# Communities JS to adapt:::
"""
<script type="text/javascript">
function doSearch01(Search01)
{window.open('https://old.reddit.com/search?q=' + Search01, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.Search01.value); return false;">
<input type="text" name="Search01" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Keyword Search" /><br></form>
<script type="text/javascript">
function doSearch02(Search02)
{window.open('https://old.reddit.com/search?q=title:' + Search02, 'Search02window');}
</script>
<form onsubmit="doSearch02(this.Search02.value); return false;">
<input type="text" name="Search02" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Title Search" /><br></form>
<script type="text/javascript">
function doSearch03(Search03)
{window.open('https://old.reddit.com/user/' + Search03, 'Search03window');}
</script>
<form onsubmit="doSearch03(this.Search03.value); return false;">
<input type="text" name="Search03" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Profile" /><br></form>
<script type="text/javascript">
function doSearch04(Search04)
{window.open('https://old.reddit.com/user/' + Search04 + '/posts/', 'Search04window');}
</script>
<form onsubmit="doSearch04(this.Search04.value); return false;">
<input type="text" name="Search04" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Posts" /><br></form>
<script type="text/javascript">
function doSearch05(Search05)
{window.open('https://old.reddit.com/user/' + Search05 + '/comments/', 'Search05window');}
</script>
<form onsubmit="doSearch05(this.Search05.value); return false;">
<input type="text" name="Search05" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Comments" /><br></form>
<script type="text/javascript">
function doSearch06(Search06)
{window.open('https://web.archive.org/web/*/https://www.reddit.com/user/' + Search06, 'Search06window');}
</script>
<form onsubmit="doSearch06(this.Search06.value); return false;">
<input type="text" name="Search06" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Archive I" /><br></form>
<script type="text/javascript">
function doSearch07(Search07)
{window.open('https://webcache.googleusercontent.com/search?q=cache:https://www.reddit.com/user/' + Search07, 'Search07window');}
</script>
<form onsubmit="doSearch07(this.Search07.value); return false;">
<input type="text" name="Search07" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Archive II" /><br></form>
<script type="text/javascript">
function doSearch08(Search08)
{window.open('https://api.pushshift.io/reddit/search/comment/?author=' + Search08 + '&sort=asc&size=1000', 'Search08window');}
</script>
<form onsubmit="doSearch08(this.Search08.value); return false;">
<input type="text" name="Search08" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Pushshift User I" /><br>
</form>
<script type="text/javascript">
function doSearch09(Search09)
{window.open('https://api.pushshift.io/reddit/search/comment/?author=' + Search09, 'Search09window');}
</script>
<form onsubmit="doSearch09(this.Search09.value); return false;">
<input type="text" name="Search09" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Pushshift User II" /><br></form>
<script type="text/javascript">
function doSearch10(Search10)
{window.open('https://api.pushshift.io/reddit/search/comment/?q=' + Search10, 'Search10window');}
</script>
<form onsubmit="doSearch10(this.Search10.value); return false;">
<input type="text" name="Search10" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Pushshift Comment" /><br></form>
<script type="text/javascript">
function doSearch11(Search11)
{window.open('https://api.pushshift.io/reddit/search/submission/?q=' + Search11, 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11.value); return false;">
<input type="text" name="Search11" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Pushshift Posts" /><br></form>
<script type="text/javascript">
function doSearch12(Search12)
{window.open('https://old.reddit.com/search?q=site:' + Search12, 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12.value); return false;">
<input type="text" name="Search12" size="30" placeholder="Domain" value="" />
<input type="submit" style="width:140px" value="Domain Search" /><br></form>
<script type="text/javascript">
function doSearch13(Search13)
{window.open('https://old.reddit.com/search?q=url:' + Search13, 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13.value); return false;">
<input type="text" name="Search13" size="30" placeholder="Domain" value="" />
<input type="submit" style="width:140px" value="Domain Mention" /><br></form>
<script type="text/javascript">
function doSearch14(Search14)
{window.open('https://old.reddit.com/subreddits/search?q=' + Search14, 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14.value); return false;">
<input type="text" name="Search14" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="SubReddit Search" /><br></form>
<script type="text/javascript">
function doSearch15(Search15)
{window.open('https://imgur.com/r/' + Search15, 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15.value); return false;">
<input type="text" name="Search15" size="30" placeholder="SubReddit Name" value="" />
<input type="submit" style="width:140px" value="Imgur Search" /><br></form>
<script type="text/javascript">
function doSearch16(Search16)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=' + Search16 + '&q=site:reddit.com', 'Search16window');}
</script>
<form onsubmit="doSearch16(this.Search16.value); return false;">
<input type="text" name="Search16" size="30" placeholder="URL" value="" />
<input type="submit" style="width:140px" value="Image Search" /><br></form>
<br>Hacker News (YCombinator):
<script type="text/javascript">
function doSearch17(Search17)
{window.open('https://hn.algolia.com/?query=' + Search17 + '&sort=byDate&prefix&page=0&dateRange=all&type=all', 'Search17window');}
</script>
<form onsubmit="doSearch17(this.Search17.value); return false;">
<input type="text" name="Search17" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Keyword Search" /><br></form>
<script type="text/javascript">
function doSearch18(Search18)
{window.open('https://news.ycombinator.com/user?id=' + Search18, 'Search18window');}
</script>
<form onsubmit="doSearch18(this.Search18.value); return false;">
<input type="text" name="Search18" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Search" /><br></form>
<script type="text/javascript">
function doSearch19(Search19)
{window.open('https://news.ycombinator.com/submitted?id=' + Search19, 'Search19window');}
</script>
<form onsubmit="doSearch19(this.Search19.value); return false;">
<input type="text" name="Search19" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Posts" /><br></form>
<script type="text/javascript">
function doSearch20(Search20)
{window.open('https://news.ycombinator.com/threads?id=' + Search20, 'Search20window');}
</script>
<form onsubmit="doSearch20(this.Search20.value); return false;">
<input type="text" name="Search20" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Comments" /><br></form>
<script type="text/javascript">
function doSearch21(Search21)
{window.open('https://news.ycombinator.com/favorites?id=' + Search21, 'Search21window');}
</script>
<form onsubmit="doSearch21(this.Search21.value); return false;">
<input type="text" name="Search21" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Favorites" /><br></form>
<script type="text/javascript">
function doSearch22(Search22)
{window.open('https://www.google.com/search?q=site:news.ycombinator.com+' + Search22, 'Search22window');}
</script>
<form onsubmit="doSearch22(this.Search22.value); return false;">
<input type="text" name="Search22" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Google Search" /><br></form>
<br>4Chan:<br>
<script type="text/javascript">
function doSearch23(Search23)
{window.open('http://4chansearch.com/?q=' + Search23 + '&s=4', 'Search23window');}
</script>
<form onsubmit="doSearch23(this.Search23.value); return false;">
<input type="text" name="Search23" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Keyword Search" /><br></form>
<script type="text/javascript">
function doSearch24(Search24)
{window.open('http://4chansearch.com/?q=' + Search24 + '&s=7', 'Search24window');}
</script>
<form onsubmit="doSearch24(this.Search24.value); return false;">
<input type="text" name="Search24" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Archive Search I" /><br></form>
<script type="text/javascript">
function doSearch25(Search25)
{window.open('https://archive.4plebs.org/_/search/text/' + Search25 + '/order/asc/', 'Search25window');}
</script>
<form onsubmit="doSearch25(this.Search25.value); return false;">
<input type="text" name="Search25" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Archive Search II" /><br></form>
<script type="text/javascript">
function doSearch26(Search26)
{window.open('https://www.google.com/search?q=site:4chan.org ' + Search26, 'Search26window');}
</script>
<form onsubmit="doSearch26(this.Search26.value); return false;">
<input type="text" name="Search26" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Google Search" /><br></form>
<br>TikTok:<br>
<script type="text/javascript">
function doSearch27(Search27)
{window.open('https://www.tiktok.com/@' + Search27, 'Search27window');}
</script>
<form onsubmit="doSearch27(this.Search27.value); return false;">
<input type="text" name="Search27" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Profile" /><br></form>
<script type="text/javascript">
function doSearch28(Search28)
{window.open('https://www.tiktok.com/search/user?q=' + Search28, 'Search28window');}
</script>
<form onsubmit="doSearch28(this.Search28.value); return false;">
<input type="text" name="Search28" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Profile Search" /><br></form>
<script type="text/javascript">
function doSearch29(Search29)
{window.open('https://www.tiktok.com/tag/' + Search29, 'Search29window');}
</script>
<form onsubmit="doSearch29(this.Search29.value); return false;">
<input type="text" name="Search29" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Tags" /><br></form>
<script type="text/javascript">
function doSearch30(Search30)
{window.open('https://www.tiktok.com/search?q=' + Search30, 'Search30window');}
</script>
<form onsubmit="doSearch30(this.Search30.value); return false;">
<input type="text" name="Search30" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Term Search" /><br></form>
<script type="text/javascript">
function doSearch31(Search31)
{window.open('https://www.tiktok.com/search/video?q=' + Search31, 'Search31window');}
</script>
<form onsubmit="doSearch31(this.Search31.value); return false;">
<input type="text" name="Search31" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Video Search" /><br></form>
<script type="text/javascript">
function doSearch32(Search32)
{window.open('https://www.google.com/search?q=site:tiktok.com+' + Search32, 'Search32window');}
</script>
<form onsubmit="doSearch32(this.Search32.value); return false;">
<input type="text" name="Search32" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Google Search" /><br></form>
<script type="text/javascript">
function doSearch33(Search33)
{window.open('https://tokcount.com/tiktok-analytics/' + Search33, 'Search33window');}
</script>
<form onsubmit="doSearch33(this.Search33.value); return false;">
<input type="text" name="Search33" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Analytics I" /><br></form>
<script type="text/javascript">
function doSearch34(Search34)
{window.open('https://exolyt.com/user/' + Search34, 'Search34window');}
</script>
<form onsubmit="doSearch34(this.Search34.value); return false;">
<input type="text" name="Search34" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Analytics II" /><br></form>
<script type="text/javascript">
function doSearch35(Search35)
{window.open('https://tokcounter.com/tiktok-analytics/' + Search35, 'Search35window');}
</script>
<form onsubmit="doSearch35(this.Search35.value); return false;">
<input type="text" name="Search35" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="Analytics III" /><br></form>
<br>Meetup:<br>
<script type="text/javascript">
function doSearch36(Search36)
{window.open('https://www.google.com/search?q=site:meetup.com+inurl:member+' + Search36, 'Search36window');}
</script>
<form onsubmit="doSearch36(this.Search36.value); return false;">
<input type="text" name="Search36" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="Member Search" /><br></form>
<script type="text/javascript">
function doSearch37(Search37)
{window.open('https://www.google.com/search?q=site:meetup.com+inurl:events+' + Search37, 'Search37window');}
</script>
<form onsubmit="doSearch37(this.Search37.value); return false;">
<input type="text" name="Search37" size="30" placeholder="Keywords" value="" />
<input type="submit" style="width:140px" value="Event Search" /><br></form>
<script type="text/javascript">
function doSearch38(Search38)
{window.open('https://www.google.com/search?q=site:meetup.com+inurl:discussions+' + Search38, 'Search38window');}
</script>
<form onsubmit="doSearch38(this.Search38.value); return false;">
<input type="text" name="Search38" size="30" placeholder="Keywords" value="" />
<input type="submit" style="width:140px" value="Post Search" /><br></form>
<script type="text/javascript">
function doSearch39(Search39)
{window.open('https://www.google.com/search?q=site:meetup.com+' + Search39, 'Search39window');}
</script>
<form onsubmit="doSearch39(this.Search39.value); return false;">
<input type="text" name="Search39" size="30" placeholder="Keywords, location, or Name" value="" />
<input type="submit" style="width:140px" value="Google Search" /><br></form>
<br>Ebay:<br>
<script type="text/javascript">
function doSearch40(Search40)
{window.open('https://www.ebay.com/dsc/i.html?&LH_TitleDesc=1&_nkw=' + Search40, 'Search40window');}
</script>
<form onsubmit="doSearch40(this.Search40.value); return false;">
<input type="text" name="Search40" size="30" placeholder="Keywords" value="" />
<input type="submit" style="width:140px" value="Text Search" /><br></form>
<script type="text/javascript">
function doSearch41(Search41)
{window.open('https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + Search41 + '&LH_Sold=1&LH_Complete=1', 'Search41window');}
</script>
<form onsubmit="doSearch41(this.Search41.value); return false;">
<input type="text" name="Search41" size="30" placeholder="Keywords" value="" />
<input type="submit" style="width:140px" value="Sold Search" /><br></form>
<script type="text/javascript">
function doSearch42(Search42)
{window.open('https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + Search42 + '&LH_Complete=1', 'Search42window');}
</script>
<form onsubmit="doSearch42(this.Search42.value); return false;">
<input type="text" name="Search42" size="30" placeholder="Keywords" value="" />
<input type="submit" style="width:140px" value="Completed Search" /><br></form>
<script type="text/javascript">
function doSearch43(Search43)
{window.open('https://www.ebay.com/usr/' + Search43, 'Search43window');}
</script>
<form onsubmit="doSearch43(this.Search43.value); return false;">
<input type="text" name="Search43" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="User Account" /><br></form>
<script type="text/javascript">
function doSearch44(Search44)
{window.open('https://feedback.ebay.com/ws/eBayISAPI.dll?ViewFeedback2&userid=' + Search44, 'Search44window');}
</script>
<form onsubmit="doSearch44(this.Search44.value); return false;">
<input type="text" name="Search44" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="User Feedback" /><br></form>
<script type="text/javascript">
function doSearch45(Search45)
{window.open('https://www.ebay.com/sch/' + Search45 + '/m.html', 'Search45window');}
</script>
<form onsubmit="doSearch45(this.Search45.value); return false;">
<input type="text" name="Search45" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="User Items" /><br></form>
<script type="text/javascript">
function doSearch46(Search46)
{window.open('https://www.google.com/search?q=site%3Ahttps%3A%2F%2Fwww.ebay.com%2Fusr+%22' + Search46 + '%22', 'Search46window');}
</script>
<form onsubmit="doSearch46(this.Search46.value); return false;">
<input type="text" name="Search46" size="30" placeholder="Full or Partial User Name" value="" />
<input type="submit" style="width:140px" value="User Search" /><br></form>
<br>Pinterest:<br>
<script type="text/javascript">
function doSearch49(Search49)
{window.open('https://www.pinterest.com/' + Search49, 'Search49window');}
</script>
<form onsubmit="doSearch49(this.Search49.value); return false;">
<input type="text" name="Search49" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="User Search" /><br></form>
<script type="text/javascript">
function doSearch50(Search50)
{window.open('https://www.pinterest.com/' + Search50 + '/pins/', 'Search50window');}
</script>
<form onsubmit="doSearch50(this.Search50.value); return false;">
<input type="text" name="Search50" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="User Pins" /><br></form>
<script type="text/javascript">
function doSearch51(Search51)
{window.open('https://www.pinterest.com/' + Search51 + '/boards/', 'Search51window');}
</script>
<form onsubmit="doSearch51(this.Search51.value); return false;">
<input type="text" name="Search51" size="30" placeholder="User Name" value="" />
<input type="submit" style="width:140px" value="User Boards" /><br></form>
<script type="text/javascript">
function doSearch54(Search54)
{window.open('https://www.pinterest.com/search/pins/?q=' + Search54 + '&rs=typo_auto_original&auto_correction_disabled=true', 'Search54window');}
</script>
<form onsubmit="doSearch54(this.Search54.value); return false;">
<input type="text" name="Search54" size="30" placeholder="Keywords or Name" value="" />
<input type="submit" style="width:140px" value="Pins Search" /><br></form>
<script type="text/javascript">
function doSearch55(Search55)
{window.open('https://www.pinterest.com/search/boards/?q=' + Search55 + '&rs=typo_auto_original&auto_correction_disabled=true', 'Search55window');}
</script>
<form onsubmit="doSearch55(this.Search55.value); return false;">
<input type="text" name="Search55" size="30" placeholder="Keywords or Name" value="" />
<input type="submit" style="width:140px" value="Boards Search" /><br></form>
<script type="text/javascript">
function doSearch56(Search56)
{window.open('https://www.google.com/search?q=site:pinterest.com+' + Search56, 'Search56window');}
</script>
<form onsubmit="doSearch56(this.Search56.value); return false;">
<input type="text" name="Search56" size="30" placeholder="Keywords or Name" value="" />
<input type="submit" style="width:140px" value="Google Search" /><br></form>
<br />Discord:<br />
<script type="text/javascript">
function doSearch57(Search57)
{window.open('https://discord.gg/' + Search57, 'Search57window');}
</script>
<form onsubmit="doSearch57(this.Search57.value); return false;">
<input type="text" name="Search57" size="30" placeholder="Server Name" value="" />
<input type="submit" style="width:140px" value="Invite Check" /><br /></form>
<script type="text/javascript">
function doSearch58(Search58)
{window.open('https://disboard.org/search?keyword=' + Search58, 'Search58window');}
</script>
<form onsubmit="doSearch58(this.Search58.value); return false;">
<input type="text" name="Search58" size="30" placeholder="Server Term" value="" />
<input type="submit" style="width:140px" value="Disboard" /><br /></form>
<script type="text/javascript">
function doSearch59(Search59)
{window.open('https://top.gg/servers/search?q=' + Search59, 'Search59window');}
</script>
<form onsubmit="doSearch59(this.Search59.value); return false;">
<input type="text" name="Search59" size="30" placeholder="Server Keyword" value="" />
<input type="submit" style="width:140px" value="Top.gg" /><br /></form>
<script type="text/javascript">
function doSearch60(Search60)
{window.open('https://discord.me/servers?search=' + Search60, 'Search60window');}
</script>
<form onsubmit="doSearch60(this.Search60.value); return false;">
<input type="text" name="Search60" size="30" placeholder="Server Keyword" value="" />
<input type="submit" style="width:140px" value="Discord.me" /><br /></form>
<script type="text/javascript">
function doSearch61(Search61)
{window.open('https://discordservers.com/search/' + Search61, 'Search61window');}
</script>
<form onsubmit="doSearch61(this.Search61.value); return false;">
<input type="text" name="Search61" size="30" placeholder="Server Keyword" value="" />
<input type="submit" style="width:140px" value="Servers" /><br /></form>
<script type="text/javascript">
function doSearch62(Search62)
{window.open('https://discordbee.com/servers?q=' + Search62, 'Search62window');}
</script>
<form onsubmit="doSearch62(this.Search62.value); return false;">
<input type="text" name="Search62" size="30" placeholder="Server Keyword" value="" />
<input type="submit" style="width:140px" value="Discordbee" /><br /></form>
<script type="text/javascript">
function doSearch63(Search63)
{window.open('https://www.google.com/search?q=site:discord.com+' + Search63, 'Search63window');}
</script>
<form onsubmit="doSearch63(this.Search63.value); return false;">
<input type="text" name="Search63" size="30" placeholder="Search Term" value="" />
<input type="submit" style="width:140px" value="Google Search" /><br /></form>
<br>Parler</br>
<script type="text/javascript">
function doSearch64(Search64)
{window.open('https://parler.com/' + Search64, 'Search64window');}
</script>
<form onsubmit="doSearch64(this.Search64.value); return false;">
<input type="text" name="Search64" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Profile" /><br /></form>
<br>Gab</br>
<script type="text/javascript">
function doSearch65(Search65)
{window.open('https://gab.com/' + Search65, 'Search65window');}
</script>
<form onsubmit="doSearch65(this.Search65.value); return false;">
<input type="text" name="Search65" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Profile" /><br /></form>
<script type="text/javascript">
function doSearch66(Search66)
{window.open('https://gab.com/groups/' + Search66, 'Search66window');}
</script>
<form onsubmit="doSearch66(this.Search66.value); return false;">
<input type="text" name="Search66" size="30" placeholder="Group Number" value="" />
<input type="submit" style="width:140px" value="Group" /><br /></form>
<br>Telegram</br>
<script type="text/javascript">
function doSearch67(Search67)
{window.open('https://t.me/' + Search67, 'Search67window');}
</script>
<form onsubmit="doSearch67(this.Search67.value); return false;">
<input type="text" name="Search67" size="30" placeholder="User/Channel Name" value="" />
<input type="submit" style="width:140px" value="Profile/Channel" /><br /></form>
<script type="text/javascript">
function doSearch68(Search68)
{window.open('https://telegram.me/s/' + Search68, 'Search68window');}
</script>
<form onsubmit="doSearch68(this.Search68.value); return false;">
<input type="text" name="Search68" size="30" placeholder="Channel Name" value="" />
<input type="submit" style="width:140px" value="Channel Preview" /><br /></form>
<script type="text/javascript">
function doSearch69(Search69)
{window.open('https://telesco.pe/' + Search69, 'Search69window');}
</script>
<form onsubmit="doSearch69(this.Search69.value); return false;">
<input type="text" name="Search69" size="30" placeholder="Username" value="" />
<input type="submit" style="width:140px" value="User Videos" /><br /></form>
<script type="text/javascript">
function doSearch70(Search70)
{window.open('https://www.telegram-group.com/en?s=' + Search70, 'Search70window');}
</script>
<form onsubmit="doSearch70(this.Search70.value); return false;">
<input type="text" name="Search70" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Group Search" /><br /></form>
<script type="text/javascript">
function doSearch71(Search71)
{window.open('https://telegramchannels.me/search?type=all&search=' + Search71, 'Search71window');}
</script>
<form onsubmit="doSearch71(this.Search71.value); return false;">
<input type="text" name="Search71" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Channel Search" /><br /></form>
<script type="text/javascript">
function doSearch72(Search72)
{window.open('https://telemetr.io/en/channels?channel=' + Search72, 'Search72window');}
</script>
<form onsubmit="doSearch72(this.Search72.value); return false;">
<input type="text" name="Search72" size="30" placeholder="Keyword" value="" />
<input type="submit" style="width:140px" value="Channel Search" /><br /></form>
</p>
"""

# TODO: Email address tool: https://inteltechniques.com/tools/Email.html

def email_query(email: str) -> dict:
    """
    function doSearch01(Search01)
                        {
                            window.open('http://google.com/search?q="' + Search01 + '"', 'Search01window');
                        }
                        </script>
                        <form onsubmit="doSearch01(this.Search01.value); return false;">
                            <input type="text" id="Search01" name="Search01" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Google"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch02(Search02)
                        {
                            window.open('http://bing.com/search?q="' + Search02 + '"', 'Search02window');
                        }
                        </script>
                        <form onsubmit="doSearch02(this.Search02.value); return false;">
                            <input type="text" id="Search02" name="Search02" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Bing"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch03(Search03)
                        {
                            window.open('https://yandex.com/search/?text="' + Search03 + '"', 'Search03window');
                        }
                        </script>
                        <form onsubmit="doSearch03(this.Search03.value); return false;">
                            <input type="text" id="Search03" name="Search03" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Yandex"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch04(Search04)
                        {
                            window.open('https://emailrep.io/query/' + Search04, 'Search04window');
                        }
                        </script>
                        <form onsubmit="doSearch04(this.Search04.value); return false;">
                            <input type="text" id="Search04" name="Search04" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Emailrep"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch05(Search05)
                        {
                            window.open('https://en.gravatar.com/site/check/' + Search05, 'Search05window');
                        }
                        </script>
                        <form onsubmit="doSearch05(this.Search05.value); return false;">
                            <input type="text" id="Search05" name="Search05" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Gravatar"/>
                            <br>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doSearch06(Search06)
                        {
                            window.open('https://haveibeenpwned.com/unifiedsearch/' + Search06, 'Search06window');
                        }
                        </script>
                        <form onsubmit="doSearch06(this.Search06.value); return false;">
                            <input type="text" id="Search06" name="Search06" size="30" placeholder="Email Address"/>
                            <input type="submit" style="width:140px" value="HIBP"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch07(Search07)
                        {
                            window.open('https://dehashed.com/search?query="' + Search07 + '"', 'Search07window');
                        }
                        </script>
                        <form onsubmit="doSearch07(this.Search07.value); return false;">
                            <input type="text" id="Search07" name="Search07" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Dehashed"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch08(Search08)
                        {
                            window.open('https://portal.spycloud.com/endpoint/enriched-stats/' + Search08, 'Search08window');
                        }
                        </script>
                        <form onsubmit="doSearch08(this.Search08.value); return false;">
                            <input type="text" id="Search08" name="Search08" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Spycloud"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch09(Search09)
                        {
                            window.open('https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email=' + Search09, 'Search09window');
                        }
                        </script>
                        <form onsubmit="doSearch09(this.Search09.value); return false;">
                            <input type="text" id="Search09" name="Search09" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="HudsonRock"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch10(Search10)
                        {
                            window.open('https://check.cybernews.com/chk/?lang=en_US&e=' + Search10, 'Search10window');
                        }
                        </script>
                        <form onsubmit="doSearch10(this.Search10.value); return false;">
                            <input type="text" id="Search10" name="Search10" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Cybernews"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch11(Search11)
                        {
                            window.open('https://psbdmp.ws/api/search/' + Search11, 'Search11window');
                        }
                        </script>
                        <form onsubmit="doSearch11(this.Search11.value); return false;">
                            <input type="text" id="Search11" name="Search11" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="PSBDMP"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch12(Search12)
                        {
                            window.open('https://intelx.io/?s=' + Search12, 'Search12window');
                        }
                        </script>
                        <form onsubmit="doSearch12(this.Search12.value); return false;">
                            <input type="text" id="Search12" name="Search12" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="IntelX"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch13(Search13)
                        {
                            var f = document.getElementById('leakedSourceEmailForm');
                            f.search.value = Search13;
                            window.open('', 'Search13window');
                            f.submit();
                        }
                        </script>
                        <form onsubmit="doSearch13(this.Search13.value); return false;">
                            <input type="text" id="Search13" name="Search13" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="LeakedSource"/>
                        </form>
                        <form id="leakedSourceEmailForm" method="post" action="https://leakedsource.ru/" target="Search13window">
                            <input type="hidden" id="search" name="search" value="">
                            <input type="hidden" name="searchType" value="email">
                            <input type="hidden" name="wildcard" value="0">
                            <input type="submit" id="searchsubmit" style="visibility: hidden;" value="Search">
                        </form>
                        <script type="text/javascript">
                        function doSearch14(Search14)
                        {
                            window.open('https://hunter.io/email-verifier/' + Search14, 'Search14window');
                        }
                        </script>
                        <form onsubmit="doSearch14(this.Search14.value); return false;">
                            <input type="text" id="Search14" name="Search14" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="HunterVerify"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch15(Search15)
                        {
                            window.open('https://data.occrp.org/search?q=' + Search15, 'Search15window');
                        }
                        </script>
                        <form onsubmit="doSearch15(this.Search15.value); return false;">
                            <input type="text" id="Search15" name="Search15" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="OCCRP"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch16(Search16)
                        {
                            window.open('https://www.spytox.com/people/search?email=' + Search16, 'Search16window');
                        }
                        </script>
                        <form onsubmit="doSearch16(this.Search16.value); return false;">
                            <input type="text" id="Search16" name="Search16" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="SpyTox"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch17(Search17)
                        {
                            window.open('https://thatsthem.com/email/' + Search17, 'Search17window');
                        }
                        </script>
                        <form onsubmit="doSearch17(this.Search17.value); return false;">
                            <input type="text" id="Search17" name="Search17" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="ThatsThem"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch18(Search18)
                        {
                            window.open('https://api.protonmail.ch/pks/lookup?op=get&search=' + Search18, 'Search18window');
                        }
                        </script>
                        <form onsubmit="doSearch18(this.Search18.value); return false;">
                            <input type="text" id="Search18" name="Search18" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Protonmail"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch19(Search19)
                        {
                            window.open('http://domainbigdata.com/email/' + Search19, 'Search19window');
                        }
                        </script>
                        <form onsubmit="doSearch19(this.Search19.value); return false;">
                            <input type="text" id="Search19" name="Search19" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="DomainData"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch20(Search20)
                        {
                            window.open('https://whoisology.com/email/' + Search20, 'Search20window');
                        }
                        </script>
                        <form onsubmit="doSearch20(this.Search20.value); return false;">
                            <input type="text" id="Search20" name="Search20" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Whoisology"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch21(Search21)
                        {
                            window.open('http://analyzeid.com/?email=' + Search21, 'Search21window');
                        }
                        </script>
                        <form onsubmit="doSearch21(this.Search21.value); return false;">
                            <input type="text" id="Search21" name="Search21" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="AnalyzeID"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch22(Search22)
                        {
                            window.open('https://www.whoxy.com/search.php?email=' + Search22, 'Search22window');
                        }
                        </script>
                        <form onsubmit="doSearch22(this.Search22.value); return false;">
                            <input type="text" id="Search22" name="Search22" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Whoxy"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch23(Search23)
                        {
                            window.open('https://scamsearch.io/search_report?searchoption=all&search=' + Search23, 'Search23window');
                        }
                        </script>
                        <form onsubmit="doSearch23(this.Search23.value); return false;">
                            <input type="text" id="Search23" name="Search23" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="ScamSearch"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch24(Search24)
                        {
                            window.open('https://myspace.com/search/people?q=' + Search24, 'Search24window');
                        }
                        </script>
                        <form onsubmit="doSearch24(this.Search24.value); return false;">
                            <input type="text" id="Search24" name="Search24" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="MySpace"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch25(Search25)
                        {
                            window.open('https://www.flickr.com/search/people/?q=' + Search25, 'Search25window');
                        }
                        </script>
                        <form onsubmit="doSearch25(this.Search25.value); return false;">
                            <input type="text" id="Search25" name="Search25" size="30" placeholder="Email Address" value=""/>
                            <input type="submit" style="width:140px" value="Flickr"/>
                            <br>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doall(all) {
                            window.open('http://google.com/search?q="' + all + '"', 'Search01window');
                            window.open('http://bing.com/search?q="' + all + '"', 'Search02window');
                            window.open('https://yandex.com/search/?text="' + all + '"', 'Search03window');
                            window.open('https://emailrep.io/query/' + all, 'Search04window');
                            window.open('https://en.gravatar.com/site/check/' + all, 'Search05window');
                            window.open('https://haveibeenpwned.com/unifiedsearch/' + all, 'Search06window');
                            window.open('https://dehashed.com/search?query="' + all + '"', 'Search07window');
                            window.open('https://portal.spycloud.com/endpoint/enriched-stats/' + all, 'Search08window');
                            window.open('https://psbdmp.ws/api/search/' + all, 'Search09window');
                            window.open('https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email=' + all, 'Search10window');
                            window.open('https://check.cybernews.com/chk/?lang=en_US&e=' + all, 'Search11window');
                            window.open('http://google.com/search?q=site:psbdmp.ws+"' + all + '"', 'Search12window');
                            window.open('https://intelx.io/?s=' + all, 'Search13window');
                            window.open('https://hunter.io/email-verifier/' + all, 'Search14window');
                            window.open('https://data.occrp.org/search?q=' + all, 'Search15window');
                            window.open('https://www.spytox.com/people/search?email=' + all, 'Search16window');
                            window.open('https://thatsthem.com/email/' + all, 'Search17window');
                            window.open('http://domainbigdata.com/email/' + all, 'Search18window');
                            window.open('https://api.protonmail.ch/pks/lookup?op=get&search=' + all, 'Search19awindow');
                            window.open('https://whoisology.com/email/' + all, 'Search21window');
                            window.open('http://analyzeid.com/?email=' + all, 'Search22window');
                            window.open('https://www.whoxy.com/search.php?email=' + all, 'Search23window');
                            window.open('https://scamsearch.io/search_report?searchoption=all&search=' + all, 'Search24window');
                            window.open('https://myspace.com/search/people?q=' + all, 'Search25window');
                            window.open('https://www.flickr.com/search/people/?q=' + all, 'Search26window');
                        }
                        </script>
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
    unction doSearch01(Search01)
                        {
                            window.open('https://www.google.com/search?q=%22' + Search01 + '%22', 'Search01window');
                        }
                        </script>
                        <form onsubmit="doSearch01(this.Search01.value); return false;">
                            <input type="text" id="Search01" name="Search01" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Google"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch02(Search02)
                        {
                            window.open('https://www.bing.com/search?q=%22' + Search02 + '%22', 'Search02window');
                        }
                        </script>
                        <form onsubmit="doSearch02(this.Search02.value); return false;">
                            <input type="text" id="Search02" name="Search02" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Bing"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch03(Search03)
                        {
                            window.open('https://yandex.com/search/?text="' + Search03 + '"', 'Search03window');
                        }
                        </script>
                        <form onsubmit="doSearch03(this.Search03.value); return false;">
                            <input type="text" id="Search03" name="Search03" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Yandex"/>
                            <br>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doSearch04(Search04)
                        {
                            window.open('https://knowem.com/checkusernames.php?u=' + Search04, 'Search04window');
                        }
                        </script>
                        <form onsubmit="doSearch04(this.Search04.value); return false;">
                            <input type="text" id="Search04" name="Search04" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="KnowEm Basic"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch05(Search05)
                        {
                            window.open('https://knowem.com/checksocialnames.php?u=' + Search05, 'Search05window');
                        }
                        </script>
                        <form onsubmit="doSearch05(this.Search05.value); return false;">
                            <input type="text" id="Search05" name="Search05" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="KnowEm Adv"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch06(Search06) {
                            window.open('https://usersearch.org/results_normal.php?URL_username=' + Search06, 'Search06awindow');
                            window.open('https://usersearch.org/results_advanced.php?URL_username=' + Search06, 'Search06bwindow');
                            window.open('https://usersearch.org/results_advanced1.php?URL_username=' + Search06, 'Search06cwindow');
                            window.open('https://usersearch.org/results_advanced2.php?URL_username=' + Search06, 'Search06dwindow');
                            window.open('https://usersearch.org/results_advanced4.php?URL_username=' + Search06, 'Search06ewindow');
                            window.open('https://usersearch.org/results_advanced5.php?URL_username=' + Search06, 'Search06fwindow');
                            window.open('https://usersearch.org/results_advanced6.php?URL_username=' + Search06, 'Search06gwindow');
                            window.open('https://usersearch.org/results_advanced7.php?URL_username=' + Search06, 'Search06hwindow');
                            window.open('https://usersearch.org/results_dating.php?URL_username=' + Search06, 'Search06iwindow');
                            window.open('https://usersearch.org/results_forums.php?URL_username=' + Search06, 'Search06jwindow');
                            window.open('https://usersearch.org/results_crypto.php?URL_username=' + Search06, 'Search06kwindow');
                        }
                        </script>
                        <form onsubmit="doSearch06(this.Search06.value); return false;">
                            <input type="text" id="Search06" name="all" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="UserSearch"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch07(Search07)
                        {
                            window.open('https://namevine.com/#/' + Search07, 'Search07window');
                        }
                        </script>
                        <form onsubmit="doSearch07(this.Search07.value); return false;">
                            <input type="text" id="Search07" name="Search07" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="NameVine"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch08(Search08)
                        {
                            window.open('https://www.social-searcher.com/search-users/?ntw=&q6=' + Search08, 'Search08window');
                        }
                        </script>
                        <form onsubmit="doSearch08(this.Search08.value); return false;">
                            <input type="text" id="Search08" name="Search08" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="SocialSearcher"/>
                            <br>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doSearch09(Search09)
                        {
                            window.open('https://haveibeenpwned.com/unifiedsearch/' + Search09, 'Search09window');
                        }
                        </script>
                        <form onsubmit="doSearch09(this.Search09.value); return false;">
                            <input type="text" id="Search09" name="Search09" size="30" placeholder="Username"/>
                            <input type="submit" style="width:140px" value="HaveIBeenPwned"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch10(Search10)
                        {
                            window.open('https://dehashed.com/search?query="' + Search10 + '"', 'Search10window');
                        }
                        </script>
                        <form onsubmit="doSearch10(this.Search10.value); return false;">
                            <input type="text" id="Search10" name="Search10" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Dehashed"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch11(Search11)
                        {
                            window.open('https://psbdmp.ws/api/search/' + Search11, 'Search11window');
                        }
                        </script>
                        <form onsubmit="doSearch11(this.Search11.value); return false;">
                            <input type="text" id="Search11" name="Search11" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="PSBDMP"/>
                            <br>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doSearch12(Search12)
                        {
                            window.open('https://en.gravatar.com/' + Search12, 'Search12window');
                        }
                        </script>
                        <form onsubmit="doSearch12(this.Search12.value); return false;">
                            <input type="text" id="Search12" name="Search12" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Gravater"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch13(Search13)
                        {
                            window.open('https://linktr.ee/' + Search13, 'Search13window');
                        }
                        </script>
                        <form onsubmit="doSearch13(this.Search13.value); return false;">
                            <input type="text" id="Search13" name="Search13" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="LinkTree"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch14(Search14)
                        {
                            window.open('https://www.searchmy.bio/search?q=' + Search14, 'Search14window');
                        }
                        </script>
                        <form onsubmit="doSearch14(this.Search14.value); return false;">
                            <input type="text" id="Search14" name="Search14" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="InstagramBio"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch15(Search15)
                        {
                            window.open('http://twitter.com/' + Search15, 'Search15window');
                        }
                        </script>
                        <form onsubmit="doSearch15(this.Search15.value); return false;">
                            <input type="text" id="Search15" name="Search15" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Twitter"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch16(Search16)
                        {
                            window.open('https://facebook.com/' + Search16, 'Search16window');
                        }
                        </script>
                        <form onsubmit="doSearch16(this.Search16.value); return false;">
                            <input type="text" id="Search16" name="Search16" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Facebook"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch17(Search17)
                        {
                            window.open('http://instagram.com/' + Search17, 'Search17window');
                        }
                        </script>
                        <form onsubmit="doSearch17(this.Search17.value); return false;">
                            <input type="text" id="Search17" name="Search17" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Instagram"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch18(Search18)
                        {
                            window.open('https://www.tiktok.com/@' + Search18, 'Search18window');
                        }
                        </script>
                        <form onsubmit="doSearch18(this.Search18.value); return false;">
                            <input type="text" id="Search18" name="Search18" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="TikTok"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch19(Search19)
                        {
                            window.open('https://tinder.com/@' + Search19, 'Search19window');
                        }
                        </script>
                        <form onsubmit="doSearch19(this.Search19.value); return false;">
                            <input type="text" id="Search19" name="Search19" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Tinder"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch20(Search20)
                        {
                            window.open('https://' + Search20 + '.tumblr.com', 'Search20window');
                        }
                        </script>
                        <form onsubmit="doSearch20(this.Search20.value); return false;">
                            <input type="text" id="Search20" name="Search20" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Tumblr"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch21(Search21)
                        {
                            window.open('https://www.snapchat.com/s/' + Search21, 'Search21window');
                        }
                        </script>
                        <form onsubmit="doSearch21(this.Search21.value); return false;">
                            <input type="text" id="Search21" name="Search21" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Snapchat"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch22(Search22)
                        {
                            window.open('https://medium.com/@' + Search22, 'Search22window');
                        }
                        </script>
                        <form onsubmit="doSearch22(this.Search22.value); return false;">
                            <input type="text" id="Search22" name="Search22" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Medium"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch23(Search23)
                        {
                            window.open('http://youtube.com/' + Search23, 'Search23window');
                        }
                        </script>
                        <form onsubmit="doSearch23(this.Search23.value); return false;">
                            <input type="text" id="Search23" name="Search23" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="YouTube"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch24(Search24)
                        {
                            window.open('https://www.reddit.com/user/' + Search24, 'Search24window');
                        }
                        </script>
                        <form onsubmit="doSearch24(this.Search24.value); return false;">
                            <input type="text" id="Search24" name="Search24" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Reddit"/>
                            <br>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doall(all) {
                            window.open('https://www.google.com/search?q=%22' + all + '%22', 'Search01window');
                            window.open('https://www.bing.com/search?q=%22' + all + '%22', 'Search02window');
                            window.open('https://yandex.com/search/?text="' + all + '"', 'Search03window');
                            window.open('https://knowem.com/checkusernames.php?u=' + all, 'Search04window');
                            window.open('https://knowem.com/checksocialnames.php?u=' + all, 'Search05window');
                            window.open('https://usersearch.org/results_normal.php?URL_username=' + all, 'Search06awindow');
                            window.open('https://usersearch.org/results_advanced.php?URL_username=' + all, 'Search06bwindow');
                            window.open('https://usersearch.org/results_advanced1.php?URL_username=' + all, 'Search06cwindow');
                            window.open('https://usersearch.org/results_advanced2.php?URL_username=' + all, 'Search06dwindow');
                            window.open('https://usersearch.org/results_advanced4.php?URL_username=' + all, 'Search06ewindow');
                            window.open('https://usersearch.org/results_advanced5.php?URL_username=' + all, 'Search06fwindow');
                            window.open('https://usersearch.org/results_advanced6.php?URL_username=' + all, 'Search06gwindow');
                            window.open('https://usersearch.org/results_advanced7.php?URL_username=' + all, 'Search06hwindow');
                            window.open('https://usersearch.org/results_dating.php?URL_username=' + all + '.html', 'Search06iwindow');
                            window.open('https://usersearch.org/results_forums.php?URL_username=' + all, 'Search06jwindow');
                            window.open('https://usersearch.org/results_crypto.php?URL_username=' + all, 'Search06kwindow');
                            window.open('https://namevine.com/#/' + all, 'Search07window');
                            window.open('https://www.social-searcher.com/search-users/?ntw=&q6=' + all, 'Search08window');
                            window.open('https://haveibeenpwned.com/unifiedsearch/' + all, 'Search09window');
                            window.open('https://dehashed.com/search?query="' + all + '"', 'Search10window');
                            window.open('https://linktr.ee/' + all, 'Search11window');
                            window.open('https://psbdmp.ws/api/search/' + all, 'Search12window');
                            window.open('https://en.gravatar.com/' + all, 'Search13window');
                            window.open('https://www.searchmy.bio/search?q=' + all, 'Search14window');
                            window.open('http://twitter.com/' + all, 'Search15window');
                            window.open('https://facebook.com/' + all, 'Search16window');
                            window.open('http://instagram.com/' + all, 'Search17window');
                            window.open('https://www.tiktok.com/@' + all, 'Search18window');
                            window.open('https://tinder.com/@' + all, 'Search19window');
                            window.open('https://' + all + '.tumblr.com', 'Search20window');
                            window.open('https://www.snapchat.com/s/' + all, 'Search21window');
                            window.open('https://medium.com/@' + all, 'Search22window');
                            window.open('http://youtube.com/' + all, 'Search23window');
                            window.open('https://www.reddit.com/user/' + all, 'Search24window');
                        }
                        </script>
                        <form onsubmit="doall(this.all.value); return false;">
                            <input type="text" id="Search90" name="all" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Submit All"/>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doall2(all2) {
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@gmail.com?truncateResponse=true', '1leakwindow');
                            }, 1000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@yahoo.com?truncateResponse=true', '2leakwindow');
                            }, 3000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@hotmail.com?truncateResponse=true', '3leakwindow');
                            }, 6000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@protonmail.com?truncateResponse=true', '4leakwindow');
                            }, 9000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@live.com?truncateResponse=true', '5leakwindow');
                            }, 12000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@outlook.com?truncateResponse=true', '6leakwindow');
                            }, 15000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@icloud.com?truncateResponse=true', '7leakwindow');
                            }, 18000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@yandex.com?truncateResponse=true', '8leakwindow');
                            }, 21000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@gmx.com?truncateResponse=true', '9leakwindow');
                            }, 23000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@mail.com?truncateResponse=true', '10leakwindow');
                            }, 26000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@mac.com?truncateResponse=true', '11leakwindow');
                            }, 29000);
                            setTimeout(function() {
                                window.open('https://haveibeenpwned.com/unifiedsearch/' + all2 + '@me.com?truncateResponse=true', '12leakwindow');
                            }, 32000);
                        }
                        </script>
                        <form onsubmit="doall2(this.all2.value); return false;">
                            <input type="text" name="all2" id="Search91" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="HIBP Emails"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doall3(all3) {
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@gmail.com%22', '1leak3window');
                            }, 1000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@yahoo.com%22', '2leak3window');
                            }, 3000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@hotmail.com%22', '3leak3window');
                            }, 6000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@protonmail.com%22', '4leak3window');
                            }, 9000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@live.com%22', '5leak3window');
                            }, 12000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@outlook.com%22', '6leak3window');
                            }, 15000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@icloud.com%22', '7leak3window');
                            }, 18000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@yandex.com%22', '8leak3window');
                            }, 21000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@gmx.com%22', '9leak3window');
                            }, 23000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@mail.com%22', '10leak3window');
                            }, 26000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@mac.com%22', '11leak3window');
                            }, 29000);
                            setTimeout(function() {
                                window.open('https://dehashed.com/search?query=%22' + all3 + '@me.com%22', '12leak3window');
                            }, 32000);
                        }
                        </script>
                        <form onsubmit="doall3(this.all3.value); return false;">
                            <input type="text" name="all3" id="Search92" size="30" placeholder="Username" value=""/>
                            <input type="submit" style="width:140px" value="Dehashed Emails"/>
                            <br>
                        </form>
                        <script type="text/javascript">
                        function doSearch25(Search25)
                        {
                            window.open('https://www.google.com/search?q=%22' + Search25 + '@gmail.com%22OR%22' + Search25 + '@yahoo.com%22OR%22' + Search25 + '@hotmail.com%22OR%22' + Search25 + '@protonmail.com%22OR%22' + Search25 + '@live.com%22OR%22' + Search25 + '@icloud.com%22OR%22' + Search25 + '@yandex.com%22OR%22' + Search25 + '@gmx.com%22OR%22' + Search25 + '@mail.com%22OR%22' + Search25 + '@mac.com%22OR%22' + Search25 + '@me.com%22', 'Search25window');
                        }
                        </script>
                        <form onsubmit="doSearch25(this.Search25.value); return false;">
                            <input type="text" name="Search25" id="Search25" size="30" placeholder="Username"/>
                            <input type="submit" style="width:140px" value="Email Search"/>
                            <br>
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
    {window.open('https://www.truepeoplesearch.com/results?name=' + Search01a + '%20' + Search01b, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.Search01a.value, this.Search01b.value); return false;">
<input type="text" name="Search01a" id="Search01a" size="12" placeholder="First Name" />
<input type="text" name="Search01b" id="Search01b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="TruePeople" /><br></form>
<script type="text/javascript">
function doSearch02(Search02a, Search02b)
{window.open('https://www.fastpeoplesearch.com/name/' + Search02a + '-' + Search02b, 'Search02window');}
</script>
<form onsubmit="doSearch02(this.Search02a.value, this.Search02b.value); return false;">
<input type="text" name="Search02a" id="Search02a" size="12" placeholder="First Name" />
<input type="text" name="Search02b" id="Search02b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="FastPeople" /><br></form>
<script type="text/javascript">
function doSearch03(Search03a, Search03b)
{window.open('https://nuwber.com/search?name=' + Search03a + '%20' + Search03b, 'Search03window');}
</script>
<form onsubmit="doSearch03(this.Search03a.value, this.Search03b.value); return false;">
<input type="text" name="Search03a" id="Search03a" size="12" placeholder="First Name" />
<input type="text" name="Search03b" id="Search03b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Nuwber" /><br></form>
<script type="text/javascript">
function doSearch04(Search04a, Search04b)
{window.open('https://xlek.com/search_results.php?fname=' + Search04a + '&lname=' + Search04b + '&locations:all', 'Search04window');}
</script>
<form onsubmit="doSearch04(this.Search04a.value, this.Search04b.value); return false;">
<input type="text" name="Search04a" id="Search04a" size="12" placeholder="First Name" />
<input type="text" name="Search04b" id="Search04b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="XLEK" /><br></form>
<script type="text/javascript">
function doSearch05(Search05a, Search05b)
{window.open('https://www.familytreenow.com/search/genealogy/results?first=' + Search05a + '&last=' + Search05b, 'Search05window');}
</script>
<form onsubmit="doSearch05(this.Search05a.value, this.Search05b.value); return false;">
<input type="text" name="Search05a" id="Search05a" size="12" placeholder="First Name" />
<input type="text" name="Search05b" id="Search05b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="FamilyTreeNow" /><br></form>
<script type="text/javascript">
function doSearch06(Search06a, Search06b)
{window.open('https://www.intelius.com/people-search/' + Search06a + '-' + Search06b, 'Search06window');}
</script>
<form onsubmit="doSearch06(this.Search06a.value, this.Search06b.value); return false;">
<input type="text" name="e1" id="Search06a" size="12" placeholder="First Name" />
<input type="text" name="e2" id="Search06b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Intelius" /><br></form>
<script type="text/javascript">
function doSearch07(Search07a, Search07b)
{window.open('https://radaris.com/p/' + Search07a + '/' + Search07b, 'Search07window');}
</script>
<form onsubmit="doSearch07(this.Search07a.value, this.Search07b.value); return false;">
<input type="text" name="Search07a" id="Search07a" size="12" placeholder="First Name" />
<input type="text" name="Search07b" id="Search07b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Radaris" /><br></form>
<script type="text/javascript">
function doSearch08(Search08a, Search08b)
{window.open('https://www.cyberbackgroundchecks.com/people/' + Search08a + '-' + Search08b, 'Search08window');}
</script>
<form onsubmit="doSearch08(this.Search08a.value, this.Search08b.value); return false;">
<input type="text" name="Search08a" id="Search08a" size="12" placeholder="First Name" />
<input type="text" name="Search08b" id="Search08b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="CyberBackground" /><br></form>
<script type="text/javascript">
function doSearch09(Search09a, Search09b)
{window.open('https://www.spytox.com/people/search?name=' + Search09a +'+' + Search09b, 'Search09window');}
</script>
<form onsubmit="doSearch09(this.Search09a.value, this.Search09b.value); return false;">
<input type="text" name="Search09a" id="Search09a" size="12" placeholder="First Name" />
<input type="text" name="Search09b" id="Search09b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Spytox" /><br></form>
<script type="text/javascript">
function doSearch10(Search10a, Search10b)
{window.open('https://www.searchpeoplefree.com/find/' + Search10a + '-' + Search10b, 'Search10window');}
</script>
<form onsubmit="doSearch10(this.Search10a.value, this.Search10b.value); return false;">
<input type="text" name="Search10a" id="Search10a" size="12" placeholder="First Name" />
<input type="text" name="Search10b" id="Search10b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="SearchPeople" /><br></form>
<script type="text/javascript">
function doSearch11(Search11a, Search11b)
{window.open('https://www.spokeo.com/' + Search11a + '-' + Search11b +'?loaded=1', 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11a.value, this.Search11b.value); return false;">
<input type="text" name="Search11a" id="Search11a" size="12" placeholder="First Name" />
<input type="text" name="Search11b" id="Search11b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Spokeo" /><br></form>
<script type="text/javascript">
function doSearch12(Search12a, Search12b)
{window.open('https://www.advancedbackgroundchecks.com/names/' + Search12a + '-' + Search12b, 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12a.value, this.Search12b.value); return false;">
<input type="text" name="Search12a" id="Search12a" size="12" placeholder="First Name" />
<input type="text" name="Search12b" id="Search12b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="AdvBackground" /><br></form>
<script type="text/javascript">
function doSearch13(Search13a, Search13b)
{window.open('http://www.yasni.com/' + Search13a + '+' + Search13b + '/check+people?sh', 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13a.value, this.Search13b.value); return false;">
<input type="text" name="Search13a" id="Search13a" size="12" placeholder="First Name" />
<input type="text" name="Search13b" id="Search13b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Yasni" /><br></form>
<script type="text/javascript">
function doSearch14(Search14a, Search14b)
{window.open('https://www.zabasearch.com/people/' + Search14a + '+' + Search14b, 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14a.value, this.Search14b.value); return false;">
<input type="text" name="Search14a" id="Search14a" size="12" placeholder="First Name" />
<input type="text" name="Search14b" id="Search14b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Zabasearch" /><br></form>
<script type="text/javascript">
function doSearch15(Search15a, Search15b)
{window.open('https://www.peoplesearchnow.com/person/' + Search15a + '-' + Search15b, 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15a.value, this.Search15b.value); return false;">
<input type="text" name="Search15a" id="Search15a" size="12" placeholder="First Name" />
<input type="text" name="Search15b" id="Search15b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="PeopleSearchNow" /><br></form>
<script type="text/javascript">
function doSearch16(Search16a, Search16b)
{window.open('http://webmii.com/people?n=%22' + Search16a + '%20' + Search16b + '%22', 'Search16window');}
</script>
<form onsubmit="doSearch16(this.Search16a.value, this.Search16b.value); return false;">
<input type="text" name="Search16a" id="Search16a" size="12" placeholder="First Name" />
<input type="text" name="Search16b" id="Search16b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="WebMii" /><br></form>
<script type="text/javascript">
function doSearch17(Search17a, Search17b)
{window.open('https://www.social-searcher.com/search-users/?q6=' + Search17a + '+' + Search17b, 'Search17window');}
</script>
<form onsubmit="doSearch17(this.Search17a.value, this.Search17b.value); return false;">
<input type="text" name="Search17a" id="Search17a" size="12" placeholder="First Name" />
<input type="text" name="Search17b" id="Search17b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="SocialSearcher" /><br></form>
<script type="text/javascript">
function doSearch18(Search18a, Search18b)
{window.open('https://www.truthfinder.com/results/?firstName=' + Search18a + '&lastName=' + Search18b + '&state=ALL', 'Search18window');}
</script>
<form onsubmit="doSearch18(this.Search18a.value, this.Search18b.value); return false;">
<input type="text" name="Search18a" id="Search18a" size="12" placeholder="First Name" />
<input type="text" name="Search18b" id="Search18b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="TruthFinder" /><br></form>
<script type="text/javascript">
function doSearch19(Search19a, Search19b)
{window.open('http://www.peoplebyname.com/people/' + Search19b + '/' + Search19a, 'Search19window');}
</script>
<form onsubmit="doSearch19(this.Search19a.value, this.Search19b.value); return false;">
<input type="text" name="Search19a" id="Search19a" size="12" placeholder="First Name" />
<input type="text" name="Search19b" id="Search19b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="PeopleByName" /><br></form>
<script type="text/javascript">
function doSearch20(Search20a, Search20b)
{window.open('https://www.whitepages.com/name/' + Search20a + '-' + Search20b, 'Search20window');}
</script>
<form onsubmit="doSearch20(this.Search20a.value, this.Search20b.value); return false;">
<input type="text" name="Search20a" id="Search20a" size="12" placeholder="First Name" />
<input type="text" name="Search20b" id="Search20b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="White Pages" /><br></form>
<script type="text/javascript">
function doSearch21(Search21a, Search21b)
{window.open('https://thatsthem.com/name/' + Search21a + '-' + Search21b, 'Search21window');}
</script>
<form onsubmit="doSearch21(this.Search21a.value, this.Search21b.value); return false;">
<input type="text" name="Search21a" id="Search21a" size="12" placeholder="First Name" />
<input type="text" name="Search21b" id="Search21b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Thats Them" /><br></form>
<script type="text/javascript">
function doSearch22(Search22a, Search22b)
{window.open('https://clustrmaps.com/persons/' + Search22a + '-' + Search22b, 'Search22window');}
</script>
<form onsubmit="doSearch22(this.Search22a.value, this.Search22b.value); return false;">
<input type="text" name="Search22a" id="Search22a" size="12" placeholder="First Name" />
<input type="text" name="Search22b" id="Search22b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="ClustrMaps" /><br></form>
<script type="text/javascript">
function doSearch23(Search23a, Search23b)
{window.open('http://google.com/search?q=site:rocketreach.co+"' + Search23a + ' ' + Search23b + '"', 'Search23window');}
</script>
<form onsubmit="doSearch23(this.Search23a.value, this.Search23b.value); return false;">
<input type="text" name="Search23a" id="Search23a" size="12" placeholder="First Name" />
<input type="text" name="Search23b" id="Search23b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="RocketReach" /><br></form>
<script type="text/javascript">
function doSearch24(Search24a, Search24b)
{window.open('https://www.officialusa.com/names/' + Search24a + '-' + Search24b, 'Search24window');}
</script>
<form onsubmit="doSearch24(this.Search24a.value, this.Search24b.value); return false;">
<input type="text" name="Search24a" id="Search24a" size="12" placeholder="First Name" />
<input type="text" name="Search24b" id="Search24b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="OfficialUSA" /><br></form>
<script type="text/javascript">
function doSearch25(Search25a, Search25b)
{window.open('https://www.addresses.com/people/' + Search25a + '-' + Search25b, 'Search25window');}
</script>
<form onsubmit="doSearch25(this.Search25a.value, this.Search25b.value); return false;">
<input type="text" name="Search25a" id="Search25a" size="12" placeholder="First Name" />
<input type="text" name="Search25b" id="Search25b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Addresses" /><br></form>
<script type="text/javascript">
function doSearch26(Search26a, Search26b)
{window.open('https://www.classmates.com/siteui/ybsearch/results?q=' + Search26a + ' ' + Search26b, 'Search26window');}
</script>
<form onsubmit="doSearch26(this.Search26a.value, this.Search26b.value); return false;">
<input type="text" name="Search26a" id="Search26a" size="12" placeholder="First Name" />
<input type="text" name="Search26b" id="Search26b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Classmates" /><br></form><br>
<script type="text/javascript">
function doall(all1, all2)
{window.open('https://www.truepeoplesearch.com/results?name=' + all1 + '%20' + all2, 'a1window');
window.open('https://www.fastpeoplesearch.com/name/' + all1 + '-' + all2, 'a2window');
window.open('https://nuwber.com/search?name=' + all1 + '%20' + all2, 'a3window');
window.open('https://cubib.com/search_results.php?fname=' + all1 + '&lname=' + all2 + '&locations:all', 'a4window');
window.open('https://www.familytreenow.com/search/genealogy/results?first=' + all1 + '&last=' + all2, 'a5window');
window.open('https://www.intelius.com/people-search/' + all1 + '-' + all2, 'a6window');
window.open('https://radaris.com/p/' + all1 + '/' + all2, 'a6window');
window.open('https://www.cyberbackgroundchecks.com/people/' + all1 + '-' + all2, 'a7window');
window.open('https://www.spytox.com/people/search?name=' + all1 + '+' + all2, 'a8window');
window.open('https://www.searchpeoplefree.com/find/' + all1 + '-' + all2, 'a9window');
window.open('https://www.spokeo.com/' + all1 + '-' + all2 +'?loaded=1', 'a10window');
window.open('https://www.advancedbackgroundchecks.com/names/' + all1 + '-' + all2, 'a11window');
window.open('http://www.yasni.com/' + all1 + '+' + all2 + '/check+people?sh', 'a12window');
window.open('https://www.zabasearch.com/people/' + all1 + '+' + all2, 'a13window');
window.open('https://www.peoplesearchnow.com/person/' + all1 + '-' + all2, 'a14window');
window.open('http://webmii.com/people?n=%22' + all1 + '%20' + all2 + '%22', 'a15window');
window.open('https://www.social-searcher.com/search-users/?q6=' + all1 + '+' + all2, 'a16window');
window.open('https://www.truthfinder.com/results/?firstName=' + all1 + '&lastName=' + all2 + '&state=ALL', 'a17window');
window.open('http://www.peoplebyname.com/people/' + all2 + '/' + all1, 'a18window');
window.open('https://www.whitepages.com/name/' + all1 + '-' + all2, 'a19window');
window.open('https://thatsthem.com/name/' + all1 + '-' + all2, 'a20window');
window.open('https://clustrmaps.com/persons/' + all1 + '-' + all2, 'a21window');
window.open('http://google.com/search?q=site:rocketreach.co+"' + all1 + ' ' + all2 + '"', 'a22window');
window.open('https://www.officialusa.com/names/' + all1 + '-' + all2, 'a23window');
window.open('https://www.classmates.com/siteui/ybsearch/results?q=' + all1 + ' ' + all2, 'a24window');
window.open('https://www.addresses.com/people/' + all1 + '-' + all2, 'a25window');
}
</script>
<form onsubmit="doall(this.all1.value,this.all2.value); return false;">
<input type="text" name="all1" id="Search99a" size="12" placeholder="First Name" />
<input type="text" name="all2" id="Search99b" size="12" placeholder="Last Name" />
<input type="submit" style="width:140px" value="Submit All" /><br></form>
</p>
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
    <script type="text/javascript">
                        function doSearch01(Search01)
                        {
                            window.open('https://www.google.com/search?q=ext%3Apdf+' + Search01, 'Search01window');
                        }
                        </script>
                        <form onsubmit="doSearch01(this.Search01.value); return false;">
                            <input type="text" id="Search01" name="Search01" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="PDF"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch02(Search02)
                        {
                            window.open('https://www.google.com/search?q=ext%3Adoc+OR+ext%3Adocx+' + Search02, 'Search02window');
                        }
                        </script>
                        <form onsubmit="doSearch02(this.Search02.value); return false;">
                            <input type="text" id="Search02" name="Search02" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="DOC/DOCX"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch03(Search03)
                        {
                            window.open('https://www.google.com/search?q=ext%3Axls+OR+ext%3Axlsx+OR+ext%3Acsv+' + Search03, 'Search03window');
                        }
                        </script>
                        <form onsubmit="doSearch03(this.Search03.value); return false;">
                            <input type="text" id="Search03" name="Search03" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="XLS/XLSX/CSV"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch04(Search04)
                        {
                            window.open('https://www.google.com/search?q=ext%3Appt+OR+ext%3Apptx+OR+ext%3Akey+' + Search04, 'Search04window');
                        }
                        </script>
                        <form onsubmit="doSearch04(this.Search04.value); return false;">
                            <input type="text" id="Search04" name="Search04" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="PPT/PPTX/KEY"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch05(Search05)
                        {
                            window.open('https://www.google.com/search?q=ext%3Atxt+OR+ext%3Artf+OR+ext%3Axml+' + Search05, 'Search05window');
                        }
                        </script>
                        <form onsubmit="doSearch05(this.Search05.value); return false;">
                            <input type="text" id="Search05" name="Search05" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="TXT/RTF/XML"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch06(Search06)
                        {
                            window.open('https://www.google.com/search?q=ext%3Aodt+OR+ext%3Aods+OR+ext%3Aodp+' + Search06, 'Search06window');
                        }
                        </script>
                        <form onsubmit="doSearch06(this.Search06.value); return false;">
                            <input type="text" id="Search06" name="Search06" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="ODT/ODS/ODP"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch07(Search07)
                        {
                            window.open('https://www.google.com/search?q=ext%3Azip+OR+ext%3Arar+OR+ext%3A7z+' + Search07, 'Search07window');
                        }
                        </script>
                        <form onsubmit="doSearch07(this.Search07.value); return false;">
                            <input type="text" id="Search07" name="Search07" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="ZIP/RAR/7Z"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch08(Search08)
                        {
                            window.open('https://www.google.com/search?q=ext%3Ajpg+OR+ext%3Ajpeg+OR+ext%3Apng+' + Search08 + '&tbm=isch', 'Search08window');
                        }
                        </script>
                        <form onsubmit="doSearch08(this.Search08.value); return false;">
                            <input type="text" id="Search08" name="Search08" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="JPG/JPEG/PNG"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch09(Search09)
                        {
                            window.open('https://www.google.com/search?q=ext%3Ampg+OR+ext%3Ampeg+OR+ext%3Amp4+' + Search09, 'Search09window');
                        }
                        </script>
                        <form onsubmit="doSearch09(this.Search09.value); return false;">
                            <input type="text" id="Search09" name="Search09" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="MPG/MP4"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch10(Search10)
                        {
                            window.open('https://www.google.com/search?q=ext%3Amp3+OR+ext%3Awav+OR+ext%3Aflac+' + Search10, 'Search10window');
                        }
                        </script>
                        <form onsubmit="doSearch10(this.Search10.value); return false;">
                            <input type="text" id="Search10" name="Search10" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="MP3/WAV"/>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doall(all)
                        {
                            window.open('https://www.google.com/search?q=ext%3Apdf+' + all, 'Search01window');
                            window.open('https://www.google.com/search?q=ext%3Adoc+OR+ext%3Adocx+' + all, 'Search02window');
                            window.open('https://www.google.com/search?q=ext%3Axls+OR+ext%3Axlsx+OR+ext%3Acsv+' + all, 'Search03window');
                            window.open('https://www.google.com/search?q=ext%3Appt+OR+ext%3Apptx+OR+ext%3Akey+' + all, 'Search04window');
                            window.open('https://www.google.com/search?q=ext%3Atxt+OR+ext%3Artf+OR+ext%3Axml+' + all, 'Search05window');
                            window.open('https://www.google.com/search?q=ext%3Aodt+OR+ext%3Aods+OR+ext%3Aodp+' + all, 'Search06window');
                            window.open('https://www.google.com/search?q=ext%3Azip+OR+ext%3Arar+OR+ext%3A7z+' + all, 'Search07window');
                            window.open('https://www.google.com/search?q=ext%3Ajpg+OR+ext%3Ajpeg+OR+ext%3Apng+' + all + '&tbm=isch', 'Search08window');
                            window.open('https://www.google.com/search?q=ext%3Ampg+OR+ext%3Ampeg+OR+ext%3Amp4+' + all, 'Search09window');
                            window.open('https://www.google.com/search?q=ext%3Amp3+OR+ext%3Awav+OR+ext%3Aflac+' + all, 'Search10window');
                        }
                        </script>
                        <form onSubmit="doall(this.all.value); return false;">
                            <input type="text" id="Search99" name="all" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Submit All"/>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doSearch11(Search11)
                        {
                            window.open('https://www.google.com/search?q=site%3Adocs.google.com+' + Search11, 'Search11window');
                        }
                        </script>
                        <form onsubmit="doSearch11(this.Search11.value); return false;">
                            <input type="text" id="Search11" name="Search11" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Google Docs"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch12(Search12)
                        {
                            window.open('https://www.google.com/search?q=site%3Adrive.google.com+' + Search12, 'Search12window');
                        }
                        </script>
                        <form onsubmit="doSearch12(this.Search12.value); return false;">
                            <input type="text" id="Search12" name="Search12" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Google Drive"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch13(Search13)
                        {
                            window.open('https://www.google.com/search?q=site%3Astorage.googleapis.com+' + Search13, 'Search13window');
                        }
                        </script>
                        <form onsubmit="doSearch13(this.Search13.value); return false;">
                            <input type="text" id="Search13" name="Search13" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Google API"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch14(Search14)
                        {
                            window.open('https://www.google.com/search?q=site%3Adocs.microsoft.com+' + Search14, 'Search14window');
                        }
                        </script>
                        <form onsubmit="doSearch14(this.Search14.value); return false;">
                            <input type="text" id="Search14" name="Search14" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="MS Docs"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch15(Search15)
                        {
                            window.open('https://www.google.com/search?q=site%3Aamazonaws.com+' + Search15, 'Search15window');
                        }
                        </script>
                        <form onsubmit="doSearch15(this.Search15.value); return false;">
                            <input type="text" id="Search15" name="Search15" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Amazon AWS"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch16(Search16)
                        {
                            window.open('https://www.google.com/search?q=site%3Acloudfront.net+' + Search16, 'Search16window');
                        }
                        </script>
                        <form onsubmit="doSearch16(this.Search16.value); return false;">
                            <input type="text" id="Search16" name="Search16" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Cloudfront"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch17(Search17)
                        {
                            window.open('https://buckets.grayhatwarfare.com/results/' + Search17, 'Search17window');
                        }
                        </script>
                        <form onsubmit="doSearch17(this.Search17.value); return false;">
                            <input type="text" id="Search17" name="Search17" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="GrayHatWarfare"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch18(Search18)
                        {
                            window.open('https://www.google.com/search?q=site%3Aslideshare.net+' + Search18, 'Search18window');
                        }
                        </script>
                        <form onsubmit="doSearch18(this.Search18.value); return false;">
                            <input type="text" id="Search18" name="Search18" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="SlideShare"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch19(Search19)
                        {
                            window.open('https://www.google.com/search?q=site%3Aprezi.com+' + Search19, 'Search19window');
                        }
                        </script>
                        <form onsubmit="doSearch19(this.Search19.value); return false;">
                            <input type="text" id="Search19" name="Search19" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Prezi"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch20(Search20)
                        {
                            window.open('https://www.google.com/search?q=site%3Aissuu.com+' + Search20, 'Search20window');
                        }
                        </script>
                        <form onsubmit="doSearch20(this.Search20.value); return false;">
                            <input type="text" id="Search20" name="Search20" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="ISSUU"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch21(Search21)
                        {
                            window.open('https://www.powershow.com/search/presentations/ppt/' + Search21, 'Search21window');
                        }
                        </script>
                        <form onsubmit="doSearch21(this.Search21.value); return false;">
                            <input type="text" id="Search21" name="Search21" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Powershow"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch22(Search22)
                        {
                            window.open('https://www.google.com/search?q=site%3Aslidebean.com+' + Search22, 'Search22window');
                        }
                        </script>
                        <form onsubmit="doSearch22(this.Search22.value); return false;">
                            <input type="text" id="Search22" name="Search22" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Slide Bean"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch23(Search23)
                        {
                            window.open('https://www.google.com/search?q=site%3Aauthorstream.com+' + Search23, 'Search23window');
                        }
                        </script>
                        <form onsubmit="doSearch23(this.Search23.value); return false;">
                            <input type="text" id="Search23" name="Search23" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Author Stream"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch24(Search24)
                        {
                            window.open('https://www.google.com/search?q=site%3Ascribd.com+' + Search24, 'Search24window');
                        }
                        </script>
                        <form onsubmit="doSearch24(this.Search24.value); return false;">
                            <input type="text" id="Search24" name="Search24" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Scribd"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch25(Search25)
                        {
                            window.open('https://www.pdfdrive.net/search?q=' + Search25, 'Search25window');
                        }
                        </script>
                        <form onsubmit="doSearch25(this.Search25.value); return false;">
                            <input type="text" id="Search25" name="Search25" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="PDF Drive"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch26(Search26)
                        {
                            window.open('https://search.wikileaks.org/?query=' + Search26 + '&exact_phrase=&any_of=&exclude_words=&document_date_start=&document_date_end=&released_date_start=&released_date_end=&new_search=True&order_by=most_relevant#results', 'Search26window');
                        }
                        </script>
                        <form onsubmit="doSearch26(this.Search26.value); return false;">
                            <input type="text" id="Search26" name="Search26" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Wikileaks"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch27(Search27)
                        {
                            window.open('https://archive.org/search.php?query=' + Search27 + '&sin=TXT', 'Search27window');
                        }
                        </script>
                        <form onsubmit="doSearch27(this.Search27.value); return false;">
                            <input type="text" id="Search27" name="Search27" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Archive.org"/>
                        </form>
                        <script type="text/javascript">
                        function doSearch28(Search28)
                        {
                            window.open('https://www.google.com/search?tbm=bks&q=' + Search28, 'Search28window');
                        }
                        </script>
                        <form onsubmit="doSearch28(this.Search28.value); return false;">
                            <input type="text" id="Search28" name="Search28" size="30" placeholder="Search Terms"/>
                            <input type="submit" style="width:140px" value="Google Books"/>
                        </form>
                        <br>
                        <script type="text/javascript">
                        function doSearch30(Search30)
                        {
                            window.open('https://www.google.com/search?q=site%3Adocs.google.com+' + Search30, 'Search01window');
                            window.open('https://www.google.com/search?q=site%3Adrive.google.com+' + Search30, 'Search02window');
                            window.open('https://www.google.com/search?q=site%3Astorage.googleapis.com+' + Search30, 'Search03awindow');
                            window.open('https://www.google.com/search?q=site%3Adocs.microsoft.com+' + Search30, 'Search04window');
                            window.open('https://www.google.com/search?q=site%3As3.amazonaws.com+' + Search30, 'Search05window');
                            window.open('https://www.google.com/search?q=site%3Acloudfront.net+' + Search30, 'Search06window');
                            window.open('https://buckets.grayhatwarfare.com/results/' + Search30, 'Search07window');
                            window.open('https://www.google.com/search?q=site%3Aslideshare.net+' + Search30, 'Search08window');
                            window.open('https://www.google.com/search?q=site%3Aprezi.com+' + Search30, 'Search09window');
                            window.open('https://www.google.com/search?q=site%3Aissuu.com+' + Search30, 'Search10window');
                            window.open('https://www.powershow.com/search/presentations/ppt/' + Search30, 'Search11window');
                            window.open('https://www.google.com/search?q=site%3Aslidebean.com+' + Search30, 'Search12window');
                            window.open('https://www.google.com/search?q=site%3Aauthorstream.com+' + Search30, 'Search13window');
                            window.open('https://www.google.com/search?q=site%3Ascribd.com+' + Search30, 'Search14window');
                            window.open('https://www.pdfdrive.net/search?q=' + Search30, 'Search15window');
                            window.open('https://search.wikileaks.org/?query=' + Search30 + '&exact_phrase=&any_of=&exclude_words=&document_date_start=&document_date_end=&released_date_start=&released_date_end=&new_search=True&order_by=most_relevant#results', 'Search16window');
                            window.open('https://archive.org/search.php?query=' + Search30 + '&sin=TXT', 'Search17window');
                            window.open('https://www.google.com/search?tbm=bks&q=' + Search30, 'Search18window');
                        }
                        </script>
                        <form onSubmit="doSearch30(this.Search30.value); return false;">
                            <input type="text" id="Search30" name="Search30" size="30" placeholder="Search Terms"/>
    """
    Docdict = {
        
    }
    return Docdict

# TODO: Pastes tool: https://inteltechniques.com/tools/Pastes.html
# Not doing right now
#def paste_query(query: str) -> dict:
#    """
#    """
#    Pastedict = {
#        
#    }
#    return Pastedict

# TODO: Images tool: https://inteltechniques.com/tools/Images.html

def img_query(query: str) -> dict:
    """
    <script type="text/javascript">
function doSearch01(Search01)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=' + Search01, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.Search01.value); return false;">
<input type="text" name="Search01" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="Google" /><br></form>
<script type="text/javascript">
function doSearch02(Search02)
{window.open('https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:' + Search02, 'Search02window');}
</script>
<form onsubmit="doSearch02(this.Search02.value); return false;">
<input type="text" name="Search02" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="Bing" /><br></form>
<script type="text/javascript">
function doSearch03(Search03)
{window.open('http://www.tineye.com/search/?url=' + Search03, 'Search03window');}
</script>
<form onsubmit="doSearch03(this.Search03.value); return false;">
<input type="text" name="Search03" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="TinEye" /><br></form>
<script type="text/javascript">
function doSearch04(Search04)
{window.open('https://yandex.com/images/search?rpt=imageview&url=' + Search04, 'Search04window');}
</script>
<form onsubmit="doSearch04(this.Search04.value); return false;">
<input type="text" name="Search04" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="Yandex" /><br></form>
<script type="text/javascript">
function doSearch05(Search05)
{window.open('https://graph.baidu.com/upload?image=' + Search05, 'Search05window');}
</script>
<form onsubmit="doSearch05(this.Search05.value); return false;">
<input type="text" name="Search05" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="Baidu" /><br></form>
<script type="text/javascript">
function doSearch06(Search06)
{window.open('https://karmadecay.com/search?q=' + Search06, 'Search06window');}
</script>
<form onsubmit="doSearch06(this.Search06.value); return false;">
<input type="text" name="Search06" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="KarmaDecay" /><br></form><br>
<script type="text/javascript">
function doimage(image)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=' + image, 'image1window');
window.open('https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:' + image, 'image2window');
window.open('http://www.tineye.com/search/?url=' + image, 'image3window');
window.open('https://yandex.com/images/search?rpt=imageview&url=' + image, 'image4window');
window.open('https://graph.baidu.com/upload?image=' + image, 'image5window');
window.open('https://karmadecay.com/search?q=' + image, 'image6window');}
</script>
<form onsubmit="doimage(this.image.value); return false;">
<input type="text" name="image" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="Submit All" /><br><br></form>
Images Search:
<script type="text/javascript">
function doPopAll(PopAll)
{var pop = document.getElementById("PopAll");
for (j = 1; j <= 100; j++){
if (j < 10){
j = "0" + j.toString();}
else {j = j.toString();}
console.log(j)
item = document.getElementById("Search" + j);
if (item != null){
item.value = pop.value;}}}
</script>
<form onsubmit="doPopAll(this.PopAll.value); return false;">
<input type="text" id="PopAll" name="PopAll" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Populate All" /><br></form><br>
<script type="text/javascript">
function doSearch07(Search07)
{window.open('https://www.google.com/search?q=' + Search07 + '&tbm=isch', 'Search07window');}
</script>
<form onsubmit="doSearch07(this.Search07.value); return false;">
<input type="text" id="Search07" name="Search07" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Google Images" /><br></form>
<script type="text/javascript">
function doSearch08(Search08)
{window.open('https://www.bing.com/images/search?q=' + Search08, 'Search08window');}
</script>
<form onsubmit="doSearch08(this.Search08.value); return false;">
<input type="text" id="Search08" name="Search08" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Bing Images" /><br></form>
<script type="text/javascript">
function doSearch09(Search09)
{window.open('https://yandex.com/images/search?text=' + Search09, 'Search09window');}
</script>
<form onsubmit="doSearch09(this.Search09.value); return false;">
<input type="text" id="Search09" name="Search09" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Yandex Images" /><br></form>
<script type="text/javascript">
function doSearch10(Search10)
{window.open('https://twitter.com/search?q=' + Search10 + '&f=image', 'Search10window');}
</script>
<form onsubmit="doSearch10(this.Search10.value); return false;">
<input type="text" id="Search10" name="Search10" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Twitter Images" /><br></form>
<script type="text/javascript">
function doSearch11(Search11)
{window.open('https://www.facebook.com/search/photos/?q=' + Search11, 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11.value); return false;">
<input type="text" id="Search11" name="Search11" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Facebook Images" /><br></form>
<script type="text/javascript">
function doSearch12(Search12)
{window.open('https://www.google.com/search?tbm=isch&q=site%3Ainstagram.com+' + Search12, 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12.value); return false;">
<input type="text" id="Search12" name="Search12" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="Instagram Images" /><br></form>
<script type="text/javascript">
function doSearch13(Search13)
{window.open('https://www.google.com/search?tbm=isch&q=site%3Alinkedin.com+' + Search13, 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13.value); return false;">
<input type="text" id="Search13" name="Search13" size="30" placeholder="Search Terms" value="" />
<input type="submit" style="width:140px" value="LinkedIn Images" /><br></form>
<script type="text/javascript">
function doSearch14(Search14)
{window.open('https://www.flickr.com/search/?text=' + Search14, 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14.value); return false;">
<input type="text" id="Search14" name="Search14" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Flickr Images" /><br></form>
<script type="text/javascript">
function doSearch15(Search15)
{window.open('https://www.tumblr.com/search/' + Search15, 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15.value); return false;">
<input type="text" id="Search15" name="Search15" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Tumblr Images" /><br></form><br>
<script type="text/javascript">
function doSearch16(Search16)
{window.open('https://www.google.com/search?q=' + Search16 + '&tbm=isch', 'image1window');
window.open('https://www.bing.com/images/search?q=' + Search16, 'image2window');
window.open('https://yandex.com/images/search?text=' + Search16, 'image3window');
window.open('https://twitter.com/search?f=image&q=' + Search16, 'image4window');
window.open('https://www.facebook.com/search/photos/?q=' + Search16, 'image5window');
window.open('https://www.google.com/search?tbm=isch&q=site%3Ainstagram.com+' + Search16, 'image6window');
window.open('https://www.google.com/search?tbm=isch&q=site%3Alinkedin.com+' + Search16, 'image7window');
window.open('https://www.flickr.com/search/?text=' + Search16, 'image8window');
window.open('https://www.tumblr.com/search/' + Search16, 'Search9window');}
</script>
<form onsubmit="doSearch16(this.Search16.value); return false;">
<input type="text" id="Search16" name="Search16" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Submit All" /><br><br></form>
Flickr API:
<script type="text/javascript">
function doflemail(flemail)
{window.open('https://api.flickr.com/services/rest/?method=flickr.people.findByEmail&api_key=27c196593dad58382fc4912b00cf1194&find_email=' + flemail, 'flickremailwindow');}
</script>
<form onSubmit="doflemail(this.flemail.value); return false;">
<input name="flemail" size="30" placeholder="Email Address" type="text" />
<input type="submit" style="width:140px" value="Email Search" /></form>
<script type="text/javascript">
function dofluser(fluser)
{window.open('https://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key=27c196593dad58382fc4912b00cf1194&username=' + fluser, 'flickruserwindow');}
</script>
<form onSubmit="dofluser(this.fluser.value); return false;">
<input name="fluser" size="30" placeholder="Username" type="text" />
<input type="submit" style="width:140px" value="Username Search" /></form>
<script type="text/javascript">
function doflnumber(flnumber)
{window.open('https://api.flickr.com/services/rest/?method=flickr.people.getInfo&api_key=27c196593dad58382fc4912b00cf1194&user_id=' + flnumber + '&format=rest', 'flickrnumberwindow');}
</script>
    """
    Imgdict = {
        
    }
    return Imgdict

# TODO: Videos tool: https://inteltechniques.com/tools/Videos.html

def vid_query(query: str) -> dict:
    """
    <script type="text/javascript">
function doSearch01(Search01)
{window.open('https://keepvid.works/?url=https://www.youtube.com/watch/v=' + Search01, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.Search01.value); return false;">
<input type="text" id="Search01" name="Search01" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Age Bypass" /><br></form>
<script type="text/javascript">
function doSearch02(Search02)
{window.open('https://www.youtube.com/embed/' + Search02, 'Search02window');}
</script>
<form onsubmit="doSearch02(this.Search02.value); return false;">
<input type="text" id="Search02" name="Search02" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Full Screen" /><br></form>
<script type="text/javascript">
function doSearch03(Search03)
{window.open('https://i.ytimg.com/vi/' + Search03 + '/maxresdefault.jpg', 'Search03window');}
</script>
<form onsubmit="doSearch03(this.Search03.value); return false;">
<input type="text" id="Search03" name="Search03" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Thumbnail HQ" /><br></form>
<script type="text/javascript">
function doSearch04(Search04)
{window.open('https://img.youtube.com/vi/' + Search04 + '/1.jpg', 'Search04window');}
</script>
<form onsubmit="doSearch04(this.Search04.value); return false;">
<input type="text" id="Search04" name="Search04" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Thumbnail 2" /><br></form>
<script type="text/javascript">
function doSearch05(Search05)
{window.open('https://img.youtube.com/vi/' + Search05 + '/2.jpg', 'Search05window');}
</script>
<form onsubmit="doSearch05(this.Search05.value); return false;">
<input type="text" id="Search05" name="Search05" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Thumbnail 3" /><br></form>
<script type="text/javascript">
function doSearch06(Search06)
{window.open('https://img.youtube.com/vi/' + Search06 + '/3.jpg', 'Search06window');}
</script>
<form onsubmit="doSearch06(this.Search06.value); return false;">
<input type="text" id="Search06" name="Search06" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Thumbnail 4" /><br></form>
<script type="text/javascript">
function doSearch07(Search07)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=https://i.ytimg.com/vi/' + Search07 + '/maxresdefault.jpg', 'Search07window');}
</script>
<form onsubmit="doSearch07(this.Search07.value); return false;">
<input type="text" id="Search07" name="Search07" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Google Reverse" /><br></form>
<script type="text/javascript">
function doSearch08(Search08)
{window.open('https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:https://i.ytimg.com/vi/' + Search08 + '/maxresdefault.jpg', 'Search08window');}
</script>
<form onsubmit="doSearch08(this.Search08.value); return false;">
<input type="text" id="Search08" name="Search08" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Bing Reverse" /><br></form>
<script type="text/javascript">
function doSearch09(Search09)
{window.open('https://yandex.com/images/search?rpt=imageview&url=https://i.ytimg.com/vi/' + Search09 + '/maxresdefault.jpg', 'Search09window');}
</script>
<form onsubmit="doSearch09(this.Search09.value); return false;">
<input type="text" id="Search09" name="Search09" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Yandex Reverse" /><br></form>
<script type="text/javascript">
function doSearch10(Search10)
{window.open('http://www.tineye.com/search/?url=https://i.ytimg.com/vi/' + Search10 + '/maxresdefault.jpg', 'Search10window');}
</script>
<form onsubmit="doSearch10(this.Search10.value); return false;">
<input type="text" id="Search10" name="Search10" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="TinEye Reverse" /><br></form>
<script type="text/javascript">
function doSearch11(Search11)
{window.open('http://polsy.org.uk/stuff/ytrestrict.cgi?ytid=' + Search11, 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11.value); return false;">
<input type="text" id="Search11" name="Search11" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Restrictions I" /><br></form>
<script type="text/javascript">
function doSearch12(Search12)
{window.open('https://watannetwork.com/tools/blocked/#url=' + Search12, 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12.value); return false;">
<input type="text" id="Search12" name="Search12" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Restrictions II" /><br></form>
<script type="text/javascript">
function doSearch13(Search13)
{window.open('https://www.googleapis.com/youtube/v3/videos?id=' + Search13 + '&part=snippet,statistics,recordingDetails&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw', 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13.value); return false;">
<input type="text" id="Search13" name="Search13" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Metadata" /><br></form>
<script type="text/javascript">
function doSearch14(Search14)
{window.open('http://www.pwnyoutube.com/watch?v=' + Search14, 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14.value); return false;">
<input type="text" id="Search14" name="Search14" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Download" /><br></form>
<script type="text/javascript">
function doSearch15(Search15)
{window.open('https://web.archive.org/web/https://www.youtube.com/watch?v=' + Search15, 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15.value); return false;">
<input type="text" id="Search15" name="Search15" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="Archives" /><br></form><br>
<script type="text/javascript">
function doSearch16(Search16)
{window.open('https://www.google.com/search?tbm=vid&q=' + Search16, 'Search16window');}
</script>
<form onsubmit="doSearch16(this.Search16.value); return false;">
<input type="text" name="Search16" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Google Videos" /><br></form>
<script type="text/javascript">
function doSearch17(Search17)
{window.open('https://www.bing.com/videos/search?q=' + Search17, 'Search17window');}
</script>
<form onsubmit="doSearch17(this.Search17.value); return false;">
<input type="text" name="Search17" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Bing Videos" /><br></form>
<script type="text/javascript">
function doSearch18(Search18)
{window.open('https://yandex.ru/video/search?text=' + Search18 + '&rpt=imageview', 'Search18window');}
</script>
<form onsubmit="doSearch18(this.Search18.value); return false;">
<input type="text" name="Search18" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Yandex Videos" /><br></form>
<script type="text/javascript">
function doSearch19(Search19)
{window.open('https://www.youtube.com/results?search_query=' + Search19, 'Search19window');}
</script>
<form onsubmit="doSearch19(this.Search19.value); return false;">
<input type="text" name="Search19" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="YouTube Videos" /><br></form>
<script type="text/javascript">
function doSearch20(Search20)
{window.open('https://twitter.com/search?q=' + Search20 + '&f=video', 'Search20window');}
</script>
<form onsubmit="doSearch20(this.Search20.value); return false;">
<input type="text" name="Search20" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Twitter Videos" /><br></form>
<script type="text/javascript">
function doSearch21(Search21)
{window.open('https://www.facebook.com/search/videos/?q=' + Search21, 'Search21window');}
</script>
<form onsubmit="doSearch21(this.Search21.value); return false;">
<input type="text" name="Search21" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Facebook Videos" /><br></form>
<script type="text/javascript">
function doSearch22(Search22)
{window.open('https://www.reddit.com/search?q=site:v.redd.it%20AND%20' + Search22, 'Search22window');}
</script>
<form onsubmit="doSearch22(this.Search22.value); return false;">
<input type="text" name="Search22" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Reddit Videos" /><br></form>
<script type="text/javascript">
function doSearch23(Search23)
{window.open('https://www.tiktok.com/tag/' + Search23, 'Search23window');}
</script>
<form onsubmit="doSearch23(this.Search23.value); return false;">
<input type="text" name="Search23" size="30" placeholder="Hashtag" />
<input type="submit" style="width:140px" value="TikTok Videos" /><br></form>
<script type="text/javascript">
function doSearch24(Search24)
{window.open('https://www.peteyvid.com/index.php?q=' + Search24, 'Search24window');}
</script>
<form onsubmit="doSearch24(this.Search24.value); return false;">
<input type="text" name="Search24" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="PeteyVid" /><br></form>
<script type="text/javascript">
function doSearch25(Search25)
{window.open('https://archive.org/details/movies?and[]=' + Search25, 'Search25window');}
</script>
<form onsubmit="doSearch25(this.Search25.value); return false;">
<input type="text" name="Search25" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Archives I" /><br></form>
<script type="text/javascript">
function doSearch26(Search26)
{window.open('https://archive.org/details/opensource_movies?and%5B%5D=' + Search26, 'Search26window');}
</script>
<form onsubmit="doSearch26(this.Search26.value); return false;">
<input type="text" name="Search26" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="Archives II" /><br></form>
<script type="text/javascript">
function doSearch27(Search27)
{window.open('https://archive.org/details/tv?q=' + Search27, 'Search27window');}
</script>
<form onsubmit="doSearch27(this.Search27.value); return false;">
<input type="text" name="Search27" size="30" placeholder="Search Terms" />
<input type="submit" style="width:140px" value="TV Archives" /><br></form><br>
<script type="text/javascript">
function doSearch28(Search28)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/0.jpg', 'rev13window');
window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/1.jpg', 'rev14window');
window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/2.jpg', 'rev15window');
window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=http://i.ytimg.com/vi/' + Search28 + '/3.jpg', 'rev16window');
window.open('http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/0.jpg', 'revt5window');
window.open('http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/1.jpg', 'revt6window');
window.open('http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/2.jpg', 'revt7window');
window.open('http://www.tineye.com/search/?url=http://i.ytimg.com/vi/' + Search28 + '/3.jpg', 'revt8window');
window.open('https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/0.jpg&rpt=imageview', 'rev17window');
window.open('https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/1.jpg&rpt=imageview', 'rev18window');
window.open('https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/2.jpg&rpt=imageview', 'rev19window');
window.open('https://yandex.com/images/search?source=collections&&url=http://i.ytimg.com/vi/' + Search28 + '/3.jpg&rpt=imageview', 'rev20window');
window.open('http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/0.jpg', 'rev21window');
window.open('http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/1.jpg', 'rev22window');
window.open('http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/2.jpg', 'rev23window');
window.open('http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=http://i.ytimg.com/vi/' + Search28 + '/3.jpg', 'rev24window');}
</script>
<form onsubmit="doSearch28(this.Search28.value); return false;">
<input type="text" id="Search28" name="Search28" size="30" placeholder="YouTube Video ID" />
<input type="submit" style="width:140px" value="YouTube Reverse" /><br></form>
<script type="text/javascript">
function doSearch29(Search29)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=https://i.vimeocdn.com/video/' + Search29, 'rev1window');
window.open('http://www.tineye.com/search/?url=https://i.vimeocdn.com/video/' + Search29, 'revt1window');
window.open('https://www.yandex.com/images/search?img_url=https://i.vimeocdn.com/video/' + Search29, 'rev5window');
window.open('http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=https://i.vimeocdn.com/video/' + Search29, 'rev9window');}
</script>
<form onsubmit="doSearch29(this.Search29.value); return false;">
<input type="text" id="Search29" name="Search29" size="30" placeholder="Vimeo Image URL" />
<input type="submit" style="width:140px" value="Vimeo Reverse" /><br></form>
<script type="text/javascript">
function doSearch30(Search30)
{window.open('https://www.google.com/searchbyimage?site=search&sa=X&image_url=' + Search30, 'image1window');
window.open('http://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=' + Search30, 'image4window');
window.open('http://www.tineye.com/search/?url=' + Search30, 'image2window');
window.open('https://yandex.com/images/search?url=' + Search30 + '&rpt=imageview', 'image3window');
window.open('https://image.baidu.com/pcdutu?queryImageUrl=' + Search30, 'image5window');}
</script>
<form onsubmit="doSearch30(this.Search30.value); return false;">
<input type="text" name="Search30" size="30" placeholder="Entire Image URL" />
<input type="submit" style="width:140px" value="General Reverse" /><br><br></form>
<script type="text/javascript">
function doSearch31(Search31)
{window.open('https://www.youtube.com/user/' + Search31, 'Search31window');}
</script>
<form onsubmit="doSearch31(this.Search31.value); return false;">
<input type="text" name="Search31" size="30" placeholder="YouTube Username" />
<input type="submit" style="width:140px" value="Profile" /><br></form>
<script type="text/javascript">
function doSearch32(Search32)
{window.open('https://www.youtube.com/feeds/videos.xml?user=' + Search32, 'Search32window');}
</script>
<form onsubmit="doSearch32(this.Search32.value); return false;">
<input type="text" name="Search32" size="30" placeholder="YouTube Username" />
<input type="submit" style="width:140px" value="Account" /><br></form>
<script type="text/javascript">
function doSearch33(Search33)
{window.open('https://youtube.googleapis.com/youtube/v3/channels?part=snippet&id=' + Search33 + '&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw', 'Search33window');}
</script>
<form onsubmit="doSearch33(this.Search33.value); return false;">
<input type="text" name="Search33" size="30" placeholder="YouTube Channel ID" />
<input type="submit" style="width:140px" value="Metadata" /><br></form>
<script type="text/javascript">
function doSearch34(Search34,term)
{window.open('https://www.googleapis.com/youtube/v3/commentThreads?part=id,snippet&videoId=' + Search34 + '&pageToken=&order=Relevance&maxResults=100&searchTerms=' + term + '&textFormat=plainText&key=AIzaSyDNALbuV1FZSRy6JpafwUaV_taSVV12wZw', 'Search34window');}
</script>
<form onsubmit="doSearch34(this.Search34.value,this.term.value); return false;">
<input type="text" name="Search34" size="17" placeholder="YouTube Video ID" />
<input type="text" name="term" size="10" placeholder="Search Term" />
<input type="submit" style="width:140px" value="Comments" /><br></form>
    """
    Vidict = {
        
    }
    return Vidict

# TODO: Domains tool: https://inteltechniques.com/tools/Domain.html

def domain_query(query: str) -> dict:
    """
    function doSearch01(Search01)
{window.open('http://viewdns.info/whois/?domain=' + Search01, 'Search01window');}
</script>
<form onsubmit="doSearch01(this.Search01.value); return false;">
<input type="text" id="Search01" name="Search01" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whois" /><br></form>
<script type="text/javascript">
function doSearch02(Search02)
{window.open('http://viewdns.info/reverseip/?host=' + Search02 + '&t=1', 'Search02window');}
</script>
<form onsubmit="doSearch02(this.Search02.value); return false;">
<input type="text" id="Search02" name="Search02" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Reverse IP" /><br></form>
<script type="text/javascript">
function doSearch03(Search03)
{window.open('http://viewdns.info/reversewhois/?q=' + Search03 + '&t=1', 'Search03window');}
</script>
<form onsubmit="doSearch03(this.Search03.value); return false;">
<input type="text" id="Search03" name="Search03" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Reverse Domain" /><br></form>
<script type="text/javascript">
function doSearch04(Search04)
{window.open('http://viewdns.info/portscan/?host=' + Search04, 'Search04window');}
</script>
<form onsubmit="doSearch04(this.Search04.value); return false;">
<input type="text" id="Search04" name="Search04" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Port Scan" /><br></form>
<script type="text/javascript">
function doSearch05(Search05)
{window.open('http://viewdns.info/iphistory/?domain=' + Search05, 'Search05window');}
</script>
<form onsubmit="doSearch05(this.Search05.value); return false;">
<input type="text" id="Search05" name="Search05" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="IP History" /><br></form>
<script type="text/javascript">
function doSearch06(Search06)
{window.open('http://viewdns.info/dnsreport/?domain=' + Search06, 'Search06window');}
</script>
<form onsubmit="doSearch06(this.Search06.value); return false;">
<input type="text" id="Search06" name="Search06" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="DNS Report" /><br></form>
<script type="text/javascript">
function doSearch07(Search07)
{window.open('http://viewdns.info/traceroute/?domain=' + Search07, 'Search07window');}
</script>
<form onsubmit="doSearch07(this.Search07.value); return false;">
<input type="text" id="Search07" name="Search07" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="TraceRoute" /><br></form>
<script type="text/javascript">
function doSearch08(Search08)
{window.open('http://who.is/whois/' + Search08, 'Search08window');}
</script>
<form onsubmit="doSearch08(this.Search08.value); return false;">
<input type="text" id="Search08" name="Search08" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Who.Is" /><br></form>
<script type="text/javascript">
function doSearch09(Search09)
{window.open('http://who.is/dns/' + Search09, 'Search09window');}
</script>
<form onsubmit="doSearch09(this.Search09.value); return false;">
<input type="text" id="Search09" name="Search09" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Who.Is DNS" /><br></form>
<script type="text/javascript">
function doSearch10(Search10)
{window.open('http://who.is/domain-history/' + Search10, 'Search10window');}
</script>
<form onsubmit="doSearch10(this.Search10.value); return false;">
<input type="text" id="Search10" name="Search10" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Who.Is History" /><br></form>
<script type="text/javascript">
function doSearch11(Search11)
{window.open('https://dmns.app/domains?q=' + Search11, 'Search11window');}
</script>
<form onsubmit="doSearch11(this.Search11.value); return false;">
<input type="text" id="Search11" name="Search11" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="DomainApp DNS" /><br></form><br>
<script type="text/javascript">
function doSearch12(Search12)
{window.open('https://www.whoxy.com/' + Search12, 'Search12window');}
</script>
<form onsubmit="doSearch12(this.Search12.value); return false;">
<input type="text" id="Search12" name="Search12" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whoxy" /><br></form>
<script type="text/javascript">
function doSearch13(Search13)
{window.open('https://whoisology.com/' + Search13, 'Search13window');}
</script>
<form onsubmit="doSearch13(this.Search13.value); return false;">
<input type="text" id="Search13" name="Search13" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whoisology" /><br></form>
<script type="text/javascript">
function doSearch15(Search15)
{window.open('https://web.archive.org/web/http://www.who.is/whois/' + Search15, 'Search15window');}
</script>
<form onsubmit="doSearch15(this.Search15.value); return false;">
<input type="text" id="Search15" name="Search15" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whois Archive 1" /><br></form>
<script type="text/javascript">
function doSearch16(Search16)
{window.open('https://web.archive.org/web/https://whois.domaintools.com/' + Search16, 'Search16window');}
</script>
<form onsubmit="doSearch16(this.Search16.value); return false;">
<input type="text" id="Search16" name="Search16" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whois Archive 2" /><br></form>
<script type="text/javascript">
function doSearch17(Search17)
{window.open('https://web.archive.org/web/https://www.whoxy.com/' + Search17, 'Search17window');}
</script>
<form onsubmit="doSearch17(this.Search17.value); return false;">
<input type="text" id="Search17" name="Search17" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whois Archive 3" /><br></form>
<script type="text/javascript">
function doSearch18(Search18)
{window.open('https://web.archive.org/web/https://domainbigdata.com/' + Search18, 'Search18window');}
</script>
<form onsubmit="doSearch18(this.Search18.value); return false;">
<input type="text" id="Search18" name="Search18" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whois Archive 4" /><br></form>
<script type="text/javascript">
function doSearch19(Search19)
{window.open('https://web.archive.org/web/https://whoisology.com/' + Search19, 'Search19window');}
</script>
<form onsubmit="doSearch19(this.Search19.value); return false;">
<input type="text" id="Search19" name="Search19" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Whois Archive 5" /><br></form><br>
<script type="text/javascript">
function doSearch20(Search20)
{window.open('http://web.archive.org/web/*/' + Search20, 'Search20window');}
</script>
<form onsubmit="doSearch20(this.Search20.value); return false;">
<input type="text" id="Search20" name="Search20" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Archive.org" /><br></form>
<script type="text/javascript">
function doSearch21(Search21)
{window.open('http://archive.md/' + Search21, 'Search21window');}
</script>
<form onsubmit="doSearch21(this.Search21.value); return false;">
<input type="text" id="Search21" name="Search21" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Archive.md" /><br></form>
<script type="text/javascript">
function doSearch22(Search22)
{window.open('http://timetravel.mementoweb.org/list/19991212110000/http://' + Search22, 'Search22window');}
</script>
<form onsubmit="doSearch22(this.Search22.value); return false;">
<input type="text" id="Search22" name="Search22" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Mementoweb" /><br></form>
<script type="text/javascript">
function doSearch23(Search23)
{window.open('https://webarchive.loc.gov/all/*/http://' + Search23, 'Search23window');}
</script>
<form onsubmit="doSearch23(this.Search23.value); return false;">
<input type="text" id="Search23" name="Search23" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Congress" /><br></form>
<script type="text/javascript">
function doSearch24(Search24)
{window.open('https://arquivo.pt/page/search?hitsPerPage=100&query=site%3A' + Search24, 'Search24window');}
</script>
<form onsubmit="doSearch24(this.Search24.value); return false;">
<input type="text" id="Search24" name="Search24" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Arquivo" /><br></form>
<script type="text/javascript">
function doSearch25(Search25)
{window.open('http://carbondate.cs.odu.edu/#' + Search25, 'Search25window');}
</script>
<form onsubmit="doSearch25(this.Search25.value); return false;">
<input type="text" id="Search25" name="Search25" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="CarbonDating" /><br></form><br>
<script type="text/javascript">
function doSearch26(Search26)
{window.open('http://google.com/search?q=site%3A' + Search26, 'Search26window');}
</script>
<form onsubmit="doSearch26(this.Search26.value); return false;">
<input type="text" id="Search26" name="Search26" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Google Site" /><br></form>
<script type="text/javascript">
function doSearch27(Search27)
{window.open('http://webcache.googleusercontent.com/search?q=cache:' + Search27, 'Search27window');}
</script>
<form onsubmit="doSearch27(this.Search27.value); return false;">
<input type="text" id="Search27" name="Search27" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Google Cache" /><br></form>
<script type="text/javascript">
function doSearch28(Search28)
{window.open('https://website.informer.com/' + Search28 + '#tab_stats', 'Search28window');}
</script>
<form onsubmit="doSearch28(this.Search28.value); return false;">
<input type="text" id="Search28" name="Search28" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Screenshot 1" /><br></form>
<script type="text/javascript">
function doSearch29(Search29)
{window.open('https://urlscan.io/domain/' + Search29, 'Search29window');}
</script>
<form onsubmit="doSearch29(this.Search29.value); return false;">
<input type="text" id="Search29" name="Search29" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Screenshot 2" /><br></form>
<script type="text/javascript">
function doSearch30(Search30)
{window.open('https://www.easycounter.com/report/' + Search30, 'Search30window');}
</script>
<form onsubmit="doSearch30(this.Search30.value); return false;">
<input type="text" id="Search30" name="Search30" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Screenshot 3" /><br></form>
<script type="text/javascript">
function doSearch31(Search31)
{window.open('https://whois.domaintools.com/' + Search31, 'Search31window');}
</script>
<form onsubmit="doSearch31(this.Search31.value); return false;">
<input type="text" id="Search31" name="Search31" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Screenshot 4" /><br></form>
<script type="text/javascript">
function doSearch32(Search32)
{window.open('https://www.domainiq.com/snapshot_history#' + Search32, 'Search32window');}
</script>
<form onsubmit="doSearch32(this.Search32.value); return false;">
<input type="text" id="Search32" name="Search32" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Screenshot 5" /><br></form>
<script type="text/javascript">
function doSearch33(Search33)
{window.open('https://files.dmns.app/screenshots/' + Search33 + '.jpg', 'Search33window');}
</script>
<form onsubmit="doSearch33(this.Search33.value); return false;">
<input type="text" id="Search33" name="Search33" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Screenshot 6" /><br></form><br>
<script type="text/javascript">
function doSearch34(Search34)
{window.open('http://spyonweb.com/' + Search34, 'Search34window');}
</script>
<form onsubmit="doSearch34(this.Search34.value); return false;">
<input type="text" id="Search34" name="Search34" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="SpyOnWeb" /><br></form>
<script type="text/javascript">
function doSearch35(Search35)
{window.open('http://analyzeid.com/?domain=' + Search35, 'Search35window');}
</script>
<form onsubmit="doSearch35(this.Search35.value); return false;">
<input type="text" id="Search35" name="Search35" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="AnalyzeID" /><br></form>
<script type="text/javascript">
function doSearch36(Search36)
{window.open('https://dnslytics.com/reverse-analytics/' + Search36, 'Search36window');}
</script>
<form onsubmit="doSearch36(this.Search36.value); return false;">
<input type="text" id="Search36" name="Search36" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Google Analytics" /><br></form>
<script type="text/javascript">
function doSearch37(Search37)
{window.open('https://dnslytics.com/reverse-adsense/' + Search37, 'Search37window');}
</script>
<form onsubmit="doSearch37(this.Search37.value); return false;">
<input type="text" id="Search37" name="Search37" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Google Adsense" /><br></form>
<script type="text/javascript">
function doSearch38(Search38)
{window.open('https://www.domainiq.com/snapshot_history?data=' + Search38 + '#' + Search38, 'Search38window');}
</script>
<form onsubmit="doSearch38(this.Search38.value); return false;">
<input type="text" id="Search38" name="Search38" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="DomainIQ" /><br></form>
<script type="text/javascript">
function doSearch39(Search39)
{window.open('http://moonsearch.com/report/' + Search39 + '.html', 'Search39awindow');}
</script>
<form onsubmit="doSearch39(this.Search39.value); return false;">
<input type="text" id="Search39" name="Search39" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="MoonSearch" /><br></form>
<script type="text/javascript">
function doSearch40(Search40)
{window.open('https://www.nerdydata.com/reports/new?search=%7B%22all%22%3A%5B%7B%22type%22%3A%22code%22,%22value%22%3A%22' + Search40 + '%22%7D%5D,%22any%22%3A%5B%5D,%22none%22%3A%5B%5D%7D', 'Search40window');}
</script>
<form onsubmit="doSearch40(this.Search40.value); return false;">
<input type="text" id="Search40" name="Search40" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="NerdyData" /><br></form>
<script type="text/javascript">
function doSearch41(Search41)
{window.open('https://builtwith.com/' + Search41, 'Search41window');}
</script>
<form onsubmit="doSearch41(this.Search41.value); return false;">
<input type="text" id="Search41" name="Search41" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="BuiltWith" /><br></form>
<script type="text/javascript">
function doSearch42(Search42)
{window.open('https://dnsdumpster.com/static/map/' + Search42 + '.png', 'Search42window');}
</script>
<form onsubmit="doSearch42(this.Search42.value); return false;">
<input type="text" id="Search42" name="Search42" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="DNSDump" /><br></form>
<script type="text/javascript">
function doSearch43(Search43)
{window.open('http://' + Search43 + '/robots.txt', 'Search43window');}
</script>
<form onsubmit="doSearch43(this.Search43.value); return false;">
<input type="text" id="Search43" name="Search43" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Robots.txt" /><br></form>
<script type="text/javascript">
function doSearch44(Search44)
{window.open('https://host.io/' + Search44, 'Search44window');}
</script>
<form onsubmit="doSearch44(this.Search44.value); return false;">
<input type="text" id="Search44" name="Search44" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Host.io" /><br></form>
<script type="text/javascript">
function doSearch45(Search45)
{window.open('https://host.io/backlinks/' + Search45, 'Search45window');}
</script>
<form onsubmit="doSearch45(this.Search45.value); return false;">
<input type="text" id="Search45" name="Search45" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Host.io Backlinks" /><br></form>
<script type="text/javascript">
function doSearch46(Search46)
{window.open('https://host.io/redirects/' + Search46, 'Search46window');}
</script>
<form onsubmit="doSearch46(this.Search46.value); return false;">
<input type="text" id="Search46" name="Search46" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Host.io Redirects" /><br></form>
<script type="text/javascript">
function doSearch47(Search47)
{window.open('https://dnslytics.com/domain/' + Search47, 'Search47window');}
</script>
<form onsubmit="doSearch47(this.Search47.value); return false;">
<input type="text" id="Search47" name="Search47" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="DNSlytics" /><br></form>
<script type="text/javascript">
function doSearch48(Search48)
{window.open('https://www.wmtips.com/tools/info/' + Search48, 'Search48window');}
</script>
<form onsubmit="doSearch48(this.Search48.value); return false;">
<input type="text" id="Search48" name="Search48" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="WMTips" /><br></form>
<script type="text/javascript">
function doSearch49(Search49)
{window.open('https://www.robtex.com/dns-lookup/' + Search49, 'Search49window');}
</script>
<form onsubmit="doSearch49(this.Search49.value); return false;">
<input type="text" id="Search49" name="Search49" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Robtex" /><br></form>
<script type="text/javascript">
function doSearch50(Search50)
{window.open('https://www.domaincodex.com/search.php?q=' + Search50, 'Search50window');}
</script>
<form onsubmit="doSearch50(this.Search50.value); return false;">
<input type="text" id="Search50" name="Search50" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="DomainCodex" /><br></form><br>
<script type="text/javascript">
function doSearch51(Search51)
{window.open('http://www.similarweb.com/website/' + Search51, 'Search51window');}
</script>
<form onsubmit="doSearch51(this.Search51.value); return false;">
<input type="text" id="Search51" name="Search51" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="SimilarWeb" /><br></form>
<script type="text/javascript">
function doSearch52(Search52)
{window.open('https://moz.com/domain-analysis?site=' + Search52, 'Search52window');}
</script>
<form onsubmit="doSearch52(this.Search52.value); return false;">
<input type="text" id="Search52" name="Search52" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Moz" /><br></form>
<script type="text/javascript">
function doSearch53(Search53)
{window.open('https://www.spyfu.com/overview/domain?query=' + Search53, 'Search53window');}
</script>
<form onsubmit="doSearch53(this.Search53.value); return false;">
<input type="text" id="Search53" name="Search53" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="SpyFu" /><br></form>
<script type="text/javascript">
function doSearch54(Search54)
{window.open('https://api.sharedcount.com/v1.0/?url=https%3A%2F%2F' + Search54 + '&apikey=1934f519a63e142e0d3c893e59cc37fe0172e98a', 'Search54window');}
</script>
<form onsubmit="doSearch54(this.Search54.value); return false;">
<input type="text" id="Search54" name="Search54" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="SharedCount" /><br></form>
<script type="text/javascript">
function doSearch55(Search55)
{window.open('https://www.reddit.com/search?q=site:' + Search55, 'Search55window');}
</script>
<form onsubmit="doSearch55(this.Search55.value); return false;">
<input type="text" id="Search55" name="Search55" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="RedditDomain" /><br></form>
<script type="text/javascript">
function doSearch56(Search56)
{window.open('http://bc.linkody.com/en/seo-tools/free-backlink-checker/' + Search56, 'Search56window');}
</script>
<form onsubmit="doSearch56(this.Search56.value); return false;">
<input type="text" id="Search56" name="Search56" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Backlinks" /><br></form>
<script type="text/javascript">
function doSearch57(Search57)
{window.open('https://www.copyscape.com/?q=http://' + Search57, 'Search57window');}
</script>
<form onsubmit="doSearch57(this.Search57.value); return false;">
<input type="text" id="Search57" name="Search57" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="CopyScape" /><br></form>
<script type="text/javascript">
function doSearch58(Search58)
{window.open('http://www.visualsitemapper.com/map/' + Search58, 'Search58window');}
</script>
<form onsubmit="doSearch58(this.Search58.value); return false;">
<input type="text" id="Search58" name="Search58" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="SiteMapper" /><br></form><br>
<script type="text/javascript">
function doSearch14(Search14)
{window.open('https://www.virustotal.com/#/domain/' + Search14, 'Search14window');}
</script>
<form onsubmit="doSearch14(this.Search14.value); return false;">
<input type="text" id="Search14" name="Search14" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="VirusTotal" /><br></form>
<script type="text/javascript">
function doSearch59(Search59)
{window.open('https://threatintelligenceplatform.com/report/' + Search59, 'Search59window');}
</script>
<form onsubmit="doSearch59(this.Search59.value); return false;">
<input type="text" id="Search59" name="Search59" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="ThreatIntel" /><br></form>
<script type="text/javascript">
function doSearch60(Search60)
{window.open('https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=100&virtual_hosts=INCLUDE&q=' + Search60, 'Search60window');}
</script>
<form onsubmit="doSearch60(this.Search60.value); return false;">
<input type="text" id="Search60" name="Search60" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Censys" /><br></form>
<script type="text/javascript">
function doSearch61(Search61)
{window.open('https://securitytrails.com/list/apex_domain/' + Search61, 'Search61window');}
</script>
<form onsubmit="doSearch61(this.Search61.value); return false;">
<input type="text" id="Search61" name="Search61" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="SecurityTrails" /><br></form>
<script type="text/javascript">
function doSearch62(Search62)
{window.open('https://www.threatcrowd.org/domain.php?domain=' + Search62, 'Search62window');}
</script>
<form onsubmit="doSearch62(this.Search62.value); return false;">
<input type="text" id="Search62" name="Search62" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="ThreatCrowd" /><br></form>
<script type="text/javascript">
function doSearch63(Search63)
{window.open('https://themarkup.org/blacklight?url=' + Search63, 'Search63window');}
</script>
<form onsubmit="doSearch63(this.Search63.value); return false;">
<input type="text" id="Search63" name="Search63" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Blacklight" /></form>
<script type="text/javascript">
function doSearch64(Search64)
{window.open('https://crt.sh/?q=' + Search64, 'Search64window');}
</script>
<form onsubmit="doSearch64(this.Search64.value); return false;">
<input type="text" id="Search64" name="Search64" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="CRT.sh" /></form><br>
<script type="text/javascript">
function doSearch65(Search65)
{window.open('https://dehashed.com/search?query=%22' + Search65 + '%22', 'Search65window');}
</script>
<form onsubmit="doSearch65(this.Search65.value); return false;">
<input type="text" id="Search65" name="Search65" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Dehashed" /><br></form>
<script type="text/javascript">
function doSearch66(Search66)
{window.open('https://www.hudsonrock.com/search?domain=' + Search66, 'Search66window');}
</script>
<form onsubmit="doSearch66(this.Search66.value); return false;">
<input type="text" id="Search66" name="Search66" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="HudsonRock" /><br></form>
<script type="text/javascript">
function doSearch67(Search67)
{window.open('https://intelx.io/?s=' + Search67, 'Search67window');}
</script>
<form onsubmit="doSearch67(this.Search67.value); return false;">
<input type="text" id="Search67" name="Search67" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="IntelligenceX" /><br></form>
<script type="text/javascript">
function doSearch68(Search68)
{window.open('https://www.skymem.info/srch?q=' + Search68, 'Search68window');}
</script>
<form onsubmit="doSearch68(this.Search68.value); return false;">
<input type="text" id="Search68" name="Search68" size="30" placeholder="Domain Name" value="" />
<input type="submit" style="width:140px" value="Skymem" /><br></form><br>
<script type="text/javascript">
function doSearch69(Search69)
{window.open('https://' + Search69 + '+', 'Search69window');}
</script>
<form onsubmit="doSearch69(this.Search69.value); return false;">
<input type="text" name="Search69" size="30" placeholder="Entire Bit.ly URL" value="" />
<input type="submit" style="width:140px" value="Bit.ly" /></form>
<script type="text/javascript">
function doSearch71(Search71)
{window.open('https://' + Search71 + '~', 'Search71window');}
</script>
<form onsubmit="doSearch71(this.Search71.value); return false;">
<input type="text" name="Search71" size="30" placeholder="Entire Tiny.cc URL" value="" />
<input type="submit" style="width:140px" value="Tiny.cc" /></form>
<script type="text/javascript">
function doSearch72(Search72)
{window.open('http://' + Search72 + '-', 'Search72window');}
</script>
<form onsubmit="doSearch72(this.Search72.value); return false;">
<input type="text" name="Search72" size="30" placeholder="Entire Bit.do URL" value="" />
<input type="submit" style="width:140px" value="Bit.do" /></form>
<script type="text/javascript">
function doSearch73(Search73)
{window.open('http://checkshorturl.com/expand.php?u=' + Search73, 'Search73window');}
</script>
<form onsubmit="doSearch73(this.Search73.value); return false;">
<input type="text" name="Search73" size="30" placeholder="Entire Short URL" value="" />
<input type="submit" style="width:140px" value="Any" /></form><br>
<script type="text/javascript">
function doSearch74(Search74)
{window.open('http://moonsearch.com/adsense/' + Search74 + '.html', 'Search74window');}
</script>
<form onsubmit="doSearch74(this.Search74.value); return false;">
<input type="text" name="Search74" size="30" placeholder="AdSense ID" value="" />
<input type="submit" style="width:140px" value="MoonSearch" /></form>
<script type="text/javascript">
function doSearch75(Search75)
{window.open('https://analyzeid.com/id/ca-pub-' + Search75, 'Search75window');}
</script>
<form onsubmit="doSearch75(this.Search75.value); return false;">
<input type="text" name="Search75" size="30" placeholder="AdSense ID" value="" />
<input type="submit" style="width:140px" value="AnalyzeID" /></form>
<script type="text/javascript">
function doSearch76(Search76)
{window.open('https://dnslytics.com/reverse-adsense/pub-' + Search76, 'Search76window');}
</script>
<form onsubmit="doSearch76(this.Search76.value); return false;">
<input type="text" name="Search76" size="30" placeholder="AdSense ID" value="" />
<input type="submit" style="width:140px" value="DNSlytics" /></form>
<script type="text/javascript">
function doSearch77(Search77)
{window.open('https://api.hackertarget.com/analyticslookup/?q=pub-' + Search77, 'Search77window');}
</script>
<form onsubmit="doSearch77(this.Search77.value); return false;">
<input type="text" name="Search77" size="30" placeholder="Adsense ID" value="" />
<input type="submit" style="width:140px" value="HackerTarget" /></form>
<script type="text/javascript">
function doSearch78(Search78)
{window.open('http://moonsearch.com/analytics/' + Search78 + '.html', 'Search78window');}
</script>
<form onsubmit="doSearch78(this.Search78.value); return false;">
<input type="text" name="Search78" size="30" placeholder="Analytics ID" value="" />
<input type="submit" style="width:140px" value="MoonSearch" /></form>
<script type="text/javascript">
function doSearch79(Search79)
{window.open('https://analyzeid.com/id/ua-' + Search79, 'Search79window');}
</script>
<form onsubmit="doSearch79(this.Search79.value); return false;">
<input type="text" name="Search79" size="30" placeholder="Analytics ID" value="" />
<input type="submit" style="width:140px" value="AnalyzeID" /></form>
<script type="text/javascript">
function doSearch80(Search80)
{window.open('https://dnslytics.com/reverse-analytics/ua-' + Search80, 'Search80window');}
</script>
<form onsubmit="doSearch80(this.Search80.value); return false;">
<input type="text" name="Search80" size="30" placeholder="Analytics ID" value="" />
<input type="submit" style="width:140px" value="DNSlytics" /></form>
<script type="text/javascript">
function doSearch81(Search81)
{window.open('https://publicwww.com/websites/%22ua-' + Search81 + '%22/', 'Search81window');}
</script>
<form onsubmit="doSearch81(this.Search81.value); return false;">
<input type="text" name="Search81" size="30" placeholder="Analytics ID" value="" />
<input type="submit" style="width:140px" value="PublicWWW" /></form>
<script type="text/javascript">
function doSearch82(Search82)
{window.open('https://api.hackertarget.com/analyticslookup/?q=UA-' + Search82, 'Search82window');}
</script>
<form onsubmit="doSearch82(this.Search82.value); return false;">
<input type="text" name="Search82" size="30" placeholder="Analytics ID" value="" />
<input type="submit" style="width:140px" value="HackerTarget" /></form>
</p>
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
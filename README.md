![bazzellpy](https://github.com/dmw94/bazzellpy/blob/main/title_img.png)

`bazzellpy` allows you to call [IntelTechniques Search Tools](https://inteltechniques.com/tools) as functions in your Python program.

Michael Bazzell's useful suite of OSINT tools are a great start for any investigation. I wanted to be able to call on these tools without having to re-paste code when working on more complex projects. I've made this library available so you can too.

***Michael Bazzell has not endorsed this library and any references to his person are merely to give him due credit for publishing his tools. I am in no way involved with IntelTechniques or Michael Bazzell.***

If you like this library, feel free to buy me a coffee!

<p align="center"><a href="https://www.buymeacoffee.com/dmw94" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></p>

# How to use bazzellpy

## Install package with pip
`pip install bazzellpy`

## Import package and required method(s)
```
import bazzellpy
from bazzellpy import <method>
```

## Search engines tool
```
searchengines(query: str) -> dict:
    """
    Output a dict containing the URLs for your query across all search engines.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """
```

## Facebook tools

```
facebook_user(username: str, userno: str) -> dict:
    """
    Output a dict containing links to different parts of a user's Facebook profile.

    :param username: the username to search - input "" if not available
    :param userno: the user number to search - input "" if not available
    :return: dict containing links to various parts of user profile
    """

facebook_search(query: str) -> dict:
    """
    Output a dict containing links to various engines to search terms across facebook.

    :param query: the term you want to search
    :return: dict containing links to the search results for your query

facebook_mutuality(UID1: str, UID2: str) -> str:
    """
    Output a string containing a URL showing common friends between two user IDs.

    :param UID1: the first User ID
    :param UID2: the second User ID
    :return: common friends result URL as string
    """
```

## Twitter tools

```
twitter_user(query: str) -> dict:
    """
    Takes Twitter username as string and returns dict of URLs to aspects of profile and third-party analysis tools
    
    :param query: the Twitter username you want to query
    :return: dictionary of URLs - Twitter profile & third-party analysis
    """

twitter_user_year(query: str, year: str) -> dict:
    """
    See a Twitter user's activity during a specific year

    :param query: the user's username
    :param year: the year you are interested in
    :return: dict of URLs that chops up activity in various ways to be selected from for further analysis 
    """

twitter_query_year(query: str, year: str) -> str:
    """
    Returns a URL giving activity for a specific term for a particular year

    :param query: search term(s)
    :param year: the year you are interested in
    :return: string of URL to page displaying activity
    """

twitter_real_name(forename: str, surname: str) -> dict:
    """
    Identify Twitter Profiles using an individual's real name.

    :param forename: the individual's real first name
    :param surname: the individual's real surname
    :return: dict containing two URLs of search results
    """

twitter_lists(list_number: str) -> dict:
    """
    Return URLs with details about Twitter lists (members and followers).

    :param list_number: the ID number of the list
    :return: dict containing the URLs
    """
```

## Instagram tools

```
instagram_user(query: str) -> dict:
    """
    Various basic queries if all you have to go on is an Instagram username

    :param query: individual's username
    :return: dict containing URLs of results
    """

instagram_follow(query: str) -> dict:
    """
    Directs to webpages containing a user's followers and who they follow

    :param query: the individual's username
    :return: dict containing the URLs of the followers and following webpages
    """

instagram_user_term(user: str, search_term: str) -> str:
    """
    Searches out a user plus a search term

    :param user: individual's username
    :param search_term: self-explanatory
    :return: string URL for search results
    """

instagram_association(user1: str, user2: str) -> str:
    """
    Identifies associations between two Instagram users

    :param user1: first individual's username
    :param user2: second individual's username
    :return: string URL for search results
    """

instagram_search_or_tag(query: str) -> dict:
    """
    Results of search term or tag queries on Instagram

    :param query: the search term
    :return: dict of search result URLs
    """
```

## LinkedIn tools

```
linkedin_person_search(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> str:
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

linkedin_post_search(keyword: str, title: str) -> str:
    """
    Searches posts given one or more keywords and the poster's job title

    :param keyword: self-explanatory
    :param title: poster's job title
    :return: string containing URL of search result
    """

linkedin_google_bing_yandex(forename: str, surname: str, keyword: str, title: str, company: str, school: str) -> dict:
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
```

## Communities tool (username only)

```
community_query(query: str) -> dict:
    """
    Username and profile searches on Reddit, Hacker News, TikTok, Meetup, Ebay, Pintrest, Discord, Telegram, Parler and Gab

    :param query: username to search
    :return: dict of URLs of search results
    """

community_term_query(query: str) -> dict:
    """
    Terms and tags search across Reddit, 4chan, TikTok, Meetup, Discord and Telegram

    :param query: the term or tag to search
    :return: a dict containing URLs of search results
    """
```

## Email address tool

```
email_query(email: str) -> dict:
    """
    Returns URLs for search results on querying a specific email address

    :param email: the email you want to search
    :return: dict containing the search result URLs
    """
```

## Username search tool (anywhere not caught by "Communities tool")

```
username_query(query: str) -> dict:
    """
    Search for an individual given their username

    :param query: the individual's username
    :return: dict of URLs to search the username
    """
```

## Name search tool

```
name_query(forename: str, surname: str) -> dict:
    """
    Returns URLs to query a given real forename and surname.

    :param forename: self-explanatory
    :param surname: self-explanatory
    :return: dict of URLs for querying an individual's real name against public databases
    """
```

## Documents search tool

```
doc_query(query: str) -> dict:
    """
    Return search engine queries for online documents containing a particular term

    :param query: your search term
    :return: query URLs in dict
    """
```

## Images tool

```
img_query_url(query: str) -> dict:
    """
    Reverse search using an image

    :param query: url of image
    :return: results of image reverse search on various search engines
    """

img_query_text(query: str) -> dict:
    """
    Search for an image given a specific text query

    :param query: search term / textual description of what you are looking for
    :return: dict of URLs of results for the query
    """
```

## Videos tool

```
YT_vid_ID_query(query: str) -> dict:
    """
    Various tools for use with Youtube (e.g., age-restriction bypass, view metadata, etc.)

    :param query: video ID of interest
    :return: dict of resultant URLs
    """

YT_vid_comments(video_id: str, search_term: str) -> str:
    """
    Return the URL of comments on a given Youtube Video

    :param video_id: the ID number of the video
    :param search_term: key terms you are looking for in comments
    :return: URL (single string) of query result webpage
    """

YT_user_query(query: str) -> dict:
    """
    Query a YouTube user given their username

    :param query: Youtube username
    :return: links to profile and account details for the given username
    """

YT_channel_metadata(channel_id: str) -> str:
    """
    Get Youtube Channel metadata given a channel ID

    :param query: channel ID of interest
    :return: URL to metadata
    """

vid_search_term(query: str) -> dict:
    """
    Search for videos across the web by term or tag

    :param query: search term or tag of interest
    :return: dict containing URLs of results on various video sharing sites and search engines
    """
```

## Domains tool

```
domain_query(query: str) -> dict:
    """
    Returns URLs of various sites to lookup information about a domain

    :param query: the domain you want to query
    :return: dict containg the URLs to lookup info
    """
```

## IP Addresses tool

```
IP_query(query: str) -> dict:
    """
    Output a dict containing the URLs for your IP query across all IP lookup providers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """
```

## Bitcoin address query

```
bitcoin_query(query: str) -> dict:
    """
    Output a dict containing the URLs for your Bitcoin address query across a number of services.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """
```

## Breach searches

```
breachQ_email(query: str) -> dict:
    """
    Output a dict containing the URLs for your email address query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

breachQ_username(query: str) -> dict:
    """
    Output a dict containing the URLs for your username query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

breachQ_domain(query: str) -> dict:
    """
    Output a dict containing the URLs for your domain query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

breachQ_telephone(query: str) -> dict:
    """
    Output a dict containing the URLs for your telephone number query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

breachQ_IP(query: str) -> dict:
    """
    Output a dict containing the URLs for your IP address query across all breach registers.

    :param query: what you want to search
    :return: dict containing URLs for your query
    """

breach_query(email: str, username: str, domain: str, telephone: str, IP_add: str) -> dict:
    """
    Output a dict containing the URLs for your IP query across all breach registers.

    :param email: email address to query - input "" to skip
    :param username: username to query - input "" to skip
    :param domain: domain to query - input "" to skip
    :param telephone: telephone number to query - input "" to skip
    :param IP_add: IP address to query - input "" to skip
    :return: dict of dicts containing URLs for your query
    """
```

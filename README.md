# Bazzell-py

### N.B. - THIS LIBRARY IS STILL UNDER DEVELOPMENT

Bazzell-py allows you to call [IntelTechniques Search Tools](https://inteltechniques.com/tools) as functions in your Python program.

Michael Bazzell's useful suite of OSINT tools are a great start for any investigation. I wanted to be able to call on these tools without having to re-paste code when working on more complex projects. I've made this library available so you can too.

If you like this library, feel free to buy me a coffee!

<p align="center"><a href="https://www.buymeacoffee.com/dmw94" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></p>

# How to use bazzellpy

## Install package with pip
`pip install bazzellpy`

## Import package and required method(s)
`import bazzellpy`

`from bazzellpy import <method>`

## Note on methods
Unless otherwise specified, the methods below will output a dictionary or dictionary of dictionaries

## Search engines tool
`searchengines(query: str)` 

## Facebook tools

### Facebook user search
`facebook_user(username: str, userno: str)`

### Facebook search
`facebook_search(query:str)`

### Facebook UID search with qualifier
`facebook_UID(UID: str, qual: str)`

### Facebook Location ID search with qualifier
`facebook_LOCID(LOCID: str, qualifier: str)`

### Facebook UID search with qualifier and query
`facebook_UID_query(UID: str, qual: str, query: str)`

### Facebook events by location
`facebook_events_by_loc(LOCID: str, query: str)`

### Facebook profiles by institution
`facebook_profiles_by_institution(IID: str, name: str)`

### Facebook mutual connections
`facebook_mutuality(UID1: str, UID2: str)`

### Facebook content by date
`facebook_content_by_date(keyword: str, start: str, end: str)`

## Twitter tools

### Twitter user
`twitter_user(query: str)`

### Twitter user by year
`twitter_user_year(query: str, year: str)`

### Search term by year
`search_term_year(query: str, year: str)`

### Real name search
`twitter_real_name(real_name: str)`

### Lists search
`twitter_lists(list_number: str)`

## Instagram tools

### User search
`instagram_user(query: str)`

### Followers / following query
instagram_follow(query: str)

### User + search term query
`instagram_user_term(user: str, search_term: str) -> str`

### Association between 2 users
`instagram_association(user1: str, user2: str) -> str`

### Hashtag and search term query
`instagram_search_term(query: str)`

### Dumpor tag query
`instagram_dumpor_tag(query: str) -> str`

## LinkedIn tools

### Person search

`linkedin_person_search(forename: str, surname: str, keyword: str, title: str, company: str, school: str)`

### Post search

`linkedin_post_search(keyword: str, title: str)`

### Person search on external engines

`linkedin_google_bing_yandex(forename: str, surname: str, keyword: str, title: str, company: str, school: str)`

### Keyword search

`linkedin_keyword(keyword: str)`

## Communities tool (username only)

`community_query(query: str)`

## Email address tool

`email_query(email: str)`

## Username search tool (anywhere not caught by "Communities tool")

`username_query(query: str)`

## Name search tool

`name_query(forename: str, surname: str)`

## Maps tool (in decimal degrees to avoid disappointment)

`map_query(lat: str, long: str)`

## Documents search tool

`doc_query(query: str)`

## Pastes tool

`paste_query(query: str)`

## Images tool

`img_query(query: str)`

## Videos tool

`vid_query(query: str)`

## Domains tool

`domain_query(query: str)`

## IP Addresses tool

```
IP_query(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

## Bitcoin address query

```
bitcoin_query(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

## Breach searches

### Query using email address

```
breachQ_email(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

### Query using username

```
breachQ_username(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

### Query using domain

```
breachQ_domain(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

### Query using telephone number

```
breachQ_telephone(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

### Query using IP address

```
breachQ_IP(query: str)
    :param query: what you want to search
    :return: dict containing URLs for your query
```

### Master query

```
breach_query(email: str, username: str, domain: str, telephone: str, IP_add: str)
    :param email: email address to query - input "" to skip
    :param username: username to query - input "" to skip
    :param domain: domain to query - input "" to skip
    :param telephone: telephone number to query - input "" to skip
    :param IP_add: IP address to query - input "" to skip
    :return: dict of dicts containing URLs for your query
```

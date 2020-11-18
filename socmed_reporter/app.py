from googlesearch import search
import collections

######################################
# exclude result from given keywords #
# certain www.xxxxx.com/ <--- page, dir, cat need to exclude
def check_keyword(site,url):
    
    if site == "facebook.com":
        keywords = [
            "pages", "directory", "category", "status", "media", "groups",
        ]
    elif site == "instagram.com":
        keywords = [
            "tags", "explore", "p",
        ]
    elif site == "twitter.com":
        keywords = [
            "search", "search-advanced", "search-home", "i",
        ]

    for keyword in keywords:
        if "/{}/".format(keyword) in url:
            return True

    return False


#################################################################
# clean name from bin, binti, a/l, a/p then combine as one name #
def name_clean(name):
    keywords = [
        "BIN", "BINTI", "A/L", "A/P",
    ]

    name2 = ""

    for keyword in keywords:
        if " {} ".format(keyword) in name:
            name = name.split(" {}".format(keyword))   
            soc_med(name[0])    # exclude bin ke atas then just search for name dia

    if isinstance(name, list):
        for x in name:
            name2 += x
        return name2
    else:
        return name 


##################################################
# social media scrapper links from google search #
def soc_med(name):
    social_media = [
        "facebook.com", "twitter.com", "instagram.com",
    ]

    for site in social_media:

        links = []
        query = "site:{} {}".format(site,name)

        if name == "print_result":
            print("\n---------- {} ----------".format(site))
            for x in socmed[f"{site}"]:
                print(x)
        else:
            for url in search(query, tld="com", num=4, stop=4, pause=0):
                if not check_keyword("{}".format(site),url):  # go check if the excluded keyword exist in the results
                    link = url.split("/")  # split the links to find which user profile is not redundant in the result
                    if link[3] == "people" and link[4] not in links:
                        links.append("people/{}".format(link[4]))  # some result has /people/ so need to manually add inside list, add the username if not in the list yet
                    elif link[3] == "public" and link[4] not in links:
                        links.append(link[4])
                    elif link[3] not in links:
                        links.append(link[3]) # add the username if not in the list yet

            for l in links:
                if f"https://www.{site}/{l}" not in socmed[f"{site}"]:
                    socmed[f"{site}"].append(f"https://www.{site}/{l}")
    return socmed      


def reporter(name):
    global socmed
    socmed = collections.defaultdict(list)
    name = name.upper()
    name = name_clean(name)
    results = soc_med(name)
    print(results)
    return results


if __name__ == "__main__":
    try:
        reporter()
    except KeyboardInterrupt:
        sys.exit()
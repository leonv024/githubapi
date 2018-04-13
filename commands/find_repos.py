import requests, sys
from prettytable import PrettyTable

def find_repos(api_url, user, token, string):
    login = requests.get(api_url + 'search/repositories?q=' + string, auth=(user,token))

    c = 0

    data = login.json()

    table = PrettyTable(['Url', 'Description']) # Header
    table.align = "l" # Text Align left

    for i in range(len(data["items"])):
        
        if not data["items"][i]["description"] == None:
            description = data["items"][i]["description"]
            # Max characters for description
            if len(description) >= 99:
                description = description[:99] + '...'
        else:
            description = None

        result = data["items"][i]["html_url"], description
        table.add_row([result[0], result[1]])

        #print('%s %s ' % (result["items"][i]["html_url"].ljust(50), description))
        c+=1

    print(table)
    print('\033[32m\nDisplaying %i out of %i results\033[0m' % (int(c), data["total_count"]))

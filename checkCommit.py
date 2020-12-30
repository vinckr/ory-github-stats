
import json
import urllib.request
from urllib.request import urlopen

# Special header needed for github api search endpoint
headers = {
'Accept': 'application/vnd.github.cloak-preview'
}

# check_commit function to check if "author" has commits in "org"
def checkCommit(author, org):
# github search api endpoint, substitutes author & org with functions arguments
    url_full = 'https://api.github.com/search/commits?q=author:{author}+org:{org}&per_page=1'.format(author=author, org=org)
# build the Request object with the correct header
    url = urllib.request.Request(url_full, data=None, headers=headers)
# open & read the Request object 
    response = urlopen(url).read()
# Decode the recevied json 
    data = json.loads(response.decode())
# Print number of total commits in the org
    print(data["total_count"])
    return data["total_count"]

# Testing call 
#commit = checkCommit("vinckr", "ory")


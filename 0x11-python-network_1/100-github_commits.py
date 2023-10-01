#!/usr/bin/python3
"""takes 2 arguments, first argument being the repository name and the second
argument being the owner name, and list 10 commits (from the most recent to
oldest) of the repository. Prints all commits by: `<sha>: <author name>` """
if __name__ == "__main__":
    import requests
    import sys

    token = "github_pat_11A55OHZI0VkGlzcUywO23_st32tcALkxCRNgq" +\
            "727sBXzOfcGzv5eiiDvLL331tFj0NVAKBZQ7p2HkO3ss"
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer ' + token,
               'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get(url, headers=headers)
    commits = response.json()
    commits.sort(
        key=lambda x: int(x.get('commit').get('author').get('date').
                          replace('-', '').replace('T', '').replace(':', '').
                          replace('Z', '')), reverse=True)
    for i, commit in enumerate(commits):
        print("{}: {}".format(
            commit.get('sha'),
            commit.get('commit').get('author').get('name')))
        if i == 9:
            break

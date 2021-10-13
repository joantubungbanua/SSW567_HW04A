import json
import requests



def getGithubRepoInfo(githubID):

    if(githubID == ""): 
        return 'Username Missing'
    #since Github username has a max of 39 characters, checks to see if what was entered actually works 
    elif (len(githubID)>=39): 
        return 'Invalid Username'
    #means user entered a valid username and will now list out associated repos and commits
    else: 
        results = {}
        #gets all repo info of specified user
        info = requests.get('https://api.github.com/users/{}/repos?page=1&per_page=1000'.format(githubID))

        #stores info in a json 

        info = info.json()

        #gets number of commits and repo name

        for repo in info:
            commits = requests.get('https://api.github.com/repos/{}/{}/commits?page=1&per_page=1000'.format(githubID, repo['name']))
        
            commits = commits.json()
            results[repo['name']] = len(commits)

            print('Repo: {} Number of commits: {}'.format(repo['name'], len(commits)))
        return results

getGithubRepoInfo('joantubungbanua')

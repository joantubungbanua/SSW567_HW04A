import requests
import json 

userID = input("What is your github username?")



def getGithubRepoName(userID): 
    query_url1 = f"https://api.github.com/users/{userID}/repos"
    r = requests.get(query_url1)
    names = r.json() 
    repoList = []
    for i in range(0,len(names)): 
        repoList.append(names[i]['name'])

    return (repoList)
        



def getgithubRepoCommits(userID, repoNames): 

    for i in range(0,len(repoNames)): 
        query_url2 = f"https://api.github.com/repos/{userID}/{repoNames[i]}/commits"
        test = requests.get(query_url2)
        commits = test.json()
        total = 0
        print("Repo Name: " + repoNames[i])
        for j in range(0,len(commits)):
            total += 1
        print("Commits: ") 
        print (total)
    




getgithubRepoCommits(userID,getGithubRepoName(userID))
       



    







    



    

    







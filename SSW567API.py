import requests
import json 



def getGithubRepoInfo(userID): 
    #checks to see if user entered an empty string 
    if(userID == ""): 
        return 'Username Missing'
    #since Github username has a max of 39 characters, checks to see if what was entered actually works 
    elif (len(userID)>=39): 
        return 'Invalid Username'
    #means user entered a valid username and will now list out associated repos and commits
    else: 
        query_url1 = f"https://api.github.com/users/{userID}/repos"
        r = requests.get(query_url1)
        names = r.json() 
        repoList = []
        for i in range(0,len(names)): 
            repoList.append(names[i]['name'])
        for j in range(0,len(repoList)): 
            query_url2 = f"https://api.github.com/repos/{userID}/{repoList[j]}/commits"
            test = requests.get(query_url2)
            commits = test.json()
            total = 0
            print("Repo Name: " + repoList[j])
            for k in range(0,len(commits)):
                total += 1
            print("Commits: ") 
            print (total)
        return("Successfully Printed!")

       



    







    



    

    







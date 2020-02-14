from ArticleNode import ArticleNode
from GetArticles import GetArticles
from MultiwayTree import multiwayTree
import time
import random
from random import randrange
from random import sample

#Initialize and preprocess data from GetArticles.py
print("Processing Articles:")
generator = GetArticles()
articles = generator.getArticles();
nodeList = list(articles.values())
for node in nodeList:
    node.articleID = int(node.articleID)
    node.references = [int(article) for article in node.cited]
    node.keywordList = list(node.keywordDict.values())

#Initialize DataStructure
tree = multiwayTree()
tree.initialize(nodeList)

#Search parameters

numberOfKeywords = random.randint(1,len(tree.keywords))
numberOfTestSearches = 10000
count = 0
successfulSearches=[]
for i in range(numberOfTestSearches):
    searchList = sample(tree.keywords,numberOfKeywords)
    searchResults = tree.keyWordSearch(searchList)
    startTime = time.time()
    tree.keyWordSearch(searchList)
    print("Search time: %s seconds" % (time.time() - startTime))
    print("SearchList: ",searchList)
    print("Search Qualified Articles :", len(searchResults))
    # print("Articles in keywords:-")
    # for keyword in searchList:
    #     print(keyword,": ", len(tree.nodeDictionary[keyword].successors))
    if(len(searchResults)>0) : 
        count+=1
        successfulSearches.append(searchList)
    print()
    print()
print("Successful Searches: ",count,"/",numberOfTestSearches)
categorizedArticles= 0
for keyword in tree.keywords:
    categorizedArticles+=len(tree.nodeDictionary[keyword].successors)

print("Number of Categorized Articles = ",categorizedArticles)
print("All keywords identified: \n", tree.keywords)
print("Successful Searches: \n", successfulSearches)
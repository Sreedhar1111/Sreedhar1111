
Hey, guys I pretty much used the WikipediaAPI which I set up using links which needed me to use parse URl and request URL to get the top 100 searches on wikipedia and then I turned them into a graph that shows how many views they get. I then used matplotlib.pyplot for the graph.

To be honest it took me a while to figure out what I wanted to do and even longer to code it. I thought It would be a pretty good introductory "project" and I attend on making more complicated things in the future, just wanted to do something small initially to have something to build on in the future.

My inital goal was to scrape a full years worth of Wikipedia data and then make a " top 10 appearances" but that took a lot of different apis and knowledge that I don't currently have, so I figured that I'll build to that and this is my initial baby version of that project.

If I end up doing it I will definitly post it on here, stay tuned if I update with a new Repo!

links for APIs:
Wikipedia API: https://pypi.org/project/Wikipedia-API/
Matlibplot.pyplot API: https://matplotlib.org
Parse URL API: https://docs.python.org/3/library/urllib.parse.html
Request URL API: https://docs.python.org/3/library/urllib.request.html
JSON API: https://docs.python.org/3/library/json.html
If you intend on replicating my graph be sure to consider that the date that I used was around the start of the 2022 Winter Olympics so a lot of the results are skewed in favor of skiers, Olympics, Countries, Etc.

Atributes:
top100 -> is a List of Directories
plt.show -> makes a graph of my data

 

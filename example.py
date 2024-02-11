import wikipedia # load wikipedia content

# get wikipedia page content; search for Crisis results in Crime content.. not sure why?
#thepage = wikipedia.search('Garbage')
#print(thepage)

wiki = wikipedia.page(title='Waste', auto_suggest=False)
print("*****")


text = wiki.content
print(text)
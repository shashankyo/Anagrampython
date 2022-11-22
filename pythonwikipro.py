import wikipedia as wiki
print(wiki.search("Python"))
wiki.set_lang("fr")
print(wiki.summary("Python"))
wiki.set_lang("en")
p = wiki.page("Python")
print(p.title)
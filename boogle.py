import wikipedia
import os
from translate import Translator
print("Boogle - Powered by Wikipedia.\n")
language_preference = input("Press 'a' to set result language to french and 'b' to set spanish. (Not mandatory)\n")
if language_preference == 'a':
  wikipedia.set_lang('fr')
  translator = Translator(to_lang ='fr')
if language_preference == 'b':
  translator = Translator(to_lang = 'es')
  wikipedia.set_lang('es')
if language_preference != 'a' and language_preference!='b':  
  translator = Translator(to_lang = 'en')


def search_engine():
  global translator
  x=0
  
  srch_text = translator.translate("What would you like to search? (type '_surprise me_' or '_r_' for a surprise)\n")
  
  srch = input(srch_text + '\n')
  if srch == '_surprise me_' or srch == '_r_':
    print(wikipedia.summary(wikipedia.random()),10)
    input()
    os.system("clear")
    search_engine()
  if srch == '':
    print("Invalid")
    input()
    os.system("clear")
    search_engine()
  results = wikipedia.search(srch,10)
  print("Possible Searches: ")
  for result in results:
    x+=1
    print(str(x)+'. ' + result)
  srch2_text= translator.translate("Based on the specifications narrow down you search. Choose the number of the search? \n")
  srch2 = input(srch2_text + '\n')
  if srch2 == '':
    print("Invalid")
    input()
    os.system("clear")
    search_engine()
  try:
    print(wikipedia.summary(results[int(srch2)-1],10))
  except:
    print(translator.translate("Sorry, no page found. It might be us or the Wikipedia API"))
  input()
  os.system("clear")
  lp = translator.translate("Press 'a' to change to french, 'b' to change to spanish, and'c' to english.\n" )
  language_preference = input(lp+'\n')
  if language_preference == 'a':
    wikipedia.set_lang('fr')
    translator = Translator(to_lang ='fr')
  if language_preference == 'b':
    translator = Translator(to_lang = 'es')
    wikipedia.set_lang('es')
  if language_preference =='c':  
    translator = Translator(to_lang = 'en')
  os.system("clear")
  search_engine()
search_engine()



import nlpcloud
class NLPApp:
 
  def __init__(self):
    self.__database = {}
    self.__first_menu()
 
  def __first_menu(self):
    first_input = input("""
    Hi how would you like to proceed?
    1. Not a member? Register
    2. Already a member? Login
    3. Galti se aa gaye? Exit
    """)
    if first_input == '1':
      self.__register()
    elif first_input == '2':
      self.__login()
    else:
      exit()
 
  def __register(self):
    name = input('enter name: ')
    email = input('enter email: ')
    password = input('enter password: ')
 
    if email in self.__database:
      print('email already exists')
      self.__first_menu()
    else:
      self.__database[email] = [name, password]
      print('registration successful. Now login')
      self.__first_menu()
 
  def __login(self):
    email = input('enter email: ')
    password = input('enter password: ')
 
    if email in self.__database:
      if self.__database[email][1] == password:
        print('login successful')
        self.__second_menu()
      else:
        print('wrong password. Try again')
        self.__login()
    else:
      print('this email is not registered')
      self.__first_menu()
 
  def __second_menu(self):
    second_input = input("""
    Hi how would you like to proceed?
    1. NER
    2. Language Detection
    3. Sentiment Analysis
    4. Logout
    """)
    if second_input == '1':
      self.__ner()
    elif second_input == '2':
      self.__language_detection()
    elif second_input == '3':
      self.__sentiment_analysis()
    elif second_input == '4':
      print('logged out successfully')
      self.__first_menu()
    else:
      print('invalid choice')
      self.__second_menu()
 
  def __ner(self):
    para = input('enter the paragraph: ')
    search_term = input('what would you like to search (e.g. person, location, organization): ')
 
    client = nlpcloud.Client("gpt-oss-120b", "a051638d59826605d71a692f298560a4da91c47a", gpu=True)
    response = client.entities(para, searched_entity=search_term)
 
    print('\n--- NER Result ---')
    if response['entities']:
      for entity in response['entities']:
        text_val = entity.get('text') or entity.get('word') or str(entity)
        type_val = entity.get('type') or search_term
        print(f'[{type_val}] -> {text_val}')
    else:
      print('no entities found')
 
    self.__second_menu()
 
  def __language_detection(self):
    para = input('enter the paragraph: ')
 
    client = nlpcloud.Client("python-langdetect", "your_api_key_here")
    response = client.langdetection(para)
 
    print('\n--- Language Detection Result ---')
    if response['languages']:
      best = sorted(response['languages'], key=lambda x: x['score'], reverse=True)[0]
      print(f"Detected Language : {best['language'].upper()}")
      print(f"Confidence        : {round(best['score'] * 100, 2)}%")
    else:
      print('could not detect language')
 
    self.__second_menu()
 
  def __sentiment_analysis(self):
    para = input('enter the paragraph: ')
 
    client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
    response = client.sentiment(para)
 
    L = []
    for i in response['scored_labels']:
      L.append(i['score'])
 
    index = sorted(list(enumerate(L)), key=lambda x: x[1], reverse=True)[0][0]
 
    print('\n--- Sentiment Result ---')
    print('Emotion :', response['scored_labels'][index]['label'].upper())
    print('Confidence :', round(L[index] * 100, 2), '%')
 
    self.__second_menu()
 
obj = NLPApp()
 
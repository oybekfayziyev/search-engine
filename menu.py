from post.add_to_post import AddPost as add_post
from utils.utils import validate, menu
from utils.core import remove_words
import sys
from search.analyze import ( 
            Analyze as analyze_obj,TfidVectorizerClass, WordProcessor as word_obj)

def getInput():

    inp = input('Your Input: ')
    text = validate(inp)

    if text:
        return text

    return None

def get_option_by_input(option):
    delete_id = None
    title = None
    description = None

    if option == '1':

        while title is None:
            print('Enter title: ')
            title = getInput()

        while description is None:
            print('Enter Description: ')
            description = getInput()
        
        post = add_post(title, description=description)
        print(post.get_description())
        post.load_data_from_json()
        post.insert(title, description)
        

    if option == '2':
        
        text2 = '''
        Xonobod 86 davlat ijrochilari keladigan xalqaro milliy estrada  festivali o‘tkazishga hozirlik ko‘rmoqda Andijon viloyatida ichki va tashqi turizmni rivojlantirish maqsadida Xonobod shahrida milliy estrada ijrochiligi bo‘yicha xalqaro festival o‘tkaziladi. Mazkur festivalga dunyoning 86 mamlakatidan milliy 
estrada xonandalarini taklif etish rejalashtirilgan. Ayni kunlarda Xonobodda tayyorgarlik ishlari olib borilmoqda.
        
        '''

        entity = []

        # text = input('Enter text you want to search: ')
        tfi_obj = TfidVectorizerClass()
            
        posts = add_post()
        title, description = posts.get_title_and_description()

        # make title and description into one string
        for index, i in enumerate(title):
            entity.append(' '.join((title[index],description[index])))

        from sklearn.svm import SVC
        clf = SVC(kernel='linear')

        # find = tfi_obj.find_similarity(text2, entity)    
        # print('find', find)

        for index, i in enumerate(entity):   
           
            find = tfi_obj.find_similarity(text2, i)   
        
            print('post id %s, related topics rate  %s: ' %(index+1, find[0]))

            
            if find[0] > 4:
                print(i)
            # print(vectorizer.get_feature_names())
        # print(X.shape)
        # print(X)
        # print('distance',distance)
      
    if option == '3':
        while delete_id is None:
            print('Enter id of the post: ')
            delete_id = getInput()
        
        post = add_post()
        post.delete(delete_id)

    if option == '4':
        post = add_post()
        title, description = post.get_title_and_description()
        print('title', title)
        print('description', description)
        result = post.select_all_items()
        data = result[0]        

        # show = show_as_dataFrame(result)
        # print(result)

    if option == '5':
        post = add_post()

        # initialize title and description data from json
        post.load_data_from_json()

        # get title and description
        title = post.get_title()
        description = post.get_description()
        
        # insert title, description, created date into table
        _len = len(title)
        for i in range(_len):       
            post.insert(title[i],description[i])
        
        print('Data inserted successfully')

    if option == '6':
        post = add_post()
        post.delete_all()
        print('All data deleted from table')

    # if option == '7':
    #     post = add_post()

    #     entity = []
    #     title, description = post.get_title_and_description()
    #     # make title and description into one string
    #     for index, i in enumerate(title):
    #         entity.append(' '.join((title[index],description[index])))
        
    #     for i in entity:
    #         tfi_obj = TfidVectorizerClass()
    #         X, Y, vectorizer = tfi_obj._transform(i)
    #         print('X', X.shape)
            

    #     return entity

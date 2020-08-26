from post.add_to_post import AddPost as add_post
from utils.utils import validate, menu
from utils.core import remove_words
import sys
from search.analyze import (StemmedCountVectorizer, StemmedTfidfCountVectorizer, 
            eucl_dist, Analyze as analyze_obj,TfidVectorizerClass, WordProcessor as word_obj)

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
        
        text = '''"Ushbu Ushbu bo'lsangiz qaror haqida 21 avgust kuni prezidentning Bektemir tumaniga tashrifi vaqtida ham aytilgandi, prezident o‘shanda O‘zbekistonda ishlab chiqarilayotgan avtomobillar tannarxini kamaytirish zarurligini ta'kidlagandi. Qarorga muvofiq, endi davlat xaridlarida yurtimizda tayyorlangan mahsulotlarga ustuvorlik berilib, ishlab chiqarish yanada rag‘batlantirilishi, jumladan, tenderda ikkitadan ko‘p o‘zbekistonlik ishlab chiqaruvchi mavjud bo‘lganda, faqat ularning mahsuloti qatnashishi, bundan buyon budjet hisobidan amalga oshiriladigan barcha xaridlarda mahalliy hokimiyat vakillari bevosita ishtirok etishi aytilgandi.Bu yilgi o‘quv yilini 14 sentabr – dushanba kunidan boshlash taklif sifatida kiritildi. Bu haqda xalq ta'limi vaziri Sherzod Shermatov xabar berdi.Vazirlik 3ta ssenariy bo‘yicha ishlayotgan edi. Ular orasida an'anaviy maktabni ochish, onlayn maktab orqali o‘qitish va aralash (gibrid) ssenariy bor. Vazirning yozishicha, «Telegram» orqali deyarli 1 mln. foydalanuvchi qatnashgan so‘rovnomada 70 foiz ota-ona bola sog‘lig‘idan xavotirda bo‘lib, uyda o‘zi onlayn o‘qitishi mumkinligi, 30 foizi esa pandemiya sharoitida ham farzandini maktabga yuborishini bildirgan.«Shuning uchun, aholini ko‘proq qatlamini rozi qilishni inobatga olib, faqat 3-ssenariy, ya'ni ota-onalarning o‘zlariga tanlash huquqini berish eng optimal variant bo‘lib turibdi.",
                "Bir tomondan, internetda ba'zi davlatlarda maktablar ochilib, kasallik ko‘payishi natijasida qaytadan yopilgani, bolalar o‘zi kuchli kasallanmasa-da, kattalarga qaraganda kuchliroq virus tashuvchisi bo‘lishi mumkinligi haqida xabarlar tarqalyapti.Ikkinchi tomondan, bu virusdan yaqin orada qutilmasligimizni, vaksina ishlab chiqilgan taqdirda ham uni barcha xavfsizlik sinovlaridan o‘tkazishga va ishlab chiqarib bizga yetib kelishiga ancha vaqt ketishi ham aniq.",
                "Shunga, ushbu vaqt davrida farzandlarimiz bilim olishdan orqada qolib ketmasliklari zarur», - deydi Sh. Shermatov."'''
     
        tfi_obj = TfidVectorizerClass()
        X, vectorizer = tfi_obj._transform(text)
        print(vectorizer.get_feature_names())
        print(X.shape)
        print(X)
      
    if option == '3':
        while delete_id is None:
            print('Enter id of the post: ')
            delete_id = getInput()
        
        post = add_post()
        post.delete(delete_id)

    if option == '4':
        post = add_post()
        result = post.select_all_items()
        data = result[0]        

        # show = show_as_dataFrame(result)
        print(result)

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


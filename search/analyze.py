from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp 
from .stemmers import FSMStemmer, WordProcessor
import sys
from utils.core import (remove_punctuation, remove_words, 
        remove_urls, to_lowercase, remove_numbers, digit_to_word)
from .stemmers import FSMStemmer

from sklearn.linear_model import SGDClassifier

class Analyze(FSMStemmer):

	def __init__(self):
		FSMStemmer().__init__()

	# tokenization
	def tokenize_word(self, text):	
		text = self.remove_punctuation_from_text(text)			 	
		return word_tokenize(text)
			
	# to lowercase
	def convert_to_lowercase(self, text):				
		text = to_lowercase(text)
		return text

	def remove_numbers_from_text(self,text):
		text = self.convert_to_lowercase(text)
		text = remove_numbers(text)
		return text
    
	# remove punctuations
	def remove_punctuation_from_text(self,text):
		text = self.remove_numbers_from_text(text)
		text = remove_punctuation(text)
		return text
	
	def remove_stop_words(self, text):
		# remove ‘ quotes from text
		text = ''.join(text.split("‘"))	
		# word tokenization	
		text = self.tokenize_word(text)
		# remove stop words from text
		stop_words = remove_words()
		# if stop word exist than reduce it from text
		filtered_text = [word for word in text if word not in stop_words]	
		 
		return filtered_text
		
	def convert_number(self,text):
		
		# split string into list of words
		temp_str = text.split()
		# initialize empty list
		new_string = []
		for word in temp_str:
			'''
			if word is digit converts the digit to number
			and appends to new_string
			'''
			if word.isdigit():
				print('word',word)
				temp = digit_to_word(word)
				new_string.append(temp)
			else:
				new_string.append(word)
		
		temp_str = ''.join(new_string)
		return temp_str
	

	def remove_white_space(self,text):
		text = self.remove_punctuation_from_text(text)	 
		text = " ".join(text.split())
		return text
	
	# convert word tokens into their root form
	def stemmer(self,text):
		text = self.remove_stop_words(text)
		stem = self.stem(text)
		return stem

class CountVectorizerClass(CountVectorizer):

	def transform_vectorizer(self,text):
		print('text')
		train_counts = self.fit_transform(text)
		return train_counts



class TfidVectorizerClass(Analyze):

	def __init__(self):
		Analyze().__init__()
	
	def _transform(self,text):
		
		text = self.stemmer(text)	
		vectorizer = TfidfVectorizer()		
		X = vectorizer.fit_transform(text)
		print(X.shape)
		return X, vectorizer

class TrainClassifer():

	pass




class StemmedCountVectorizer(CountVectorizer) :
	def build_analyser(self) :

		'''this function returns the function ( lambda used to return a function ) that
		stems each word using the english_stemmer 'english_stemmer.stem(word)' after it has done
		tokenization.
		english_stemmer.stem("graphics") returns "graphic" '''
		analyser = super(StemmedCountVectorizer,self).build_analyser()
       
		return lambda document : (FSMStemmer().do_stem(word) for word in analyser(document))



class StemmedTfidfCountVectorizer(TfidfVectorizer) :
	def build_analyser(self) :

		'''this function returns the function ( lambda used to return a function ) that
		stems each word using the english_stemmer 'english_stemmer.stem(word)' after it has done
		tokenization.Here the tokenization is done after applying Tf-Idf.
		english_stemmer.stem("graphics") returns "graphic" '''
		analyser = super(StemmedTfidfCountVectorizer,self).build_analyser()
		return lambda document : (FSMStemmer().do_stem(word) for word in analyser(document))




def eucl_dist(v1,v2) :

	''' Returns the eucledian distance between two vectors 
	lialg is linear algebra and norm returns the magnitude of the vector
	we apply normalization by dividing the vector with its magnitude, 
	use to array when using norm'''

	v1_normalized = v1/sp.linalg.norm(v1.toarray())
	v2_normalized = v2/sp.linalg.norm(v2.toarray())
	delta = v1_normalized - v2_normalized 
	return sp.linalg.norm(delta.toarray())


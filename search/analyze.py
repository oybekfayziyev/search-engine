from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp 
from .stemmers import FSMStemmer, WordProcessor
import sys
import numpy as np
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
		Y = vectorizer.transform(text)
		 
		return X, Y, vectorizer
	
	def train_test_data(self, X, Y):
		from sklearn.model_selection import train_test_split
		
		x_train, x_test, y_train, y_test = train_test_split(X, Y[:,0])
		return x_train, x_test, y_train, y_test

	def removePC(self,document):
		# from sklearn.decomposition import PCA

		from sklearn.decomposition import TruncatedSVD
		

		pca = TruncatedSVD(1)
		X_pca = pca.fit_transform(document)
		
		return X_pca
	
	def normalize(self, embedding):
		
		if len(embedding.shape) > 1:
			embedding /= np.linalg.norm(embedding, axis=1)[:, np.newaxis]
		else:
			embedding /= np.linalg.norm(embedding)
		
		return embedding
	
	def transform(self, document):
		embedding, _, _ = self._transform(document)
		 
		embedding = self.removePC(embedding)
		 
		embedding = self.normalize(embedding)
	 
		return embedding

	def find_similarity(self, query, document):
		 
		query = self.transform(query).reshape(1,-1)
	 
		document = self.transform(document) 
		
		return np.dot(query, document[:query.shape[1], :])[0]


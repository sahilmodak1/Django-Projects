from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'home.html', {'hello1':'one','hello2':'two'})

def sahil(request):
	return HttpResponse('SAAHIL')

def modak(request):
	return HttpResponse('MODAKKKK')

def count(request):
	text = request.GET['text1']
	word_list = text.split()
	word_count = dict()
	for word in word_list:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count[word]=1

	sorted_word_dict = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
	header = {
		'text':text, 
		'words_length': len(word_list), 
		'sorted_word_dict':sorted_word_dict
	}
	return render(request, 'count.html', header)
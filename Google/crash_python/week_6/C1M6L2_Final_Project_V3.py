#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# <br><br>
# Now you will need to upload your input file here so that your script will be able to process it.  To do the upload, you will need an uploader widget.  Run the following cell to perform all the installs and imports for your word cloud script and uploader widget.  It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.
# <br><br>
# **Enabling notebook extension fileupload/extension...**
# <br>
# **- Validating: <font color =green>OK</font>**

# In[1]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed. 
# <br><br>
# **IMPORTANT!** If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above,  select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.
# <br><br>
# To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# In[26]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* that your word cloud script can process. This was a lot of preliminary work, but you are now ready to begin your script. 

# Write a function in the cell below that iterates through the words in *file_contents*, removes punctuation, and counts the frequency of each word.  Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the".  Then use it in the `generate_from_frequencies` function to generate your very own word cloud!
# <br><br>
# **Hint:** Try storing the results of your iteration in a dictionary before passing them into wordcloud via the `generate_from_frequencies` function.

# If you have done everything correctly, your word cloud image should appear after running the cell below.  Fingers crossed!

# In[42]:


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ['было', 'себе', 'лет', 'которые', 'мог', 'этом', 'этих', 'друхих', 'между', 'эту', 'над', 'моих', 'всех', "был", "них", "него", "тебя, ""и", "в", "не", "на", "я", "быть", "он", "с", "что", "а", "по", "это", "она", "этот", "к", "но", "они", "мы", "как", "из", "у", "который", "то", "за", "свой", "что", "весь", "год", "от", "так", "о", "для", "ты", "же", "все", "тот", "мочь", "вы", "человек", "такой", "его", "сказать", "только", "или", "ещё", "бы", "себя", "один", "как", "уже", "до", "время", "если",
                           "сам", "когда", "другой", "вот", "говорить", "наш", "мой", "знать", "стать", "при", "чтобы", "дело", "жизнь", "кто", "первый", "очень", "два", "день", "её", "новый", "рука", "даже", "во", "со", "раз", "где", "там", "под", "можно", "ну", "какой", "после", "их", "работа", "без", "самый", "потом", "надо", "хотеть", "ли", "слово", "идти", "большой", "должен", "место", "иметь", "ничто"]
    my_count = {}
    
    for word in file_contents.split():
        if word.lower() in uninteresting_words:
            continue
        elif word.isalpha():
            if word not in my_count:
                my_count[word.lower()] = 0
            my_count[word.lower()] += 1
            
     
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(my_count)
    return cloud.to_array()
    

calculate_frequencies(file_contents) 


# In[43]:


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequecy count dictionary into the `generate_from_frequencies` function of `wordcloud`. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!

# In[ ]:





# In[ ]:





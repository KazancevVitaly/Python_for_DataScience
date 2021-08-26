#!/usr/bin/env python
# coding: utf-8

# Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


author_id = [1, 2, 3]
author_name = ['Тургенев', 'Чехов', 'Островский']
author = pd.DataFrame({
    'author_id': author_id,
    'author_name': author_name
})
print(author)


# In[3]:


author_id = [1, 1, 1, 2, 2, 3, 3]
book_title = [
    'Отцы и дети', 
    'Рудин', 'Дворянское гнездо', 
    'Толстый и тонкий', 
    'Дама с собачкой', 
    'Гроза', 
    'Таланты и поклонники'
]
price = [450, 300, 350, 500, 450, 370, 290]
book = pd.DataFrame({
    'author_id': author_id,
    'book_title': book_title,
    'price': price
})
print(book)


# Задание 2.
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

# In[4]:


author_price = pd.merge(author, book, on='author_id', how='outer')    #how='inner', 'left', 'right' or 'outer'
print(author_price)


# Задание 3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[5]:


top5 = author_price.nlargest(5, 'price')
print(top5)


# Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

# In[6]:


author_stat = author_price.groupby('author_name')
# print(author_stat)
author_stat = pd.DataFrame({
    'max_price': author_stat['price'].max(),
    'min_price': author_stat['price'].min(),
    'mean_price': author_stat['price'].mean()
})
print(author_stat)


# Задание 5**
# Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
# ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
# Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
# Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.
# 

# In[7]:


get_ipython().run_line_magic('pinfo', 'pd.pivot_table')


# In[8]:


cover = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
author_price.insert(3, 'cover', cover, True)
print(author_price)


# In[9]:


book_info = pd.pivot_table(
    author_price,
    index=['author_name'],
    columns=['cover'],
    values=['price'],
    aggfunc='sum',
    fill_value=0
)
print(book_info)


# In[10]:


book_info.to_pickle('book_info.pkl')


# In[11]:


book_info2 = pd.read_pickle('book_info.pkl')
print(book_info2)


# In[12]:


book_info.equals(book_info2)


import urllib
import urllib.request

def counting_sort(lst, key):
    elem_lst = []
    for i in range(127):
        elem_lst.append([])
    new_lst = []
    for elem in lst:
        elem_lst[key(elem)].append(elem)
    for l in elem_lst:
        for elem in l:
            new_lst.append(elem)
    return new_lst

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words_lst = book_to_words(book_url)
    print(len(words_lst))
    longest = len(max(words_lst, key=lambda x: len(x)))
    for i in range(longest):
        words_lst = counting_sort(words_lst, lambda b: 0 if i >= len(b) else b[-i])
    return words_lst
lst = radix_a_book()
print(len(lst))
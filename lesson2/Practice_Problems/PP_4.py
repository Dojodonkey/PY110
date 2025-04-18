'''
Problem Statement:
How would you sort the following list of dictionaries based on the year of publication of each book,
from the earliest to the most recent?
'''
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def get_year(dictionary):
    year = dictionary.get('published')
    return int(year)

def sort_by_year(lst):
    lst.sort(key=get_year)
    return lst

print(sort_by_year(books))

# Expected Result:
# Pretty printed for clarity
# [
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800'
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869'
#     },
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967'
#     }
# ]
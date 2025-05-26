'''
Write a function that, given a URL as a string, parses out just the domain
name and returns it.

Examples:
domain_name("http://github.com/carbonfive/raygun") # should return "github"
domain_name("https://www.cnet.com") # should return "cnet"


Problem
    - return domain name
    - input - string
    - output - string

E:
- observations:
    - urls commanality is '.com'
    - difference, sometimes 'www.' and sometimes 'https://'

D:
- strings and reassigning the input by stripping leading and trailing strings

High Level
    - lstrip - http://
    - use condtional to get rid of www.
    - split at .
    - return index -

'''
def domain_name(dom_string):
    # strip leading chars
    if dom_string.startswith('https://'):
        dom_string = dom_string.lstrip('https://')
    else:
        dom_string = dom_string.lstrip('http://')
    # check for leading 'www.'
    if dom_string.startswith('www.'):
        dom_string = dom_string.lstrip('www.')
    # return first string before '.'
    return dom_string.split('.')[0]



print(domain_name("http://github.com/carbonfive/raygun"))  # should return "github"
print(domain_name("https://www.cnet.com"))                 # should return "cnet"
print(domain_name("http://github.com/carbonfive/raygun"))  # github
print(domain_name("https://www.cnet.com"))                 # cnet
print(domain_name("www.xkcd.com"))                         # xkcd
print(domain_name("http://google.co.uk"))                  # google
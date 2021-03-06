import re

def mapper(key, value):
    page_name, text = value.split(':')
    page_number = page_name.split('-')[1]
    matches = re.findall('\w+', text)
    for word in matches:
        if len(word) < 4: continue
        yield word.lower(), page_number

def reducer(key, values):
    pageset = set()
    for pages in values:
        for page in pages.split(','):
            pageset.add(page)
    pagelist = list(pageset)
    pagelist.sort()
    yield key, ','.join(pagelist)

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper, reducer)

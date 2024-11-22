import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}
    
    # Check if feed has a title
    if not hasattr(d.feed, 'title'):
        print(f"Failed to parse feed {url}: 'title' attribute not found")
        return None, None
    
    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description
        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    
    return d.feed.title, wc

def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


apcount = {}
wordcounts = {}

# Load the list of feeds from the file
feedlist = [line.strip() for line in open('./datasets/feedlist.txt')]

for feedurl in feedlist:
    try:
        title, wc = getwordcounts(feedurl)
        if title is None:
            continue  # Skip this feed if there was an error

        wordcounts[title] = wc
        for word, count in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except Exception as e:
        print(f"Failed to parse feed {feedurl}: {e}")

# Filter words to include in the final wordlist
wordlist = []
for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5:
        wordlist.append(w)

# Write the output to a file
with open('./datasets/blogdata1.txt', 'w') as out:
    out.write('Blog')
    for word in wordlist:
        out.write(f'\t{word}')
    out.write('\n')
    for blog, wc in wordcounts.items():
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write(f'\t{wc[word]}')
            else:
                out.write('\t0')
        out.write('\n')
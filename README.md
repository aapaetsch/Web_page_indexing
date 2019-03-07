# webpage_indexing
## How To Use
- Creating the index
  - Currenty run by <python path> index_creation.py
  - Follow the directions in the terminal

## Description
This program creates an index from user entered URL's that can be queried after the index is created.<br />
Currenty only works on a link by link basis, eventually I wish to implement scraping and indexing all pages for a given site and<br />
allowing those to be calculated into the query. I also wish to eventually create a version that allows for pages to be added or<br />
removed from the index. The end goal for this program is for it to act like a mini search engine.

## Working features 
- Parsing data from raw html
- Stripping links from sites
- Individual inverted index creation
- Can add to the index after it has been created, repeat links will be ignored


## Not supported
- Indexing of subpages for a webpage
  - It would be easy to implement subpages where they contribute to the scores of the parent page
- Queries have not yet been added


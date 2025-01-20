import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    tm = dict()

    if len(corpus[page]) == 0:
        prob = 1/len(corpus)
        for p in corpus:
            tm[p] = prob
        return tm

    for p in corpus:
        if p not in corpus[page]:
            prob = (1-damping_factor)/len(corpus)
            tm[p] = prob
        else:
            prob = (damping_factor/len(corpus[page])) + (1-damping_factor)/len(corpus)
            tm[p] = prob

    return tm

    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    start = random.randrange(0, len(corpus))
    count = dict()
    i = 0
    # Choose random start page and initialise count values
    for p in corpus:
        if i == start:
            start_page = str(p)
            count[str(p)] = 1
        else:
            count[str(p)] = 0
        i += 1

    trans_mod = transition_model(corpus, start_page, damping_factor)

    for num in range(0, n):
        choice = []
        prob = []
        for p in trans_mod:
            choice.append(p)
            prob.append(trans_mod[p])
        ch_page = random.choices(choice, prob)
        page = ch_page[0]
        count[page] += 1
        trans_mod = transition_model(corpus, page, damping_factor)

    sam_pr = dict()
    for p in count:
        sam_pr[p] = count[p]/n

    return sam_pr

    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_rank = dict()
    new_rank = dict()
    N = len(corpus)

    for p in corpus:
        current_rank[p] = 1/N
        if len(corpus[p]) == 0:
            pages = set()
            for r in corpus:
                pages.add(r)
                corpus[p] = pages

    iter = True
    while iter == True:
        for p in current_rank:
            sigma = 0
            for r in corpus:
                if p in corpus[r]:
                    sigma += current_rank[r]/len(corpus[r])
            new_rank[p] = ((1-damping_factor)/N)+damping_factor*(sigma)

        for p in current_rank:
            for r in new_rank:
                if p == r:
                    diff = current_rank[p] - new_rank[p]
        if abs(diff) < 0.001:
            iter = False
        else:
            for p in current_rank:
                current_rank[p] = new_rank[p]
            new_rank.clear()

    return new_rank

    raise NotImplementedError


if __name__ == "__main__":
    main()

import os
import requests
from bs4 import BeautifulSoup

# This program downloads one or two books from WIKIBOOKS.ORG and compares the word frequencies

def download_book(book_name):
    url = "https://en.wikibooks.org/wiki/" + book_name
    req = requests.get(url, headers)  # http request to given url for connectiono
    soup = BeautifulSoup(req.content, 'html.parser')  # scraping the html of the website
    main_page = soup.find("div", class_="mw-parser-output")  # finds the div's with the class of mw-parser-output
    # because when you look at the html of the page
    # all the texts are in these divs
    page = main_page.find_all(["p", "li", "h2"])  # scraping the texts from paragraph, list items and headers
    all_text = []
    for i in page:
        all_text.append(i.text)  # appends all the found texts to a list

    with open(book_name + ".txt", "w", encoding="utf-8") as file:  # creates a text file with the book name
        file.writelines(all_text)  # writes all the text to text file
    print("The books was saved to " + os.getcwd() + " as " + book_name + ".txt")
    print("############################")


def word_freq_single(book_name, stopValue):
    words = []  # aynı kelimeler var
    words2 = []  # aynı kelimeler yok
    words3 = []
    print("Book Name : " + book_name)
    print("No\tFreq\tWord")

    # lines below opens the saved text file and puts every word in a list except the repeated ones
    with open(book_name + ".txt", "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                words.append(word.lower())

        for word in words:
            if word not in words2:
                words2.append(word)

        for word in words2:
            if word not in stop_list:  # if the word is a stop word dont add to list
                words3.append([words.count(word), word])  # words and their count times are pushed in to list

        words3.sort(reverse=True)

        for i in range(stopValue):  # stopValue is the input from user for how many words does he/she wants to see.
            print(str(i + 1) + "\t", end=" ")

            for j in range(len(words3[i])):
                print(words3[i][j], end="       ")

            print()


def common_words(book_name, book_name2):
    words = []  # aynı kelimeler var
    words2 = []  # aynı kelimeler yok
    words3 = []
    #######
    words4 = []  # aynı kelimeler var
    words5 = []  # aynı kelimeler yok
    words6 = []
    common_word_list = []

    with open(book_name + ".txt", "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                words.append(word.lower())

        for word in words:
            if word not in words2:
                words2.append(word)

        for word in words2:
            if word not in stop_list:  # if the word is a stop word dont add to list
                words3.append([words.count(word), word])

        words3.sort(reverse=True)

    with open(book_name2 + ".txt", "r", encoding="utf-8") as file2:
        for line in file2:
            for word in line.split():
                words4.append(word.lower())

        for word in words4:
            if word not in words5:
                words5.append(word)

        for word in words5:
            if word not in stop_list:  # if the word is a stop word dont add to list
                words6.append([words4.count(word), word])

        words6.sort(reverse=True)

    print("########################")
    print("Book Names : " + book_name + "\t" + book_name2)
    print("Common Words")
    print("No\tFreq\tWord")

    common_word_list = [word for word in words3 if
                        word in words6]  # this line finds the common words in both of the books
    # then prints it with for loops
    not_common_word_list = [word for word in words3 if word not in words6] #finds the not common words

    for i in range(len(common_word_list)):
        print(str(i + 1) + "\t", end=" ")

        for j in range(len(common_word_list[i])):
            print(common_word_list[i][j], end="       ")

        print()
    # printing the distinct words
    print("########################")
    print("Book Names : " + book_name + "\t" + book_name2)
    print("Distinct Words")
    print("No\tFreq\tWord")
    for i in range(stopValue):
        print(str(i + 1) + "\t", end=" ")

        for j in range(len(not_common_word_list[i])):
            print(not_common_word_list[i][j], end="       ")

        print()


def main():  # calls the methods according to user input
    if book_number == 1:
        download_book(book_name)
        word_freq_single(book_name, stopValue)
    elif book_number == 2:
        download_book(book_name)
        download_book(book_name2)
        word_freq_single(book_name, stopValue)
        print("#######################################")
        word_freq_single(book_name2, stopValue)
        common_words(book_name, book_name2)


# below are the stop words in english language
stop_words = """a
about
above
after
again
against
all
am
an
and
any
are
aren't
as
at
be
because
been
before
being
below
between
both
but
by
can't
cannot
could
couldn't
did
didn't
do
does
doesn't
doing
don't
down
during
each
few
for
from
further
had
hadn't
has
hasn't
have
haven't
having
he
he'd
he'll
he's
her
here
here's
hers
herself
him
himself
his
how
how's
i
i'd
i'll
i'm
i've
if
in
into
is
isn't
it
it's
its
itself
let's
me
more
most
mustn't
my
myself
no
nor
not
of
off
on
once
only
or
other
ought
our
ours
ourselves
out
over
own
same
shan't
she
she'd
she'll
she's
should
shouldn't
so
some
such
than
that
that's
the
their
theirs
them
themselves
then
there
there's
these
they
they'd
they'll
they're
they've
this
those
through
to
too
under
until
up
very
was
wasn't
we
we'd
we'll
we're
we've
were
weren't
what
what's
when
when's
where
where's
which
while
who
who's
whom
why
why's
with
won't
would
wouldn't
you
you'd
you'll
you're
you've
your
yours
yourself
yourselves"""

stop_list = stop_words.split()  # stop words string is converted to a list

headers = {  # these headers for tricking the website. because some websites dont want web scrapers
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}
print("How many books do you want to download: (type 1 or 2 ) :  ")
book_number = int(input())
print("How many words do you want to see: ")
stopValue = int(input())
book_name2 = ""
if book_number == 1:
    print("Please enter a book name from wikibooks.org (Case sensitive): ", end="")
    book_name = input()
    main()
elif book_number == 2:
    print("Please enter the first books name from wikibooks.org (Case sensitive): ", end="")
    book_name = input()
    print("Please enter the second books name from wikibooks.org (Case sensitive): ", end="")
    book_name2 = input()
    main()

# Python 2.7
# Note: This is a rough draft for Reddit user calmatt; it is not meant to be pretty.
# Goes to the zkillboard.com killmail link provided and stores the dropped 
# items list into a text file in highest to lowest ISK value order.

from bs4 import BeautifulSoup   # Web scraping
import urllib   # Access internet and make network requests

def read_killmail(url):
    # Identify the code that makes the killmail page.
    soup = BeautifulSoup(urllib.urlopen(url).read(), "html.parser")
    # Identify the area of code which contains relevant information.
    items = soup.find_all("tr", class_="item_dropped_row")
    # Prepare for the list of items.
    item_database = []

    # For each item in the relevant information...
    # Note: [2:-1] skips the irrelevant info on the outsides of what we want.
    for item in items[2:-1]:
        # Split the information (name, quantity, and price) into chunks
        raw_data = item.get_text().split()

        # Label each chunk appropriately
        name = ' '.join(raw_data[:-2])
        quantity, price = raw_data[-2:]
        # Replace commas in the price so we can sort by price.
        price = price.replace(',', '')

        # Put it all together and store it in our database.
        item_info = [name, quantity, price]
        item_database.append(item_info)

    # Sort by price
    sorted_database = sorted(item_database, key=lambda item_info: float(item_info[2]))

    # Create or open text file named 'loot.txt' and prepare to write in it.
    f = open('loot.txt', 'w')
    # Reverse the database so it goes by highest price first then..
    for item in reversed(sorted_database):
        # Add some formatting to make it more readable
        clean_text = '  ||  '.join(item)
        # Then write it to the file and we're done!
        # Note: We use 'try' and 'except' to make sure the program runs
        #   even if there is a unicode error.
        try:
            f.write("{0}\n".format(clean_text))
        except:
            f.write("<ERROR: Unicode error.>")
    print("All done! Check your file now. ^^")

read_killmail(raw_input('Paste killmail URL here: '))

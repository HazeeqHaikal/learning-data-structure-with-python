import sys
from load import load_strings

names = load_strings(sys.argv[1])


search_names = ["Titus", "Harv", "Wolfgang", "Moshe", "Len", "Cosmo", "Bernd", "Tray", "Derrin", "Garry", "Tomlin", "Pace", "Wilfrid", "Ulysses", "Uli", "Ave", "Val", "Todd", "Chrissy", "Terry", "Mischa", "Elwood", "Earl", "Alec", "Demetrius", "Fulton", "Zechariah", "Wolfram", "Jeth", "Sergent", "Jotham", "Ferguson", "Andreas", "Thaine", "Eduardo", "Thorny", "Ambrosi", "Keil", "Ephrem", "Socrates", "Reinhard", "Gary", "Joaquin", "Beowulf", "Ritchie", "Denis", "Abraham", "Wynton", "Robinson", "Solly",
                "Dell", "Rahul", "Archibald", "Robbert", "Melvyn", "Virgie", "Douggie", "Anton", "Janus", "Ajai", "Obadias", "Winslow", "Tobie", "Corby", "Drew", "Sascha", "Ferdinand", "Shaine", "Harman", "Elvis", "Bruno", "Germaine", "Halvard", "Urson", "Wolfy", "Duffy", "Hervey", "Phillip", "Merry", "Geoffry", "Burke", "Thadeus", "Immanuel", "Ansel", "Horatius", "Randall", "Lawton", "Aguste", "Felipe", "Derrick", "Torre", "Sanson", "Winford", "Pasquale", "Vance", "Neddie", "Sterling", "Wait", "Davoud", "Guthrey"]

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None


for n in names:
    index = index_of_item(names, n)
    print(index)

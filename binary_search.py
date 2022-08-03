import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = ["Titus", "Harv", "Wolfgang", "Moshe", "Len", "Cosmo", "Bernd", "Tray", "Derrin", "Garry", "Tomlin", "Pace", "Wilfrid", "Ulysses", "Uli", "Ave", "Val", "Todd", "Chrissy", "Terry", "Mischa", "Elwood", "Earl", "Alec", "Demetrius", "Fulton", "Zechariah", "Wolfram", "Jeth", "Sergent", "Jotham", "Ferguson", "Andreas", "Thaine", "Eduardo", "Thorny", "Ambrosi", "Keil", "Ephrem", "Socrates", "Reinhard", "Gary", "Joaquin", "Beowulf", "Ritchie", "Denis", "Abraham", "Wynton", "Robinson", "Solly",
                "Dell", "Rahul", "Archibald", "Robbert", "Melvyn", "Virgie", "Douggie", "Anton", "Janus", "Ajai", "Obadias", "Winslow", "Tobie", "Corby", "Drew", "Sascha", "Ferdinand", "Shaine", "Harman", "Elvis", "Bruno", "Germaine", "Halvard", "Urson", "Wolfy", "Duffy", "Hervey", "Phillip", "Merry", "Geoffry", "Burke", "Thadeus", "Immanuel", "Ansel", "Horatius", "Randall", "Lawton", "Aguste", "Felipe", "Derrick", "Torre", "Sanson", "Winford", "Pasquale", "Vance", "Neddie", "Sterling", "Wait", "Davoud", "Guthrey"]


def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


for n in search_names:
    result = binary_search(names, n)
    print(result)

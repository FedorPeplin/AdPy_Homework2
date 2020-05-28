import json
import wget
import hashlib

def recieving_countries_list():

    url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
    wget.download(url, 'сountries.json')


    handle = open("сountries.json", "r")
    data = json.load(handle)
    countries_list=[]
    final_names_list=[]
    for items in data:
        countries_list.append (items['name']['common'])
    for elements in countries_list:
        final_name = elements.split()
        final_name = '_'.join(final_name)
        final_names_list.append(final_name)
    handle.close()
    return final_names_list


class Iterator:

    def __init__(self, lst):
        self.lst = lst
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self.lst[self.start]
        except IndexError:
            raise StopIteration
        self.start += 1

        return value + ' – ' + 'https://en.wikipedia.org/wiki/' + value + '\n' + '\n'


if __name__ == '__main__':
    list=recieving_countries_list()
    with open('country_with_link.txt', 'w', encoding="utf-8") as file_with_links:
        for item in Iterator(list):
            file_with_links.write(item)

    def generator():
        original_file = open('сountries.json', 'r')
        lines=original_file.readlines()
        for line in lines:
            yield hashlib.md5(line.encode())

    mygenerator=generator()
    with open('hex-codes.txt', 'w') as hashfile:
        for element in mygenerator:
            hashfile.write(element.hexdigest()+'\n')
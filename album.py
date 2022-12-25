from song import *


class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []


    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def addSongs(self, *new_songs):
        counter = 0

        for j in new_songs:
            if self.__songs == []:
                counter += 1
                self.__songs.append(j)
                continue

            flag = True
            for i in self.__songs:
                if not ((i.getTitle() != j.getTitle()) or (i.getReleaseYear() != j.getReleaseYear()) or (i.getDuration() != j.getDuration())):
                    flag = False
                    break
            if flag:
                counter+=1
                self.__songs.append(j)        
            


        return counter



    def sortBy(self, byKey, reverse):
        return self.__songs.sort(key=byKey, reverse=reverse)

    def sortByName(self, reverse):
        return self.sortBy(lambda x: x.getTitle(), reverse)
    
    def sortByPopularity(self, reverse):
        return self.sortBy(lambda x: x.getLikes(), reverse)

    def sortByDuration(self, reverse):
        return self.sortBy(lambda x: x.getDuration(), reverse)

    def sortByReleaseYear(self, reverse):
        return self.sortBy(lambda x: x.getReleaseYear(), reverse)


    def helperTotalLikes(self):
        likes = []
        amount = 0
        for i in self.__songs:
            likes.append(i.getLikes())
        for i in likes:
            amount = amount + i
        return amount



    def __str__(self):
        songString = '{'
        for i in self.__songs:
            songString+=str(i) + '|'
        if self.__songs==[]:
            songString = "{}"
        return f'Title:{self.__title},Release year:{self.__releaseYear},songs:{songString[:-1]+"}"}'



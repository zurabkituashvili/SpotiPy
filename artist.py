from song import *
from album import *


class Artist:
    def __init__(self, firstName, lastName, birthYear):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = []
        self.__singles = []


    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingles(self):
        return self.__singles



    def addAlbum(self, *newAlbum):

        for j in newAlbum:
            if self.__albums == []:
                self.__albums.append(j)
                continue

            flag = True
            for i in self.__albums:
                if not ((i.getTitle() != j.getTitle()) or (i.getReleaseYear() != j.getReleaseYear())):
                    flag = False
                    break
            if flag:
                self.__albums.append(j)        



    def addSingles(self, *newSingle):

        for j in newSingle:
            if self.__singles == []:
                self.__singles.append(j)
                continue

            flag = True
            for i in self.__singles:
                if not ((i.getTitle() != j.getTitle()) or (i.getReleaseYear() != j.getReleaseYear()) or (i.getDuration() != j.getDuration()) or i.getLikes() != j.getLikes()):
                    flag = False
                    break
            if flag:
                self.__singles.append(j)        





    def mostLikedSong(self):
        likes1 = []
        for i in self.__albums:
            for j in i.getSongs():
                likes1.append(j.getLikes())
        likes1.sort()
        if likes1 != []:
            mostLiked=likes1[-1]


        likesOfSingles1 = []
        for i in self.__singles:
            likesOfSingles1.append(i.getLikes())
        likesOfSingles1.sort()
        if likesOfSingles1 != []:
            mostLikedSingle = likesOfSingles1[-1]


        mostLikedSongVar = 0
        if likes1 != [] and likesOfSingles1 != []:
            if mostLiked >= mostLikedSingle:
                if mostLiked != []:
                    mostLikedSongVar = mostLiked

            else:
                if mostLikedSingle!=[]:
                    mostLikedSongVar = mostLikedSingle


        if likes1 == [] and likesOfSingles1 != []:
            mostLikedSongVar = mostLikedSingle
        
        if likesOfSingles1 == [] and likes1 != []:
            mostLikedSongVar = mostLiked


        for i in self.__albums:
            for j in i.getSongs():
                if j.getLikes() == mostLikedSongVar:
                    return j

        for a in self.__singles:
            if a.getLikes() == mostLikedSongVar:
                return a


        


    def leastLikedSong(self):
        likes1 = []
        for i in self.__albums:
            for j in i.getSongs():
                likes1.append(j.getLikes())
        likes1.sort()
        if likes1 != []:
            leastLiked=likes1[:1]


        likesOfSingles1 = []
        for i in self.__singles:
            likesOfSingles1.append(i.getLikes())
        likesOfSingles1.sort()
        if likesOfSingles1 != []:
            leastLikedSingle = likesOfSingles1[:1]


        leastLikedSongVar = 0
        if likes1 != [] and likesOfSingles1 != []:
            if leastLiked <= leastLikedSingle:
                if leastLiked != []:
                    leastLikedSongVar = leastLiked[0]

            else:
                if leastLikedSingle!=[]:
                    leastLikedSongVar = leastLikedSingle[0]


        if likes1 == [] and likesOfSingles1 != []:
            leastLikedSongVar = leastLikedSingle[0]
        
        if likesOfSingles1 == [] and likes1 != []:
            leastLikedSongVar = leastLiked[0]


        for i in self.__albums:
            for j in i.getSongs():
                if j.getLikes() == leastLikedSongVar:
                    return j

        for a in self.__singles:
            if a.getLikes() == leastLikedSongVar:
                return a



    def totalLikes(self):
        global totLikes
        totalLikes = []
        amount = 0
        for i in self.__albums:
            for j in i.getSongs():
                totalLikes.append(j.getLikes())
        for k in totalLikes:
            amount+=k
        
        totalLikesOfSingles = []
        singlesAmount = 0
        for i in self.__singles:
                totalLikesOfSingles.append(i.getLikes())
        for k in totalLikesOfSingles:
            singlesAmount+=k
        totLikes = amount + singlesAmount
        return totLikes
        

    def __str__(self):
        totLikes = 0
        totalLikes = []
        amount = 0
        for i in self.__albums:
            for j in i.getSongs():
                totalLikes.append(j.getLikes())
        for k in totalLikes:
            amount+=k
        
        totalLikesOfSingles = []
        singlesAmount = 0
        for i in self.__singles:
                totalLikesOfSingles.append(i.getLikes())
        for k in totalLikesOfSingles:
            singlesAmount+=k
        totLikes = amount + singlesAmount

        
        return f'Name: {self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{totLikes}'
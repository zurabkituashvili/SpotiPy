from song import *
from album import *
from artist import *
class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *newArtist):
        for j in newArtist:
            if self.__artists == []:
                self.__artists.append(j)
                continue

            flag = True
            for i in self.__artists:
                if not ((i.getFirstName() != j.getFirstName()) or (i.getLastName() != j.getLastName()) or  (i.getBirthYear() != j.getBirthYear())):
                    flag = False
                    break
            if flag:
                self.__artists.append(j)


    

    def getTopTrendingArtist(self):
        if self.__artists != []:
            artistLikes = []
            for l in self.__artists:
                artistLikes.append(l.totalLikes())
            artistLikes.sort()
            trendingArtist = artistLikes[-1]


            for j in self.__artists:
                if j.totalLikes() == trendingArtist:
                    return (j.getFirstName(), j.getLastName())
        else:
            return None



    def getTopTrendingAlbum(self):
        if self.__artists != []:
            albumLikes = []
            for i in self.__artists:
                for j in i.getAlbums():
                    albumLikes.append(j.helperTotalLikes())

            albumLikes.sort()
            trendingAlbum = albumLikes[-1]
            for artists in self.__artists:
                for albums in artists.getAlbums():
                    if albums.helperTotalLikes() == trendingAlbum:
                        return albums
        else:
            return None


        


    def getTopTrendingSong(self):
        mostLiked = 0
        topLikes = []
        for i in self.__artists:
            for j in i.getAlbums():
                for l in j.getSongs():
                    topLikes.append(l.getLikes())
        for k in topLikes:
            if k >= mostLiked:
                mostLiked = k


        topLikedSingle = 0
        topLikesOfSingles = []
        for i in self.__artists:
            for j in i.getSingles():
                topLikesOfSingles.append(j.getLikes())

        for k in topLikesOfSingles:
            if k >= topLikedSingle:
                topLikedSingle = k

        
        topLikedSongVar = 0
        if mostLiked >= topLikedSingle:
            topLikedSongVar = mostLiked
        else:
            topLikedSongVar = topLikedSingle

        for albums in self.__artists:
            if albums.getAlbums() != []:
                for i in albums.getAlbums():
                    for j in i.getSongs():
                        if j.getLikes() == topLikedSongVar:
                            return j


        for singles in self.__artists:
            for i in singles.getSingles():
                if i.getLikes() == topLikedSongVar:
                    return i


    def loadFromFile(self):
        pass



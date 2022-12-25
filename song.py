class Song:
    def __init__(self, title, releaseYear, duration=60, likes=0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getDuration(self):
        return self.__duration
    def getLikes(self):
        return self.__likes

    
    def setDuration(self, new):
        if new < 0:
            return False
        if new > 720:
            return False
        if new == self.__duration:
            return False
        else:
            self.__duration=new
            return True

    def like(self):
        self.__likes+=1
        return self.__likes
    
    def unlike(self):
        self.__likes-=1
        return self.__likes

    def __str__(self):
        durationBy60 = ''
        if self.__duration%60==0:
            durationBy60+=str(int(self.__duration/60))
        else:
            durationBy60+=str(self.__duration/60)
        return f'Title:{self.__title},Duration:{durationBy60} minutes,Release year:{self.__releaseYear},Likes:{self.__likes}'




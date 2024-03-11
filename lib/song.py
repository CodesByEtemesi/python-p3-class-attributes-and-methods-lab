class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genre not in cls.genres:
            cls.genres.append(cls.genre)

    @classmethod
    def add_to_artists(cls):
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre not in cls.genre_count:
            cls.genre_count[cls.genre] = 1
        else:
            cls.genre_count[cls.genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        if cls.artist not in cls.artist_count:
            cls.artist_count[cls.artist] = 1
        else:
            cls.artist_count[cls.artist] += 1

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
single_ladies = Song("Single Ladies", "Beyonce", "Pop")
hello = Song("Hello", "Adele", "Pop")

print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.artists)  # Output: ['Jay-Z', 'Beyonce', 'Adele']
print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 2}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Beyonce': 1, 'Adele': 1}

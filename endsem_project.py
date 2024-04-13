class Song:
    def __init__(self, name, artist, album, genre, year):
        self.name = name
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = year

class Playlist:
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, playlist_name):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = []
            print("Playlist Created Successfully!  :>)")
        else:
            print("Playlist Already Exists :|")

    def view_playlists(self):
        if self.playlists:
            print("Available playlists:")
            for playlist in self.playlists:
                print("->", playlist)
        else:
            print("No Playlist Available :(")

    def add_song_to_playlist(self, playlist_name, song_title):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append(song_title)
            print("Song Added to the playlist Successfully!!!!!")
        else:
            print("SORRY, Playlist  does not found :( ")

class MusicLibrary:
    def __init__(self):
        self.song_library = []

    def add_song(self, name, artist, album, genre, year):
        self.song_library.append(Song(name, artist, album, genre, year))
        print("Song Added Successfully :)")

    def search_song(self, search_term):
        found = False
        for song in self.song_library:
            if search_term.lower() in song.name.lower() or search_term.lower() in song.artist.lower():
                print("\nName:", song.name)
                print("Artist:", song.artist)
                print("Album:", song.album)
                print("Genre:", song.genre)
                print("Year:", song.year)
                print()
                found = True
        if not found:
            print("Song not found :( ")

# Example usage

music_library = MusicLibrary()
playlists = Playlist()

while True:
        print("\nMusic Library Management System")
        print("1. Add new Song")
        print("2. Manage YOur Playlists")
        print("3. Search for a Song")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter song name: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            genre = input("Enter genre: ")
            year = input("Enter year: ")
            music_library.add_song(name, artist, album, genre, year)

        elif choice == '2':
            print("\nPlaylist Management")
            print("1. Create a new playlist")
            print("2. View playlists")
            print("3. Add a song to a playlist")
            playlist_choice = input("Enter your choice: ")
            if playlist_choice == '1':
                playlist_name = input("Enter the name of the new playlist: ")
                playlists.create_playlist(playlist_name)
            elif playlist_choice == '2':
                playlists.view_playlists()
            elif playlist_choice == '3':
                playlist_name = input("Enter the name of the playlist: ")
                song_title = input("Enter the title of the song to add: ")
                playlists.add_song_to_playlist(playlist_name, song_title)

        elif choice == '3':
            search_term = input("Enter the title or artist of the song to search: ")
            music_library.search_song(search_term)

        elif choice == '4':
            print("Thank you :) for using the Music Library Management System!")
            break

        else:
            print("Invalid choice :>")
            print("Please enter a number from 1 to 4 :>")

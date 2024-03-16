# Function to add a new song to the library
def add_song(song_library):
    print("\nEnter the details of the song:  ")
    name = input("name: ")
    artist = input("Artist: ")
    album = input("Album: ")
    genre = input("Genre: ")
    year = input("Year: ")

    song_library.append({
        'Name': name,
        'artist': artist,
        'album': album,
        'genre': genre,
        'year': year
    })
    print("Song added successfully!")

# Function to manage playlists
def manage_playlists(playlists):
    print("\n1. Create a new playlist")
    print("2. View playlists")
    print("3. Add a song to a playlist")
    choice = input("Enter your choice: ")

    if choice == '1':
        playlist_name = input("Enter the name of the new playlist: ")
        playlists[playlist_name] = []
        print("Playlist created successfully!")

    elif choice == '2':
        print("Available playlists:")
        for playlist in playlists:
            print("-", playlist)

    elif choice == '3':
        playlist_name = input("Enter the name of the playlist: ")
        if playlist_name in playlists:
            song_title = input("Enter the title of the song to add: ")
            playlists[playlist_name].append(song_title)
            print("Song added to the playlist successfully!")
        else:
            print("Playlist not found.")

# Function to search for a song
def search_song(song_library):
    search_term = input("\nEnter the name or artist of the song to search: ")
    found = False
    for song in song_library:
        if search_term.lower() in song['name'].lower() or search_term.lower() in song['artist'].lower():
            print("\nName:", song['name'])
            print("Artist:", song['artist'])
            print("Album:", song['album'])
            print("Genre:", song['genre'])
            print("Year:", song['year'])
            print()
            found = True
    if not found:
        print("Song not found.")


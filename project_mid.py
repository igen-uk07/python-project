from main_project import add_song
from main_project import manage_playlists
from main_project import search_song

def main():
    song_library = []  # List to store songs
    playlists = {}  # Dictionary to store playlists

    while True:
        print("\n-- Music Library--")
        print("1. Add a song")
        print("2. Manage playlists")
        print("3. Search for a song")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_song(song_library)
        elif choice == '2':
            manage_playlists(playlists)
        elif choice == '3':
            search_song(song_library)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
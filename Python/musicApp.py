music = (('Green Day',
         [
            (1, "Somewhere Now"),
            (2, "Bang Bang"), 
            (3, "Revolution Radio"),
            (4,  "Say Goodbye"),
            (5, "Outlaws")
            ]),
        ("Metallica",
        [
            (1, "Battery"),
            (2, " Master of Puppets"),
            (3, "The Thing That Should Not Be"),
            (4, "Welcome Home (Sanitarium)")
        ]),
        ("U2", 
        [
            (1, "The Miracle"),
            (2, "Every Breaking Wave"),
            (3, "California"),
            (4, " Song for Someone"),
            (5, "Iris (Hold Me Close)")
        ])
      )

def printPlaylist():
    for bIndex, band in enumerate(music):
        name , songs = band
        for songNo, songname in songs:
            print(f"{bIndex+1}.{songNo} {name} - {songname}")

printPlaylist()

while True:     
    selectedSong = input("Select a song to play using number:'(1:1)' - ")
    bandno = int(selectedSong[0])
    songNo = int(selectedSong[2])
    bandName = music[bandno -1][0]
    for songno, songName in music[bandno -1][1]:
        if songno == songNo:
            print(f"{bandName} - {songName} playing now...")
    changeSong = input("Press C to change song or any letter to quit APP: ").upper()
    if changeSong != 'C':
        break


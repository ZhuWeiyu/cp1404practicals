'''
CP1404 Assignment 1:
Student Name: Weiyu Zhu
Student ID: 14187098
'''

import csv
is_finished = True   # Kind of using while true
total = -1  # This is a name for count how many element in songs_list
count = 0   # To count how many songs not learned
counts = 0  # To count how many song user already learned
with open('data.csv', 'r') as f:  # open the csv file
    wen = csv.reader(f)           # read it and list it
    songs_list = list(wen)

print("Songs to Learn 1.0 - by Lindsay Ward")
print("6 songs loaded")

def main():
    Menu = '''Menu:   
L - List songs
A - Add new song
C - Complete a song
Q - Quit'''   # To set the menu list
    while True:   # To set a recycle make sure it can be asked when the wrong choose comes out
        print(Menu)
        choose = input(">>> ").upper()
        if choose == "L":  # To explain l-choice
            get_l(songs_list, total, count, counts)
        if choose == "A":  # To explain a_choice
            get_a(songs_list)
        if choose == "C":  # TO explain c_choice
            get_c(songs_list)
        if choose == "Q":  # When you quit, what will happen
            get_q(songs_list)
            print(f"{counts} songs has been loaded in data.csv")  # Count how many song we already learned
            print("Have a nice day!")
            exit()   # quit


def get_l(songs_list, total, count, counts):
    for song in songs_list:   # use for function to count how many element are there in songs_list
        total += 1            # every time count 1 element total plus 1, better to get the 0 to n(the total element -1)
        if song[3] == "u":    # when there are "u" in list
            count += 1        # count the unread song
            print(f"{total}. * {song[0]:<35}\t- {song[1]:30}\t({song[2]})")  # To print formal of song
        else:
            counts += 1       # To count how many song you already learned
            print(f"{total}.   {song[0]:<35}\t- {song[1]:30}\t({song[2]})")  # print it with the same formal

    print(f"{counts} songs learned,{count} songs still to learn")  # To show the user how many songs already learned,how
                                                                   # many not
def get_a(songs_list):   # to explain when the function of a_choice
    global title_song, artist_of_song, input_year   # To put function to get_a
    while True:
        title_song = input("Title: ")  # put title_song here
        if title_song == "":           # when there are nothing here, it should ask user reput
            print("Input can not be blank")
        else:                          # otherwise,stop while and come to next step
            break
    while True:
        artist_of_song = input("Artist: ")   # put artist in here
        if artist_of_song == "":    # when there are nothing here, it should ask user reput
            print("Input can not be blank")
        else:
            break   # otherwise,stop while and come to next step
    while True:
        try:        # estimate value
            while is_finished != False: # while true
                input_year = int(input("Year: "))   # evaluate the year
                if input_year < 0:    # year < 0, remind user
                    print("Number must be >= 0")
                else:    # otherwise, comes to next step
                    break
        except ValueError:   # when there are no number or wrong combination input , it should evaluate as wrong
            print("Invalid input; enter a valid number")
        else:
            a = "u"    # added song must be new, so add * to mark as new
            b = [title_song, artist_of_song, str(input_year), a]   # to set a formal added to lst
            add_song = f"{title_song} by {artist_of_song} {input_year} added to song list"  # formal of printing
            print(add_song)  # print the add_song formal
            songs_list.insert(4,b)   # insert it into the fourth element of the list
            break


def get_c(songs_list):
    if not 'u' in [i[3] for i in songs_list]:   # add a function when no songs is unread to tell user, no songs now
        print('No songs to learn now!')
    else:
        while True:
            try:   # use try except function to think
                t = -1   # this is for assist song_list from 0 to n
                a_number = int(input("Enter the number of a song to mark as learned: "))
                for i in songs_list:
                    t += 1  # make the number before the list
                if a_number < 0:  # when number < 0
                    print("Number must be >= 0")
                elif a_number > t:  # when number > the hole number of list of song then
                    print("Invalid number input")
                elif 0 <= a_number <= t:    # when it's ok
                    if songs_list[a_number][3] == 'u':   # when it is u, change it to l
                        songs_list[a_number][3] = "l"
                        print(f"{songs_list[a_number][0]} by {songs_list[a_number][1]} has been learned")
                    elif songs_list[a_number][3] == 'l':  # when it is l, tell user it's already learned
                        print(f"You have already learned {songs_list[a_number][1]}")
                    break
            except ValueError:   # when there are no number or wrong combination of number, tell user
                print("Invalid input; enter a valid number")


def get_q(songs_list):   # when u quit what will happen
    with open('data.csv', 'w', newline="") as file:
        csvf = csv.writer(file)  # write all element into csv file
        csvf.writerows(songs_list)


main()
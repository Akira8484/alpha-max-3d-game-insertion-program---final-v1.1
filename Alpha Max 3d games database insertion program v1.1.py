"""This is my first python program, it's fully fuctional but can be improved on
feel free to edit it or suggest better ways to do it, look out for future versions.
Description : Program to automatically add games to the Alpha Max 3d games datbase(games.db) with user input"""

#import sqlite3 module to connect to database files
import sqlite3

# print name of program
print ("Alpha Max 3D Games Database Insertion Program v1.0: ")
print ("Brought to you by Mr. Matt's Arcade - mrmattsrcade.com , facebook.com/mrmattarcade: ")
print ("--" * 79)

#define function to not allow a blank input
def get_non_blank_input(prompt):
    while True:
        try:
            value = (input(prompt))
        except ValueError:
                print("Oops! try again...: ")
                continue
        if value == (""):
            print("Oops!  can't be blank.  Try again...: ")
            continue
        else:
            break
    return value

# while loop
while True:
    try:
        #check to end program
        check = input("Press Enter to start, or type 'quit' to exit: ")

        if check == 'quit':
            print("Program Closed, Goodbye: ")
            break
        
        #get user input from keyboard
        #use previously defined function to prevent blank input
        k_game = get_non_blank_input("Rom Name: ")        
        k_suffix = get_non_blank_input("File Extension: ")
        k_display_name = get_non_blank_input("Display Name: ")
        k_en_match = get_non_blank_input("Search Name: ")
        k_path = get_non_blank_input("File Path: Example /sdcard/game/cps: ")
        
        #continue after invalid entry
        while True:
            try:
                k_game_type = int(input("Emulator number 0-30, refer to start_game.sh for available cores: "))
        
            except ValueError:
                print("Oops!  That was not a number.  Try again...: ")
                continue
            if k_game_type >= 31:
                print("Out of range, try again...: ")
            else:
                break
            
        while True:
            try:
                k_mode = int(input("3D or 2D game?: 1=3d, 2=2d: "))
                
            except ValueError:
                print("Oops!  That was not a number.  Try again...: ")
                continue
            if k_mode >= 3:
                print ("wrong number, Try again...: ")
            else:
                 break
                
        while True:
            try:
                k_vert = int(input("Vertical: 1=Yes 0=No: "))
                
            except ValueError:
                print("Oops!  That was not a number.  Try again...")
                continue
            if k_vert >= 2:
                print ("wrong number, Try again ...: ")
            else:
                break
            
        #connect to games.db database file
        conn = sqlite3.connect('games.db')

        #sql statement to insert into the tbl_game with some default values as well as our user input values
        sql = """ INSERT INTO tbl_game
        (gameid, game, suffix,video_id, game_type, hard, path, mode, vert, en_match, sp_match, zh_match)
            VALUES ((SELECT MAX(gameid)+1 FROM tbl_game),'{}','{}',
            (SELECT MAX(gameid)+1 FROM tbl_game),'{}', 0, '{}','{}','{}','{}','{}','{}');""".format(
                k_game, k_suffix, k_game_type, k_path, k_mode, k_vert, k_en_match, k_en_match, k_en_match )

        #executing first insert statement 
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print ("Insert into tbl_game OK: ")
        cursor.close()

        conn = sqlite3.connect('games.db')

        #sql insert statement for tbl_en with max id from tbl_game and user input
        sql2 = "INSERT INTO tbl_en (id, title) VALUES ( (SELECT MAX(gameid) FROM tbl_game), '{}');".format( k_display_name )

        #executing second insert statement 
        cursor = conn.cursor()
        cursor.execute(sql2)
        conn.commit()
        print ("Insert into tbl_en OK: ")
        cursor.close()

        
        conn = sqlite3.connect('games.db')

        #insert statement for tbl_en_match with max id from tbl_game and user input
        sql3 = "INSERT INTO tbl_en_match (id, match) VALUES ( (SELECT MAX(gameid) FROM tbl_game), '{}');".format( k_en_match )

        #executing last insert statement 
        cursor = conn.cursor()
        cursor.execute(sql3)
        conn.commit()
        print ("Insert into tbl_en_match OK: ")
        cursor.close()
        
    # database entry error    
    except sqlite3.Error as e:
        print ("Error while inserting data, Check if database file is present and try again... : ", e)

    #end loop, close database connection
    finally:
        if (conn):
            conn.close()
            print ("Connection closed, Game on my friends: ")
                               


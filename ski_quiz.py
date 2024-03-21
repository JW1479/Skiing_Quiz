#Modulimport
import random
from quiz_katalog import questions, points
import os
import time

last_score_player1 = 0
last_score_player2 = 0
highscore_player1 = 0
highscore_player2 = 0
questions_open = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                  "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

#Funktionsdefinitionen für Einzel- und Mehrspieler
def play():
      global highscore_player1
      global highscore_player2
      global questions_open
      counter_player1 = 0
      counter_player2 = 0

      print(f"""{name_player1} mach dich bereit! Hier kommen deine 10 Fragen.
Schaffst du es deinen heutigen Highscore von {highscore_player1} Punkten zu übertreffen?""")
      clear(2)
      for number in range(1,11):
            question_choice = random.choice(questions_open)
            questions_open.remove(question_choice)
            print(f"Frage {number}:", questions[question_choice]["question"])
            print("       A:", questions[question_choice]["A"])
            print("       B:", questions[question_choice]["B"])
            print("       C:", questions[question_choice]["C"])
            print("       D:", questions[question_choice]["D"])

            still_answering = True
            while still_answering:
                  print()
                  answer = input("Bitte gib deine Antwort ein: ").upper()
                  if answer != "A" and answer != "B" and answer != "C" and answer != "D":
                        print("Bitte gib eine gültige Antwort ein.")
                  else:
                        if answer == questions[question_choice]["answer"]:
                              print("Das ist richtig! Das gibt einen Punkt für dich!")
                              still_answering = False
                              counter_player1 = counter_player1+1
                        else:
                              print(f"Leider war dies nicht richtig. Die richtige Antwort wäre {questions[question_choice]['answer']}!")
                              still_answering = False

            if questions_open == []:
                  questions_open =  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                  "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", ]

            clear(2)

      if another_player == "2":
            print(f"""{name_player2} du bist dran! Hier kommen deine 10 Fragen.
Schaffst du es mehr Fragen richtig zu beantworten als {name_player1}?
Oder schaffst du es sogar deine Bestleistung von {highscore_player2} zu schlagen?""")
            clear(3.5)
            for number in range(1, 11):
                  question_choice = random.choice(questions_open)
                  questions_open.remove(question_choice)
                  print(f"Frage {number}: ", questions[question_choice]["question"])
                  print("        A:", questions[question_choice]["A"])
                  print("        B:", questions[question_choice]["B"])
                  print("        C:", questions[question_choice]["C"])
                  print("        D:", questions[question_choice]["D"])

                  still_answering = True
                  while still_answering:
                        print()
                        answer = input("Bitte gib deine Antwort ein: ").upper()
                        if answer != "A" and answer != "B" and answer != "C" and answer != "D":
                              print("Bitte gib eine gültige Antwort ein.")
                        else:
                              if answer == questions[question_choice]["answer"]:
                                    print("Das ist richtig! Das gibt einen Punkt für dich!")
                                    still_answering = False
                                    counter_player2 = counter_player2+1
                              else:
                                    print(f"Leider war dies nicht richtig. Die richtige Antwort wäre {questions[question_choice]['answer']}!")
                              still_answering = False

                  if questions_open == []:
                        questions_open = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                        "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

                  clear(2)

      print()
      print("Damit ist das Quiz vorbei!")
      if another_player == "2":
            if counter_player1 > counter_player2:
                print(f"{name_player1} hat gewonnen!")
                print()
                print(f"{name_player1}: ", points[str(counter_player1)])
                print(f"{name_player2}: ", points[str(counter_player2)])
            if counter_player1 < counter_player2:
                print(f"{name_player2} hat gewonnen!")
                print()
                print(f"{name_player1}: ", points[str(counter_player1)])
                print(f"{name_player2}: ", points[str(counter_player2)])
            if counter_player1 == counter_player2:
                print(f"Das ist wohl ein Unentschieden! Ihr beide habt jeweils {counter_player1} Punkte erreicht!")
                print(f"{name_player1} & {name_player2}:", points[str(counter_player1)])

            if int(counter_player1) > highscore_player1:
                print()
                highscore_player1 = int(counter_player1)
                print(f"""Unglaublich {name_player1}, du hast dich selbst geschlagen!
Der Highscore von {name_player1} lautet derzeit: {highscore_player1} Punkte.""")

            if int(counter_player2) > highscore_player2:
                print()
                highscore_player2 = int(counter_player2)
                print(f"""Unglaublich {name_player2}, du hast dich selbst geschlagen!
Der Highscore von {name_player2} lautet derzeit: {highscore_player2} Punkte.""")


      else:
            print(points[str(counter_player1)])
            print()

            global last_score_player1

            if last_score_player1 > int(counter_player1):
                print(f"""In der Runde davor hast du {last_score_player1} Punkte und diese Runde hast du {counter_player1} Punkte erreicht. 
Nicht traurig sein! Versuche es erneut und schaffe es die Punktzahl aus der letzten Runde zu übertreffen!""")
            elif last_score_player1 < int(counter_player1):
                print(f"""Sehr gut! Du hast diese Runde {counter_player1} Punkte erreicht. 
In der Runde davor hattest du nur {last_score_player1} Punkte. Du hast dich selbst übertroffen!""")
            elif last_score_player1 == int(counter_player1):
                print(f"""Du hast mit {counter_player1} genausoviele Punkte in dieser und in der Runde davor erspielt!
Schaffst du es dich nun zu übertreffen? Probier es doch mal aus!""")
            last_score_player1 = counter_player1

            if highscore_player1 < int(counter_player1):
                time.sleep(1)
                print()
                print(f"""Echt unglaublich, du hast deinen alten Highscore von {highscore_player1} Punkten übertroffen!
Dein neuer Highscore beträgt: {counter_player1} Punkte.""")
                highscore_player1 = int(counter_player1)

      #Noch einmal spielen?
      time.sleep(5)
      print()
      play_again = input('Noch einmal spielen? Dann schreib "Ja": ').lower()
      clear(0.5)
      if play_again == "ja":
            play()
      else:
            print("Vielen Dank fürs Spielen und bis zum nächsten Mal! :)")
            time.sleep(3)
            exit()

def clear(sec):
    time.sleep(sec)
    os.system('cls')

#Spielstart
print(r"""
                /----|       .         .
  .            /     [   .        .         .
         ______|---- _|__     .        .
.     _--    --\_<_//   \-----           .
     _  _--___   \__/     ___  -----_ **     *
*  _- _-      --_         /  [ ----__  --_  *
*/__-      .    [           _[  *** --_  [*
  [*/ .          __[/-----__/   [**     [*/
        .     /--  /            /
     .        /   /   /[----___/        .
             /   /*[  !   /==/              .
  .         /   /==[   |/==/      .
          _/   /=/ | _ |=/   .               .
         /_   //  / _ _//              .
 .       [ '//    |__//    .    .            .
        /==/  .  /==/                .
      /==/     /==/                       .
    /==/     /==/       .       .    .
 _/==/    _/==/            .
 [|*      [|*                   """)
print()
print("""Willkommen beim Skigebiets Quiz!
In diesem Quiz werden dir 10 Fragen zu verschiedensten Skigebieten gestellt werden.
Du hast immer die Auswahl zwischen 4 Antwortmöglichkeiten.
Ich wünsche dir viel Spaß und Erfolg beim Quiz!
""")
name_player1 = input("Bitte gib deinen Namen ein: ").title()
clear(0)
another_player = input('''Möchtest du alleine oder zu zweit spielen? FÜr den Einzelspieler drücke einfach Enter.
Wenn du zu zweit spielen möchtest schreibe jetzt "2": ''')
if another_player == "2":
    name_player2 = input("Spieler 2, bitte gib deinen Namen ein: ").title()
    clear(0)
    play()
else:
    clear(0)
    play()









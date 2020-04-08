import Start as start
import pickle
import os

if __name__== '__main__':
    empty = set([])
    if os.path.getsize('settings.txt') > 0:
        with open('settings.txt', 'rb') as settings:
            load_start = pickle.load(settings)
            print(load_start.preferred_screen)
            start.Start.preferred_screen=load_start.preferred_screen

    if start.Start.preferred_screen == "":
        start_window = start.Start()
        with open('settings.txt', 'wb') as settings:
            # Step 3
            pickle.dump(start_window, settings, -1)
    else:
        if start.Start.preferred_screen == 'Beginner':
            if os.path.getsize('novice.txt') > 0:
                with open('novice.txt', 'rb') as n_s:
                    load_start = pickle.load(n_s)
                    novice = start.NoviceWindow(load_start.listBoxBuffer)
            else:

                novice = start.NoviceWindow(empty)
        elif start.Start.preferred_screen == 'Medium':
            if os.path.getsize('typical.txt') > 0:
                with open('typical.txt', 'rb') as n_s:
                    load_start = pickle.load(n_s)
                    typical = start.TypicalWindow(load_start.listBoxBuffer)
            else:
                typical = start.TypicalWindow(empty)
        elif start.Start.preferred_screen == 'Expert':
            main = start.ExpertWindow()


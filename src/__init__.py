import src.Start as start
import pickle
import os

if __name__== '__main__':
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
            main = start.NoviceWindow()
        elif start.Start.preferred_screen == 'Medium':
            main = start.TypicalWindow()
        elif start.Start.preferred_screen == 'Expert':
            main = start.ExpertWindow()


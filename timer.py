import time

def countdown_timer(seconds):
    
    while seconds > 0:
        
        seconds_resto = seconds

        week, seconds_resto  = divmod(seconds_resto, 604800)
        days, seconds_resto = divmod(seconds_resto, 86400)
        hora, seconds_resto = divmod(seconds_resto, 3600)
        mins, seconds_resto = divmod(seconds_resto, 60)
        secs, seconds_resto = divmod(seconds_resto, 1)

        timer = f'{week}:{days}:{hora}:{mins}:{secs}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

    print('Tempo Esgotado!')

seconds = input("Digite o tempo em segundos: ")

countdown_timer(int(seconds))
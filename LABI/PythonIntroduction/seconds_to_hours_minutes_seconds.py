def convert_seconds_to_time_format():
    try:    
        seconds = int(input("Input the seconds here: "))
    except ValueError:
        print("Error: Please enter a valid integer for seconds.")
        return

    if seconds < 0:
        print("Error: Please enter a non-negative integer for seconds.")
        return
    
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds %= 60

    print(f"{seconds}s is {hours}h {minutes}min e {remaining_seconds}s")
    
convert_seconds_to_time_format()

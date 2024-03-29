import pandas as pd

def check_price(file_path):
    try:
        df = pd.read_csv(file_path)
        next(df)
        for row in df:
            if row[2] <= row[3]:
                send_mail(row[0], row[1])
                print('An email about ' + row[1] + ' price has been sent')
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

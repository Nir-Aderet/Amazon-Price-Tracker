import pandas as pd

def check_price(file_path, sender_email, sender_password):
    df = pd.read_csv(file_path)
    next(df)
    for row in df:
        if row[2] <= row[3]:
            send_mail(row[0], row[1])
            print('An email about ' + row[1] + ' price has been sent')

import pandas as pd
from data_retrieval import get_price_and_titles
from notification import send_mail
from csv_management import check_price
from config import DATA, HEADERS

def main():
    # create a DataFrame with the given URLs
    df = pd.DataFrame(DATA)
    original_csv_file = 'url_data.csv'

    # create a CSV file from the DataFrame
    df.to_csv(original_csv_file,index=False)

    # Read the original CSV file into a DataFrame
    df_original = pd.read_csv(original_csv_file)

    # get all the URLs from the CSV file
    urls = df_original.iloc[:, 0].tolist()

    # Add additional columns (title, price, alert price) to the DataFrame
    df_titles, df_prices, alert_price = get_price_and_titles(urls)
    if df_titles != [] and df_prices != [] and alert_price != []:
        df['Title'] = df_titles
        df['price'] = df_prices
        df['alert price'] = alert_price
        # Save the new DataFrame to a new CSV file
        new_csv_file = 'full_data.csv'
        df_original.to_csv(new_csv_file, index=False)
        print(f'New CSV file "{new_csv_file}" created successfully.')
        check_price(new_csv_file)


if __name__ == "__main__":  # when running the file run only the main function
    main()

import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd

# urls for the items we wish to price track; Here is where you add the items to be price tracked
DATA = {'URL': [
    'https://www.amazon.com/Upgrade-Cooling-KeiBn-15-6-17-3-Laptops/dp/B09NRTVV3M/ref=sr_1_12?crid=2Q8J5K4JPYHFO' \
    '&keywords=cooling%2Bfan%2Bfor%2Blaptop&qid=1695706802&refinements=p_n_is_free_shipping%3A10236242011%2Cp_72' \
    '%3A1248879011&rnid=1248877011&s=electronics&sprefix=cooling%2Bfan%2Bfor%2Bla%2Caps%2C405&sr=1-12&th=1 ',
    'https://www.amazon.com/Name-Wind-Anniversary-Kingkiller-Chronicle/dp/0756413710/ref=sr_1_6?crid=PIJPJ5TJS9C'
    '&keywords=patrick+rothfuss&qid=1695729567&sprefix=patri%2Caps%2C374&sr=8-6',
    'https://www.amazon.com/Regard-Silent-Things-Kingkiller-Chronicle/dp/0756411327/ref=d_pd_sbs_sccl_3_3/133-3715102'
    '-2100713?pd_rd_w=Hi50N&content-id=amzn1.sym.83180963-0377-46ea-9aa4-1ece655ef63e&pf_rd_p=83180963-0377-46ea-9aa4'
    '-1ece655ef63e&pf_rd_r=14MYF3HCVSDR5W31F2PF&pd_rd_wg=tcsu4&pd_rd_r=5dd15f65-49a0-46c4-bd30-68115103a743&pd_rd_i'
    '=0756411327&psc=1']}

#  what your web browser is sending in the "User-Agent" header for your HTTP requests
HEADERS = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'}


def get_price_and_titles(urls):
    df_titles, df_prices, discount_price = [], [], []
    for url in urls:
        # return all the data from the website
        page = requests.get(url, headers=HEADERS)
        # parse the information and pull individual items
        soup = BeautifulSoup(page.content, 'html.parser')
        # limit the amount of times to try and scrape data
        limit_find = 100
        title = None
        while title is None:
            title = soup.find(id="productTitle")
            limit_find -= 1
            if limit_find == 0:
                print('Error: To many inquiries')
                return [], [], []
        df_titles.append(title.get_text())
        price = None
        while price is None:
            price = soup.find("span", {"class": "a-price-whole"})
            limit_find -= 1
            if limit_find == 0:
                print('Error: To many inquiries')
                return [], [], []
        p = float(price.get_text()[0:2])
        df_prices.append(p)
        discount_price.append(p * 0.7)
    return df_titles, df_titles, discount_price


def send_mail(url, title):
    try:
        """SMTP client session object that can be used to send mail to any internet machine
        with an SMTP or ESMTP listener daemon."""
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('nirisworking@gmail.com', 'skge ehbm wdgr loaj')

        subject = 'An Item you requested has a lower price!'
        body = 'The item ' + title + ' is on sale!\nCheck this link for more information: ' + url
        msg = f"subject: {subject}\n\n{body}"

        server.sendmail('nirisworking@gmail.com', 'nirisworking@gmail.com', msg)
        print('A massage has been sent')
    finally:
        server.quit()


def check_price(file_path):
    df = pd.read_csv(file_path)
    next(df)
    for row in df:
        if row[2] <= row[3]:
            send_mail(row[0], row[1])
            print('An email about ' + row[1] + ' price has been sent')


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

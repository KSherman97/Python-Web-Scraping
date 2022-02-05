import pandas as pd
import sys
import io

def main():

    # Define the page url
    url = 'https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table'

    # define the file I want to output to
    output_file = './2020_medals.json'

    # Define the variables I will use for storing the values from the table
    rank = ""
    NOC = ""
    gold = 0
    silver = 0
    bronze = 0
    total = 0

    # Parse the HTML table from the webpage
    df = pd.read_html(url)

    # Set the dataframe to the result of the 2nd index
    df = df[2]

    # df = df.drop(columns=['Rank']) # drop the rank column
    df.drop(df.tail(1).index,inplace=True) # drop the last row
    
    json = df.to_json(output_file, orient='index')

    # print(df)
    # print(df.columns)

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

    main()
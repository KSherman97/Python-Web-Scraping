import pandas as pd
import sys
import io

def medals_2020():
    # Define the page url
    url = 'https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table'

    # define the file I want to output to
    output_file = './2020_medals.json'

    # Parse the HTML table from the webpage
    data_frame = pd.read_html(url)

    # Set the dataframe to the result of the 2nd index
    data_frame = data_frame[2]

    # data_frame = data_frame.drop(columns=['Rank']) # drop the rank column
    data_frame.drop(data_frame.tail(1).index,inplace=True) # drop the last row

    # There is a broken character in the name column for each country so fix it
    data_frame['NOC'] = data_frame['NOC'].str.replace('\u00a0',' ')
    
    # Output the dataframe to a JSON file oriented by index
    json = data_frame.to_json(output_file, orient='index')

    # Uncomment these if you want to see what the dataframe looks like
    ########################################################
    # print(data_frame)
    # print(data_frame.columns)
    ########################################################

def medals_2022():
        # Define the page url
    url = 'https://en.wikipedia.org/wiki/2022_Winter_Olympics_medal_table'

    # define the file I want to output to
    output_file = './2022_medals.json'

    # Parse the HTML table from the webpage
    data_frame = pd.read_html(url)

    # Set the dataframe to the result of the 2nd index
    data_frame = data_frame[3]

    # data_frame = data_frame.drop(columns=['Rank']) # drop the rank column
    data_frame.drop(data_frame.tail(1).index,inplace=True) # drop the last row

    data_frame = data_frame.rename({'.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}NOC' : 'NOC'}, axis=1)

    # There is a broken character in the name column for each country so fix it
    data_frame['NOC'] = data_frame['NOC'].str.replace('\u00a0',' ')
    
    # Output the dataframe to a JSON file oriented by index
    json = data_frame.to_json(output_file, orient='index')

    # Uncomment these if you want to see what the dataframe looks like
    ########################################################
    # print(data_frame)
    # print(data_frame.columns)
    ########################################################

def main():
    medals_2022()

if __name__ == "__main__":
    # This fixes formatting issues for output on Windows; uncomment if you're having issues
    ########################################################
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
    ########################################################

    main()
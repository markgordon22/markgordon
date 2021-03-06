import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('markgordonsandwiches')


def get_sales_data():
    """
    get sales figures input from user
    """
    print("please enter sales data from the last market")
    print("data should be six numbers with commas")
    print("Example: 10,20,30,40,50,60,70,80\n")

    data_str = input("enter your data here: ")
    print(f"the data provided is {data_str}")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    inside the try convert the strings to integers
     using the int() method
    """

    try:
        if len(values) != 6:
            raise ValueError(f" exactly 6 values required, you provided {len(values)}")

    except ValueError as e:
            print(f" invalid data {e}, try again please")



get_sales_data()






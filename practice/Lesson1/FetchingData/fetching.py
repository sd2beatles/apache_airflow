import pandas as pd
LOCAL_DIR="replace_me"

def main():
    #create a dataframe under name tweets
    tweets=pd.read_csv("replace_me",encoding='latin1')
    #format time by using pd.to_dataframe and drop out the column called "row ID"
    tweets=tweets.assign(Time=pd.to_datetime(data.Time)).drop("row ID",axis=1)
    #export the data frame to a new csv file with the current date
    tweets.to_csv(LOCAL_DIR+'data_fetched.csv',idnex=False)

if __name__=='__main__':
    main()

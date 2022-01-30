import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ArgumentsExceeded(Error):
    """Raised when number of arguments are more than two"""
    pass

class WrongArguments(Error):
    """Raised when arguments are wrong"""
    pass

class NotAdequateColumns(Error):
    """Raised when number of columns in input file are not 3"""
    pass

def main():
    n = len(sys.argv)
    try:
        if n>2:
            raise ArgumentsExceeded

        if n==0 or n==1:
            raise FileNotFoundError

        if sys.argv[0]!='101916056-2.py':
            raise WrongArguments

        flname = sys.argv[1]

        f_log = open("101916056-log.txt","a")

        df = pd.read_csv(flname)
        # df.reset_index(drop=True, inplace=True)


        df.drop(['RollNumber'], axis = 1, inplace=True)

        df["Total"] = df.sum(axis=1)
        # Line chart
        fig , ax = plt.subplots()
        for i in df.columns[0:-1]:
            df[i].value_counts().sort_index().plot(ax=ax)

        plt.title("Line Chart Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Number of students")
        plt.legend(df.columns[0:-1])
        plt.savefig('101916056-line-count.png')

        # Histogram of total
        fig = plt.figure(figsize =(15, 15))  
        colors = ['blue']
        plt.hist(df.iloc[:,-1], bins = [i for i in range(0,40,2)], histtype='bar', stacked=True, label=df.columns[-1])
        plt.legend(loc="upper right")
        plt.xlabel("Marks")
        plt.ylabel("Number of students")
        plt.title('Histogram Marks Distribution of Total')
        plt.savefig('101916056-histogram-total.png')

        # Histogram 
        fig = plt.figure(figsize =(15, 15))  
        colors = ['blue', 'orange', 'green', 'yellow', 'red']
        plt.hist(df.iloc[:, 0:-1], bins = [i for i in range(0,20,2)], histtype='bar', stacked=True, label=df.columns[0:-1])
        plt.xlabel("Marks")
        plt.legend(loc="upper right")
        plt.title('Histogram Marks Distribution')
        plt.ylabel("Number of students",)
        plt.savefig('101916056-histogram-count.png')

        # Pie Chart
        data = []
        coolms = list(df.columns)
        del coolms[-1]
        for i in coolms:
            data.append(df[i].sum())
        fig = plt.figure(figsize =(15, 15))    
        plt.pie(data, labels = coolms, autopct='%1.2f%%', textprops={'fontsize': 18})
        plt.title("Pie Chart Marks Distribution")
        plt.savefig('101916056-pie.png')
        # Line chart
        fig , ax = plt.subplots()
        df['Total'].value_counts().sort_index().plot(ax=ax)
        plt.title("Line Chart Marks Distribution")
        plt.legend('Total')
        plt.ylabel("Number of students")
        plt.xlabel("Marks")
        plt.savefig('101916056-line-total.png')


        # Apply the descriptive stats
        all_info = pd.DataFrame(df.describe(include = 'all'))

        new_list = np.concatenate((['Description'],all_info.columns))
        new = pd.DataFrame(columns=new_list)
        to_find = ['min', 'max', 'mean', 'median', 'std', 'num_of_missing_val', 'count_non_numeric_val']

        for i in to_find:
            if i == 'median':
                new.loc[len(new.index)] = [i] + list(all_info.loc['50%'])
            elif i == 'count_non_numeric_val':
                new.loc[len(new.index)] = [i,0,0,0,0,0,0] 
            elif i == 'num_of_missing_val':
                new.loc[len(new.index)] = [i,0,0,0,0,0,0]
            else:
                new.loc[len(new.index)] = [i] + list(all_info.loc[i])

        stats_info = new.to_string()

        f = open("101916056-statistics.txt","a")
        f.write(stats_info)
        f.close()

    except ArgumentsExceeded:
        f_log.write('More than two arguments given as input')

    except WrongArguments:
        f_log.write('Wrong files given as input')

    except FileNotFoundError:
        f_log.write('File not Found')

    except NotAdequateColumns:
        f_log.write("Columns in input file are not equal to 3")

    finally:
        f_log.close()


if __name__ == '__main__':
    main()
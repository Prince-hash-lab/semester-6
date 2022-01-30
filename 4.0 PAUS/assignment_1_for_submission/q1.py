import pandas as pd
df=pd.read_csv('input.csv')

odf=pd.DataFrame(columns=['RollNumber', 'P1', 'P2','P3','P5','P6'])


def unique(list1):
    list_set=set(list1)
    unique_list=list(list_set)
    return unique_list

lt=[]
for i in range(len(df)):
    lt.append(df.iloc[i][0])
lt=unique(lt)
lt.sort()


odf=pd.DataFrame({"RollNumber":lt, 'P1':[0 for i in range(len(lt))], 'P2':[0 for i in range(len(lt))],'P3':[0 for i in range(len(lt))],'P5':[0 for i in range(len(lt))],'P6':[0 for i in range(len(lt))]})


for j in range(len(df)):
    roll=df.RollNumber[j]
    sub=df.Submission[j]
    mark=df.Marks[j]
#     if sub=='P4':
#         print('yes')
#     print(roll, sub, mark)
    if sub!='P4'and mark!='X':
        index=-1
        for i in range(len(odf)):
            if odf.loc[i,'RollNumber' ]==roll:
                index=i
                break;
        odf.loc[index, sub]=mark


print(odf.head(10))

odf.to_csv('op.csv', index=False)
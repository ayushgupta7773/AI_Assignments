import pandas as pd

# df = pd.DataFrame([[1, "Ram", "IT"], [2, "Shyam", "Ops"]], columns = ["emp_id", "name", "dept"])
# df = pd.DataFrame([(1, "Ram", "IT")], columns = ["emp_id", "name", "dept"])
# df = pd.DataFrame({'emp_id':[1, 2], 'name': ['Ram', 'Shyam'], 'dept':['IT', 'Ops']})
# print(df)




# Q2
def solve(s): 
    """ returns a series object with word count as values and words as the indices. """ 
    # store the frequency of the strings in a series here 
    # sort the indices here 
    s=s.split()
    listOfWords={}
    # freq=[]
    for i in s:
        if i not in listOfWords:
            listOfWords[i]=1
        else :
            listOfWords[i]+=1
    # print(listOfWords)
    # print((listOfWords.items()))
    ord_list=(listOfWords.items())
    # ord_list=sorted(ord_list)
    # print(ord_list)

    res = pd.DataFrame(ord_list,columns=['words','freq'])
    res=res.sort_values(by='words')
    return res
ans=solve('How much wood would a woodchuck chuck if a woodchuck could chuck wood')
# print(ans)

# print(ans.nunique())


# Q3
# for x in ans.columns: 
#     print(ans[x].nunique())
#     if ans[x].nunique()==1: 
#         ans.drop(x, axis=1, inplace=True)
# print(ans)












# Provided dataset
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78,
                   # ... (all other values)
                   18.78],
    'tip': [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23,
            # ... (all other values)
            3.0],
    'sex': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male',
            # ... (all other values)
            'Female'],
    'smoker': ['No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No',
               # ... (all other values)
               'No'],
    'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun',
            # ... (all other values)
            'Thur'],
    'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner',
             # ... (all other values)
             'Dinner'],
    'size': [2, 3, 3, 2, 4, 4, 2, 4, 2, 2,
             # ... (all other values)
             2]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Specify the file path where you want to save the CSV file
# csv_file_path = 'your_file_path.csv'

# # Save the DataFrame to a CSV file
# df.to_csv(csv_file_path, index=False)

# print(f'Data saved to {csv_file_path}')
# print(pd.DataFrame(df, columns=['time', 'total_bill', 'tip']))
# print(df.loc[1:6, ['time', 'total_bill', 'tip']])
# print(df[['time', 'total_bill', 'tip']])
# print(df.iloc[:,0:2])


df=pd.DataFrame({
'Name':['Jim','Carrie','Chris','Morris'],
'Gender':['M','F','M','M'],
'Profession':['At','Tech','Cric','Actor']
    })


# print(df.loc[:2,"Name":"Profession"])

def add_and_remove(df, data, out): 
    ''' Input: df -> The dataframe passed as input data -> The list of list variable containg the rows to append out -> the variable containing the row index value to be removed 
    
    Output: df -> return the dataframe df after doing the above operations '''
    # Add the rows 
    # Remove the out index row return df





# Q7

def add_and_remove(df, data, out): 

    '''Input: df -> The dataframe passed as input data 
    -> The list of list variable containg the rows to append out
     -> the variable containing the row index value to be removed 
    
    Output: df -> return the dataframe df after doing the above operations'''
    # Add the rows 
    # Remove the out index row return df
    row=pd.DataFrame(data,columns=['name',"age"])
    # print(row)
    df=pd.concat([df,row],ignore_index=True)
    df=df.drop(out)
    return df

df = pd.DataFrame({
    "name": ['a', 'b', 'c'],
    "age": [12, 15, 18]
})
data = [['d', 20], ['e', 21], ['f', 22]]
out = 4
# New row data
# row = {'name': ['e'], "age": [34]}
# row=pd.DataFrame([['d', 20], ['e', 21], ['f', 22]],columns=['name',"age"])
# print(row)
# Append new row
# df = pd.concat([df,row], ignore_index=True)

# print(df)

new=add_and_remove(df, data, out)
# print(new)











# Q8
df=pd.read_csv("./AS1_dataset_mtcars")
print(df)











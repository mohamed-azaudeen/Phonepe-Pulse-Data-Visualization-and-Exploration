import os
import json
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import requests

def get_insert_data():
    path = "C:/Users/azaru/Azar documents/data/pulse/data/aggregated/transaction/country/india/state/"
    agg_state_list = os.listdir(path)

    clm = {'State':[], 'Year':[], 'Quater':[], 'Transacion_type':[], 'Transacion_count':[],  'Transacion_amount':[]}

    for i in agg_state_list:
        p_i=path+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j+"/"
            agg_year_list=os.listdir(p_j)
            for k in agg_year_list:
                p_k=p_j+k
                data=open(p_k,'r')
                D=json.load(data)
                for z in D['data']['transactionData']:
                    name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['Transacion_type'].append(name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

    agg_trans=pd.DataFrame(clm)   

    agg_trans['State']=agg_trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    agg_trans['State']=agg_trans['State'].str.replace('-',' ')
    agg_trans['State']=agg_trans['State'].str.title()
    agg_trans['State']=agg_trans['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    path1="C:/Users/azaru/Azar documents/data/pulse/data/aggregated/user/country/india/state/"
    agg_state_list_1=os.listdir(path1)

    clm1={'State':[], 'Year':[], 'Quater':[], 'brand_name':[], 'Transacion_count':[], 'percentage':[]}

    for i in agg_state_list_1:
        q_i=path1+i+"/"
        agg_user_year=os.listdir(q_i)
        for j in agg_user_year:
            q_j=q_i+j+"/"
            agg_user_year_list=os.listdir(q_j)
            for k in agg_user_year_list:
                q_k=q_j+k
                data1=open(q_k,'r')
                D1=json.load(data1)
                try:
                    for z in D1['data']['usersByDevice']:
                        brand=z['brand']
                        count=z['count']
                        percentage=z['percentage']
                        clm1['brand_name'].append(brand)
                        clm1['Transacion_count'].append(count)
                        clm1['percentage'].append(percentage)
                        clm1['State'].append(i)
                        clm1['Year'].append(j)
                        clm1['Quater'].append(int(k.strip('.json')))
                except:
                    pass    

    agg_user=pd.DataFrame(clm1)

    agg_user['State']=agg_user['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    agg_user['State']=agg_user['State'].str.replace('-',' ')
    agg_user['State']=agg_user['State'].str.title()
    agg_user['State']=agg_user['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')
                
    path2="C:/Users/azaru/Azar documents/data/pulse/data/map/transaction/hover/country/india/state/"
    map_trans_list = os.listdir(path2)

    clm2={'State':[], 'Year':[], 'Quater':[], 'state_name':[], 'Transacion_count':[],  'Transacion_amount':[]}

    for i in map_trans_list:
        p_i=path2+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j+"/"
            agg_year_list=os.listdir(p_j)
            for k in agg_year_list:
                p_k=p_j+k
                data=open(p_k,'r')
                D2=json.load(data)
                for z in D2['data']['hoverDataList']:
                    name=z['name']
                    count=z['metric'][0]['count']
                    amount=z['metric'][0]['amount']
                    clm2['state_name'].append(name)
                    clm2['Transacion_count'].append(count)
                    clm2['Transacion_amount'].append(amount)
                    clm2['State'].append(i)
                    clm2['Year'].append(j)
                    clm2['Quater'].append(int(k.strip('.json')))

    map_trans=pd.DataFrame(clm2)                

    map_trans['State']=map_trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    map_trans['State']=map_trans['State'].str.replace('-',' ')
    map_trans['State']=map_trans['State'].str.title()
    map_trans['State']=map_trans['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    path3="C:/Users/azaru/Azar documents/data/pulse/data/map/user/hover/country/india/state/"
    map_user_list = os.listdir(path3)

    clm3={'State':[], 'Year':[], 'Quater':[], 'district':[], 'registeredUsers':[], 'appOpens':[]}

    for i in map_user_list:
        q_i=path3+i+"/"
        agg_user_year=os.listdir(q_i)
        for j in agg_user_year:
            q_j=q_i+j+"/"
            agg_user_year_list=os.listdir(q_j)
            for k in agg_user_year_list:
                q_k=q_j+k
                data1=open(q_k,'r')
                D3=json.load(data1)
                for z in D3['data']['hoverData'].items():
                    district=z[0]
                    registeredUsers=z[1]['registeredUsers']
                    appOpens=z[1]['appOpens']
                    clm3['district'].append(district)
                    clm3['registeredUsers'].append(registeredUsers)
                    clm3['appOpens'].append(appOpens)
                    clm3['State'].append(i)
                    clm3['Year'].append(j)
                    clm3['Quater'].append(int(k.strip('.json')))

    map_user=pd.DataFrame(clm3)   

    map_user['State']=map_user['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    map_user['State']=map_user['State'].str.replace('-',' ')
    map_user['State']=map_user['State'].str.title()
    map_user['State']=map_user['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')    

    path4="C:/Users/azaru/Azar documents/data/pulse/data/top/transaction/country/india/"
    top_trans_state_list = os.listdir(path4)

    clm4={'Year':[], 'Quater':[], 'state_name':[], 'Transacion_count':[],  'Transacion_amount':[]}

    for i in top_trans_state_list:
        p_i=path4+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j
            data=open(p_j,'r')
            D4=json.load(data)
            for z in D4['data']['states']:
                        name=z['entityName']
                        count=z['metric']['count']
                        amount=z['metric']['amount']
                        clm4['state_name'].append(name)
                        clm4['Transacion_count'].append(count)
                        clm4['Transacion_amount'].append(amount)
                        clm4['Year'].append(i)
                        clm4['Quater'].append(int(j.strip('.json')))
                        
    top_trans_state=pd.DataFrame(clm4)     

    top_trans_state['state_name']=top_trans_state['state_name'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    top_trans_state['state_name']=top_trans_state['state_name'].str.replace('-',' ')
    top_trans_state['state_name']=top_trans_state['state_name'].str.title()
    top_trans_state['state_name']=top_trans_state['state_name'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    path5="C:/Users/azaru/Azar documents/data/pulse/data/top/transaction/country/state/"
    top_trans_dist_list = os.listdir(path5)

    clm5={'State':[], 'Year':[], 'Quater':[], 'district_name':[], 'Transacion_count':[],  'Transacion_amount':[]}

    for i in top_trans_dist_list:
        p_i=path5+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j+"/"
            agg_year_list=os.listdir(p_j)
            for k in agg_year_list:
                p_k=p_j+k
                data=open(p_k,'r')
                D5=json.load(data)  
                for z in D5['data']['districts']:
                        name=z['entityName']
                        count=z['metric']['count']
                        amount=z['metric']['amount']
                        clm5['district_name'].append(name)
                        clm5['Transacion_count'].append(count)
                        clm5['Transacion_amount'].append(amount)
                        clm5['State'].append(i)
                        clm5['Year'].append(j)
                        clm5['Quater'].append(int(k.strip('.json')))
                                
            
            
    top_trans_dist=pd.DataFrame(clm5)   

    top_trans_dist['State']=top_trans_dist['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    top_trans_dist['State']=top_trans_dist['State'].str.replace('-',' ')
    top_trans_dist['State']=top_trans_dist['State'].str.title()
    top_trans_dist['State']=top_trans_dist['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    path6="C:/Users/azaru/Azar documents/data/pulse/data/top/transaction/country/state/"
    top_trans_pin_list = os.listdir(path6)

    clm6={'State':[], 'Year':[], 'Quater':[], 'pincode':[], 'Transacion_count':[],  'Transacion_amount':[]}

    for i in top_trans_pin_list:
        p_i=path6+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j+"/"
            agg_year_list=os.listdir(p_j)
            for k in agg_year_list:
                p_k=p_j+k
                data=open(p_k,'r')
                D6=json.load(data)  
                for z in D6['data']['pincodes']:
                        name=z['entityName']
                        count=z['metric']['count']
                        amount=z['metric']['amount']
                        clm6['pincode'].append(name)
                        clm6['Transacion_count'].append(count)
                        clm6['Transacion_amount'].append(amount)
                        clm6['State'].append(i)
                        clm6['Year'].append(j)
                        clm6['Quater'].append(int(k.strip('.json')))
                                
            
            
    top_trans_pin=pd.DataFrame(clm6)      

    top_trans_pin['State']=top_trans_pin['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    top_trans_pin['State']=top_trans_pin['State'].str.replace('-',' ')
    top_trans_pin['State']=top_trans_pin['State'].str.title()
    top_trans_pin['State']=top_trans_pin['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    path7="C:/Users/azaru/Azar documents/data/pulse/data/top/user/country/india/"
    top_user_state_list = os.listdir(path7)

    clm7={'Year':[], 'Quater':[], 'state_name':[], 'registeredUsers':[]}

    for i in top_user_state_list:
        p_i=path7+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j
            data=open(p_j,'r')
            D7=json.load(data)
            for z in D7['data']['states']:
                        name=z['name']
                        reguser=z['registeredUsers']
                        clm7['state_name'].append(name)
                        clm7['registeredUsers'].append(reguser)
                        clm7['Year'].append(i)
                        clm7['Quater'].append(int(j.strip('.json')))
                        
    top_user_state=pd.DataFrame(clm7)   

    top_user_state['state_name']=top_user_state['state_name'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    top_user_state['state_name']=top_user_state['state_name'].str.replace('-',' ')
    top_user_state['state_name']=top_user_state['state_name'].str.title()
    top_user_state['state_name']=top_user_state['state_name'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')      

    path8="C:/Users/azaru/Azar documents/data/pulse/data/top/user/country/state/"
    top_user_dist_list = os.listdir(path8)

    clm8={'State':[], 'Year':[], 'Quater':[], 'district_name':[], 'registeredUsers':[]}

    for i in top_user_dist_list:
        p_i=path8+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j+"/"
            agg_year_list=os.listdir(p_j)
            for k in agg_year_list:
                p_k=p_j+k
                data=open(p_k,'r')
                D8=json.load(data)
                for z in D8['data']['districts']:
                    name=z['name']
                    reguser=z['registeredUsers']
                    clm8['district_name'].append(name)
                    clm8['registeredUsers'].append(reguser)
                    clm8['State'].append(i)
                    clm8['Year'].append(j)
                    clm8['Quater'].append(int(k.strip('.json')))

    top_user_dist=pd.DataFrame(clm8)  

    top_user_dist['State']=top_user_dist['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    top_user_dist['State']=top_user_dist['State'].str.replace('-',' ')
    top_user_dist['State']=top_user_dist['State'].str.title()
    top_user_dist['State']=top_user_dist['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    path9="C:/Users/azaru/Azar documents/data/pulse/data/top/user/country/state/"
    top_user_pin_list = os.listdir(path9)

    clm9={'State':[], 'Year':[], 'Quater':[], 'pincode':[], 'registeredUsers':[]}

    for i in top_user_pin_list:
        p_i=path9+i+"/"
        agg_year=os.listdir(p_i)
        for j in agg_year:
            p_j=p_i+j+"/"
            agg_year_list=os.listdir(p_j)
            for k in agg_year_list:
                p_k=p_j+k
                data=open(p_k,'r')
                D9=json.load(data)
                for z in D8['data']['pincodes']:
                    name=z['name']
                    reguser=z['registeredUsers']
                    clm9['pincode'].append(name)
                    clm9['registeredUsers'].append(reguser)
                    clm9['State'].append(i)
                    clm9['Year'].append(j)
                    clm9['Quater'].append(int(k.strip('.json')))

    top_user_pin=pd.DataFrame(clm9)  

    top_user_pin['State']=top_user_pin['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
    top_user_pin['State']=top_user_pin['State'].str.replace('-',' ')
    top_user_pin['State']=top_user_pin['State'].str.title()
    top_user_pin['State']=top_user_pin['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','Dadra and Nagar Haveli and Daman and Diu')

    client = mysql.connector.connect(
        host="localhost",
        user="root",
        password="azarudeen1997", 
        database="phonepe_data"
    )   
    cursor = client.cursor()

    query = """create table if not exists agg_transaction(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    Transacion_type varchar(250),
                                                    Transacion_count int,
                                                    Transacion_amount bigint 
                                                    )"""


    cursor.execute(query) 

    query = "insert into agg_transaction values (%s,%s,%s,%s,%s,%s)"
    values = []
    for i in agg_trans.index:
        row = tuple(agg_trans.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]),int(row[5]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists agg_users(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    brand_name varchar(250),
                                                    Transacion_count int,
                                                    percentage decimal(4,2) 
                                                    )"""


    cursor.execute(query) 

    query = "insert into agg_users values (%s,%s,%s,%s,%s,%s)"
    values = []
    for i in agg_user.index:
        row = tuple(agg_user.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]),float(row[5]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists map_transaction(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    state_name varchar(250),
                                                    Transacion_count int,
                                                    Transacion_amount bigint 
                                                    )"""


    cursor.execute(query) 

    query = "insert into map_transaction values (%s,%s,%s,%s,%s,%s)"
    values = []
    for i in map_trans.index:
        row = tuple(map_trans.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]),int(row[5]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists map_users(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    district varchar(250),
                                                    registeredUsers int,
                                                    appOpens bigint 
                                                    )"""


    cursor.execute(query) 

    query = "insert into map_users values (%s,%s,%s,%s,%s,%s)"
    values = []
    for i in map_user.index:
        row = tuple(map_user.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]),int(row[5]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists top_transaction_states(
                                                    Year int,
                                                    Quater int,
                                                    state_name varchar(250),
                                                    Transacion_count bigint,
                                                    Transacion_amount bigint 
                                                    )"""


    cursor.execute(query) 

    query = "insert into top_transaction_states values (%s,%s,%s,%s,%s)"
    values = []
    for i in top_trans_state.index:
        row = tuple(top_trans_state.loc[i].values)
        value = (int(row[0]),int(row[1]),str(row[2]),int(row[3]),int(row[4]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists top_transaction_district(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    district_name varchar(250),
                                                    Transacion_count bigint,
                                                    Transacion_amount bigint 
                                                    )"""


    cursor.execute(query) 

    query = "insert into top_transaction_district values (%s,%s,%s,%s,%s,%s)"
    values = []
    for i in top_trans_dist.index:
        row = tuple(top_trans_dist.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]),int(row[5]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists top_transaction_pincode(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    pincode varchar(150),
                                                    Transacion_count bigint,
                                                    Transacion_amount bigint 
                                                    )"""


    cursor.execute(query) 

    query = "insert into top_transaction_pincode values (%s,%s,%s,%s,%s,%s)"
    values = []
    for i in top_trans_pin.index:
        row = tuple(top_trans_pin.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]),int(row[5]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists top_user_states(
                                                    Year int,
                                                    Quater int,
                                                    state_name varchar(250),
                                                    registeredUsers bigint
                                                    )"""


    cursor.execute(query) 

    query = "insert into top_user_states values (%s,%s,%s,%s)"
    values = []
    for i in top_user_state.index:
        row = tuple(top_user_state.loc[i].values)
        value = (int(row[0]),int(row[1]),str(row[2]),int(row[3]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists top_user_district(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    district_name varchar(250),
                                                    registeredUsers bigint
                                                    )"""


    cursor.execute(query) 

    query = "insert into top_user_district values (%s,%s,%s,%s,%s)"
    values = []
    for i in top_user_dist.index:
        row = tuple(top_user_dist.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

    query = """create table if not exists top_user_pincode(State varchar(150),
                                                    Year int,
                                                    Quater int,
                                                    pincode varchar(250),
                                                    registeredUsers bigint
                                                    )"""


    cursor.execute(query) 

    query = "insert into top_user_pincode values (%s,%s,%s,%s,%s)"
    values = []
    for i in top_user_pin.index:
        row = tuple(top_user_pin.loc[i].values)
        value = (str(row[0]),int(row[1]),int(row[2]),str(row[3]),int(row[4]))
        values.append(value)
    cursor.executemany(query,values)
    client.commit()

client = mysql.connector.connect(
    host="localhost",
    user="root",
    password="azarudeen1997", 
    database="phonepe_data"
)   
cursor = client.cursor()

query = '''select * from agg_transaction'''
cursor.execute(query)
data = cursor.fetchall()
agg_trans_data = pd.DataFrame(data,columns=['State','Year','Quater','Transacion_type','Transacion_count','Transacion_amount'])
query = '''select State,SUM(Transacion_amount) as Transacion_amount ,SUM(Transacion_count) as Transacion_count 
            from agg_transaction
            group by State'''
cursor.execute(query)
data_1 = cursor.fetchall()
agg_trans_data_1 = pd.DataFrame(data_1,columns=['State','Transacion_count','Transacion_amount'])

query = "select * from agg_users"
cursor.execute(query)
data_2 = cursor.fetchall()
agg_user_data = pd.DataFrame(data_2,columns=['State','Year','Quater','brand_name','Transacion_count','percentage'])

query = '''select brand_name,percentage,SUM(Transacion_count) as Transacion_count 
            from agg_users
            group by brand_name,percentage
            ORDER BY Transacion_count '''
cursor.execute(query)
data_3 = cursor.fetchall()
agg_user_data_1 = pd.DataFrame(data_3,columns=['brand_name','percentage','Transacion_count'])

query = "select * from map_transaction"
cursor.execute(query)
data_4 = cursor.fetchall()
map_trans_data = pd.DataFrame(data_4,columns=['State','Year','Quater','state_name','Transacion_count','Transacion_amount'])

query = '''select state_name,SUM(Transacion_amount) as Transacion_amount ,SUM(Transacion_count) as Transacion_count
            from  map_transaction
            group by state_name'''
cursor.execute(query)
data_5 = cursor.fetchall()
map_trans_data_1 = pd.DataFrame(data_5,columns=['state_name','Transacion_count','Transacion_amount'])

query = "select * from map_users"
cursor.execute(query)
data_5 = cursor.fetchall()
map_user_data = pd.DataFrame(data_5,columns=['State','Year','Quater','district','registeredUsers','appOpens'])

query = '''select State,district,registeredUsers
            from map_users
            group by State,district,registeredUsers'''
cursor.execute(query)
data_6 = cursor.fetchall()
map_user_data_1 = pd.DataFrame(data_6,columns=['State','district','registeredUsers'])

def trans_amount_count_Y(df , year):
    trans_agg_ac=df[df['Year'] == year]
    trans_agg_ac.reset_index(drop=True,inplace=True)

    return trans_agg_ac    

def trans_amount_count_Y_Q(df , quater):
    trans_agg_ac=df[df['Quater'] == quater]
    trans_agg_ac.reset_index(drop=True,inplace=True)

    trans_agg_ac_grp=trans_agg_ac.groupby("State")[["Transacion_count","Transacion_amount"]].sum()
    trans_agg_ac_grp.reset_index(inplace=True)

    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for feature in data1["features"]:
        state_name.append(feature["properties"]["ST_NM"])

    state_name.sort()
    

    fig_india = px.choropleth(
    trans_agg_ac_grp,
    geojson=url,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transacion_amount',
    color_continuous_scale='icefire',
    range_color=(trans_agg_ac_grp["Transacion_amount"].min(),trans_agg_ac_grp["Transacion_amount"].max()),
    hover_name='State',
    title=f"TRANSACTION AMOUNT - {trans_agg_ac["Year"].unique()} YEAR - {quater} QUATER ",
    height=900,
    width=1200)

    fig_india.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_india)
   
    fig_india_1 = px.choropleth(
    trans_agg_ac_grp,
    geojson=url,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transacion_count',
    color_continuous_scale='tropic',
    range_color=(trans_agg_ac_grp["Transacion_count"].min(),trans_agg_ac_grp["Transacion_count"].max()),
    hover_name='State',
    title=f"TRANSACTION COUNT - {trans_agg_ac["Year"].unique()} YEAR - {quater} QUATER ",
    height=900,
    width=1200 )

    fig_india_1.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_india_1)

    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(trans_agg_ac_grp, x="State", y="Transacion_amount", title=f"TRANSACTION AMOUNT - {trans_agg_ac["Year"].unique()} YEAR - {quater} QUATER ", color_discrete_sequence=px.colors.sequential.Magenta_r)
        st.plotly_chart(fig_amount)
    with col2:
        fig_count = px.bar(trans_agg_ac_grp, x="State", y="Transacion_count", title=f"TRANSACTION COUNT - {trans_agg_ac["Year"].unique()} YEAR - {quater} QUATER ", color_discrete_sequence=px.colors.sequential.YlGnBu_r)
        st.plotly_chart(fig_count)

    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(agg_trans_data_1, x="State", y="Transacion_amount", title=f"TOTAL - TRANSACTION AMOUNT ", color_discrete_sequence=px.colors.sequential.Electric_r)
        st.plotly_chart(fig_amount)
    with col2:
        fig_count = px.bar(agg_trans_data_1, x="State", y="Transacion_count", title=f"TOTAL - TRANSACTION COUNT ", color_discrete_sequence=px.colors.sequential.haline_r)
        st.plotly_chart(fig_count)    

def trans_amount_count_S(df , State):
    trans_agg_ac=df[df['State'] == State]
    trans_agg_ac.reset_index(drop=True,inplace=True)

    trans_agg_ac_grp=trans_agg_ac.groupby("Transacion_type")[["Transacion_count","Transacion_amount"]].sum()
    trans_agg_ac_grp.reset_index(inplace=True)
    col1,col2 = st.columns(2)
   
    with col1:
        fig_pie_1 = px.pie(data_frame=trans_agg_ac_grp , names='Transacion_type' ,values='Transacion_amount' ,hole=0.5,width=600,title=f'{State} - Transacion_amount',color_discrete_sequence=px.colors.carto.Agsunset_r)
        st.plotly_chart(fig_pie_1)
    with col2:
        fig_pie_2 = px.pie(data_frame=trans_agg_ac_grp , names='Transacion_type' ,values='Transacion_count' ,hole=0.5,width=600,title=f'{State} - Transacion_count',color_discrete_sequence=px.colors.carto.Agsunset_r)
        st.plotly_chart(fig_pie_2)

def user_amount_count_Y(df , year):
    trans_agg_user=df[df['Year'] == year]
    trans_agg_user.reset_index(drop=True,inplace=True)

    return trans_agg_user

def user_amount_count_Q(df , quater):
    trans_agg_user=df[df['Quater'] == quater]
    trans_agg_user.reset_index(drop=True,inplace=True)

    trans_agg_user_grp=trans_agg_user.groupby("brand_name")[["Transacion_count","percentage"]].sum()
    trans_agg_user_grp.reset_index(inplace=True)

    trans_agg_user_grp_1=trans_agg_user.groupby("State")[["Transacion_count","brand_name"]].sum()
    trans_agg_user_grp_1.reset_index(inplace=True)

    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for feature in data1["features"]:
        state_name.append(feature["properties"]["ST_NM"])

    state_name.sort()

    
    fig_india = px.choropleth(
    trans_agg_user_grp_1,
    geojson=url,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transacion_count',
    color_continuous_scale='ylorrd',
    range_color=(trans_agg_user_grp_1["Transacion_count"].min(),trans_agg_user_grp_1["Transacion_count"].max()),
    hover_name='State',
    title=f"TRANSACTION COUNT - {trans_agg_user["Year"].unique()} YEAR {quater} QUATER",
    height=600,
    width=900 
    )

    fig_india.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig_india)
        
    col1,col2 = st.columns(2)
    with col1:
        fig_count = px.bar(trans_agg_user_grp, x="brand_name", y="Transacion_count", title=f"TRANSACTION COUNT - {trans_agg_user["Year"].unique()} YEAR {quater} QUATER", color_discrete_sequence=px.colors.sequential.ice_r,hover_name="brand_name",width=600,height=600)
        st.plotly_chart(fig_count)
    with col2:
        st.table(trans_agg_user_grp)   

    fig_count_1 = px.line(data_frame=trans_agg_user_grp ,x="brand_name" ,y="Transacion_count",hover_data="percentage",title="BRANDS , TRANSACTION COUNT , PERCENTAGE",width=1200,height=500,markers=True)     
    st.plotly_chart(fig_count_1)

    fig_count_2 = px.bar(agg_user_data_1, x="Transacion_count", y="brand_name", title=f"TOTAL - TRANSACTION COUNT", color_discrete_sequence=px.colors.sequential.Peach_r,hover_name="brand_name",width=1200,height=600,orientation='h')
    st.plotly_chart(fig_count_2)

def map_amount_count_Y(df , year):
    map_agg_ac=df[df['Year'] == year]
    map_agg_ac.reset_index(drop=True,inplace=True)

    return map_agg_ac

def map_amount_count_Y_Q(df , quater):
    map_agg_ac=df[df['Quater'] == quater]
    map_agg_ac.reset_index(drop=True,inplace=True)

    map_agg_ac_grp=map_agg_ac.groupby("State")[["Transacion_count","Transacion_amount"]].sum()
    map_agg_ac_grp.reset_index(inplace=True)

    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for feature in data1["features"]:
        state_name.append(feature["properties"]["ST_NM"])

    state_name.sort()
    col1,col2 = st.columns(2)
    with col1:
        fig_india = px.choropleth(
        map_agg_ac_grp,
        geojson=url,
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transacion_amount',
        color_continuous_scale='tempo',
        range_color=(map_agg_ac_grp["Transacion_amount"].min(),map_agg_ac_grp["Transacion_amount"].max()),
        hover_name='State',
        title=f"TRANSACTION AMOUNT - {map_agg_ac["Year"].unique()} YEAR {quater} QUATER ",
        height=600,
        width=650 )

        fig_india.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_india)
    
    with col2:
        fig_india_1 = px.choropleth(
        map_agg_ac_grp,
        geojson=url,
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transacion_count',
        color_continuous_scale='viridis',
        range_color=(map_agg_ac_grp["Transacion_count"].min(),map_agg_ac_grp["Transacion_count"].max()),
        hover_name='State',
        title=f"TRANSACTION COUNT - {map_agg_ac["Year"].unique()} YEAR {quater} QUATER ",
        height=600,
        width=650 )

        fig_india_1.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_india_1)
    

def map_amount_count_S(df , State):
    map_agg_ac=df[df['State'] == State]
    map_agg_ac.reset_index(drop=True,inplace=True)

    map_agg_ac_grp=map_agg_ac.groupby("state_name")[["Transacion_count","Transacion_amount"]].sum()
    map_agg_ac_grp.reset_index(inplace=True)

    fig_amount = px.bar(map_agg_ac_grp, x="Transacion_amount", y="state_name",orientation='h' ,title=f"TRANSACTION AMOUNT - {map_agg_ac["Year"].unique()} - YEAR  ", color_discrete_sequence=px.colors.sequential.Peach_r,width=1200,height=500)
    st.plotly_chart(fig_amount)

    fig_count = px.bar(map_agg_ac_grp, x="Transacion_count", y="state_name",orientation='h', title=f"TRANSACTION COUNT - {map_agg_ac["Year"].unique()} - YEAR  ", color_discrete_sequence=px.colors.sequential.Plotly3_r,width=1200,height=500)
    st.plotly_chart(fig_count)

    fig_1 = px.area(map_trans_data_1,x='Transacion_amount',y='state_name',color='state_name',markers=True,width=1200,height=500)
    st.plotly_chart(fig_1)

def map_user_amount_count_Y(df , year):
    map_agg_user=df[df['Year'] == year]
    map_agg_user.reset_index(drop=True,inplace=True)

    return map_agg_user

def map_user_amount_count_Q(df , quater):
    map_agg_user=df[df['Quater'] == quater]
    map_agg_user.reset_index(drop=True,inplace=True)

    map_agg_user_ac_grp=pd.DataFrame(map_agg_user.groupby("State")["registeredUsers"].sum())
    map_agg_user_ac_grp.reset_index(inplace=True)

   

    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name=[]
    for feature in data1["features"]:
        state_name.append(feature["properties"]["ST_NM"])

    state_name.sort()

    fig_india = px.choropleth(
   map_agg_user_ac_grp,
    geojson=url,
    featureidkey='properties.ST_NM',
    locations='State',
    color='registeredUsers',
    color_continuous_scale='ylgn',
    range_color=(map_agg_user_ac_grp["registeredUsers"].min(),map_agg_user_ac_grp["registeredUsers"].max()),
    hover_name='State',
    title=f"TRANSACTION AMOUNT - {map_agg_user["Year"].unique()} YEAR {quater} QUATER ",
    height=600,
    width=900 )

    fig_india.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_india)
    

def map_user_amount_count_S(df , State):
    map_agg_user=df[df['State'] == State]
    map_agg_user.reset_index(drop=True,inplace=True)

    map_agg_user_ac_grp_1=pd.DataFrame(map_agg_user.groupby("district")["registeredUsers"].sum())
    map_agg_user_ac_grp_1.reset_index(inplace=True)

    fig_count_1 = px.line(data_frame=map_agg_user_ac_grp_1 ,x="district" ,y="registeredUsers",hover_data="district",title=f"{State} - Registered Users",width=1200,height=500,markers=True)
    st.plotly_chart(fig_count_1)

    fig_amount_2 = px.bar(map_agg_user_ac_grp_1, x="registeredUsers", y="district",orientation='h' ,title=f"{State} - Registered Users ", color_discrete_sequence=px.colors.sequential.haline_r,width=1200,height=500)
    st.plotly_chart(fig_amount_2)  
    
st.set_page_config(layout="wide")

st.title("Phnpe Pulse Data Visualization & Exploration")

with st.sidebar:

    select = option_menu("Main Menu",["Data Exploration","Top Charts"])

if select == "Data Exploration":
    st.title(":blue[Transaction & User - Analysis]")
    tab1,tab2 = st.tabs(["Aggregated Analysis" ,"Map Analysis"])

    with tab1:
        method =st.radio("Select the Method",["Transaction Analysis","User Analysis"])

        if method == "Transaction Analysis":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select the year",agg_trans_data['Year'].min(),agg_trans_data['Year'].max(),agg_trans_data['Year'].min())
            tac_Y = trans_amount_count_Y(agg_trans_data , years)
            with col2:
                quater = st.selectbox("Select the Quater",tac_Y['Quater'].unique())    
            trans_amount_count_Y_Q(tac_Y , quater)
               
            states = st.selectbox("select the State",tac_Y['State'].unique())
            trans_amount_count_S(tac_Y , states)

        elif method == "User Analysis":
            col1,col2 = st.columns(2)
            with col1:
                years_1 = st.slider("Select your year",agg_user_data['Year'].min(),agg_user_data['Year'].max(),agg_user_data['Year'].min())
            user_op = user_amount_count_Y(agg_user_data,years_1)
            with col2:
                quater_1 = st.selectbox("Select your Quater",user_op['Quater'].unique())    
            user_amount_count_Q(user_op , quater_1)

    with tab2:
        method_1 =st.radio("Select the Method",["Map Transaction Analysis","Map User Analysis"]) 

        if method_1 == "Map Transaction Analysis":
            col1,col2 = st.columns(2)
            with col1:
                years_2 = st.slider("Select The year",map_trans_data['Year'].min(),map_trans_data['Year'].max(),map_trans_data['Year'].min())
            map_transc = map_amount_count_Y(map_trans_data,years_2)
            with col2:
                quater_2 = st.selectbox("Select The Quater",map_transc['Quater'].unique())    
            map_amount_count_Y_Q(map_transc,quater_2)
               
            states_2 = st.selectbox("select The State",map_transc['State'].unique())
            map_amount_count_S(map_transc,states_2)
        
        elif method_1 == "Map User Analysis":
            col1,col2 = st.columns(2)
            with col1:
                years_3 = st.slider("Select Your year",map_user_data['Year'].min(),map_user_data['Year'].max(),map_user_data['Year'].min())
            map_user = map_user_amount_count_Y(map_user_data,years_3)
            with col2:
                quater_3 = st.selectbox("Select Your Quater",map_user['Quater'].unique())    
            map_user_amount_count_Q(map_user , quater_3)
               
            states_3 = st.selectbox("select Your State",map_user['State'].unique())
            map_user_amount_count_S(map_user,states_3)

elif select == "Top Charts":

    st.title(":red[TOP Charts -  Analysis]")

    client = mysql.connector.connect(
        host="localhost",
        user="root",
        password="azarudeen1997", 
        database="phonepe_data"
    )   
    cursor = client.cursor()

    question=st.selectbox("Select Your Questions",("1 - what are the top 10 districts  of total Transacion_amount",
                                                "2 - what are the top 10 postal codes of Average Transacion_amount",
                                                "3 - what are the top 10 States of total Transacion_amount",
                                                "4 - what are the least 10 district  their respective states of total Registered Users",
                                                "5 - what are the top 10 Postal codes of total Registered Users ",
                                                "6 - what are the top 10 States of total Registered Users",
                                                "7 - what are the Total Transaction Amount & Count for their corresponding Transaction Types",
                                                "8 - what are the top 10 Brands of Total_Transacion_count",
                                                "9 - what are the Least 10 Transaction Amount & Count for their corresponding Districts",
                                                "10 - what are the TOP 10 Districts of Total_registeredUsers"))

    if question=="1 - what are the top 10 districts  of total Transacion_amount":
        query = '''select district_name,SUM(Transacion_amount) AS Total_Transacion_amount  from top_transaction_district
                    GROUP BY district_name 
                    ORDER BY Total_Transacion_amount desc
                    LIMIT 10'''
        cursor.execute(query)
        data = cursor.fetchall()

        ques_1 = pd.DataFrame(data ,columns=['district_name','Total_Transacion_amount'])
        col1,col2 = st.columns(2)
        with col1:
            fig_q1 = px.bar(ques_1 , x='district_name',y='Total_Transacion_amount',title='Top 10 Districts - Transaction Amount',color='district_name',width=600)
            st.plotly_chart(fig_q1) 
        with col2:
            st.write(ques_1)    

        fig_q_1 = px.pie(data_frame=ques_1 ,names='district_name',values='Total_Transacion_amount',title='Top 10 Districts - Transaction Amount',color_discrete_sequence=px.colors.colorbrewer.Accent_r,width=1100)
        st.plotly_chart(fig_q_1)
        
        
                                                 

    elif question=="2 - what are the top 10 postal codes of Average Transacion_amount":
        query = '''select State,pincode,AVG(Transacion_amount) AS Average_Transacion_amount  from top_transaction_pincode 
            GROUP BY pincode,State
            ORDER BY Average_Transacion_amount desc
            LIMIT 10 '''
        cursor.execute(query)
        data_1 = cursor.fetchall() 
        ques_2 = pd.DataFrame(data_1 ,columns=['State','pincode','Average_Transacion_amount'])
        col1,col2 = st.columns(2)
        with col1:
            fig_q_2 = px.line(data_frame=ques_2 ,x='State',y='Average_Transacion_amount',title='Top 10 State Postal Codes - Average Transacion amount',color_discrete_sequence=px.colors.carto.Emrld,markers=True)
            st.plotly_chart(fig_q_2)                                     

        with col2:
            st.write(ques_2)

        fig_q2 = px.bar(ques_2 , x='State',y='Average_Transacion_amount',color='State',hover_data='pincode',title='Top 10 State Postal Codes - Average Amount',color_discrete_sequence=px.colors.sequential.YlOrRd_r,width=1200,height=500)
        st.plotly_chart(fig_q2)    

        
    elif question=="3 - what are the top 10 States of total Transacion_amount":
        query = '''select state_name ,SUM(Transacion_amount) AS Total_Transacion_amount from top_transaction_states 
            GROUP BY state_name
            ORDER BY Total_Transacion_amount DESC
            LIMIT 10 '''
        cursor.execute(query)
        data_2 = cursor.fetchall() 
        ques_3 = pd.DataFrame(data_2 ,columns=['state_name','Total_Transacion_amount'])
        col1,col2 = st.columns(2)
        with col1:
            fig_q_3 = px.pie(data_frame=ques_3 ,names='state_name',title='Top 10 Districts - Transaction Amount',values='Total_Transacion_amount',color_discrete_sequence=px.colors.colorbrewer.Oranges_r,width=600)
            st.plotly_chart(fig_q_3)
        with col2:
            st.write(ques_3)     

        fig_q3 = px.bar(ques_3 , x='Total_Transacion_amount',y='state_name',title='Top 10 States - Total Transaction Amount',color_discrete_sequence=px.colors.sequential.Cividis_r,orientation='h',width=1200,height=500)
        st.plotly_chart(fig_q3)

    elif question=="4 - what are the least 10 district  their respective states of total Registered Users":
        query = '''select State,district_name ,SUM(registeredUsers) AS Total_registeredUsers from top_user_district 
            GROUP BY State,district_name
            ORDER BY Total_registeredUsers
            LIMIT 10 '''
        cursor.execute(query)
        data_3 = cursor.fetchall() 
        ques_4 = pd.DataFrame(data_3 ,columns=['State','district_name','Total_registeredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            fig_q4 = px.bar(ques_4 , x='district_name',y='Total_registeredUsers',hover_name='State',title='Least 10 Districts - Registered Users',color_discrete_sequence=px.colors.sequential.Greens_r,orientation='v',width=600)
            st.plotly_chart(fig_q4)
        with col2:
            st.write(ques_4)    

        fig_q_4 = px.scatter(ques_4,x='State',y='Total_registeredUsers',color='district_name',title='Least 10 States - Registered Users',color_discrete_sequence=px.colors.carto.Agsunset_r,width=1200,height=500)
        fig_q_4.update_traces(marker_size=40)
        st.plotly_chart(fig_q_4)                                              

    elif question=="5 - what are the top 10 Postal codes of total Registered Users ":
        query = '''select State,pincode ,SUM(registeredUsers) AS Total_registeredUsers from top_user_pincode
            GROUP BY State,pincode
            ORDER BY State desc
            LIMIT 10 '''
        cursor.execute(query)
        data_4 = cursor.fetchall() 
        ques_5 = pd.DataFrame(data_4 ,columns=['State','pincode','Total_registeredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            fig_q5 = px.line(ques_5 ,x='Total_registeredUsers',y='pincode',title='TOP 10 Postal Codes - Registered Users',color_discrete_sequence=px.colors.carto.Sunsetdark,markers=True)
            st.plotly_chart(fig_q5)
        with col2:
            st.write(ques_5)
        fig_q_5 = px.sunburst(ques_5,path=['State','pincode','Total_registeredUsers'],values='Total_registeredUsers',title='TOP 10 Postal Codes - Registered Users',color_discrete_sequence=px.colors.colorbrewer.Set2_r,width=1100,height=700)
        st.plotly_chart(fig_q_5)

    elif question=="6 - what are the top 10 States of total Registered Users":
        query = '''select state_name ,SUM(registeredUsers) AS Total_registeredUsers from top_user_states 
            GROUP BY state_name
            ORDER BY Total_registeredUsers desc
            LIMIT 10 '''
        cursor.execute(query)
        data_5 = cursor.fetchall() 
        ques_6 = pd.DataFrame(data_5 ,columns=['state_name','Total_registeredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            fig_q6 = px.sunburst(ques_6,path=['state_name', 'Total_registeredUsers'],values='Total_registeredUsers',title='TOP 10 States - Registered Users',color_discrete_sequence=px.colors.cyclical.mygbm_r,width=500,height=500)
            st.plotly_chart(fig_q6)
        with col2:
            st.write(ques_6)

        fig_q_6 = px.funnel(ques_6,x='state_name',y='Total_registeredUsers',title='TOP 10 States - Registered Users',color='state_name',color_discrete_sequence=px.colors.carto.Burgyl_r,width=1200,height=650)
        st.plotly_chart(fig_q_6)

    elif question=="7 - what are the Total Transaction Amount & Count for their corresponding Transaction Types":
        query = '''select Transacion_type ,SUM(Transacion_amount) AS Total_Transacion_amount,SUM(Transacion_count) AS Total_Transacion_count
            from agg_transaction 
            GROUP BY Transacion_type
            ORDER BY Total_Transacion_amount desc '''
        cursor.execute(query)
        data_6 = cursor.fetchall() 
        ques_7 = pd.DataFrame(data_6 ,columns=['Transacion_type','Total_Transacion_amount','Total_Transacion_count'])

        fig_q7 = px.funnel(ques_7,x='Transacion_type',y='Total_Transacion_amount',title='Transacion type - Transaction Amount & Transaction Count',color_discrete_sequence=px.colors.carto.Oryel_r,width=1200,height=550)
        st.plotly_chart(fig_q7)

        fig_q_7 = px.treemap(ques_7,path=['Transacion_type','Total_Transacion_amount','Total_Transacion_count'],title='Transacion type - Transaction Amount & Transaction Count',color_discrete_sequence=px.colors.cyclical.mrybm_r,width=1200)
        fig_q_7.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig_q_7)

    elif question=="8 - what are the top 10 Brands of Total_Transacion_count":
        query = '''select brand_name ,SUM(Transacion_count) AS Total_Transacion_count
            from agg_users 
            GROUP BY brand_name
            ORDER BY Total_Transacion_count desc
            LIMIT 10  '''
        cursor.execute(query)
        data_7 = cursor.fetchall() 
        ques_8 = pd.DataFrame(data_7 ,columns=['brand_name','Total_Transacion_count'])

        fig_q8 = px.scatter(ques_8,x='brand_name',y='Total_Transacion_count',color='brand_name',title='Top 10 Brands - Total Transaction Count',color_discrete_sequence=px.colors.carto.Purpor_r,width=1200)
        fig_q8.update_traces(marker_size=30)
        st.plotly_chart(fig_q8)
        col1,col2 = st.columns(2)
        with col1:
            fig_q_8 = px.bar(ques_8,x='brand_name',y='Total_Transacion_count',color='brand_name',title='Top 10 Brands - Total Transaction Count',color_discrete_sequence=px.colors.carto.Purpor_r,height=450,width=600)
            st.plotly_chart(fig_q_8)
        with col2:
            st.write(ques_8)    

    elif question=="9 - what are the Least 10 Transaction Amount & Count for their corresponding Districts":
        query = '''select state_name ,SUM(Transacion_amount) AS Total_Transacion_amount,SUM(Transacion_count) AS Total_Transacion_count
            from map_transaction 
            GROUP BY state_name
            ORDER BY Total_Transacion_amount  
            LIMIT 10'''
        cursor.execute(query)
        data_8 = cursor.fetchall() 
        ques_9 = pd.DataFrame(data_8 ,columns=['Districts','Total_Transacion_amount','Total_Transacion_count'])

        fig_q9 = px.area(ques_9,x='Districts',y='Total_Transacion_amount',title='Least 10 Districts - Transaction Amount & Transaction Count',color='Districts',markers=True,width=1200,height=500)
        st.plotly_chart(fig_q9)
        col1,col2 = st.columns(2)
        with col1:
            fig_q_9 = px.pie(ques_9,names='Districts',values='Total_Transacion_count',title='Least 10 Districts - Transaction Amount & Transaction Count',color_discrete_sequence=px.colors.colorbrewer.Spectral_r,width=600)
            st.plotly_chart(fig_q_9)
        with col2:
            st.write(ques_9)    

    elif question=="10 - what are the TOP 10 Districts of Total_registeredUsers":
        query = '''select district ,SUM(registeredUsers) AS Total_registeredUsers from map_users 
            GROUP BY district
            ORDER BY Total_registeredUsers DESC
            LIMIT 10 '''
        cursor.execute(query)
        data_9 = cursor.fetchall() 
        ques_10 = pd.DataFrame(data_9 ,columns=['Districts','Total_registeredUsers'])

        fig_q10 = px.funnel(ques_10,x='Total_registeredUsers',y='Districts',title='TOP 10 Districts - Registered Users',color_discrete_sequence=px.colors.diverging.RdYlBu_r,color='Districts',orientation='h',width=1350,height=650)
        st.plotly_chart(fig_q10)

        fig_q_10 = px.scatter(ques_10,x='Districts',y='Total_registeredUsers',title='TOP 10 Districts - Registered Users',color_discrete_sequence=px.colors.diverging.RdYlBu_r,color='Districts',symbol='Total_registeredUsers',width=1300,height=500)
        fig_q_10.update_traces(marker_size=15)
        st.plotly_chart(fig_q_10)

    else:
        pass    
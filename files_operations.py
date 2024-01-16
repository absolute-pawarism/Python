import pickle
def Serialize():
    countries={'india':91,'uk':44}
    F=open("D:\\Harshal Pawar Msc.DataScience\\Python_lab\\countriesdata.pkl.py",'wb')
    pickle.dump(countries, F)
    F.close()
  
def DeSerialize():
    F=open("D:\\Harshal Pawar Msc.DataScience\\Python_lab\\countriesdata.pkl.py",'rb')
    countries = pickle.load(F)
    countries['us']=1
    print(countries)
    F.close()
Serialize()
DeSerialize()
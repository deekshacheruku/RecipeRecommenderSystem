from flask import Flask,request,render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd




def Create():
    data=pd.read_csv('data.csv')
    #create a count matrix
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(data['Description'])
    #create a similarity matrix
    sim=cosine_similarity(count_matrix)
    return data,sim

def recom(rec):
    rec=rec.lower()
    #check data and sim are assigned
    try:
        data.head()
        sim.shape
    except :
        data,sim=Create()
    #check if recipe is there or not
    if rec not in data['Recipe_Name'].unique():
        return("Check your spelling.\n If your spelling is correct then Sorry! This Recipe is not in our Database.Kindly try another.")
    else:
        ans=[]
        #get the index of the recipe
        ind=data.loc[data['Recipe_Name']==rec].index[0]
        lst=enumerate(sim[ind])
        
        #sort in desending order
        lst=sorted(lst,key=lambda a:a[1],reverse=True)
        
        #Getting the top 10 Recommended Recipes
        lst=lst[1:11]
    
        for i in range(len(lst)):
            a=lst[i][0]
            ans.append(data['Recipe_Name'][a])
        return ans

app=Flask(__name__)
    


@app.route('/')

def home():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    rec=request.args.get('recipe')
    r=recom(rec)
    rec=rec.upper()
    if type(r) == type('string'):
        return render_template('recom.html',rec=rec,r=r,t='s')
    else:
        return render_template('recom.html',rec=rec,r=r,t='l')
    
    

if __name__ == "__main__":
    app.run()
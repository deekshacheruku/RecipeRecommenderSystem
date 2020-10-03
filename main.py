from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def Create():
    data=pd.read_csv('data.csv')
    #create a count matrix
    cv=TfidfVectorizer()
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

def Display1(x):
    nba=pd.read_csv("data2.csv")
    n=nba.loc[nba["Category"] == x]
    ser1 = pd.Series(n['Recipe_Name'])
    ans=[]
    for i in ser1:
        z1=""
        for b in i.split():
            z1=z1+b.capitalize()+" "
        z1=z1[:-1]
        ans.append(z1)
    return ans
    
def Display(z): 
    c=0
    ans=[]
    nba=pd.read_csv("data2.csv",index_col ="Recipe_Name")
    rows=nba.loc[[z]]
    for i in rows:
        c=c+1
        ser9 = pd.Series(rows[i])
        for k in ser9:
            if c == 7:
                h=""
                if "Diabetic Appropriate" in k:
                    h=h+", Diabetic Appropriate"
                if "Hearty" in k:
                    h=h+", Hearty Healthy"
                if "High Calorie" in k:
                    h=h+", High Calorie"
                if "Fat" in k:
                    h=h+", Low Fat"
                if "Low Calorie" in k:
                    h=h+", Low Calorie"
                if "fiber" in k:
                    h=h+", High Fiber"
                if "Rich" in k:
                    h=h+", Rich Minerals"
                if "Fiber" in k:
                    h=h+", High Fiber"
                if "High protien" in k:
                    h=h+", High protien"
                if "Healthy Aging" in k:
                    h=h+", Healthy Aging"
                if "Healthy Preganancy" in k:
                    h=h+", Healthy Preganancy"
                if "High Calcium" in k:
                    h=h+", High Calcium"
                if "Healthy Immunity" in k:
                    h=h+", Healthy Immunity"
                if "Low Added Sugars" in k:
                    h=h+"Low Added Sugars"
                if "vitamins" in k:
                    h=h+"High Vitamins"
                if "antioxidants" in k:
                    h=h+"High Antioxidants"
                if "Low Carbohydrate" in k:
                    h=h+"Low Carbohydrate"
                if " Diabetic free" in k:
                    h=h+"Diabetic Free"
                if h !="":
                    ans.append(h)
                else:
                    ans.append(k)

                '''
                if k == "None":
                    ans.append(k)
                else:
                    h=""
                    k=" ".join(k.split("  "))
                    k=k.split(" ")
                    for l in range(0,len(k),2):
                        if l !=len(k)-2:
                            h=h+k[l]+" "+k[l+1]+', '
                        else:
                            h=h+k[l]+" "+k[l+1]
                    ans.append(h)
                '''
            elif c == 8:
                h=""
                for l in k:
                    l1=l.replace(' ',', ')
                    h=h+l1
                ans.append(h)
            elif c == 16:
                k=k.split("Step")
                h=[]
                for l in k:
                    l1=l.replace(':','')
                    h.append(l1)
                ans.append(h)
            else:
                ans.append(k)
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
    
@app.route('/get_Items/<m>')
def get_Items(m):
    d=m.lower()
    d=d.replace(',','')
    a=Display(d)
    z1=""
    for b in m.split():
        z1=z1+b.capitalize()+" "
    z1=z1[:-1]
    return render_template('display.html',m=z1,a=a,n=len(a))
    
@app.route('/get_soups')
def get_soups():
    s=Display1("Soups")
    return render_template('get_.html',s=s,n=len(s))
    
@app.route('/get_homemaderemedies')
def get_homemaderemedies():
    s=Display1("Homemade Remedies")
    return render_template('get_.html',s=s,n=len(s))
    
@app.route('/get_drinks')
def get_drinks():
    s=Display1("Drinks")
    return render_template('get_.html',s=s,n=len(s))
    
@app.route('/get_breakfast')
def get_breakfast():
    s=Display1("Breakfast")
    return render_template('get_.html',s=s,n=len(s))
    
@app.route('/get_pancakes')
def get_pancakes():
    s=Display1("Pancakes")
    return render_template('get_.html',s=s,n=len(s))
    
@app.route('/get_noodles')
def get_noodles():
    s=Display1("Noodles")
    return render_template('get_.html',s=s,n=len(s))
    
@app.route('/get_lunch')
def get_lunch():
    s=Display1("Lunch")
    return render_template('get_.html',s=s,n=len(s))

@app.route('/get_salad')
def get_salad():
    s=Display1("Salad")
    return render_template('get_.html',s=s,n=len(s))
    

if __name__ == "__main__":
    app.run()
   

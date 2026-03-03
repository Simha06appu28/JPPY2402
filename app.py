from flask import Flask,render_template,url_for,request

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np 


import pickle

app = Flask(__name__)

random_malware = pickle.load(open('logic_malware.pkl','rb'))
ExtraTree_malware = pickle.load(open('ExtraTree_malware.pkl','rb'))

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset)
        return render_template("preview.html",df_view = df)


@app.route('/prediction')
def prediction():
    return render_template("prediction.html")

@app.route('/predict',methods=["POST"])
def predict():
    if request.method == 'POST':
        ACCESS_ALL_DOWNLOADS = request.form['ACCESS_ALL_DOWNLOADS']
        if ACCESS_ALL_DOWNLOADS =='0':
            access_all = "No"
        else:
             access_all = "Yes"   
        ACCESS_CACHE_FILESYSTEM = request.form['ACCESS_CACHE_FILESYSTEM']
        if ACCESS_CACHE_FILESYSTEM =='0':
            access_cache = "No"
        else:
             access_cache = "Yes" 
        ACCESS_FINE_LOCATION = request.form['ACCESS_FINE_LOCATION']
        if ACCESS_FINE_LOCATION =='0':
            access_fine = "No"
        else:
             access_fine = "Yes" 
        ACCESS_NETWORK_STATE = request.form['ACCESS_NETWORK_STATE']
        if ACCESS_NETWORK_STATE =='0':
            access_net = "No"
        else:
             access_net = "Yes" 
        ACCESS_SERVICE = request.form['ACCESS_SERVICE']
        if ACCESS_SERVICE =='0':
            access_ser = "No"
        else:
             access_ser = "Yes" 
        ACCESS_SHARED_DATA = request.form['ACCESS_SHARED_DATA'] 
        if ACCESS_SHARED_DATA =='0':
            access_sha = "No"
        else:
             access_sha = "Yes" 
        ACCESS_SUPERUSER = request.form['ACCESS_SUPERUSER']
        if ACCESS_SUPERUSER =='0':
            access_sup = "No"
        else:
             access_sup = "Yes" 
        ACCESS_WIFI_STATE = request.form['ACCESS_WIFI_STATE']
        if ACCESS_WIFI_STATE =='0':
            access_wifi = "No"
        else:
             access_wifi = "Yes" 
        CAMERA = request.form['CAMERA']
        if CAMERA =='0':
            camera = "No"
        else:
             camera = "Yes" 
        CHANGE_CONFIGURATION = request.form['CHANGE_CONFIGURATION']
        if CHANGE_CONFIGURATION =='0':
            change = "No"
        else:
             change = "Yes" 
        DELETE_CACHE_FILES = request.form['DELETE_CACHE_FILES']
        if DELETE_CACHE_FILES =='0':
            delete = "No"
        else:
             delete = "Yes" 
        READ_ATTACHMENT = request.form['READ_ATTACHMENT']
        if READ_ATTACHMENT =='0':
            read_atta = "No"
        else:
             read_atta = "Yes" 
        READ_CONTACTS = request.form['READ_CONTACTS']
        if READ_CONTACTS =='0':
            read_cont = "No"
        else:
             read_cont = "Yes" 
        READ_DATA = request.form['READ_DATA']
        if READ_DATA =='0':
            read_data = "No"
        else:
             read_data = "Yes" 
        READ_EXTERNAL_STORAGE = request.form['READ_EXTERNAL_STORAGE']
        if READ_EXTERNAL_STORAGE =='0':
            read_extra = "No"
        else:
             read_extra = "Yes" 
        READ_GMAIL = request.form['READ_GMAIL']
        if READ_GMAIL =='0':
            read_g = "No"
        else:
             read_g = "Yes" 
        READ_HISTORY_BOOKMARKS = request.form['READ_HISTORY_BOOKMARKS']
        if READ_HISTORY_BOOKMARKS =='0':
            read_hi = "No"
        else:
             read_hi = "Yes" 
        READ_MESSAGES = request.form['READ_MESSAGES']
        if READ_MESSAGES =='0':
            read_mess = "No"
        else:
             read_mess = "Yes" 
        READ_PHONE_STATE = request.form['READ_PHONE_STATE']
        if READ_PHONE_STATE =='0':
            read_phone = "No"
        else:
             read_phone = "Yes" 
        READ_SETTINGS = request.form['READ_SETTINGS']
        if READ_SETTINGS =='0':
            read_sett = "No"
        else:
             read_sett = "Yes" 
        READ_SMS = request.form['READ_SMS']
        if READ_SMS =='0':
            read_sms = "No"
        else:
             read_sms = "Yes" 
        RECEIVE_BOOT_COMPLETED = request.form['RECEIVE_BOOT_COMPLETED']
        if RECEIVE_BOOT_COMPLETED =='0':
            rece_boot = "No"
        else:
             rece_boot = "Yes" 
        RECEIVE_SMS = request.form['RECEIVE_SMS']
        if RECEIVE_SMS =='0':
            rece_sms = "No"
        else:
             rece_sms = "Yes" 


        model = request.form['model']
        
		# Clean the data by convert from unicode to float 
        
        sample_data = [ACCESS_ALL_DOWNLOADS,ACCESS_CACHE_FILESYSTEM,ACCESS_FINE_LOCATION,
                 ACCESS_NETWORK_STATE,
ACCESS_SERVICE,
ACCESS_SHARED_DATA,
ACCESS_SUPERUSER,
ACCESS_WIFI_STATE,
CAMERA,
CHANGE_CONFIGURATION,
DELETE_CACHE_FILES,
READ_ATTACHMENT,
READ_CONTACTS,
READ_DATA,
READ_EXTERNAL_STORAGE,
READ_GMAIL,
READ_HISTORY_BOOKMARKS,
READ_MESSAGES,
READ_PHONE_STATE,
READ_SETTINGS,
READ_SMS,
RECEIVE_BOOT_COMPLETED,
RECEIVE_SMS]
 
        # clean_data = [float(i) for i in sample_data]
        # int_feature = [x for x in sample_data]
        int_feature = [float(i) for i in sample_data]
        print(int_feature)
    

		# Reshape the Data as a Sample not Individual Features
        
        ex1 = np.array(int_feature).reshape(1,-1)
        print(ex1)
		# ex1 = np.array([6.2,3.4,5.4,2.3]).reshape(1,-1)

        # Reloading the Model
        if model == 'LogisticRegression':
           result_prediction = random_malware.predict(ex1)
           
            
        elif model == 'ExtraTreeClassifier':
          result_prediction = ExtraTree_malware.predict(ex1)
           
           
        
        # if result_prediction > 0.5:
        #     result = 'Malware'
        # else:
        #     result = 'Benign'    

          

    return render_template('result.html', prediction_text= result_prediction[0], model = model,access_all=access_all,access_cache=access_cache,access_fine=access_fine,access_net=access_net,access_ser=access_ser,access_sha=access_sha,access_sup=access_sup,access_wifi=access_wifi,camera=camera,change=change,delete=delete,read_atta=read_atta,read_cont=read_cont,read_data=read_data,read_extra=read_extra,read_g=read_g,read_hi=read_hi,read_mess=read_mess,read_phone=read_phone,read_sett=read_sett,read_sms=read_sms,rece_boot=rece_boot,rece_sms=rece_sms)

@app.route('/performance')
def performance():
    return render_template("performance.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")    

if __name__ == '__main__':
	app.run(debug=True)

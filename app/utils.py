import json,numpy as np,pandas as pd
import pickle
import os,CONFIG
from flask import Flask,request,render_template

class predictions():
    def __init__(self):
        print(os.getcwd())

    def load_raw_model(self):
        with open(CONFIG.MODEL_PATH,'rb') as model_file: 
            self.model = pickle.load(model_file)
    
        with open(CONFIG.ASSET_PATH,'r') as col_file: 
            self.column_names = json.load(col_file)
            
        with open(CONFIG.ENCODED_PATH,'r') as encode_file:
            self.encoded_data = json.load(encode_file)

    def predicted_millage(self,data):

        self.load_raw_model()
        self.data = data

        user_input = np.zeros(len(self.column_names['Column Names']))
        array = np.array(self.column_names['Column Names'])
        Make= self.data['html_make']
        Type= self.data['html_type']
        Origin=self.data['html_origin']
        DriveTrain=self.data['html_drive']
        MSRP=self.data['html_msrp']
        Invoice=self.data['html_invoice']
        EngineSize=self.data['html_esize']
        Cylinders=self.data['html_cyl']
        Horsepower=self.data['html_hpower']
        MPG_Highway=self.data['html_mpgh']
        Weight=self.data['html_weight']
        Wheelbase=self.data['html_whbase']
        Length=self.data['html_length']
        

        Make_string = 'Make_'+Make
        Make_index = np.where(array == Make_string)[0][0]
        user_input[Make_index] = 1 

        user_input[0] = int(Type)
        user_input[1] = int(Origin)
        user_input[2] = int(DriveTrain)
        user_input[3] = MSRP
        user_input[4] = Invoice
        user_input[5] = EngineSize
        user_input[6] = Cylinders
        user_input[7] = Horsepower
        user_input[8] = MPG_Highway
        user_input[9] = Weight
        user_input[10] = Wheelbase
        user_input[11] = Length

        print(f"{user_input=}")
        print(len(user_input))

        Millage_City = self.model.predict([user_input])
        print(f"Predicted millage = {Millage_City}")

        #return (f"Millage in city:",Millage_City)
        return render_template("car.html",PREDICT_MILLAGE=Millage_City)

if __name__=="__main__":

    pred_obj=predictions()
    pred_obj.load_raw_model()
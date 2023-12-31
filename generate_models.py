#we'll store here the models generated by the user in the app running the manage.py command

#sync_models() will be called by the manage.py command

# Path: generate_models.py

import os
from db import connect_mongo, create_db
from main import models

connect_mongo()

#sync_models() function:
# 1. get all the models from the database
# 2. create a new database
# 3. create a new collection for each model
# 4. create a new document for each model

#import variables from the main.py file and .env file

# Path: generate_models.py

env = os.environ.get('ENV', 'dev')

if env == 'dev':
    from dotenv import load_dotenv
    load_dotenv()
    from main import models
else:    
    models = models
    
    

def sync_models():
    #get all the models from the database
    models = get_models()
    #create a new database
    db = create_db('test')
    #create a new collection for each model
    for model in models:
        collection = db[model]
        #create a new document for each model
        collection.insert_one({'name': model})
        
def get_models():
    #get all the models from the database
    client = connect_mongo()
    db = client['test']
    models = db.list_collection_names()
    return models



    
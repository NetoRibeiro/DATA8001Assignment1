"""
    DATA8001 - Assignment 1 2021
    
    description: All Assignment 1 functions required to reproduce results
    
    version   1.0       ::  2021-03-02  ::  started version control

                                            ----------------------------------
                                                GENERIC FUNCTIONS
                                            ----------------------------------
                                            
                                            + data_etl
                                            + load_run_model
                                            
                                            ----------------------------------
                                                USER DEFINED FUNCTIONS
                                            ----------------------------------
                                            + 
"""

##########################################################################################
##########################################################################################
#
#   IMPORTS
#
##########################################################################################
##########################################################################################

import re
import pandas as pd
import numpy as np
import pickle
from datetime import datetime as dt



##########################################################################################
##########################################################################################
#
#   GENERIC FUNCTIONS
#
##########################################################################################
##########################################################################################

def data_etl(student_id):
    """
        Load original dataset and clean
        
        :param str student_id:
            The student_id to load the original dataset as provided in assignment zip file.

        :return: Processed (cleaned) pandas dataframe.
        :rtype: pandas.core.frame.DataFrame
    """
    try:

        print(f'cleaning data for {student_id} ...')
        
        #
        # 1. load the dataset
        #
        df_original = pd.read_csv(f'data/{student_id}_original.csv')

        #
        # 2. TODO - CLEAN THE DATA
        #

        df_processed = df_original.copy()

        #
        # 3. return processed (clean) data
        #
        return (df_processed)
        
    except Exception as ex:
        raise Exception(f'data_etl :: {ex}')


def load_run_model(student_id, df_test):
    """
        Load a Linear Regression pickle model and run the ML model on unseen data.
        
        :param str student_id:
            The student_id to load the model file path of the pickled model.
        :param df_test pandas.core.frame.DataFrame:
            The test data to predict.

        :return: Model predictions and accuracy
        :rtype: list, float
    """
    try:
        
        print(f'loading and running the linear regression model for {student_id} ...')

        predictions = []
        accuracy = 0.0

        #
        # 1. load the pickled model
        #
        
        
        #
        # 2. Pre-Process the unseen test data
        #
        

        
        #
        # 3. run the model on the pre-processed data and return predictions and model accuracy
        #

        return (predictions, accuracy)
        
    except Exception as ex:
        raise Exception(f'load_run_model :: {ex}')
        
        
class Data8001():
    """
        Data8001 model & transformation class
    """               
        
    #############################################
    #
    # Class Constructor
    #
    #############################################
    
    def __init__(self, transformations:list, model:object):
        """
            Initialse the objects.

            :param list transformations:
                A list of any data pre-processing transformations required
            :param object model:
                Model object
        """
        try:
            
            # validate inputs
            if transformations is None:
                transformations = []
            if type(transformations) != list:
                raise Exception('invalid transformations object type')
            if model is None:
                raise Exception('invalid model, cannot be none')                                
            
            # set the class variables
            self._transformations = transformations
            self._model = model
            
            print('data8001 initialised ...')
            
        except Exception as ex:
            raise Exception(f'Data8001 Constructor :: {ex}')
            
    #############################################
    #
    # Class Properties
    #
    #############################################
    
    def get_transformations(self) -> list:
        """
            Get the model transformations
            
            :return: A list of model transformations
            :rtype: list
        """
        return self._transformations
    
    def get_model(self) -> object:
        """
            Get the model object
            
            :return: A model object
            :rtype: object
        """
        return self._model

        
##########################################################################################
##########################################################################################
#
#   USER DEFINED FUNCTIONS
#
#   provide your custom functions below this box.
#
##########################################################################################
##########################################################################################


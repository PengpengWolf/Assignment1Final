# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:02:51 2020

@author: irisy
"""


def makeTerminalDict(terminal_rdf_SSH,terminal_connection_SSH):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(terminal_rdf_SSH)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']=terminal_rdf_SSH[l]#Get rdf and transform the format starting from a #       
        temp_dict['connection']=terminal_connection_SSH[l]#Get name     df
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict

def makeBreakerDict(breaker_rdf_SSH,breaker_connection_SSH):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(breaker_rdf_SSH)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']=breaker_rdf_SSH[l]#Get rdf and transform the format starting from a #       
        temp_dict['op_status']=breaker_connection_SSH[l]#Get name     df
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict


def makeSynMachineDict(synmachine_rdf_SSH,synmachine_P_SSH,synmachine_Q_SSH,synmachine_regulation_SSH):        
    host_dict=[]#Define list in which every element is a dictionary     
    for l in range(len(synmachine_rdf_SSH)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']=synmachine_rdf_SSH[l]#Get rdf and transform the format starting from a #       
        temp_dict['active_P']=synmachine_P_SSH[l]#Get P
        temp_dict['reactive_Q']=synmachine_Q_SSH[l]#Get Q
        temp_dict['regulation']=synmachine_regulation_SSH[l]#Get Q
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict

def makeEnergyConsumerDict(energyconsumer_rdf_SSH,energyconsumer_P_SSH,energyconsumer_Q_SSH):        
    host_dict=[]#Define list in which every element is a dictionary     
    for l in range(len(energyconsumer_rdf_SSH)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']=energyconsumer_rdf_SSH[l]#Get rdf and transform the format starting from a #       
        temp_dict['active_P']=energyconsumer_P_SSH[l]#Get P
        temp_dict['reactive_Q']=energyconsumer_Q_SSH[l]#Get Q
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict
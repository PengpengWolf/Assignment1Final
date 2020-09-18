# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:11:07 2020

@author: irisy
"""

def makeBusbarDict(busbar_rdf,busbar_name,busbar_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary 
    
    for l in range(len(busbar_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+busbar_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=busbar_name[l]#Get name     
        temp_dict['EC_rdf']=busbar_EC_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'bus'#type
        temp_dict['bus']= 'null'#type
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict


def makeACLineDict(ACLine_rdf,ACLine_name,ACLine_EC_rdf,ACLine_len,ACLine_vol,ACLine_r,ACLine_x,ACLine_bch,ACLine_gch,ACLine_agg):      
    host_dict=[]#Define list in which every element is a dictionary 
    for l in range(len(ACLine_name)):        
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+ACLine_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=ACLine_name[l]#Get name     
        temp_dict['EC_rdf']=ACLine_EC_rdf[l]#Get equipment container rdf
        temp_dict['len']=ACLine_len[l]#Get line length
        temp_dict['vol_rdf']=ACLine_vol[l]#Get rated voltage
        temp_dict['r']=ACLine_r[l]#Get r per kilometer
        temp_dict['x']=ACLine_x[l]#Get x per kilometer
        temp_dict['bch']=ACLine_bch[l]#Get bch per kilometer
        temp_dict['gch']=ACLine_gch[l]#Get gch per kilometer
        temp_dict['aggregate']=ACLine_agg[l]#Get x per kilometer
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'ACline'#type
        temp_dict['hs_bus']= 'null'
        temp_dict['ls_bus']= 'null' 
        
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict

def makeBreakerDict(breaker_rdf,breaker_name,breaker_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(breaker_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+breaker_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=breaker_name[l]#Get name     
        temp_dict['EC_rdf']=breaker_EC_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'breaker'#type
        temp_dict['hs_bus']= 'null'
        temp_dict['ls_bus']= 'null'
        temp_dict['op_status']= 'null'
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict


def makeEnergyConsumerDict(energyconsumer_rdf,energyconsumer_name,energyconsumer_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(energyconsumer_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+energyconsumer_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=energyconsumer_name[l]#Get name     
        temp_dict['EC_rdf']=energyconsumer_EC_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'EnergyConsumer'#type
        temp_dict['active_P']=0#Get P
        temp_dict['reactive_Q']=0#Get Q        
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict

def makeGeneratingUnitDict(generatingunit_rdf,generatingunit_name,generatingunit_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(generatingunit_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+generatingunit_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=generatingunit_name[l]#Get name     
        temp_dict['EC_rdf']=generatingunit_EC_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'GeneratingUnit'#type
        
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict

def makeLineDict(line_rdf,line_name,line_region_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(line_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+line_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=line_name[l]#Get name     
        temp_dict['region_rdf']=line_region_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'EC'#type 
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict

def makeLinearShuntCompDict(linearshuntcomp_rdf,linearshuntcomp_name,linearshuntcomp_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(linearshuntcomp_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+linearshuntcomp_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=linearshuntcomp_name[l]#Get name     
        temp_dict['EC_rdf']=linearshuntcomp_EC_rdf[l]#Get equipment container rdf 
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'LinearShuntComp'#type
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict

def makePowerTrDict(powertr_rdf,powertr_name,powertr_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(powertr_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+powertr_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=powertr_name[l]#Get name     
        temp_dict['EC_rdf']=powertr_EC_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'PowerTr'#type
        temp_dict['vol']= 0
        temp_dict['hs']= 0
        temp_dict['ls']= 0
        temp_dict['hs_bus']= 'null'
        temp_dict['ls_bus']= 'null'       
        host_dict.append(temp_dict)#append the dict to the list 

    return host_dict

def makePowerTrEndDict(powertrend_rdf,powertrend_name,powertrend_vol,powertrend_tr,powertrend_term,powertrend_number):        
    host_dict=[]#Define list in which every element is a dictionary  
    for l in range(len(powertrend_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+powertrend_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=powertrend_name[l]#Get name     
        temp_dict['vol']=powertrend_vol[l]#Get equipment container rdf
        temp_dict['transformer']=powertrend_tr[l]#Get equipment container rdf
        temp_dict['terminal']=powertrend_term[l]#Get equipment container rdf       
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'PowerTrEnd'#type
        temp_dict['endNumber']= powertrend_number[l]#type
        
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict

def makeRatioTapChangerDict(ratiotapchanger_rdf,ratiotapchanger_name,ratiotapchanger_control,ratiotapchanger_trend):        
    host_dict=[]#Define list in which every element is a dictionary  
    for l in range(len(ratiotapchanger_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+ratiotapchanger_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=ratiotapchanger_name[l]#Get name     
        temp_dict['control']=ratiotapchanger_control[l]#Get equipment container rdf
        temp_dict['trend']=ratiotapchanger_trend[l]#Get equipment container rdf  
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type 
        temp_dict['CE_type']= 'RatioTapChanger'#type
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict

def makeSubstationDict(substation_rdf,substation_name,substation_region_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(substation_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+substation_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=substation_name[l]#Get name     
        temp_dict['region_rdf']=substation_region_rdf[l]#Get equipment container rdf         
        temp_dict['type']= 'EC'#type 
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict


def makeSubGeoRegionDict(subgeoregion_rdf,subgeoregion_name,subgeoregion_region_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(subgeoregion_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+subgeoregion_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=subgeoregion_name[l]#Get name     
        temp_dict['region_rdf']=subgeoregion_region_rdf[l]#Get equipment container rdf
        temp_dict['type']= 'EC'#type 
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict


def makeSynMachineDict(synmachine_rdf,synmachine_name,synmachine_earth,synmachine_S,synmachine_PF):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(synmachine_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+synmachine_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=synmachine_name[l]#Get name     
        temp_dict['earth']=synmachine_earth[l]#Get equipment container rdf        
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CE'#type
        temp_dict['CE_type']= 'SynMachine'#type
        temp_dict['bus']= 'null'#type
        temp_dict['S']=float(synmachine_S[l])
        temp_dict['PF']=float(synmachine_PF[l])
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict



def makeTerminalDict(terminal_rdf,terminal_name,terminal_seq,terminal_CE_rdf,terminal_CN_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(terminal_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+terminal_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=terminal_name[l]#Get name     
        temp_dict['seq']=terminal_seq[l]#Get equipment container rdf
        temp_dict['CE_rdf']=terminal_CE_rdf[l]#Get name     
        temp_dict['CN_rdf']=terminal_CN_rdf[l]#Get equipment container rdf
        temp_dict['traversal_flag'] = 0# traversed or not
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'TE'#type 
        host_dict.append(temp_dict)#append the dict to the list
    return host_dict

def makeVoltageLevelDict(vol_Level_rdf,vol_Level_name,vol_Level_sub,vol_Level_base_rdf):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(vol_Level_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+vol_Level_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=vol_Level_name[l]#Get name     
        temp_dict['substation']=vol_Level_sub[l]#Get equipment container rdf
        temp_dict['base_rdf']=vol_Level_base_rdf[l]#Get equipment container rdf       
        temp_dict['type']= 'EC'#type 
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict


def makeVoltageBaseDict(vol_base_rdf,vol_base_name,vol_base_nominal):        
    host_dict=[]#Define list in which every element is a dictionary    
    for l in range(len(vol_base_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+vol_base_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=vol_base_name[l]#Get name     
        temp_dict['nominal']=vol_base_nominal[l]#Get equipment container rdf        
        temp_dict['type']= 'EC'#type 
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict

       
def makeConnnectivityNodeDict(CN_rdf,CN_name,CN_EC_rdf):        
    host_dict=[]#Define list in which every element is a dictionary 
    
    for l in range(len(CN_name)):
        temp_dict={}#Temp dict for use in the loop
        temp_dict['rdf']='#'+CN_rdf[l]#Get rdf and transform the format starting from a #       
        temp_dict['name']=CN_name[l]#Get name     
        temp_dict['EC_rdf']=CN_EC_rdf[l]#Get equipment container rdf
        temp_dict['Terminal_list'] = []#terminals connected
        temp_dict['num_attachTerms'] = 0#numbers of terminals connected
        temp_dict['type']= 'CN'#type 
        temp_dict['vol']= 0
        temp_dict['bus']= 'null'
        host_dict.append(temp_dict)#append the dict to the list 
    return host_dict




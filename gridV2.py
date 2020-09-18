# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:49:36 2020

@author: Pengpeng sun
"""

# This python program is an introduction to reading and parsing CIM-XML files  as part of the 
# EH2745 Computer Applications in power systems course at KTH
# Author: Pengpeng Sun, pengpeng@kth.se 
# Date: 2020-04-17
#
#

# First thing we need to do is to import the ElementTree library
import xml.etree.ElementTree as ET
import makeDict as md
import makeDictSSH as mdSSH
import pandapower as pp #import pandapower
import random
from pandapower.plotting.plotly import simple_plotly




#Next step is to create a tree by parsing the XML file referenced
# We are here using ENTSO-E  model files used in Interoperability testing
tree_EQ = ET.parse('Assignment_EQ_reduced.xml')
tree_SSH = ET.parse('Assignment_SSH_reduced.xml')
#If you have not already, please open up the books.xml file

# After these two steps we now have read the XML file and converted (parsed) 
# the XML data with its tags, attributes and data into a tree stored in memory

# We can access the root of the tree and print it
grid_EQ = tree_EQ.getroot()
grid_SSH = tree_SSH.getroot()


# To make working with the file easier, it may be useful to store the 
# namespace identifiers in strings and reuse when you search for tags
    
ns = {'cim':'http://iec.ch/TC57/2013/CIM-schema-cim16#',
      'entsoe':'http://entsoe.eu/CIM/SchemaExtension/3/1#',
      'rdf':'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'}

# We create a dictionary  (above) and store the namespace names and their 
# respective URIs in it. We can then reference the namespace like below
# To make pritount more compact, we can replace the namespace URI with a 
# shorter string or even a null-string "".

# Note that in the dictionary, the curly braces '{' are used for the RDF tag
# but not for the cim and entsoe tags. This is a special solution to fix
# a problem of dual use of the curly braces in python dictionaries and the
# XML namespace tags. 


               
# Store the data of different equipments in seperate dictionaries. 
# The key attributes should include as more information as possible.

node_list=[]

# Busbarsection: attributes include rdf, name and equipment container rdf
# if length of tags, name and equipment container rdf are different, an error is ouput.
busbar_rdf=[]
busbar_name=[]
busbar_EC_rdf=[]
# find all attributes in the file:
for busbars in grid_EQ.findall('cim:BusbarSection', ns):
    busbar_rdf.append(busbars.get(ns['rdf']+'ID')) 
    name = busbars.find('cim:IdentifiedObject.name',ns)
    busbar_name.append(name.text)
    EC = busbars.find('cim:Equipment.EquipmentContainer',ns)
    busbar_EC_rdf.append(EC.get(ns['rdf']+'resource'))
busbar_num=len(busbar_rdf) 
#if length of different attributes are different, an error is output
assert busbar_num==len(busbar_EC_rdf)
assert busbar_num==len(busbar_name)
#Create the busbuar dictionary
busbar_dict=md.makeBusbarDict(busbar_rdf,busbar_name,busbar_EC_rdf)

#print(busbar_dict[1]['rdf'])
#print(busbar_dict)


# Connectivitynode: attributes include rdf, name and equipment container rdf
# if length of tags, name and equipment container rdf are different, an error is ouput.
CN_rdf=[]
CN_name=[]
CN_EC_rdf=[]
# find all attributes in the file:
for cn in grid_EQ.findall('cim:ConnectivityNode', ns):
    CN_rdf.append(cn.get(ns['rdf']+'ID')) 
    name = cn.find('cim:IdentifiedObject.name',ns)
    CN_name.append(name.text)
    EC = cn.find('cim:ConnectivityNode.ConnectivityNodeContainer',ns)
    CN_EC_rdf.append(EC.get(ns['rdf']+'resource'))
CN_num=len(CN_rdf) 
#if length of different attributes are different, an error is output
assert CN_num==len(CN_EC_rdf)
assert CN_num==len(CN_name)
#Create the busbuar dictionary
CN_dict=md.makeConnnectivityNodeDict(CN_rdf,CN_name,CN_EC_rdf)

#print(busbar_dict[1]['rdf'])
#print(busbar_dict)



# ACLineSegment: attributes include rdf, name， equipment container rdf， length, basevoltage
# if length of tags, name and equipment container rdf are different, an error is ouput.
ACLine_rdf=[]
ACLine_name=[]
ACLine_EC_rdf=[]
ACLine_len=[]
ACLine_vol=[]
ACLine_r=[]
ACLine_x=[]
ACLine_gch=[]
ACLine_bch=[]
ACLine_agg=[]
# find all attributes in the file:
for line in grid_EQ.findall('cim:ACLineSegment', ns):
    ACLine_rdf.append(line.get(ns['rdf']+'ID')) 
    name = line.find('cim:IdentifiedObject.name',ns)
    ACLine_name.append(name.text)
    EC = line.find('cim:Equipment.EquipmentContainer',ns)
    ACLine_EC_rdf.append(EC.get(ns['rdf']+'resource'))
    length=line.find('cim:Conductor.length',ns)
    ACLine_len.append(length.text)
    vol=line.find('cim:ConductingEquipment.BaseVoltage',ns)
    ACLine_vol.append(vol.get(ns['rdf']+'resource'))   
    r=line.find('cim:ACLineSegment.r',ns)
    ACLine_r.append(r.text)
    x=line.find('cim:ACLineSegment.x',ns)
    ACLine_x.append(x.text)
    bch=line.find('cim:ACLineSegment.bch',ns)
    ACLine_bch.append(bch.text)
    gch=line.find('cim:ACLineSegment.gch',ns)
    ACLine_gch.append(x.text)
    agg=line.find('cim:Equipment.aggregate',ns)
    ACLine_agg.append(agg.text)
ACLine_num=len(ACLine_rdf) 
#if length of different attributes are different, an error is output
assert ACLine_num==len(ACLine_EC_rdf)
assert ACLine_num==len(ACLine_name)
assert ACLine_num==len(ACLine_len)
assert ACLine_num==len(ACLine_vol)
assert ACLine_num==len(ACLine_r)
assert ACLine_num==len(ACLine_x)
assert ACLine_num==len(ACLine_bch)
assert ACLine_num==len(ACLine_gch)
#assert ACLine_num==len(ACLine_agg)
#Create the ACline dictionary
ACLine_dict=md.makeACLineDict(ACLine_rdf,ACLine_name,ACLine_EC_rdf,ACLine_len,ACLine_vol,ACLine_r,ACLine_x,ACLine_bch,ACLine_gch,ACLine_agg)


# Breaker: attributes include rdf, name and equipment container rdf
# if length of rdf, name and equipment container rdf are different, an error is ouput.
breaker_rdf=[]
breaker_name=[]
breaker_EC_rdf=[]
# find all attributes in the file:
for breaker in grid_EQ.findall('cim:Breaker', ns):
    breaker_rdf.append(breaker.get(ns['rdf']+'ID')) 
    name = breaker.find('cim:IdentifiedObject.name',ns)
    breaker_name.append(name.text)
    EC = breaker.find('cim:Equipment.EquipmentContainer',ns)
    breaker_EC_rdf.append(EC.get(ns['rdf']+'resource'))
breaker_num=len(breaker_rdf)
#print(breaker_rdf,'/',breaker_EC_rdf,'/',breaker_name) 
#print(breaker_num,len(breaker_EC_rdf),len(breaker_name))
#if length of different attributes are different, an error is output
assert breaker_num==len(breaker_EC_rdf)
assert breaker_num==len(breaker_name)
#Create the busbuar dictionary
breaker_dict=md.makeBreakerDict(breaker_rdf,breaker_name,breaker_EC_rdf)

#print(breaker_dict)


# EnergyConsumer: attributes include rdf, name and equipment container rdf
# if length of rdf, name and equipment container rdf are different, an error is ouput.
energyconsumer_rdf=[]
energyconsumer_name=[]
energyconsumer_EC_rdf=[]
# find all attributes in the file:
for energyconsumer in grid_EQ.findall('cim:EnergyConsumer', ns):
    energyconsumer_rdf.append(energyconsumer.get(ns['rdf']+'ID')) 
    name = energyconsumer.find('cim:IdentifiedObject.name',ns)
    energyconsumer_name.append(name.text)
    EC = energyconsumer.find('cim:Equipment.EquipmentContainer',ns)
    energyconsumer_EC_rdf.append(EC.get(ns['rdf']+'resource'))       
energyconsumer_num=len(energyconsumer_rdf)
#print(breaker_rdf,'/',breaker_EC_rdf,'/',breaker_name) 
#print(breaker_num,len(breaker_EC_rdf),len(breaker_name))
#if length of different attributes are different, an error is output
assert energyconsumer_num==len(energyconsumer_EC_rdf)
assert energyconsumer_num==len(energyconsumer_name)
#Create the busbuar dictionary
energyconsumer_dict=md.makeEnergyConsumerDict(energyconsumer_rdf,energyconsumer_name,energyconsumer_EC_rdf)


# GeneratingUnit: attributes include rdf, name and equipment container rdf
# if length of rdf, name and equipment container rdf are different, an error is ouput.
generatingunit_rdf=[]
generatingunit_name=[]
generatingunit_EC_rdf=[]
# find all attributes in the file:
for generatingunit in grid_EQ.findall('cim:GeneratingUnit', ns):
    generatingunit_rdf.append(generatingunit.get(ns['rdf']+'ID')) 
    name = generatingunit.find('cim:IdentifiedObject.name',ns)
    generatingunit_name.append(name.text)
    EC = generatingunit.find('cim:Equipment.EquipmentContainer',ns)
    generatingunit_EC_rdf.append(EC.get(ns['rdf']+'resource'))
generatingunit_num=len(generatingunit_rdf)
#if length of different attributes are different, an error is output
assert generatingunit_num==len(generatingunit_EC_rdf)
assert generatingunit_num==len(generatingunit_name)
#Create the busbuar dictionary
generatingunit_dict=md.makeGeneratingUnitDict(generatingunit_rdf,generatingunit_name,generatingunit_EC_rdf)


# Line: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
line_rdf=[]
line_name=[]
line_region_rdf=[]
# find all attributes in the file:
for line in grid_EQ.findall('cim:Line', ns):
    line_rdf.append(line.get(ns['rdf']+'ID')) 
    name = line.find('cim:IdentifiedObject.name',ns)
    line_name.append(name.text)
    region = line.find('cim:Line.Region',ns)
    line_region_rdf.append(region.get(ns['rdf']+'resource'))
line_num=len(line_rdf)
#if length of different attributes are different, an error is output
assert line_num==len(line_region_rdf)
assert line_num==len(line_name)
#Create the busbuar dictionary
line_dict=md.makeLineDict(line_rdf,line_name,line_region_rdf)


# LinearShuntCompensator: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
linearshuntcomp_rdf=[]
linearshuntcomp_name=[]
linearshuntcomp_EC_rdf=[]
# find all attributes in the file:
for linearshuntcomp in grid_EQ.findall('cim:LinearShuntCompensator', ns):
    linearshuntcomp_rdf.append(linearshuntcomp.get(ns['rdf']+'ID')) 
    name = linearshuntcomp.find('cim:IdentifiedObject.name',ns)
    linearshuntcomp_name.append(name.text)
    EC = linearshuntcomp.find('cim:Equipment.EquipmentContainer',ns)
    linearshuntcomp_EC_rdf.append(EC.get(ns['rdf']+'resource'))
linearshuntcomp_num=len(linearshuntcomp_rdf)
#print(breaker_rdf,'/',breaker_EC_rdf,'/',breaker_name) 
#print(breaker_num,len(breaker_EC_rdf),len(breaker_name))
#if length of different attributes are different, an error is output
assert linearshuntcomp_num==len(linearshuntcomp_EC_rdf)
assert linearshuntcomp_num==len(linearshuntcomp_name)
#Create the busbuar dictionary
linearshuntcomp_dict=md.makeLinearShuntCompDict(linearshuntcomp_rdf,linearshuntcomp_name,linearshuntcomp_EC_rdf)


# PowerTransformer: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
powertr_rdf=[]
powertr_name=[]
powertr_EC_rdf=[]
# find all attributes in the file:
for powertr in grid_EQ.findall('cim:PowerTransformer', ns):
    powertr_rdf.append(powertr.get(ns['rdf']+'ID')) 
    name = powertr.find('cim:IdentifiedObject.name',ns)
    powertr_name.append(name.text)
    EC = powertr.find('cim:Equipment.EquipmentContainer',ns)
    powertr_EC_rdf.append(EC.get(ns['rdf']+'resource'))
powertr_num=len(powertr_rdf)
#if length of different attributes are different, an error is output
assert powertr_num==len(powertr_EC_rdf)
assert powertr_num==len(powertr_name)
#Create the busbuar dictionary
powertr_dict=md.makePowerTrDict(powertr_rdf,powertr_name,powertr_EC_rdf)        

#print(powertr_dict)

# PowerTransformerEnd: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
powertrend_rdf=[]
powertrend_name=[]
powertrend_vol=[]
powertrend_tr=[]
powertrend_term=[]
powertrend_number=[]
# find all attributes in the file:
for powertrend in grid_EQ.findall('cim:PowerTransformerEnd', ns):
    powertrend_rdf.append(powertrend.get(ns['rdf']+'ID')) 
    name = powertrend.find('cim:IdentifiedObject.name',ns)
    powertrend_name.append(name.text)
    vol = powertrend.find('cim:TransformerEnd.BaseVoltage',ns)
    powertrend_vol.append(vol.get(ns['rdf']+'resource'))
    tr = powertrend.find('cim:PowerTransformerEnd.PowerTransformer',ns)
    powertrend_tr.append(tr.get(ns['rdf']+'resource'))
    term = powertrend.find('cim:TransformerEnd.Terminal',ns)
    powertrend_term.append(term.get(ns['rdf']+'resource'))     
    num = powertrend.find('cim:TransformerEnd.endNumber',ns)
    powertrend_number.append(num.text) 
powertrend_num=len(powertrend_rdf)
#if length of different attributes are different, an error is output
assert powertrend_num==len(powertrend_vol)
assert powertrend_num==len(powertrend_name)
assert powertrend_num==len(powertrend_tr)
assert powertrend_num==len(powertrend_term)
#Create the dictionary
powertrend_dict=md.makePowerTrEndDict(powertrend_rdf,powertrend_name,powertrend_vol,powertrend_tr,powertrend_term,powertrend_number)
#print(powertrend_dict)


# RatioTapChanger: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
ratiotapchanger_rdf=[]
ratiotapchanger_name=[]
ratiotapchanger_control=[]
ratiotapchanger_trend=[]
# find all attributes in the file:
for ratiotapchanger in grid_EQ.findall('cim:RatioTapChanger', ns):
    ratiotapchanger_rdf.append(ratiotapchanger.get(ns['rdf']+'ID')) 
    name = ratiotapchanger.find('cim:IdentifiedObject.name',ns)
    ratiotapchanger_name.append(name.text)
    control = ratiotapchanger.find('cim:TapChanger.TapChangerControl',ns)
    ratiotapchanger_control.append(control.get(ns['rdf']+'resource'))
    trend = ratiotapchanger.find('cim:RatioTapChanger.TransformerEnd',ns)
    ratiotapchanger_trend.append(trend.get(ns['rdf']+'resource'))   
ratiotapchanger_num=len(ratiotapchanger_rdf)
#if length of different attributes are different, an error is output
assert ratiotapchanger_num==len(ratiotapchanger_control)
assert ratiotapchanger_num==len(ratiotapchanger_name)
assert ratiotapchanger_num==len(ratiotapchanger_trend)
#Create the busbuar dictionary
ratiotapchanger_dict=md.makeRatioTapChangerDict(ratiotapchanger_rdf,ratiotapchanger_name,ratiotapchanger_control,ratiotapchanger_trend) 
#print(ratiotapchanger_dict)

# Substation: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
substation_rdf=[]
substation_name=[]
substation_region_rdf=[]
# find all attributes in the file:
for substation in grid_EQ.findall('cim:Substation', ns):
    substation_rdf.append(substation.get(ns['rdf']+'ID')) 
    name = substation.find('cim:IdentifiedObject.name',ns)
    substation_name.append(name.text)
    region = substation.find('cim:Substation.Region',ns)
    substation_region_rdf.append(region.get(ns['rdf']+'resource'))
substation_num=len(line_rdf)
#if length of different attributes are different, an error is output
assert substation_num==len(substation_region_rdf)
assert substation_num==len(substation_name)
#Create the busbuar dictionary
substation_dict=md.makeSubstationDict(substation_rdf,substation_name,substation_region_rdf)

#print(substation_dict)

# SubGeographicalRegion: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
subgeoregion_rdf=[]
subgeoregion_name=[]
subgeoregion_region_rdf=[]
# find all attributes in the file:
for subgeoregion in grid_EQ.findall('cim:SubGeographicalRegion', ns):
    subgeoregion_rdf.append(subgeoregion.get(ns['rdf']+'ID')) 
    name = subgeoregion.find('cim:IdentifiedObject.name',ns)
    subgeoregion_name.append(name.text)
    region = subgeoregion.find('cim:SubGeographicalRegion.Region',ns)
    subgeoregion_region_rdf.append(region.get(ns['rdf']+'resource'))
subgeoregion_num=len(subgeoregion_rdf)
#if length of different attributes are different, an error is output
assert subgeoregion_num==len(subgeoregion_region_rdf)
assert subgeoregion_num==len(subgeoregion_name)
#Create the busbuar dictionary
subgeoregion_dict=md.makeSubGeoRegionDict(subgeoregion_rdf,subgeoregion_name,subgeoregion_region_rdf)

#print(subgeoregion_dict)


# SynchronousMachine: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
synmachine_rdf=[]
synmachine_name=[]
synmachine_earth=[]
synmachine_S=[]
synmachine_PF=[]
# find all attributes in the file:
for synmachine in grid_EQ.findall('cim:SynchronousMachine', ns):
    synmachine_rdf.append(synmachine.get(ns['rdf']+'ID')) 
    name = synmachine.find('cim:IdentifiedObject.name',ns)
    synmachine_name.append(name.text)
    region = synmachine.find('cim:SynchronousMachine.earthing',ns)
    synmachine_earth.append(region.text)
    rated_S = synmachine.find('cim:RotatingMachine.ratedS',ns)
    synmachine_S.append(rated_S.text)
    PF = synmachine.find('cim:RotatingMachine.ratedPowerFactor',ns)
    synmachine_PF.append(PF.text)    
synmachine_num=len(synmachine_rdf)
#if length of different attributes are different, an error is output
assert synmachine_num==len(synmachine_earth)
assert synmachine_num==len(synmachine_name)
#Create the busbuar dictionary
synmachine_dict=md.makeSynMachineDict(synmachine_rdf,synmachine_name,synmachine_earth,synmachine_S,synmachine_PF)

#print(synmachine_dict)

# Terminal: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
terminal_rdf=[]
terminal_name=[]
terminal_seq=[]
terminal_CE_rdf=[]
terminal_CN_rdf=[]
# find all attributes in the file:
for terminal in grid_EQ.findall('cim:Terminal', ns):    
    terminal_rdf.append(terminal.get(ns['rdf']+'ID')) 
    name = terminal.find('cim:IdentifiedObject.name',ns)
    terminal_name.append(name.text)
    seq = terminal.find('cim:ACDCTerminal.sequenceNumber',ns)
    terminal_seq.append(seq.text)
    CE_rdf = terminal.find('cim:Terminal.ConductingEquipment',ns)
    terminal_CE_rdf.append(CE_rdf.get(ns['rdf']+'resource'))
    CN_rdf = terminal.find('cim:Terminal.ConnectivityNode',ns)
    terminal_CN_rdf.append(CN_rdf.get(ns['rdf']+'resource'))                           
terminal_num=len(terminal_rdf)
#if length of different attributes are different, an error is output
assert terminal_num==len(terminal_seq)
assert terminal_num==len(terminal_name)
assert terminal_num==len(terminal_CE_rdf)
assert terminal_num==len(terminal_CN_rdf)
#Create the busbuar dictionary
terminal_dict=md.makeTerminalDict(terminal_rdf,terminal_name,terminal_seq,terminal_CE_rdf,terminal_CN_rdf)

#print(synmachine_dict)

 
# VoltageLevel attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
vol_Level_rdf=[]
vol_Level_name=[]
vol_Level_sub=[]
vol_Level_base_rdf=[]
# find all attributes in the file:
for vol in grid_EQ.findall('cim:VoltageLevel', ns):
    vol_Level_rdf.append(vol.get(ns['rdf']+'ID')) 
    name = vol.find('cim:IdentifiedObject.name',ns)
    vol_Level_name.append(name.text)
    sub = vol.find('cim:VoltageLevel.Substation',ns)
    vol_Level_sub.append(sub.get(ns['rdf']+'resource'))
    base_rdf = vol.find('cim:VoltageLevel.BaseVoltage',ns)
    vol_Level_base_rdf.append(base_rdf.get(ns['rdf']+'resource'))   
vol_Level_num=len(vol_Level_rdf)
#if length of different attributes are different, an error is output
assert vol_Level_num==len(vol_Level_sub)
assert vol_Level_num==len(vol_Level_name)
#Create the busbuar dictionary
vol_Level_dict=md.makeVoltageLevelDict(vol_Level_rdf,vol_Level_name,vol_Level_sub,vol_Level_base_rdf)

#print(vol_Level_dict)

# BaseVoltage: attributes include rdf, name and geographical region
# if length of rdf, name and geographical region rdf are different, an error is ouput.
vol_base_rdf=[]
vol_base_name=[]
vol_base_nominal=[]
# find all attributes in the file:
for vol in grid_EQ.findall('cim:BaseVoltage', ns):
    vol_base_rdf.append(vol.get(ns['rdf']+'ID')) 
    name = vol.find('cim:IdentifiedObject.name',ns)
    vol_base_name.append(name.text)
    nominal = vol.find('cim:BaseVoltage.nominalVoltage',ns)
    vol_base_nominal.append(nominal.text)
vol_base_num=len(vol_base_rdf)
#if length of different attributes are different, an error is output
assert vol_base_num==len(vol_base_nominal)
assert vol_base_num==len(vol_base_name)
#Create the busbuar dictionary
vol_base_dict=md.makeVoltageBaseDict(vol_base_rdf,vol_base_name,vol_base_nominal)

#print(vol_base_dict)



# Gather data from SSH
# For ternimals, the information is the connection true or false.
# For breakers, the information is the open status true or false.
# For SynchronousMachine, the information is p and q, regulation enabled or not.
# For RatioTapChanger, the information is step and regulation enabled or not.
# For LinearShuntCompensator, the information is sections and regulation enabled or not.
# For TapChangerControl, the information is rdf, way of control, deadband,regulation enabled or not and target value.
# For RegulatingControl, the information is rdf, way of control, deadband,regulation enabled or not and target value.

# Terminal: attributes include rdf, connection true or false.
# if length of rdf, connection are different, an error is ouput.
terminal_rdf_SSH=[]
terminal_connection_SSH=[]
# find all attributes in the file:
for ter in grid_SSH.findall('cim:Terminal', ns):
    terminal_rdf_SSH.append(ter.get(ns['rdf']+'about')) 
    connection = ter.find('cim:ACDCTerminal.connected',ns)
    terminal_connection_SSH.append(connection.text)
terminal_num_SSH=len(terminal_rdf_SSH)
#if length of different attributes are different, an error is output
assert terminal_num_SSH==len(terminal_connection_SSH)

#Create the busbuar dictionary
terminal_dict_SSH=mdSSH.makeTerminalDict(terminal_rdf_SSH,terminal_connection_SSH)

#print(terminal_dict_SSH)

# Breakers: attributes include rdf, open status true or false.
# if length of rdf, connection are different, an error is ouput.
breaker_rdf_SSH=[]
breaker_connection_SSH=[]
# find all attributes in the file:
for breaker in grid_SSH.findall('cim:Breaker', ns):
    breaker_rdf_SSH.append(breaker.get(ns['rdf']+'about')) 
    op_status = breaker.find('cim:Switch.open',ns)
    breaker_connection_SSH.append(op_status.text)
breaker_num_SSH=len(breaker_rdf_SSH)
#if length of different attributes are different, an error is output
assert breaker_num_SSH==len(breaker_connection_SSH)

#Create the busbuar dictionary
breaker_dict_SSH=mdSSH.makeBreakerDict(breaker_rdf_SSH,breaker_connection_SSH)

#print(breaker_dict_SSH)


# SynchronousMachine, the information is p and q, regulation enabled or not.
# if length of rdf, connection are different, an error is ouput.
synmachine_rdf_SSH=[]
synmachine_P_SSH=[]
synmachine_Q_SSH=[]
synmachine_regulation_SSH=[]
# find all attributes in the file:
for synmachine in grid_SSH.findall('cim:SynchronousMachine', ns):
    synmachine_rdf_SSH.append(synmachine.get(ns['rdf']+'about')) 
    active_P = synmachine.find('cim:RotatingMachine.p',ns)
    synmachine_P_SSH.append(active_P.text)
    reactive_Q = synmachine.find('cim:RotatingMachine.q',ns)
    synmachine_Q_SSH.append(reactive_Q.text)  
    regulation = synmachine.find('cim:RegulatingCondEq.controlEnabled',ns)
    synmachine_regulation_SSH.append(regulation.text)
synmachine_num_SSH=len(synmachine_rdf_SSH)
#if length of different attributes are different, an error is output
assert synmachine_num_SSH==len(synmachine_P_SSH)
assert synmachine_num_SSH==len(synmachine_Q_SSH)
assert synmachine_num_SSH==len(synmachine_regulation_SSH)

#Create the dictionary
synmachine_dict_SSH=mdSSH.makeSynMachineDict(synmachine_rdf_SSH,synmachine_P_SSH,synmachine_Q_SSH,synmachine_regulation_SSH)

# Energyconsumer, the information is p and q.
# if length of rdf, connection are different, an error is ouput.
energyconsumer_rdf_SSH=[]
energyconsumer_P_SSH=[]
energyconsumer_Q_SSH=[]
# find all attributes in the file:
for energyconsumer in grid_SSH.findall('cim:EnergyConsumer', ns):
    energyconsumer_rdf_SSH.append(energyconsumer.get(ns['rdf']+'about')) 
    active_P = energyconsumer.find('cim:EnergyConsumer.p',ns)
    energyconsumer_P_SSH.append(active_P.text)
    reactive_Q = energyconsumer.find('cim:EnergyConsumer.q',ns)
    energyconsumer_Q_SSH.append(reactive_Q.text)  
energyconsumer_num_SSH=len(energyconsumer_rdf_SSH)
#if length of different attributes are different, an error is output
assert energyconsumer_num_SSH==len(energyconsumer_P_SSH)
assert energyconsumer_num_SSH==len(energyconsumer_Q_SSH)


#Create the dictionary
energyconsumer_dict_SSH=mdSSH.makeEnergyConsumerDict(energyconsumer_rdf_SSH,energyconsumer_P_SSH,energyconsumer_Q_SSH)



#print(synmachine_dict_SSH)


# Identify the nominal voltage in Voltagelevel
for l in range(len(vol_Level_dict)):
    for i in range(len(vol_base_dict)):
        if vol_Level_dict[l]['base_rdf'] == vol_base_dict[i]['rdf']:
            vol_Level_dict[l]['base_vol'] = vol_base_dict[i]['nominal']
# Identify the nominal voltage of different equipments
for l in range(len(busbar_dict)):
    for i in range(len(vol_Level_dict)):
        if busbar_dict[l]['EC_rdf'] == vol_Level_dict[i]['rdf']:
            busbar_dict[l]['vol'] = vol_Level_dict[i]['base_vol']
for l in range(len(ACLine_dict)):
    for i in range(len(vol_base_dict)):        
        if ACLine_dict[l]['vol_rdf'] == vol_base_dict[i]['rdf']:
            ACLine_dict[l]['vol'] = vol_base_dict[i]['nominal']

for l in range(len(CN_dict)):
    for i in range(len(vol_Level_dict)):        
        if CN_dict[l]['EC_rdf'] == vol_Level_dict[i]['rdf']:
            CN_dict[l]['vol'] = vol_Level_dict[i]['base_vol']       

for l in range(len(powertrend_dict)):
    for i in range(len(vol_base_dict)):        
        if powertrend_dict[l]['vol'] == vol_base_dict[i]['rdf']:
            powertrend_dict[l]['vol'] = vol_base_dict[i]['nominal']
                    
# Identify which region
for l in range(len(line_dict)):
    for i in range(len(subgeoregion_dict)):
        if line_dict[l]['region_rdf'] == subgeoregion_dict[i]['rdf']:
            line_dict[l]['region_name'] = subgeoregion_dict[i]['name']
for l in range(len(ACLine_dict)):
    for i in range(len(line_dict)):
        if ACLine_dict[l]['EC_rdf'] == line_dict[i]['rdf']:
            ACLine_dict[l]['region_name'] = line_dict[i]['name']            
#print(ACLine_dict)            

# find the connectivity node which is attached to a terminal

for j in range(len(CN_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CN_rdf'] == CN_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            CN_dict[j]['Terminal_list'] = temp
            CN_dict[j]['num_attachTerms'] = len(CN_dict[j]['Terminal_list'])
            
#print(CN_dict[j]['Terminal_list'])
#print(CN_dict[j]['num_attachTerms'])
# find the conducting equipment which is attached to a terminal
#busbar_dict
for j in range(len(busbar_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == busbar_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            busbar_dict[j]['Terminal_list'] = temp
            busbar_dict[j]['num_attachTerms'] = len(busbar_dict[j]['Terminal_list'])
#ACLine_dict

for j in range(len(ACLine_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == ACLine_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            ACLine_dict[j]['Terminal_list'] = temp
            ACLine_dict[j]['num_attachTerms'] = len(ACLine_dict[j]['Terminal_list'])           
#breaker_dict
for j in range(len(breaker_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == breaker_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            breaker_dict[j]['Terminal_list'] = temp
            breaker_dict[j]['num_attachTerms'] = len(breaker_dict[j]['Terminal_list'])              
            
#energyconsumer_dict
for j in range(len(energyconsumer_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == energyconsumer_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            energyconsumer_dict[j]['Terminal_list'] = temp
            energyconsumer_dict[j]['num_attachTerms'] = len(energyconsumer_dict[j]['Terminal_list'])              
            
            
#generatingunit_dict
for j in range(len(generatingunit_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == generatingunit_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            generatingunit_dict[j]['Terminal_list'] = temp
            generatingunit_dict[j]['num_attachTerms'] = len(generatingunit_dict[j]['Terminal_list'])             
            
#linearshuntcomp_dict
for j in range(len(linearshuntcomp_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == linearshuntcomp_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            linearshuntcomp_dict[j]['Terminal_list'] = temp
            linearshuntcomp_dict[j]['num_attachTerms'] = len(linearshuntcomp_dict[j]['Terminal_list'])             
            
#powertr_dict
for j in range(len(powertr_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == powertr_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            powertr_dict[j]['Terminal_list'] = temp
            powertr_dict[j]['num_attachTerms'] = len(powertr_dict[j]['Terminal_list'])              
            
#synmachine_dict     
for j in range(len(synmachine_dict)):
    temp=[]
    for i in range(len(terminal_dict)):
        if terminal_dict[i]['CE_rdf'] == synmachine_dict[j]['rdf']:
            temp.append(terminal_dict[i])
            synmachine_dict[j]['Terminal_list'] = temp
            synmachine_dict[j]['num_attachTerms'] = len(synmachine_dict[j]['Terminal_list'])              


#print(node_list[1][1]['rdf'])     
 
node_list.append(terminal_dict)
node_list.append(synmachine_dict)
#node_list.append(ratiotapchanger_dict)
#node_list.append(powertrend_dict)
node_list.append(powertr_dict)
node_list.append(linearshuntcomp_dict)
#node_list.append(line_dict)
node_list.append(generatingunit_dict)
node_list.append(energyconsumer_dict)
node_list.append(breaker_dict)
node_list.append(ACLine_dict)
node_list.append(CN_dict)
node_list.append(busbar_dict)


# find next node. This method is defined according the paper
def find_next_node(prev_node, curr_node):
    if curr_node['type'] == 'TE' and prev_node['type'] == 'CE':
        next_node_rdf = curr_node['CN_rdf']
        #print(next_node_rdf)
        for i in range(len(node_list)):
            for j in range(len(node_list[i])):
                if node_list[i][j]['rdf']== next_node_rdf:
                    #print(1)
                    #print(node_list[i][j])
                    return (node_list[i][j])
                                       
    elif curr_node['type'] == 'CN':
        #print(2)
        rand=random.choice(curr_node['Terminal_list'])
        #print(rand)
        return rand
            
    elif curr_node['type'] == 'CE':    
        #print(3)
        rand=random.choice(curr_node['Terminal_list'])
        #print(rand)
        return rand   
    else:
        next_node_rdf = curr_node['CE_rdf']
        #print(curr_node['name'])
        #print(next_node_rdf )
        for i in range(len(node_list)):
            for j in range(len(node_list[i])):
                
                if node_list[i][j]['rdf']== next_node_rdf:
                    #print(4)
                    #print(node_list[i][j])
                    return node_list[i][j]        
 
#k={'rdf': '#_93cec50e-e92e-4773-b408-e2419dad090d', 'name': 'BE_TR_BUS2', 'EC_rdf': '#_469df5f7-058f-4451-a998-57a48e8a56fe', 'Terminal_list': [{'rdf': '#_c3774d3f-f48c-4954-a0cf-b4572eb714fd', 'name': 'BE-TR2_1 - T1', 'seq': '1', 'CE_rdf': '#_a708c3bc-465d-4fe7-b6ef-6fa6408a62b0', 'CN_rdf': '#_93cec50e-e92e-4773-b408-e2419dad090d', 'traversal_flag': 0, 'Terminal_list': [], 'num_attachTerms': 0, 'type': 'TE'}, {'rdf': '#_345d8528-1a7e-4245-92d6-15db7a7e3c86', 'name': 'BE_Breaker_2 - T1', 'seq': '1', 'CE_rdf': '#_6b564930-b5e2-49d3-9d06-e1de28d6fd65', 'CN_rdf': '#_93cec50e-e92e-4773-b408-e2419dad090d', 'traversal_flag': 0, 'Terminal_list': [], 'num_attachTerms': 0, 'type': 'TE'}], 'num_attachTerms': 2, 'type': 'CN', 'vol': 0}           
# traversal algorithm initialization
CN_CE_stack =[]
CN_CE_type_stack = []
stack_list = []
type_stack_list = []

# find connectivity node which is attatched to busbar
CN_attached_to_busbar_dict = []
Ter_attached_to_busbar_dict = []
for i in range(len(busbar_dict)):
    for j in range(len(terminal_dict)):
        if busbar_dict[i]['rdf']==terminal_dict[j]['CE_rdf']:
            Ter_attached_to_busbar_dict.append(terminal_dict[j])
for i in range(len(Ter_attached_to_busbar_dict)):
    for j in range(len(CN_dict)):
        if Ter_attached_to_busbar_dict[i]['CN_rdf']==CN_dict[j]['rdf']:
            CN_attached_to_busbar_dict.append(CN_dict[j])

#print(CN_attached_to_busbar_list)

#list of CNs that are not attached to busbar
CN_not_attached_to_busbar_dict = []
j=len(CN_attached_to_busbar_dict)
#for i in range(len(CN_dict)):
#    for j in range(len(CN_attached_to_busbar_dict)):
#        if CN_dict[i]['rdf']!= CN_attached_to_busbar_dict[j]['rdf']:
#            CN_not_attached_to_busbar_dict.append(i)
for i in CN_dict:
    #print(i)
    if i not in CN_attached_to_busbar_dict:
        CN_not_attached_to_busbar_dict.append(i)
#print(CN_not_attached_to_busbar_list)


#print(k['Terminal_list'][1]['traversal_flag'])
# loop between CNs:
        
for i in range(len(CN_dict)):
    if CN_dict[i]['num_attachTerms'] > 0:
        #print(CN_dict[i]['num_attachTerms'])
        for j in range(len(CN_dict[i]['Terminal_list'])):
            if CN_dict[i]['Terminal_list'][j]['traversal_flag']==0:                
                CN_CE_stack = [CN_dict[i]]
                CN_CE_type_stack = [CN_dict[i]['type']] 
                curr_node=CN_dict[i]
                CN_dict[i]['num_attachTerms']-=1
                CN_dict[i]['Terminal_list'][j]['traversal_flag']=1
                prev_node = curr_node
                #print(prev_node)
                curr_node = CN_dict[i]['Terminal_list'][j]
                #print(curr_node['CN_rdf'])
                #print(prev_node['type'])
                #print(curr_node['type'])
                next_node = find_next_node(prev_node, curr_node)
                #print(next_node)
                CN_CE_stack.append(next_node)
                CN_CE_type_stack.append(next_node['type'])
                k = next_node
                if k['num_attachTerms'] > 1:
                    for l in range(len(k['Terminal_list'])):
                        if k['Terminal_list'][l]['traversal_flag']==0:
                            prev_node = k
                            curr_node = k['Terminal_list'][l]
                            next_node = find_next_node(prev_node, curr_node)
                            CN_CE_stack.append(next_node)
                            CN_CE_type_stack.append(next_node['type'])
                            #print(5)
            if CN_CE_stack not in stack_list:
                #print(6)
                stack_list.append(CN_CE_stack)
                type_stack_list.append(CN_CE_type_stack)
print('stack_list:')
#print(stack_list) 
#print(type_stack_list)                          


# pandapower
print('PandaPower:')
net = pp.create_empty_network()


# create bus
# conducting equipment__Bus
for i in range(len(busbar_dict)):
    busbar_dict[i]['bus']=pp.create_bus(net, name= busbar_dict[i]['name'], vn_kv = busbar_dict[i]['vol'], type='b')

for i in range(len(CN_not_attached_to_busbar_dict)):
    CN_not_attached_to_busbar_dict[i]['bus']=pp.create_bus(net, name= CN_not_attached_to_busbar_dict[i]['name'], vn_kv = CN_not_attached_to_busbar_dict[i]['vol'], type='n')    
#for i in busbar_section_list:
#    i.bus = pp.create_bus(net, name= i.name, vn_kv = i.basevoltage, type='b')

          
# connectivity nodes which are attached to busbar
for i in range(len(CN_attached_to_busbar_dict)):
    for j in range(len(CN_attached_to_busbar_dict[i]['Terminal_list'])):
        pre_node=CN_attached_to_busbar_dict[i]
        curr_node=CN_attached_to_busbar_dict[i]['Terminal_list'][j]
        next_node = find_next_node(prev_node, curr_node)
        if next_node['CE_type'] == 'bus':
            #print(next_node['bus'])
            CN_attached_to_busbar_dict[i]['bus'] = next_node['bus'] 
#print(len(busbar_dict))
#print(CN_attached_to_busbar_dict)  
#print(CN_dict) 
            
# create transformer
#identify the voltage and buses of the two sides of the transformer
for i in range(len(powertr_dict)):
    for j in range(len(powertrend_dict)):
        if powertr_dict[i]['rdf']==powertrend_dict[j]['transformer']:
            if powertrend_dict[j]['endNumber']=='1':
                powertr_dict[i]['hs']=powertrend_dict[j]['vol']
            elif powertrend_dict[j]['endNumber']=='2':
                powertr_dict[i]['ls']=powertrend_dict[j]['vol']
                
#for i in range(len(powertr_dict)):
#    for j in range(len(CN_attached_to_busbar_dict)):
#        if powertr_dict[i]['hs']==CN_attached_to_busbar_dict[j]['vol']:
#            powertr_dict[i]['hs_bus']=CN_attached_to_busbar_dict[j]['bus']
#        elif powertr_dict[i]['ls']==CN_attached_to_busbar_dict[j]['vol']:
#            powertr_dict[i]['ls_bus']=CN_attached_to_busbar_dict[j]['bus']   
            
for i in range(len(powertr_dict)):
    for j in range(len(powertr_dict[i]['Terminal_list'])):
        for k in range(len(CN_dict)) :
            for l in range(len(CN_dict[k]['Terminal_list'])):
                if powertr_dict[i]['Terminal_list'][j]==CN_dict[k]['Terminal_list'][l]:
                    if powertr_dict[i]['Terminal_list'][j]['seq']=='1':
                        powertr_dict[i]['hs_bus']=CN_dict[k]['bus']
                    if powertr_dict[i]['Terminal_list'][j]['seq']=='2':
                        powertr_dict[i]['ls_bus']=CN_dict[k]['bus']                    
                        
           
            
# create transformer
pp_transformer_list = []         
for i in range(len(powertr_dict)):
    pp_transformer_list.append(pp.create_transformer(net, powertr_dict[i]['hs_bus'], powertr_dict[i]['ls_bus'], name = powertr_dict[i]['name'], std_type = '160 MVA 380/110 kV'))
            
# create lines
pp_line_list = []
#identify the voltage and buses of the two sides of the lines
for i in range(len(ACLine_dict)):
    for j in range(len(terminal_dict)):
        if ACLine_dict[i]['rdf']==terminal_dict[j]['CE_rdf']:
            for k in range(len(CN_dict)):
                if terminal_dict[j]['CN_rdf'] == CN_dict[k]['rdf']:
                    if terminal_dict[j]['seq'] == '1':
                        ACLine_dict[i]['hs'] = CN_dict[k]['bus']
                    elif terminal_dict[j]['seq'] == '2':
                        ACLine_dict[i]['ls'] = CN_dict[k]['bus']
# print(pp_line_list)
for l in range(len(ACLine_dict)):
    pp_line_list.append(pp.create_line_from_parameters(net, ACLine_dict[l]['hs'], ACLine_dict[l]['ls'], length_km=ACLine_dict[l]['len'], r_ohm_per_km=ACLine_dict[l]['r'], x_ohm_per_km=ACLine_dict[l]['x'], c_nf_per_km=ACLine_dict[l]['bch'], g_us_per_km=ACLine_dict[l]['gch'],max_i_ka=0.4, type='ol', in_service=True,name=ACLine_dict[l]['name']))

# create switches
pp_breaker_list = []
#identify the voltage and buses of the two sides of the breakers
for i in range(len(breaker_dict)):
    for j in range(len(terminal_dict)):
        if breaker_dict[i]['rdf']==terminal_dict[j]['CE_rdf']:
            for k in range(len(CN_dict)):
                if terminal_dict[j]['CN_rdf'] == CN_dict[k]['rdf']:
                    if terminal_dict[j]['seq'] == '1':
                        breaker_dict[i]['hs'] = CN_dict[k]['bus']
                    elif terminal_dict[j]['seq'] == '2':
                        breaker_dict[i]['ls'] = CN_dict[k]['bus']
#get the status of each breaker
for i in range(len(breaker_dict)):
    for j in range(len(breaker_dict_SSH)):
        if breaker_dict[i]['rdf']== breaker_dict_SSH[j]['rdf']:
            breaker_dict[i]['op_status']=breaker_dict_SSH[j]['op_status']
# create breakers            
for i in range(len(breaker_dict)):
    if breaker_dict[i]['op_status']=='true':
        pp_breaker_list.append(pp.create_switch(net, breaker_dict[i]['hs'], breaker_dict[i]['ls'], et="b", type="CB", closed=False,name=breaker_dict[i]['name']))
    elif breaker_dict[i]['op_status']=='false':
        pp_breaker_list.append(pp.create_switch(net, breaker_dict[i]['hs'], breaker_dict[i]['ls'], et="b", type="CB", closed=True,name=breaker_dict[i]['name']))
        
# create generators
pp_generator_list = []
#identify the buses of the gen
for i in range(len(synmachine_dict)):
    for j in range(len(terminal_dict)):
        if synmachine_dict[i]['rdf']==terminal_dict[j]['CE_rdf']:
            for k in range(len(CN_dict)):
                if terminal_dict[j]['CN_rdf'] == CN_dict[k]['rdf']:
                    synmachine_dict[i]['bus']=CN_dict[k]['bus']
# create generators
for i in range(len(synmachine_dict)):
    pp_generator_list.append(pp.create_sgen_from_cosphi(net,synmachine_dict[i]['bus'],sn_mva=synmachine_dict[i]['S'], cos_phi=synmachine_dict[i]['PF'],mode='ind',name=synmachine_dict[i]['name']))
#print(generatingunit_dict)       
         
# create load
pp_load_list = []
#get P and Q from SSH
for i in range(len(energyconsumer_dict)):
    for j in range(len(energyconsumer_dict_SSH)):
        if energyconsumer_dict[i]['rdf']==energyconsumer_dict_SSH[j]['rdf']:
            energyconsumer_dict[i]['active_P']=energyconsumer_dict_SSH[j]['active_P']
            energyconsumer_dict[i]['reactive_Q']=energyconsumer_dict_SSH[j]['reactive_Q']
            
#identify the buses of the load
for i in range(len(energyconsumer_dict)):
    for j in range(len(terminal_dict)):
        if energyconsumer_dict[i]['rdf']==terminal_dict[j]['CE_rdf']:
            for k in range(len(CN_dict)):
                if terminal_dict[j]['CN_rdf'] == CN_dict[k]['rdf']:
                    energyconsumer_dict[i]['bus']=CN_dict[k]['bus']
for i in range(len(energyconsumer_dict)):
    pp_load_list.append(pp.create_load(net, energyconsumer_dict[i]['bus'], p_mw= energyconsumer_dict[i]['active_P'], q_mvar=energyconsumer_dict[i]['reactive_Q'], scaling=1, name =energyconsumer_dict[i]['name'])) 
                    
# create shunt
pp_shunt_list = []
#identify the buses of the shunt
for i in range(len(linearshuntcomp_dict)):
    for j in range(len(terminal_dict)):
        if linearshuntcomp_dict[i]['rdf']==terminal_dict[j]['CE_rdf']:
            for k in range(len(CN_dict)):
                if terminal_dict[j]['CN_rdf'] == CN_dict[k]['rdf']:
                    linearshuntcomp_dict[i]['bus']=CN_dict[k]['bus']
for i in range(len(linearshuntcomp_dict)):
    pp_load_list.append(pp.create_shunt(net, linearshuntcomp_dict[i]['bus'], p_mw= 0, q_mvar=0, name =linearshuntcomp_dict[i]['name'])) 
       
# print(pp_shunt_list)

net.bus
net.line 
net.trafo 
net.sgen
net.load  
net.shunt        
print(net)
print(net.bus)            
print(net.trafo) 
print(net.line) 
print(net.switch) 
print(net.sgen) 
print(net.load) 
print(net.shunt)
pp.plotting.simple_plot(net)


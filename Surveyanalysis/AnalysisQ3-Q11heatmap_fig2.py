# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:08:06 2026

@author: giber
"""


# import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import textwrap
import pandas as pd
from collections import Counter
############# now clean and classify the inputs 
import re


# Change the directory
path = 'G:\\My Drive\\progetti\\CEE\\COST_IMPROVE\\2026\SurveyAnalysis\\'
localpath = path
#path = 'G:\\My Drive\\progetti\\CEE\\COST_IMPROVE\\2025\survey\\'
os.chdir(path)
fname = os.listdir()
i=0
for F in fname:
    if (F.split('.')[-1] == 'xlsx'):
        print (i,F)
    i = i+1
#print (fname)
IF  = int(input('enter which file you want to analyze'))
# Load the Excel file
excel_file = fname[IF] # 'Content_Export_WG2_CA_IMPROVE_2024_resultsSruveyImprove_24Oct2024.xls'
print ('analysing this file: ', excel_file)

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file,header = 3)
numerodati  = int(input('HOW MANY ITEMNS YOU WANT TO ANALYSE????'))

df = df.iloc[:numerodati].copy()


columns = df.columns.tolist()

print ('%%%%%%%%%%%%%%%%% size of the data set:',len(df))
# Print the column names
for i in range(len(columns)): 
    print(i,columns[i])

# Access a specific column by name
column_name = '1. In which country do you primarily work?'
column_data = df[column_name]
column_name_stage = '2. What is your current academic position?'
column_data_stage = df[column_name_stage]

column_name_field = '3. What is your primary research target of interest?'
column_data_field = df[column_name_field]

column_name_research = '4. What type of research are you mainly involved in?'
column_data_research = df[column_name_research]

column_name_challenge = '4. Rank the following challenges in the implementation of 3Rs based on your experience (most challenge on top).'
column_data_challenge = df[column_name_challenge]

column_name_institution = '5. What type of institution do you work in?'
column_data_institution = df[column_name_institution]

column_name_role = '6. What is your role in your organization (also specify better in Q.7)?'
column_data_role = df[column_name_role]

column_name_familiar = '7. How familiar are you with the 3Rs principles?'
column_data_familiar = df[column_name_familiar]

column_name_methods = '8. What 3R methods are you primarily and currently involved in?'
column_data_methods = df[column_name_methods]

column_name_phase = '2. In which phase(s) of the implementation of 3R methods are you involved?"'
column_data_phase = df[column_name_phase]


# Print the data in the column
# Print the unique entries
#################   PART 2 ######################################
'''
'3. In your opinion, in which activities/phases are Universities involved?',
'4. In your opinion, in which activities/phases are Research Institutes involved?',
'5. In your opinion, in which activities/phases is Industry involved?',
'7. In your opinion, in which activities/phases are organizations for animal protection, welfare or research involved (e.g. 3Rs' centers)?',
'8. In your opinion, in which activities/phases are Health organizations involved (e.g. ECVMA, EMA, NIH...)?',
'9. In your opinion, in which activities/phases are funding organizations involved?',
'10. In your opinion, in which activities/phases are scientific journals involved?',
'10. In your opinion, in which activities/phases are legislative and regulatory bodies involved?',
'11. In your opinion, in which activities/phases are political bodies involved?',

'''

column_name_Q3  = '3. In your opinion, in which activities/phases are Universities involved?'
column_data_Q3  = df[column_name_Q3]
column_name_Q4  = '4. In your opinion, in which activities/phases are Research Institutes involved?'
column_data_Q4  = df[column_name_Q4]
column_name_Q5  = '5. In your opinion, in which activities/phases is Industry involved?'
column_data_Q5  = df[column_name_Q5]
column_name_Q7  = '6. In your opinion, in which activities/phases are organizations for animal protection, welfare or research involved (e.g. 3Rs\' centers)?'
column_data_Q7  = df[column_name_Q7]
column_name_Q8  = '7. In your opinion, in which activities/phases are Health organizations involved (e.g. ECVMA, EMA, NIH...)?'
column_data_Q8 = df[column_name_Q8]
column_name_Q9 = '8. In your opinion, in which activities/phases are funding organizations involved?'
column_data_Q9 = df[column_name_Q9]
column_name_Q10 = '9. In your opinion, in which activities/phases are scientific journals involved?'
column_data_Q10 = df[column_name_Q10]
column_name_Q10b = '10. In your opinion, in which activities/phases are legislative and regulatory bodies involved?'
column_data_Q10b = df[column_name_Q10b]
column_name_Q11 = '11. In your opinion, in which activities/phases are political bodies involved?'
column_data_Q11 = df[column_name_Q11]

column_name_rankQ4 ='4. Rank the following challenges in the implementation of 3Rs based on your experience (most challenge on top).'
column_data_rankQ4 = df[column_name_rankQ4]
column_name_rankQ2 = '2. In your opinion, which phase of the implementation curve in the figure (part 2) is the most constraining and why?'
column_data_rankQ2 = df[column_name_rankQ2]


#########################################  NOW THE COUNTRY
unique_entries = df[column_name].unique()
unique_entries_country = unique_entries  # store for later 
# Get unique labels and their counts unique_labels, 
unique_labels, counts = np.unique(column_data, return_counts=True) 
# Create a 2D matrix with labels and their counts
hist_matrix_survey = np.column_stack((unique_labels, counts)) 
# Print the histogram matrix 
print('Histogram Matrix Countries:') 
#print(hist_matrix_survey)

#print(unique_entries)
print ('total number of answers  for Countries: ',len(column_data))

country_counts = column_data.value_counts()

# Sort by count descending
sorted_countries = country_counts.sort_values(ascending=False)
#  NOW PLOT IN BARS 

x = np.arange(len(sorted_countries.index))  # numeric positions

plt.figure(figsize=(10,6))
plt.bar(x, sorted_countries.values, width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

plt.xticks(x, sorted_countries.index, rotation=45, ha='right', fontsize=12)

plt.xlabel('Country',fontsize = 16)
plt.ylabel('Frequency',fontsize = 16)
plt.title('Histogram of Countries Where Respondents Work (Sorted by Frequency)')
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y')
#print ('first 5 countries / total = ',np.round(100*sorted_countries.values[0:5].sum()/sorted_countries.values[:].sum(),1),' %')
print ('total number of countries represented:',len(sorted_countries))

# Show the plot
plt.show()

#########  analysis of part2 Array-questionsl. 

def GetSuperlist(col):
    superlist = []
#    VV = col.unique()
    VV = col
    for k in range(len(VV)):
        WW = VV[k].split(';')
        for h in range(len(WW)):
            #print (k,h,WW[h])
            superlist.append(WW[h])

    superlist = [s.lstrip() for s in superlist]
    return superlist

#########  analysis of part2 Array-questionsl. 

def GetSuperlist_stratif(col,col_research,string_research):
    ###  I need to single put the different institutions separated by ;
    ### or research
    superlist = []
    VV = col
    for k in range(len(VV)):
        WW = VV[k].split(';')
        for h in range(len(WW)):
            ### if ONE of the items in col_research == string_research.... 
            research_items = [x.strip() for x in col_research[k].split(';')]
#            if col_research[k] == string_research: 
            if string_research in research_items:
            #    print (k,h,WW[h],string_research)
                superlist.append(WW[h])

    superlist = [s.lstrip() for s in superlist]
    return superlist

###############################################################################
def plot_histogram_data(labels, values):
    titolix =  []
    #notepiepagina = []
    for k in range(len(labels)):
        sss = labels[k].split(" (")[0]
        wrapped = textwrap.fill(sss, width=20)
        titolix.append(wrapped)
        #notepiepagina.append(labels[k].split(" (")[1])

# Create a histogram of the entries in the specific column

    x = np.arange(len(labels))  # numeric positions

    plt.figure(figsize=(6,6))
    plt.bar(x, values, edgecolor='black')

    plt.xticks(x, titolix, rotation=45, ha='right', fontsize=12)
    plt.ylabel('Frequency', fontsize=18)
    plt.title('Histogram of Research Field')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()
    return titolix
###############################################################################

local_path = "G:\\My Drive\\progetti\\CEE\\COST_IMPROVE\\2026\\SurveyAnalysis\\"
###############################################################################

superlist = GetSuperlist(column_data_Q3)
print ('total number of answers in Q3:',len(superlist))

counter = Counter(superlist)
sorted_data = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
#print ('sorted Q3',sorted_data.items())
labels, values = zip(*sorted_data.items())

####   titolix = plot_histogram_data(labels, values)

sorted_data_Q3 = sorted_data

superlist = GetSuperlist(column_data_Q4)
counter = Counter(superlist)
sorted_data_Q4 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q4:',len(superlist))
#print ('sorted Q4',sorted_data_Q4.items())


superlist = GetSuperlist(column_data_Q5)
counter = Counter(superlist)
sorted_data_Q5 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q5:',len(superlist))
#print ('sorted Q5',sorted_data_Q5.items())

superlist = GetSuperlist(column_data_Q7)
counter = Counter(superlist)
sorted_data_Q7 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q7:',len(superlist))
#print ('sorted Q7',sorted_data_Q7.items())

superlist = GetSuperlist(column_data_Q8)
counter = Counter(superlist)
sorted_data_Q8 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q8:',len(superlist))

superlist = GetSuperlist(column_data_Q9)
counter = Counter(superlist)
sorted_data_Q9 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q9:',len(superlist))

superlist = GetSuperlist(column_data_Q10)
counter = Counter(superlist)
sorted_data_Q10 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10:',len(superlist))

superlist = GetSuperlist(column_data_Q10b)
counter = Counter(superlist)
sorted_data_Q10b = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10b:',len(superlist))

superlist = GetSuperlist(column_data_Q11)
counter = Counter(superlist)
sorted_data_Q11 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q11:',len(superlist))

########## do it on all the quyestions opf part2
########### builkd a matrix. 
SuperMatrix = np.zeros((6,9),dtype='int')

SuperMatrix[0,0] = sorted_data_Q3['Acceptance']
SuperMatrix[0,1] = sorted_data_Q4['Acceptance'] 
SuperMatrix[0,2] = sorted_data_Q5['Acceptance'] 
SuperMatrix[0,3] = sorted_data_Q7['Acceptance'] 
SuperMatrix[0,4] = sorted_data_Q8['Acceptance'] 
SuperMatrix[0,5] = sorted_data_Q9['Acceptance'] 
SuperMatrix[0,6] = sorted_data_Q10['Acceptance'] 
SuperMatrix[0,7] = sorted_data_Q10b['Acceptance'] 
SuperMatrix[0,8] = sorted_data_Q11['Acceptance'] 

SuperMatrix[1,0] = sorted_data_Q3['Effective use by end users']
SuperMatrix[1,1] = sorted_data_Q4['Effective use by end users'] 
SuperMatrix[1,2] = sorted_data_Q5['Effective use by end users'] 
SuperMatrix[1,3] = sorted_data_Q7['Effective use by end users'] 
SuperMatrix[1,4] = sorted_data_Q8['Effective use by end users'] 
SuperMatrix[1,5] = sorted_data_Q9['Effective use by end users'] 
SuperMatrix[1,6] = sorted_data_Q10['Effective use by end users'] 
SuperMatrix[1,7] = sorted_data_Q10b['Effective use by end users'] 
SuperMatrix[1,8] = sorted_data_Q11['Effective use by end users'] 

SuperMatrix[2,0] = sorted_data_Q3['Independent review']
SuperMatrix[2,1] = sorted_data_Q4['Independent review'] 
SuperMatrix[2,2] = sorted_data_Q5['Independent review'] 
SuperMatrix[2,3] = sorted_data_Q7['Independent review'] 
SuperMatrix[2,4] = sorted_data_Q8['Independent review'] 
SuperMatrix[2,5] = sorted_data_Q9['Independent review'] 
SuperMatrix[2,6] = sorted_data_Q10['Independent review'] 
SuperMatrix[2,7] = sorted_data_Q10b['Independent review'] 
SuperMatrix[2,8] = sorted_data_Q11['Independent review'] 

SuperMatrix[3,0] = sorted_data_Q3['Problem formulation, context of use']
SuperMatrix[3,1] = sorted_data_Q4['Problem formulation, context of use'] 
SuperMatrix[3,2] = sorted_data_Q5['Problem formulation, context of use'] 
SuperMatrix[3,3] = sorted_data_Q7['Problem formulation/context of use'] 
SuperMatrix[3,4] = sorted_data_Q8['Problem formulation, context of use'] 
SuperMatrix[3,5] = sorted_data_Q9['Problem formulation, context of use'] 
SuperMatrix[3,6] = sorted_data_Q10['Problem formulation, context of use'] 
SuperMatrix[3,7] = sorted_data_Q10b['Problem formulation, context of use'] 
SuperMatrix[3,8] = sorted_data_Q11['Problem formulation, context of use'] 

SuperMatrix[4,0] = sorted_data_Q3['Research and development']
SuperMatrix[4,1] = sorted_data_Q4['Research and development'] 
SuperMatrix[4,2] = sorted_data_Q5['Research and development'] 
SuperMatrix[4,3] = sorted_data_Q7['Research and development'] 
SuperMatrix[4,4] = sorted_data_Q8['Research and development'] 
SuperMatrix[4,5] = sorted_data_Q9['Research and development'] 
SuperMatrix[4,6] = sorted_data_Q10['Research and development'] 
SuperMatrix[4,7] = sorted_data_Q10b['Research and development'] 
SuperMatrix[4,8] = sorted_data_Q11['Research and development'] 

SuperMatrix[5,0] = sorted_data_Q3['Scientific validation']
SuperMatrix[5,1] = sorted_data_Q4['Scientific validation'] 
SuperMatrix[5,2] = sorted_data_Q5['Scientific validation'] 
SuperMatrix[5,3] = sorted_data_Q7['Scientific validation'] 
SuperMatrix[5,4] = sorted_data_Q8['Scientific validation'] 
SuperMatrix[5,5] = sorted_data_Q9['Scientific validation'] 
SuperMatrix[5,6] = sorted_data_Q10['Scientific validation'] 
SuperMatrix[5,7] = sorted_data_Q10b['Scientific validation'] 
SuperMatrix[5,8] = sorted_data_Q11['Scientific validation'] 




titoliy =  []

titoliy.append('Acceptance')
titoliy.append('Effective use ')
titoliy.append('Independent review')
titoliy.append('Problem formulation ')
titoliy.append('Research and development')
titoliy.append('Scientific validation')

titolix = []
titolix.append('Universities') 
titolix.append('Research Institutes')  
titolix.append('Industry ') 
titolix.append('Organizations animal protect.') 
titolix.append('Health organizations')  
titolix.append('funding organizations')  
titolix.append('scientific journals')  
titolix.append('legislative, regulat. bodies')  
titolix.append('political bodies')  

'''
# Create a histogram of the entries in the specific column
######## FIRST HEATMAP AS IT IS
y = np.arange(len(titoliy))  # numeric positions
x = np.arange(len(titolix))  # numeric positions

plt.figure(figsize=(10,6))

plt.imshow(SuperMatrix,cmap='magma')
plt.colorbar()

plt.yticks(y, titoliy, rotation=0, ha='right', fontsize=14)
plt.xticks(x, titolix, rotation=45, ha='right', fontsize=14)
plt.title('In which activities/phases are these entities involved?',fontsize=16,y=1.05)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
'''
#################################################################
##### now try an ordered version of the heatmap in terms of the Fig1. of the paper
#################################################################
new_order = [3, 4, 5, 2, 0, 1]

SuperMatrix_reordered = SuperMatrix[new_order, :]
titoliy_reordered = [titoliy[i] for i in new_order]
y = np.arange(len(titoliy_reordered))
x = np.arange(len(titolix))


figSM_reord, ax_reord = plt.subplots(figsize=(10,6))

im_reord = ax_reord.imshow(SuperMatrix_reordered, cmap='magma')

# Create a new axis above the heatmap for the colorbar
cbar_ax = figSM_reord.add_axes([0.45, 0.69, 0.29, 0.03])

# Horizontal colorbar
cbar = figSM_reord.colorbar(im_reord,
                            cax=cbar_ax,
                            orientation='horizontal',
                            pad=-1.2,        # distance from the plot
                            fraction=0.05)   # thickness of the bar

# Move tick labels ABOVE the bar
cbar.ax.xaxis.set_ticks_position('top')
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=12)   # increase tick font size

ax_reord.set_yticks(y, titoliy_reordered, rotation=0, ha='right', fontsize=12)
ax_reord.set_xticks(x, titolix, rotation=45, ha='right', fontsize=12)
ax_reord.set_title('In which activities/phases are these entities involved (Fig1)?', 
                   fontsize=10, y=1.35)
#plt.grid(axis='y')

plt.tight_layout()
plt.show()

figSM_reord.savefig(localpath+'Fig8_heatmap_orderedFig1.png',
                    bbox_inches='tight',
                    pad_inches=0.2)
'''
##### now try an ordered version of the heatmap in terms of higher Countings 
figSM,axSM = plt.subplots(figsize=(10,6))
row_order = np.argsort(SuperMatrix.mean(axis=1))
col_order = np.argsort(SuperMatrix.mean(axis=0))
SM_sorted = SuperMatrix[row_order][:, col_order]
rows_sorted = [titoliy[i] for i in row_order]
cols_sorted = [titolix[j] for j in col_order]

iSM = axSM.imshow(SM_sorted,cmap='magma')

plt.colorbar(iSM, ax=axSM)

axSM.set_yticks(y, rows_sorted, rotation=0, ha='right', fontsize=14)
axSM.set_xticks(x, cols_sorted, rotation=45, ha='right', fontsize=14)
figSM.suptitle('In which activities/phases are these entities involved?',fontsize=16,y=1.05)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
figSM.savefig('Fig7_heatmap_ordered.png')
'''

################ now write it out 
print ('I am writing the comatrix in comatrixFig7.csv',path)
dfSuper = pd.DataFrame(SuperMatrix,
                       index  = titoliy,
                       columns = titolix)
dfSuper.to_csv("comatrixFig7.csv")

#### reorder
desired_order = [
    "Problem formulation",
    "R&D",
    "Scientific validation",
    "Independent review",
    "Acceptance",
    "Effective use by users"
]


########################################################################
#################   CLustered heatmap
#########################################################################
ClusterMatrix = np.zeros((6,5),dtype='int')

ClusterMatrix[0,0] = sorted_data_Q3['Acceptance']  +  sorted_data_Q4['Acceptance'] 
ClusterMatrix[0,1] = sorted_data_Q5['Acceptance']  +  sorted_data_Q8['Acceptance'] 
ClusterMatrix[0,2] = sorted_data_Q10['Acceptance'] + sorted_data_Q10b['Acceptance'] 
ClusterMatrix[0,3] = sorted_data_Q9['Acceptance']  + sorted_data_Q11['Acceptance'] 
ClusterMatrix[0,4] = sorted_data_Q7['Acceptance'] 

ClusterMatrix[1,0] = sorted_data_Q3['Effective use by end users']  +  sorted_data_Q4['Effective use by end users'] 
ClusterMatrix[1,1] = sorted_data_Q5['Effective use by end users']  +  sorted_data_Q8['Effective use by end users'] 
ClusterMatrix[1,2] = sorted_data_Q10['Effective use by end users'] + sorted_data_Q10b['Effective use by end users'] 
ClusterMatrix[1,3] = sorted_data_Q9['Effective use by end users']  + sorted_data_Q11['Effective use by end users'] 
ClusterMatrix[1,4] = sorted_data_Q7['Effective use by end users'] 

ClusterMatrix[2,0] = sorted_data_Q3['Independent review']  +  sorted_data_Q4['Independent review'] 
ClusterMatrix[2,1] = sorted_data_Q5['Independent review']  +  sorted_data_Q8['Independent review'] 
ClusterMatrix[2,2] = sorted_data_Q10['Independent review'] + sorted_data_Q10b['Independent review'] 
ClusterMatrix[2,3] = sorted_data_Q9['Independent review']  + sorted_data_Q11['Independent review'] 
ClusterMatrix[2,4] = sorted_data_Q7['Independent review'] 

ClusterMatrix[3,0] = sorted_data_Q3['Problem formulation, context of use']  +  sorted_data_Q4['Problem formulation, context of use'] 
ClusterMatrix[3,1] = sorted_data_Q5['Problem formulation, context of use']  +  sorted_data_Q8['Problem formulation, context of use'] 
ClusterMatrix[3,2] = sorted_data_Q10['Problem formulation, context of use'] + sorted_data_Q10b['Problem formulation, context of use'] 
ClusterMatrix[3,3] = sorted_data_Q9['Problem formulation, context of use']  + sorted_data_Q11['Problem formulation, context of use'] 
ClusterMatrix[3,4] = sorted_data_Q7['Problem formulation/context of use'] 

ClusterMatrix[4,0] = sorted_data_Q3['Research and development']  +  sorted_data_Q4['Research and development'] 
ClusterMatrix[4,1] = sorted_data_Q5['Research and development']  +  sorted_data_Q8['Research and development'] 
ClusterMatrix[4,2] = sorted_data_Q10['Research and development'] + sorted_data_Q10b['Research and development'] 
ClusterMatrix[4,3] = sorted_data_Q9['Research and development']  + sorted_data_Q11['Research and development'] 
ClusterMatrix[4,4] = sorted_data_Q7['Research and development'] 

ClusterMatrix[5,0] = sorted_data_Q3['Scientific validation']  +  sorted_data_Q4['Scientific validation'] 
ClusterMatrix[5,1] = sorted_data_Q5['Scientific validation']  +  sorted_data_Q8['Scientific validation'] 
ClusterMatrix[5,2] = sorted_data_Q10['Scientific validation'] + sorted_data_Q10b['Scientific validation'] 
ClusterMatrix[5,3] = sorted_data_Q9['Scientific validation']  + sorted_data_Q11['Scientific validation'] 
ClusterMatrix[5,4] = sorted_data_Q7['Scientific validation'] 

titoliy =  []

titoliy.append('Acceptance')
titoliy.append('Effective use by end users')
titoliy.append('Independent review')
titoliy.append('Problem formulation ')
titoliy.append('Research and development')
titoliy.append('Scientific validation')


titolix = []
titolix.append('Knowledge prod.') 
titolix.append('Implementers')  
titolix.append('Gatekeepers ') 
titolix.append('Supporters') 
titolix.append('Advocates')  

################### reorder according to Fig1
new_order = [3, 4, 5, 2, 0, 1]

ClusterMatrix_reordered = ClusterMatrix[new_order, :]
titoliy_reordered = [titoliy[i] for i in new_order]
y = np.arange(len(titoliy_reordered))
x = np.arange(len(titolix))


figSMc_re,axSMc_re = plt.subplots(1,figsize=(10,6))

im_re = axSMc_re.imshow(ClusterMatrix_reordered,cmap='magma')

# Create a new axis above the heatmap for the colorbar
cbar_ax = figSMc_re.add_axes([0.435, 0.75, 0.2, 0.03])

# Horizontal colorbar
cbar = figSMc_re.colorbar(im_re,
                            cax=cbar_ax,
                            orientation='horizontal',
                            pad=-1.2,        # distance from the plot
                            fraction=0.05)   # thickness of the bar

# Move tick labels ABOVE the bar
cbar.ax.xaxis.set_ticks_position('top')
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=14)   # increase tick font size


axSMc_re.set_yticks(y, titoliy_reordered, rotation=0, ha='right', fontsize=14)
axSMc_re.set_xticks(x, titolix, rotation=45, ha='right', fontsize=14)
axSMc_re.set_title('In which activities/phases are these subgroups involved?',fontsize=10,y=1.3)

plt.tight_layout()
plt.show()
figSMc_re.savefig(localpath+'Fig8_clustered_heatmap_orderedFig1.png')



################################################################
################################################################
################################################################
##### stratification on different RESEARCH FIELDS
################################################################
################################################################
################################################################

print ('research fields are:')
print (column_data_research.unique())

strat_string  = column_data_research.unique()[3]
strat_string1 = column_data_research.unique()[4]
print ('stratifying to ',strat_string)
print ('stratifying to ',strat_string1)

superlist0 =  GetSuperlist_stratif(column_data_Q3,column_data_research,strat_string)
superlist1 =  GetSuperlist_stratif(column_data_Q3,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
print ('total number of answers in Q3:',len(superlist))
counter = Counter(superlist)
sorted_data = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
labels, values = zip(*sorted_data.items())
sorted_data_Q3 = sorted_data

superlist0 = GetSuperlist_stratif(column_data_Q4,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q4,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q4 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q4:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q5,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q5,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q5 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q5:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q7,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q7,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q7 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q7:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q8,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q8,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q8 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q8:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q9,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q9,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q9 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q9:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q10,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q10,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q10 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q10b,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q10b,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q10b = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10b:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q11,column_data_research,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q11,column_data_research,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q11 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q11:',len(superlist))

########## do it on all the quyestions opf part2
########### builkd a matrix. 
SuperMatrix = np.zeros((6,9),dtype='int')

SuperMatrix[0,0] = sorted_data_Q3['Acceptance']
SuperMatrix[0,1] = sorted_data_Q4['Acceptance'] 
SuperMatrix[0,2] = sorted_data_Q5['Acceptance'] 
SuperMatrix[0,3] = sorted_data_Q7['Acceptance'] 
SuperMatrix[0,4] = sorted_data_Q8['Acceptance'] 
SuperMatrix[0,5] = sorted_data_Q9['Acceptance'] 
SuperMatrix[0,6] = sorted_data_Q10['Acceptance'] 
SuperMatrix[0,7] = sorted_data_Q10b['Acceptance'] 
SuperMatrix[0,8] = sorted_data_Q11['Acceptance'] 

SuperMatrix[1,0] = sorted_data_Q3['Effective use by end users']
SuperMatrix[1,1] = sorted_data_Q4['Effective use by end users'] 
SuperMatrix[1,2] = sorted_data_Q5['Effective use by end users'] 
SuperMatrix[1,3] = sorted_data_Q7['Effective use by end users'] 
SuperMatrix[1,4] = sorted_data_Q8['Effective use by end users'] 
SuperMatrix[1,5] = sorted_data_Q9['Effective use by end users'] 
SuperMatrix[1,6] = sorted_data_Q10['Effective use by end users'] 
SuperMatrix[1,7] = sorted_data_Q10b['Effective use by end users'] 
SuperMatrix[1,8] = sorted_data_Q11['Effective use by end users'] 

SuperMatrix[2,0] = sorted_data_Q3['Independent review']
SuperMatrix[2,1] = sorted_data_Q4['Independent review'] 
SuperMatrix[2,2] = sorted_data_Q5['Independent review'] 
SuperMatrix[2,3] = sorted_data_Q7['Independent review'] 
SuperMatrix[2,4] = sorted_data_Q8['Independent review'] 
SuperMatrix[2,5] = sorted_data_Q9['Independent review'] 
SuperMatrix[2,6] = sorted_data_Q10['Independent review'] 
SuperMatrix[2,7] = sorted_data_Q10b['Independent review'] 
SuperMatrix[2,8] = sorted_data_Q11['Independent review'] 

SuperMatrix[3,0] = sorted_data_Q3['Problem formulation, context of use']
SuperMatrix[3,1] = sorted_data_Q4['Problem formulation, context of use'] 
SuperMatrix[3,2] = sorted_data_Q5['Problem formulation, context of use'] 
SuperMatrix[3,3] = sorted_data_Q7['Problem formulation/context of use'] 
SuperMatrix[3,4] = sorted_data_Q8['Problem formulation, context of use'] 
SuperMatrix[3,5] = sorted_data_Q9['Problem formulation, context of use'] 
SuperMatrix[3,6] = sorted_data_Q10['Problem formulation, context of use'] 
SuperMatrix[3,7] = sorted_data_Q10b['Problem formulation, context of use'] 
SuperMatrix[3,8] = sorted_data_Q11['Problem formulation, context of use'] 

SuperMatrix[4,0] = sorted_data_Q3['Research and development']
SuperMatrix[4,1] = sorted_data_Q4['Research and development'] 
SuperMatrix[4,2] = sorted_data_Q5['Research and development'] 
SuperMatrix[4,3] = sorted_data_Q7['Research and development'] 
SuperMatrix[4,4] = sorted_data_Q8['Research and development'] 
SuperMatrix[4,5] = sorted_data_Q9['Research and development'] 
SuperMatrix[4,6] = sorted_data_Q10['Research and development'] 
SuperMatrix[4,7] = sorted_data_Q10b['Research and development'] 
SuperMatrix[4,8] = sorted_data_Q11['Research and development'] 

SuperMatrix[5,0] = sorted_data_Q3['Scientific validation']
SuperMatrix[5,1] = sorted_data_Q4['Scientific validation'] 
SuperMatrix[5,2] = sorted_data_Q5['Scientific validation'] 
SuperMatrix[5,3] = sorted_data_Q7['Scientific validation'] 
SuperMatrix[5,4] = sorted_data_Q8['Scientific validation'] 
SuperMatrix[5,5] = sorted_data_Q9['Scientific validation'] 
SuperMatrix[5,6] = sorted_data_Q10['Scientific validation'] 
SuperMatrix[5,7] = sorted_data_Q10b['Scientific validation'] 
SuperMatrix[5,8] = sorted_data_Q11['Scientific validation'] 

titoliy =  []

titoliy.append('Acceptance')
titoliy.append('Effective use ')
titoliy.append('Independent review')
titoliy.append('Problem formulation ')
titoliy.append('Research and development')
titoliy.append('Scientific validation')

titolix = []
titolix.append('Universities') 
titolix.append('Research Institutes')  
titolix.append('Industry ') 
titolix.append('Organizations animal protect.') 
titolix.append('Health organizations')  
titolix.append('funding organizations')  
titolix.append('scientific journals')  
titolix.append('legislative, regulat. bodies')  
titolix.append('political bodies')  
#################################################################
##### now try an ordered version of the heatmap in terms of the Fig1. of the paper
#################################################################
new_order = [3, 4, 5, 2, 0, 1]

SuperMatrix_reordered = SuperMatrix[new_order, :]
titoliy_reordered = [titoliy[i] for i in new_order]
y = np.arange(len(titoliy_reordered))
x = np.arange(len(titolix))


figSM_reord, ax_reord = plt.subplots(figsize=(10,6))

im_reord = ax_reord.imshow(SuperMatrix_reordered, cmap='magma')

# Create a new axis above the heatmap for the colorbar
cbar_ax = figSM_reord.add_axes([0.45, 0.69, 0.29, 0.03])

# Horizontal colorbar
cbar = figSM_reord.colorbar(im_reord,
                            cax=cbar_ax,
                            orientation='horizontal',
                            pad=-1.2,        # distance from the plot
                            fraction=0.05)   # thickness of the bar

# Move tick labels ABOVE the bar
cbar.ax.xaxis.set_ticks_position('top')
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=12)   # increase tick font size

ax_reord.set_yticks(y, titoliy_reordered, rotation=0, ha='right', fontsize=12)
ax_reord.set_xticks(x, titolix, rotation=45, ha='right', fontsize=12)
ax_reord.set_title('in which activ. involved? strafied by '+ strat_string.split('(')[0] + strat_string1.split('(')[0],
                  fontsize=10, y=1.35)
#plt.grid(axis='y')

plt.tight_layout()
plt.show()

figSM_reord.savefig(localpath+'Fig8_heatmap_Strat_orderedFig1.png',
                    bbox_inches='tight',
                    pad_inches=0.2)



################################################################
################################################################
################################################################
##### stratification on different INSTITUTIONS 
################################################################
################################################################
def Get_RealUniques(data):
#### we take put the fact that there maybe people working in 
## different institutions, spearated by semicolumn
    k = 0
    List_out = []
    for A in column_data_institution.unique():
        B = A.split(';') ## the whole set
        for b in B:
            b = b.strip()
            #print(k, b)
            List_out.append(b)
            k = k + 1

# make unique, preserving order
    Lout = list(dict.fromkeys(List_out))
    return Lout    
    
################################################################

print ('what type of institution do you work in :')
#print (column_data_institution.unique())

print('NEW UNIQUE')
Lista_Instit_unique = Get_RealUniques(column_data_institution.unique())
print('LOUT\n',Lista_Instit_unique)

#strat_string  = column_data_institution.unique()[0]
strat_string  = Lista_Instit_unique[4]
strat_string1 = "" 
print ('stratifying to ',strat_string)
print ('stratifying to ',strat_string1)

superlist0 =  GetSuperlist_stratif(column_data_Q3,column_data_institution,strat_string)
superlist1 =  GetSuperlist_stratif(column_data_Q3,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
print ('total number of answers in Q3:',len(superlist),len(superlist0),len(superlist1))
counter = Counter(superlist)
sorted_data = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
#labels, values = zip(*sorted_data.items())
sorted_data_Q3 = sorted_data

superlist0 = GetSuperlist_stratif(column_data_Q4,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q4,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q4 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q4:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q5,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q5,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q5 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q5:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q7,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q7,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q7 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q7:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q8,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q8,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q8 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q8:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q9,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q9,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q9 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q9:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q10,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q10,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q10 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q10b,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q10b,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q10b = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10b:',len(superlist))

superlist0 = GetSuperlist_stratif(column_data_Q11,column_data_institution,strat_string)
superlist1 = GetSuperlist_stratif(column_data_Q11,column_data_institution,strat_string1)
superlist  =  superlist0 + superlist1 
counter = Counter(superlist)
sorted_data_Q11 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q11:',len(superlist))

########## do it on all the quyestions opf part2
########### builkd a matrix. 

SuperMatrix = np.zeros((6,9),dtype='int')

SuperMatrix[0,0] = sorted_data_Q3.get('Acceptance', 0)
SuperMatrix[0,1] = sorted_data_Q4.get('Acceptance', 0)
SuperMatrix[0,2] = sorted_data_Q5.get('Acceptance', 0)
SuperMatrix[0,3] = sorted_data_Q7.get('Acceptance', 0)
SuperMatrix[0,4] = sorted_data_Q8.get('Acceptance', 0) 
SuperMatrix[0,5] = sorted_data_Q9.get('Acceptance', 0) 
SuperMatrix[0,6] = sorted_data_Q10.get('Acceptance', 0) 
SuperMatrix[0,7] = sorted_data_Q10b.get('Acceptance', 0) 
SuperMatrix[0,8] = sorted_data_Q11.get('Acceptance', 0) 

SuperMatrix[1,0] = sorted_data_Q3.get('Effective use by end users', 0)
SuperMatrix[1,1] = sorted_data_Q4.get('Effective use by end users', 0)
SuperMatrix[1,2] = sorted_data_Q5.get('Effective use by end users', 0)
SuperMatrix[1,3] = sorted_data_Q7.get('Effective use by end users', 0)
SuperMatrix[1,4] = sorted_data_Q8.get('Effective use by end users', 0)
SuperMatrix[1,5] = sorted_data_Q9.get('Effective use by end users', 0)
SuperMatrix[1,6] = sorted_data_Q10.get('Effective use by end users', 0)
SuperMatrix[1,7] = sorted_data_Q10b.get('Effective use by end users', 0)
SuperMatrix[1,8] = sorted_data_Q11.get('Effective use by end users', 0)

SuperMatrix[2,0] = sorted_data_Q3.get('Independent review', 0)
SuperMatrix[2,1] = sorted_data_Q4.get('Independent review', 0)
SuperMatrix[2,2] = sorted_data_Q5.get('Independent review', 0)
SuperMatrix[2,3] = sorted_data_Q7.get('Independent review', 0)
SuperMatrix[2,4] = sorted_data_Q8.get('Independent review', 0)
SuperMatrix[2,5] = sorted_data_Q9.get('Independent review', 0)
SuperMatrix[2,6] = sorted_data_Q10.get('Independent review', 0)
SuperMatrix[2,7] = sorted_data_Q10b.get('Independent review', 0)
SuperMatrix[2,8] = sorted_data_Q11.get('Independent review', 0) 

SuperMatrix[3,0] = sorted_data_Q3.get('Problem formulation, context of use', 0)
SuperMatrix[3,1] = sorted_data_Q4.get('Problem formulation, context of use', 0)
SuperMatrix[3,2] = sorted_data_Q5.get('Problem formulation, context of use', 0)
SuperMatrix[3,3] = sorted_data_Q7.get('Problem formulation, context of use', 0)
SuperMatrix[3,4] = sorted_data_Q8.get('Problem formulation, context of use', 0) 
SuperMatrix[3,5] = sorted_data_Q9.get('Problem formulation, context of use', 0) 
SuperMatrix[3,6] = sorted_data_Q10.get('Problem formulation, context of use', 0)
SuperMatrix[3,7] = sorted_data_Q10b.get('Problem formulation, context of use', 0) 
SuperMatrix[3,8] = sorted_data_Q11.get('Problem formulation, context of use', 0)

SuperMatrix[4,0] = sorted_data_Q3.get('Research and development', 0) 
SuperMatrix[4,1] = sorted_data_Q4.get('Research and development', 0)  
SuperMatrix[4,2] = sorted_data_Q5.get('Research and development', 0)  
SuperMatrix[4,3] = sorted_data_Q7.get('Research and development', 0) 
SuperMatrix[4,4] = sorted_data_Q8.get('Research and development', 0) 
SuperMatrix[4,5] = sorted_data_Q9.get('Research and development', 0) 
SuperMatrix[4,6] = sorted_data_Q10.get('Research and development', 0) 
SuperMatrix[4,7] = sorted_data_Q10b.get('Research and development', 0) 
SuperMatrix[4,8] = sorted_data_Q11.get('Research and development', 0) 

SuperMatrix[5,0] = sorted_data_Q3.get('Scientific validation', 0) 
SuperMatrix[5,1] = sorted_data_Q4.get('Scientific validation', 0) 
SuperMatrix[5,2] = sorted_data_Q5.get('Scientific validation', 0) 
SuperMatrix[5,3] = sorted_data_Q7.get('Scientific validation', 0)
SuperMatrix[5,4] = sorted_data_Q8.get('Scientific validation', 0)
SuperMatrix[5,5] = sorted_data_Q9.get('Scientific validation', 0)
SuperMatrix[5,6] = sorted_data_Q10.get('Scientific validation', 0)
SuperMatrix[5,7] = sorted_data_Q10b.get('Scientific validation', 0)
SuperMatrix[5,8] = sorted_data_Q11.get('Scientific validation', 0)

titoliy =  []

titoliy.append('Acceptance')
titoliy.append('Effective use ')
titoliy.append('Independent review')
titoliy.append('Problem formulation ')
titoliy.append('Research and development')
titoliy.append('Scientific validation')

titolix = []
titolix.append('Universities') 
titolix.append('Research Institutes')  
titolix.append('Industry ') 
titolix.append('Organizations animal protect.') 
titolix.append('Health organizations')  
titolix.append('funding organizations')  
titolix.append('scientific journals')  
titolix.append('legislative, regulat. bodies')  
titolix.append('political bodies')  
#################################################################
##### now try an ordered version of the heatmap in terms of the Fig1. of the paper
#################################################################
new_order = [3, 4, 5, 2, 0, 1]

SuperMatrix_reordered = SuperMatrix[new_order, :]
titoliy_reordered = [titoliy[i] for i in new_order]
y = np.arange(len(titoliy_reordered))
x = np.arange(len(titolix))


figSM_reord, ax_reord = plt.subplots(figsize=(10,6))

im_reord = ax_reord.imshow(SuperMatrix_reordered, cmap='magma')

# Create a new axis above the heatmap for the colorbar
cbar_ax = figSM_reord.add_axes([0.45, 0.69, 0.29, 0.03])

# Horizontal colorbar
cbar = figSM_reord.colorbar(im_reord,
                            cax=cbar_ax,
                            orientation='horizontal',
                            pad=-1.2,        # distance from the plot
                            fraction=0.05)   # thickness of the bar

# Move tick labels ABOVE the bar
cbar.ax.xaxis.set_ticks_position('top')
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=12)   # increase tick font size

ax_reord.set_yticks(y, titoliy_reordered, rotation=0, ha='right', fontsize=12)
ax_reord.set_xticks(x, titolix, rotation=45, ha='right', fontsize=12)
ax_reord.set_title('I,in which activ. involved? strafied by '+strat_string.split('(')[0] + strat_string1.split('(')[0],
                  fontsize=10, y=1.35)
#plt.grid(axis='y')

plt.tight_layout()
plt.show()


figSM_reord.savefig(localpath+'Fig8_heatmap_Strat_Instit_orderedFig1.png',
                    bbox_inches='tight',
                    pad_inches=0.2)

print (SuperMatrix_reordered.sum())
print (SuperMatrix_reordered)
conteggiTOT = SuperMatrix_reordered.sum()
print ('conteggiTot:',conteggiTOT)
sample_a = SuperMatrix_reordered[4:6,7:9].ravel()
print (titolix[7:9],titoliy_reordered[4:6],sample_a.sum()/conteggiTOT,sample_a.std()/conteggiTOT)

print (sample_a)

from scipy import stats

# Example data: two independent samples
total_a = 2728
sample_a_4_6_0_2 = np.array([38, 41 ,43 ,50])/ total_a
sample_a_0_2_0_2 = np.array([77, 63, 97, 99]) / total_a

total_b = 61
sample_b_4_6_0_2 = np.array([0, 2, 0, 1]) / total_b
sample_b_0_2_0_2 = np.array([2, 1, 2, 2]) /total_b 

total_c = 243
sample_c_4_6_0_2 = np.array([3, 3, 4, 4]) / total_c
sample_c_0_2_0_2 = np.array([8, 9, 9, 8]) / total_c

try:
    # Independent two-sample t-test (equal variance assumed by default)
    t_stat, p_value = stats.ttest_ind(sample_a_0_2_0_2, sample_c_0_2_0_2, equal_var=True)

    print("Independent Two-Sample t-test:")
    print(f"t-statistic = {t_stat:.4f}")
    print(f"p-value     = {p_value:.6f}")
    print ('meana:',sample_a_4_6_0_2.mean(),sample_a_4_6_0_2.std())
    print ('meanb:',sample_c_4_6_0_2.mean(),sample_c_4_6_0_2.std())
except Exception as e:
    print(f"Error performing t-test: {e}")


########################################################################
#################   CLustered heatmap, then repeated below
#########################################################################
ClusterMatrix = np.zeros((6,5),dtype='int')

ClusterMatrix[0,0] = sorted_data_Q3.get('Acceptance', 0)  +  sorted_data_Q4.get('Acceptance', 0) 
ClusterMatrix[0,1] = sorted_data_Q5.get('Acceptance', 0)  +  sorted_data_Q8.get('Acceptance', 0)
ClusterMatrix[0,2] = sorted_data_Q10.get('Acceptance', 0) + sorted_data_Q10b.get('Acceptance', 0) 
ClusterMatrix[0,3] = sorted_data_Q9.get('Acceptance', 0)  + sorted_data_Q11.get('Acceptance', 0) 
ClusterMatrix[0,4] = sorted_data_Q7.get('Acceptance', 0) 

ClusterMatrix[1,0] = sorted_data_Q3.get('Effective use by end users', 0) +  sorted_data_Q4.get('Effective use by end users', 0) 
ClusterMatrix[1,1] = sorted_data_Q5.get('Effective use by end users', 0)  +  sorted_data_Q8.get('Effective use by end users', 0) 
ClusterMatrix[1,2] = sorted_data_Q10.get('Effective use by end users', 0) + sorted_data_Q10b.get('Effective use by end users', 0) 
ClusterMatrix[1,3] = sorted_data_Q9.get('Effective use by end users', 0)  + sorted_data_Q11.get('Effective use by end users', 0) 
ClusterMatrix[1,4] = sorted_data_Q7.get('Effective use by end users', 0) 

ClusterMatrix[2,0] = sorted_data_Q3.get('Independent review', 0)  +  sorted_data_Q4.get('Independent review', 0) 
ClusterMatrix[2,1] = sorted_data_Q5.get('Independent review', 0)  +  sorted_data_Q8.get('Independent review', 0) 
ClusterMatrix[2,2] = sorted_data_Q10.get('Independent review', 0) + sorted_data_Q10b.get('Independent review', 0) 
ClusterMatrix[2,3] = sorted_data_Q9.get('Independent review', 0)  + sorted_data_Q11.get('Independent review', 0) 
ClusterMatrix[2,4] = sorted_data_Q7.get('Independent review', 0) 

ClusterMatrix[3,0] = sorted_data_Q3.get('Problem formulation, context of use', 0)  +  sorted_data_Q4.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,1] = sorted_data_Q5.get('Problem formulation, context of use', 0)  +  sorted_data_Q8.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,2] = sorted_data_Q10.get('Problem formulation, context of use', 0) + sorted_data_Q10b.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,3] = sorted_data_Q9.get('Problem formulation, context of use', 0)  + sorted_data_Q11.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,4] = sorted_data_Q7.get('Problem formulation, context of use', 0) 

ClusterMatrix[4,0] = sorted_data_Q3.get('Research and development', 0)  +  sorted_data_Q4.get('Research and development', 0) 
ClusterMatrix[4,1] = sorted_data_Q5.get('Research and development', 0)  +  sorted_data_Q8.get('Research and development', 0) 
ClusterMatrix[4,2] = sorted_data_Q10.get('Research and development', 0) + sorted_data_Q10b.get('Research and development', 0) 
ClusterMatrix[4,3] = sorted_data_Q9.get('Research and development', 0)  + sorted_data_Q11.get('Research and development', 0) 
ClusterMatrix[4,4] = sorted_data_Q7.get('Research and development', 0) 

ClusterMatrix[5,0] = sorted_data_Q3.get('Scientific validation', 0)  +  sorted_data_Q4.get('Scientific validation', 0) 
ClusterMatrix[5,1] = sorted_data_Q5.get('Scientific validation', 0)  +  sorted_data_Q8.get('Scientific validation', 0) 
ClusterMatrix[5,2] = sorted_data_Q10.get('Scientific validation', 0) + sorted_data_Q10b.get('Scientific validation', 0)
ClusterMatrix[5,3] = sorted_data_Q9.get('Scientific validation', 0)  + sorted_data_Q11.get('Scientific validation', 0) 
ClusterMatrix[5,4] = sorted_data_Q7.get('Scientific validation', 0) 

titoliy =  []

titoliy.append('Acceptance')
titoliy.append('Effective use by end users')
titoliy.append('Independent review')
titoliy.append('Problem formulation ')
titoliy.append('Research and development')
titoliy.append('Scientific validation')


titolix = []
titolix.append('Knowledge prod.') 
titolix.append('Implementers')  
titolix.append('Gatekeepers ') 
titolix.append('Supporters') 
titolix.append('Advocates')  

################### reorder according to Fig1
new_order = [3, 4, 5, 2, 0, 1]

ClusterMatrix_reordered = ClusterMatrix[new_order, :]
titoliy_reordered = [titoliy[i] for i in new_order]
y = np.arange(len(titoliy_reordered))
x = np.arange(len(titolix))


figSMc_re,axSMc_re = plt.subplots(1,figsize=(10,6))

im_re = axSMc_re.imshow(ClusterMatrix_reordered,cmap='magma')

# Create a new axis above the heatmap for the colorbar
cbar_ax = figSMc_re.add_axes([0.435, 0.75, 0.2, 0.03])

# Horizontal colorbar 
cbar = figSMc_re.colorbar(im_re,
                            cax=cbar_ax,
                            orientation='horizontal',
                            pad=-1.2,        # distance from the plot
                            fraction=0.05)   # thickness of the bar

# Move tick labels ABOVE the bar
cbar.ax.xaxis.set_ticks_position('top')
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=14)   # increase tick font size


axSMc_re.set_yticks(y, titoliy_reordered, rotation=0, ha='right', fontsize=14)
axSMc_re.set_xticks(x, titolix, rotation=45, ha='right', fontsize=14)
axSMc_re.set_title('In which activities/phases are these subgroups involved?',fontsize=10,y=1.3)

plt.tight_layout()
plt.show()
figSMc_re.savefig(localpath+'Fig8_clustered_heatmap_orderedFig1.png')

#####################################################
##########      NOW STRATIFY ACCORDING TO INSTITUTIONS
#####################################################
print ('stratirfy the clustered matrix on - what type of institution do you work in?- :')
#print (column_data_institution.unique())


print('NEW UNIQUE - Clustered ')
Lista_Instit_unique = Get_RealUniques(column_data_institution.unique())
print('LOUT\n',Lista_Instit_unique)
#strat_string  = column_data_institution.unique()[4]
strat_string  = Lista_Instit_unique[4]


print ('stratifying to ',strat_string)

superlist =  GetSuperlist_stratif(column_data_Q3,column_data_institution,strat_string)
print ('total number of answers in Q3:',len(superlist))
counter = Counter(superlist)
sorted_data = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
sorted_data_Q3 = sorted_data

superlist = GetSuperlist_stratif(column_data_Q4,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q4 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q4:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q5,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q5 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q5:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q7,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q7 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q7:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q8,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q8 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q8:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q9,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q9 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q9:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q10,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q10 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q10b,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q10b = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q10b:',len(superlist))

superlist = GetSuperlist_stratif(column_data_Q11,column_data_institution,strat_string)
counter = Counter(superlist)
sorted_data_Q11 = dict(sorted(counter.items(), key=lambda item: item[0], reverse=False))
print ('total number of answers in Q11:',len(superlist))

########################################################################
#################   CLustered stratified heatmap
#########################################################################
ClusterMatrix = np.zeros((6,5),dtype='int')

ClusterMatrix[0,0] = sorted_data_Q3.get('Acceptance', 0)  +  sorted_data_Q4.get('Acceptance', 0) 
ClusterMatrix[0,1] = sorted_data_Q5.get('Acceptance', 0)  +  sorted_data_Q8.get('Acceptance', 0) 
ClusterMatrix[0,2] = sorted_data_Q10.get('Acceptance', 0) + sorted_data_Q10b.get('Acceptance', 0)
ClusterMatrix[0,3] = sorted_data_Q9.get('Acceptance', 0)  + sorted_data_Q11.get('Acceptance', 0) 
ClusterMatrix[0,4] = sorted_data_Q7.get('Acceptance', 0) 

ClusterMatrix[1,0] = sorted_data_Q3.get('Effective use by end users', 0)  +  sorted_data_Q4.get('Effective use by end users', 0) 
ClusterMatrix[1,1] = sorted_data_Q5.get('Effective use by end users', 0)  +  sorted_data_Q8.get('Effective use by end users', 0)
ClusterMatrix[1,2] = sorted_data_Q10.get('Effective use by end users', 0) + sorted_data_Q10b.get('Effective use by end users', 0) 
ClusterMatrix[1,3] = sorted_data_Q9.get('Effective use by end users', 0)  + sorted_data_Q11.get('Effective use by end users', 0)
ClusterMatrix[1,4] = sorted_data_Q7.get('Effective use by end users', 0) 

ClusterMatrix[2,0] = sorted_data_Q3.get('Independent review', 0)  +  sorted_data_Q4.get('Independent review', 0) 
ClusterMatrix[2,1] = sorted_data_Q5.get('Independent review', 0)  +  sorted_data_Q8.get('Independent review', 0) 
ClusterMatrix[2,2] = sorted_data_Q10.get('Independent review', 0) + sorted_data_Q10b.get('Independent review', 0) 
ClusterMatrix[2,3] = sorted_data_Q9.get('Independent review', 0)  + sorted_data_Q11.get('Independent review', 0) 
ClusterMatrix[2,4] = sorted_data_Q7.get('Independent review', 0)

ClusterMatrix[3,0] = sorted_data_Q3.get('Problem formulation, context of use', 0)  +  sorted_data_Q4.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,1] = sorted_data_Q5.get('Problem formulation, context of use', 0)  +  sorted_data_Q8.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,2] = sorted_data_Q10.get('Problem formulation, context of use', 0) + sorted_data_Q10b.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,3] = sorted_data_Q9.get('Problem formulation, context of use', 0)  + sorted_data_Q11.get('Problem formulation, context of use', 0) 
ClusterMatrix[3,4] = sorted_data_Q7.get('Problem formulation, context of use', 0) 

ClusterMatrix[4,0] = sorted_data_Q3.get('Research and development', 0)   +  sorted_data_Q4.get('Research and development', 0)  
ClusterMatrix[4,1] = sorted_data_Q5.get('Research and development', 0)   +  sorted_data_Q8.get('Research and development', 0)  
ClusterMatrix[4,2] = sorted_data_Q10.get('Research and development', 0) + sorted_data_Q10b.get('Research and development', 0) 
ClusterMatrix[4,3] = sorted_data_Q9.get('Research and development', 0)   + sorted_data_Q11.get('Research and development', 0)  
ClusterMatrix[4,4] = sorted_data_Q7.get('Research and development', 0)  

ClusterMatrix[5,0] = sorted_data_Q3.get('Scientific validation', 0)  +  sorted_data_Q4.get('Scientific validation', 0)
ClusterMatrix[5,1] = sorted_data_Q5.get('Scientific validation', 0)  +  sorted_data_Q8.get('Scientific validation', 0)
ClusterMatrix[5,2] = sorted_data_Q10.get('Scientific validation', 0) + sorted_data_Q10b.get('Scientific validation', 0)
ClusterMatrix[5,3] = sorted_data_Q9.get('Scientific validation', 0)  + sorted_data_Q11.get('Scientific validation', 0)
ClusterMatrix[5,4] = sorted_data_Q7.get('Scientific validation', 0) 

titoliy =  []

titoliy.append('Acceptance')
titoliy.append('Effective use by end users')
titoliy.append('Independent review')
titoliy.append('Problem formulation ')
titoliy.append('Research and development')
titoliy.append('Scientific validation')


titolix = []
titolix.append('Knowledge prod.') 
titolix.append('Implementers')  
titolix.append('Gatekeepers ') 
titolix.append('Supporters') 
titolix.append('Advocates')  

################### reorder according to Fig1
new_order = [3, 4, 5, 2, 0, 1]

ClusterMatrix_reordered = ClusterMatrix[new_order, :]
titoliy_reordered = [titoliy[i] for i in new_order]
y = np.arange(len(titoliy_reordered))
x = np.arange(len(titolix))


figSMc_re,axSMc_re = plt.subplots(1,figsize=(10,6))

im_re = axSMc_re.imshow(ClusterMatrix_reordered,cmap='magma')

# Create a new axis above the heatmap for the colorbar
cbar_ax = figSMc_re.add_axes([0.435, 0.75, 0.2, 0.03])

# Horizontal colorbar
cbar = figSMc_re.colorbar(im_re,
                            cax=cbar_ax,
                            orientation='horizontal',
                            pad=-1.2,        # distance from the plot
                            fraction=0.05)   # thickness of the bar

# Move tick labels ABOVE the bar
cbar.ax.xaxis.set_ticks_position('top')
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=14)   # increase tick font size


axSMc_re.set_yticks(y, titoliy_reordered, rotation=0, ha='right', fontsize=14)
axSMc_re.set_xticks(x, titolix, rotation=45, ha='right', fontsize=14)
axSMc_re.set_title('activities/phases fpr subgroups, stratified by '+strat_string,fontsize=10,y=1.3)

plt.tight_layout()
plt.show()
figSMc_re.savefig(localpath+'Fig8_clustered_heatmap_ordered_strat_instit_Fig1.png')

print (ClusterMatrix_reordered.sum())
print (ClusterMatrix_reordered)
conteggiTOT = ClusterMatrix_reordered.sum()
print ('conteggiTot:',conteggiTOT)
sample_a = ClusterMatrix_reordered[4:6,2:5].ravel()
print (titolix[3:5],titoliy_reordered[4:6],sample_a.sum()/conteggiTOT,sample_a.std()/conteggiTOT)
sample_aC = ClusterMatrix_reordered[4:6,0].ravel()
print (titolix[0],titoliy_reordered[4:6],sample_aC.sum()/conteggiTOT,sample_aC.std()/conteggiTOT)

print (sample_a)




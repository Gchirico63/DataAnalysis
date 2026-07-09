# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:57:06 2026

@author: giber
"""
# import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import textwrap
import pandas as pd
from collections import Counter


##reduce length pf the entries
def SP_string(string, max_length):
    if len(string) <= max_length:
        return string
    mid = len(string) // 2
    return string[:mid] + '\n' + string[mid:]

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
print(hist_matrix_survey)

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
print ('first 5 countries / total = ',np.round(100*sorted_countries.values[0:5].sum()/sorted_countries.values[:].sum(),1),' %')
print ('total number of countries represented:',len(sorted_countries))

# Show the plot
plt.show()

# Print the data in the column
# Print the unique entries

##################################################  NOW THE stage OF THE CAREER
unique_entries_stage, counts_stage = np.unique(column_data_stage, return_counts=True) 

max_length = 20
Data_Stage = column_data_stage
shortened_entries = [entry.split(" (")[0] for entry in unique_entries_stage]
footnotes = [entry.split(" (", 1)[1] if " (" in entry else "" 
             for entry in unique_entries_stage]

split_entries = [textwrap.fill(entry, width = max_length) for entry in shortened_entries]
print (footnotes)
# Create a histogram of the entries in the specific column
x = np.arange(len(unique_entries_stage))  # numeric positions
plt.figure()
'''
plt.bar(x, counts_stage, width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

plt.xticks(x, split_entries, rotation=45, ha='right', fontsize=14)
plt.yticks( [0,10,20,30],fontsize=14)

#plt.hist(split_entries, bins = len(unique_entries_stage), edgecolor='black')

plt.ylabel('Frequency',fontsize= 16)
'''
####################### a pie plot ##################
totalE = np.sum(counts_stage)

def autopct_abs(pct):
    absolute = int(round(pct/100 * totalE))
    return f"{pct:.1f}%\n({absolute})"

# Pattern hatch diversi
hatches = ['///', '\\\\\\', 'xxx', '---', '+++', 'ooo', '***', '...']

figPIE, axPIE = plt.subplots(figsize=(7,7))

wedges, texts, autotexts = axPIE.pie(
    counts_stage,
    labels=split_entries,
    autopct=autopct_abs,
    startangle=90,
    counterclock=False,
    colors=['white'] * len(counts_stage),   # tutto bianco
    wedgeprops=dict(edgecolor='black', linewidth=1.2,alpha=0.3)
)

# Applica hatch diversi a ogni settore
for w, h in zip(wedges, hatches):
    w.set_hatch(h)
    
for t in texts:
    t.set_fontsize(18)   # aumenta qui (16–22 è un buon range)
for t in autotexts:
    t.set_fontsize(16)    
figPIE.suptitle('Histogram of career stage')
plt.tight_layout()
#plt.xticks(rotation=45,size=12,ha='right')
plt.grid(True)

# Show the plot
plt.show()
figPIE.savefig('PIE_careerStage.png')


# Print the data in the column
# Print the unique entries
unique_entries_field = df[column_name_field].unique()

print ('how many insitution answers:',len(df[column_name_institution]))
###  NOW THE INSTITUTIONS
L_institutions = []
for INS in df[column_name_institution]:
    INSplit = INS.split(';')
    L_institutions.append(INSplit[0].strip())
print ('total primary institutions answers:',len(L_institutions))
unique_entries_institutions = list(set(L_institutions))

#unique_entries = df[column_name_institution].unique()
# Get unique labels and their counts unique_labels, 
unique_labels, counts = np.unique(L_institutions, return_counts=True) 

# Create a 2D matrix with labels and their counts
hist_matrix_survey = np.column_stack((unique_labels, counts)) 
print (hist_matrix_survey)
print(hist_matrix_survey.shape)
plt.figure()
max_length = 10
split_entries = [SP_string(entry, max_length) for entry in L_institutions]

counter = Counter(split_entries)
sorted_data = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
print ('sorted',sorted_data.items())
labels, values = zip(*sorted_data.items())


titolix =  []
notepiepagina = []
for k in range(len(labels)):
    sss = labels[k].split(" (")[0]
    wrapped = textwrap.fill(sss, width=20)
    titolix.append(wrapped)
    notepiepagina.append(labels[k].split(" (")[1])

# Create a histogram of the entries in the specific column

x = np.arange(len(labels))  # numeric positions

plt.figure(figsize=(10,6))
plt.bar(x, values, edgecolor='black')

plt.xticks(x, titolix, rotation=45, ha='right', fontsize=12)
plt.ylabel('Frequency', fontsize=18)
plt.title('Histogram of Research Field')
plt.grid(axis='y')

plt.tight_layout()
plt.show()


#########
############################# nopw open the list of the cost action aprticipants. 
fname_partic = "G:\\My Drive\\progetti\\CEE\\COST_IMPROVE\\2026\\SurveyAnalysis\\CA21139-WG-members - 2024-06-25 PLUS activity preferences.xlsx"

# Read the Excel file
df_COST = pd.read_excel(fname_partic, engine="openpyxl")

# Show the first rows
print ('read in the list of Cost participants')
survey_counts = df[column_name].value_counts().rename("Survey_Count")
cost_counts   = df_COST["Country"].value_counts().rename("COST_Count")
print ('HERE')
print (survey_counts)
print ('HERE')
print (cost_counts)

df_corr = pd.concat([survey_counts, cost_counts], axis=1)
df_corr = df_corr.fillna(0).astype(int)
print(df_corr)

####################################################
'''
nOW analyze the 
column_name_rankQ4 ='4. Rank the following challenges in the implementation of 3Rs based on your experience (most challenge on top).'

column_data_rankQ4
'''
print ('analysizng now: ', column_data_rankQ4 )
'''
there were 5 choices possible, up to 5 responses
'''

LresultsQ4_1 = []
LresultsQ4_2 = []
LresultsQ4_3 = []
LresultsQ4_4 = []
LresultsQ4_5 = []
for k in range(len(column_data_rankQ4)):
    V = column_data_rankQ4[k].split(';')  ### contains the 5 responses per respondent
    LresultsQ4_1.append(V[0])
    LresultsQ4_2.append(V[1])
    LresultsQ4_3.append(V[2])
    LresultsQ4_4.append(V[3])
    LresultsQ4_5.append(V[4])

LresultsQ4_1 = [item.strip() for item in LresultsQ4_1]
LresultsQ4_2 = [item.strip() for item in LresultsQ4_2]
LresultsQ4_3 = [item.strip() for item in LresultsQ4_3]
LresultsQ4_4 = [item.strip() for item in LresultsQ4_4]
LresultsQ4_5 = [item.strip() for item in LresultsQ4_5]

print (len(LresultsQ4_1))
print (len(LresultsQ4_2))
print (len(LresultsQ4_3))
print (len(LresultsQ4_4))
print (len(LresultsQ4_5))

import pandas as pd

unique_entriesQ4_1 = pd.Series(LresultsQ4_1).unique()
unique_entries = unique_entriesQ4_1
unique_entriesQ4_2 = pd.Series(LresultsQ4_2).unique()
unique_entriesQ4_3 = pd.Series(LresultsQ4_3).unique()
unique_entriesQ4_4 = pd.Series(LresultsQ4_4).unique()
unique_entriesQ4_5 = pd.Series(LresultsQ4_5).unique()
print(unique_entriesQ4_1)

###build the histogram 
counter1 = Counter(LresultsQ4_1)
counter2 = Counter(LresultsQ4_2)
counter3 = Counter(LresultsQ4_3)
counter4 = Counter(LresultsQ4_4)
counter5 = Counter(LresultsQ4_5)


def prepare_bar(counter):
    sorted_data = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    labels, values = zip(*sorted_data.items())
    titolix =  []
    for k in range(len(labels)):
        sss = labels[k].split(" (")[0]
        wrapped = textwrap.fill(sss, width=20)
        titolix.append(wrapped)

    x = np.arange(len(labels))  # numeric positions
    return x,values,titolix

x1,values1,titolix1 = prepare_bar(counter1)
x2,values2,titolix2 = prepare_bar(counter2)
x3,values3,titolix3 = prepare_bar(counter3)
x4,values4,titolix4 = prepare_bar(counter4)
x5,values5,titolix5 = prepare_bar(counter5)

print (titolix1)
print (values1)
print (titolix2)
print (values2)
print (titolix3)
print (values3)
print (titolix3)
print (values3)
print (titolix4)
print (values4)
print (titolix5)
print (values5)


def get_value(target_flat, values, titolix):
    for v, t in zip(values, titolix):
        if t.replace('\n', ' ') == target_flat:
            return v
    return 0

target_flat = 'lack of awareness and training'

total = (get_value(target_flat, values1, titolix1)
         + get_value(target_flat, values2, titolix2)
         + get_value(target_flat, values3, titolix3)
         + get_value(target_flat, values4, titolix4)
         + get_value(target_flat, values5, titolix5))

print('total for', target_flat, ':', total)   

target_flat = 'limited collaboration across stakeholders'

total = (get_value(target_flat, values1, titolix1)
         + get_value(target_flat, values2, titolix2)
         + get_value(target_flat, values3, titolix3)
         + get_value(target_flat, values4, titolix4)
         + get_value(target_flat, values5, titolix5))
print('total for', target_flat, ':', total)   

target_flat = 'resistance change'

total = (get_value(target_flat, values1, titolix1)
         + get_value(target_flat, values2, titolix2)
         + get_value(target_flat, values3, titolix3)
         + get_value(target_flat, values4, titolix4)
         + get_value(target_flat, values5, titolix5))
print('total for', target_flat, ':', total)   

target_flat = 'resource constraints'

total = (get_value(target_flat, values1, titolix1)
         + get_value(target_flat, values2, titolix2)
         + get_value(target_flat, values3, titolix3)
         + get_value(target_flat, values4, titolix4)
         + get_value(target_flat, values5, titolix5))
print('total for', target_flat, ':', total)   

 ################################################### 
######### now plot

F,A = plt.subplots(2,3, figsize=(10,6))

A[0,0].bar(x1 , values1 , width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

A[0,0].set_xticks(x1, titolix1, rotation=45, ha='right', fontsize=10)
A[0,0].set_ylabel('Frequency', fontsize=18)
A[0,0].set_title('first choice  challenges')

A[0,1].bar(x2 , values2 , width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

A[0,1].set_xticks(x2, titolix2, rotation=45, ha='right', fontsize=10)
A[0,1].set_ylabel('Frequency', fontsize=18)
A[0,1].set_title('second choice challenges')

A[0,2].bar(x3 , values3 , width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

A[0,2].set_xticks(x3, titolix3, rotation=45, ha='right', fontsize=10)
A[0,2].set_ylabel('Frequency', fontsize=18)
A[0,2].set_title('third choice challenges')

A[1,0].bar(x3 , values3 , width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

A[1,0].set_xticks(x3, titolix3, rotation=45, ha='right', fontsize=10)
A[1,0].set_ylabel('Frequency', fontsize=18)
A[1,0].set_title('fourth choice challenges')

A[1,1].bar(x3 , values3 , width=1.0, 
        edgecolor='black', 
        facecolor='none',   # no fill
        hatch='//')         # hatch pattern

A[1,1].set_xticks(x3, titolix3, rotation=45, ha='right', fontsize=10)
A[1,1].set_ylabel('Frequency', fontsize=18)
A[1,1].set_title('fifth choice challenges')

plt.tight_layout()
plt.show()

print (LresultsQ4_2)

##########################     ORDERED PLOT 
import matplotlib.pyplot as plt
import numpy as np
import textwrap
from collections import Counter

# Define a mapping from challenge descriptions to letters
challenge_map = {
    "lack of awareness and training": "A",
    "resource constraints": "B",
    "regulatory hurdles": "C",
    "resistance change": "D",
    "limited collaboration across stakeholders": "E"
}

def prepare_bar(counter):
    sorted_data = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    labels, values = zip(*sorted_data.items())
    # Map labels to A–E codes
    titolix = [challenge_map.get(label, label) for label in labels]
    x = np.arange(len(labels))
    return x, values, titolix

# Prepare each ranking level
x1, values1, titolix1 = prepare_bar(counter1)
x2, values2, titolix2 = prepare_bar(counter2)
x3, values3, titolix3 = prepare_bar(counter3)
x4, values4, titolix4 = prepare_bar(counter4)
x5, values5, titolix5 = prepare_bar(counter5)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 6))
axes = axes.flatten()

# Titles for each subplot
titles = [
    "First Choice Challenges",
    "Second Choice Challenges",
    "Third Choice Challenges",
    "Fourth Choice Challenges",
    "Fifth Choice Challenges"
]

# Data for each subplot
data = [
    (x1, values1, titolix1),
    (x2, values2, titolix2),
    (x3, values3, titolix3),
    (x4, values4, titolix4),
    (x5, values5, titolix5)
]

# Plot only the first five subplots
for i in range(5):
    x, values, labels = data[i]
    axes[i].bar(x, values, width=1.0, edgecolor='black', facecolor='none', hatch='//')
    axes[i].set_xticks(x, labels, rotation=0, fontsize=12)
    axes[i].set_ylabel("Frequency", fontsize=12)
    axes[i].set_title(titles[i], fontsize=14)

# Hide the sixth subplot (bottom right)
axes[5].axis("off")

x0 = 0.9
for label in unique_entries:
    S0 =  challenge_map[label] + ' : ' + label 
    axes[5].text(0.02,x0,S0)
    x0 = x0 - 0.2

plt.tight_layout()
plt.show()
######## npw the stacked percxentage bar plot 

###à# PERCENTAGE of 3R challenge per research type
canonical_order = ["A", "B", "C", "D", "E"]   # replace with your real labels
#We reorder each (values#, titolix#) pair to match canonical_order.
reordered_values = []

for x, values, labels in data:
    # Build a mapping from label → value
    mapping = dict(zip(labels, values))

    # Reorder values according to canonical order
    reordered = [mapping[label] for label in canonical_order]

    reordered_values.append(reordered)

######### perncetage 
percent_values = []

for rv in reordered_values:
    total = sum(rv)
    percent_values.append([v / total * 100 for v in rv])


fig, ax = plt.subplots(figsize=(10,6))

labels = canonical_order
x = np.arange(len(labels))
width = 0.7

bottom = np.zeros(len(labels))

for i in range(5):   # 5 subplots
    ax.bar(
        x,
        percent_values[i],
        bottom=bottom,
        width=width,
        label=f"Choice {i+1}"
    )
    bottom += percent_values[i]

ax.set_xticks(x, labels, rotation=0, ha='right', fontsize=18)
ax.tick_params(axis='y', labelsize=18)
ax.set_ylabel("Percentage (%)", fontsize=26)
ax.set_title("Frequency", fontsize=20)
ax.set_ylim(0, 100)
ax.legend(loc='center left', fontsize = 22 ,bbox_to_anchor=(1.02, 0.5))


plt.tight_layout()
plt.show()

fig.savefig(localpath+'rankingplotbar.png',dpi=300)
######### trnapose
percent_values_T = np.array(percent_values).T

fig, ax = plt.subplots(figsize=(10,6))

choices = [f"Choice {i+1}" for i in range(5)]
x = np.arange(len(choices))
width = 0.7

bottom = np.zeros(len(choices))

for j, label in enumerate(canonical_order):   # loop over A,B,C,D,E
    ax.bar(
        x,
        percent_values_T[j],
        bottom=bottom,
        width=width,
        label=label
    )
    bottom += percent_values_T[j]

ax.set_xticks(x, choices, rotation=0, fontsize=18)
ax.tick_params(axis='y', labelsize=18)
ax.set_ylabel("Percentage (%)", fontsize=26)
ax.set_title("Frequency", fontsize=20)
ax.set_ylim(0, 100)

ax.legend(loc='center left', fontsize=22, bbox_to_anchor=(1.02, 0.5))

plt.tight_layout()
plt.show()

fig.savefig(localpath+'rankingplotbar_reversed.png', dpi=300)

#print (percent_values)
''' 
########## stratification per sector
column_name_research = '4. What type of research are you mainly involved in?'
column_data_research = df[column_name_research]
'''
######################################################################
########################## STRATIFICATION: first-choice challenge vs research field #########################

# Research field per respondent, aligned with LresultsQ4_1 (same row order)
# If a respondent could tick more than one field, keep only the first one (like you did for institutions)

research_field_raw = df[column_name_research].astype(str)
research_field = [r.split(';')[0].strip() for r in research_field_raw]
#### take only the first choesen research field
print('len research_field:', len(research_field))
print('len LresultsQ4_1:  ', len(LresultsQ4_1))

# Map each first-choice challenge to its A-E code, same mapping used before
challenge1_coded = [challenge_map.get(item, item) for item in LresultsQ4_1]
challenge2_coded = [challenge_map.get(item, item) for item in LresultsQ4_2]


FLAG = 2  
if FLAG == 1:
    print ('I am FLAG 1')
# Build a cross-tab: rows = research field, columns = challenge code (A-E)
    df_strat = pd.DataFrame({
        'research_field': research_field,
        'challenge': challenge1_coded
        })
    crosstab = pd.crosstab(df_strat['research_field'], df_strat['challenge'])

# stack: each respondent appears twice, once per choice, same research_field both times
elif FLAG == 2: 
    print ('I am FLAG 2')
    df_strat_combined = pd.DataFrame({
        'research_field': research_field + research_field,
        'challenge': challenge1_coded + challenge2_coded,
        'choice_rank': ['1st'] * len(research_field) + ['2nd'] * len(research_field)
        })
    crosstab = pd.crosstab(df_strat_combined['research_field'], df_strat_combined['challenge'])


# Make sure all A-E columns exist and are in canonical order, even if some are 0
for c in canonical_order:
    if c not in crosstab.columns:
        crosstab[c] = 0
crosstab = crosstab[canonical_order]

print ('stgrtifrication with the research field')

print(crosstab)

# Convert counts to row-wise percentages
crosstab_pct = crosstab.div(crosstab.sum(axis=1), axis=0) * 100

print(crosstab_pct)

# --- stacked percentage bar plot, one bar per research field ---
fig, ax = plt.subplots(figsize=(8, 6))

fields = crosstab_pct.index.tolist()
x = np.arange(len(fields))
width = 0.7
bottom = np.zeros(len(fields))

for c in canonical_order:
    ax.bar(x, crosstab_pct[c], bottom=bottom, width=width, label=c)
    bottom += crosstab_pct[c].values

wrapped_fields = [textwrap.fill(f, width=15) for f in fields]
ax.set_xticks(x, wrapped_fields, rotation=45, ha='right', fontsize=16)
ax.tick_params(axis='y', labelsize=18)
ax.set_ylabel('Percentage (%)', fontsize=18)
ax.set_title('First-choice challenge, stratified by research field: '+str(FLAG), fontsize=16)
ax.set_ylim(0, 100)
ax.legend(title='Challenge', loc='center left', fontsize=14, bbox_to_anchor=(1.02, 0.5))

plt.tight_layout()
plt.show()

fig.savefig( localpath + str(FLAG) + 'firstchoice_by_researchfield.png', dpi=300)

# also add the A-E legend text like you did before, for reference
print('\nLegend:')
for label in unique_entries:
    print(challenge_map[label], ':', label)


######################################################################
########################## STRATIFICATION: first-choice challenge vs institution  #########################

# Research field per respondent, aligned with LresultsQ4_1 (same row order)
# If a respondent could tick more than one field, keep only the first one (like you did for institutions)
#column_name_institution = '5. What type of institution do you work in?'
#column_data_institution = df[column_name_institution]

institution_raw = df[column_name_institution].astype(str)
institution     = [r.split(';')[0].strip() for r in institution_raw]
#### take only the first choesen research field
print('len institution_raw:', len(institution_raw))
print('len LresultsQ4_1:  ' , len(LresultsQ4_1))

# Map each first-choice challenge to its A-E code, same mapping used before
challenge1_coded = [challenge_map.get(item, item) for item in LresultsQ4_1]
challenge2_coded = [challenge_map.get(item, item) for item in LresultsQ4_2]

FLAG = 2
if FLAG == 1:
# Build a cross-tab: rows = research field, columns = challenge code (A-E)
    df_strat = pd.DataFrame({
        'institution': institution,
        'challenge': challenge1_coded
        })
    crosstab = pd.crosstab(df_strat['institution'], df_strat['challenge'])

elif FLAG ==2:
    df_strat = pd.DataFrame({
        'institution': institution + institution,
        'challenge': challenge1_coded + challenge2_coded,
        'choice_rank': ['1st'] * len(research_field) + ['2nd'] * len(research_field)
        })
    crosstab = pd.crosstab(df_strat['institution'], df_strat['challenge'])

# Make sure all A-E columns exist and are in canonical order, even if some are 0

for c in canonical_order:
    if c not in crosstab.columns:
        crosstab[c] = 0

crosstab = crosstab[canonical_order]

print ('stratifrication with the institution')
print(crosstab)

# Convert counts to row-wise percentages
crosstab_pct = crosstab.div(crosstab.sum(axis=1), axis=0) * 100

print(crosstab_pct)
print ('LENNNN:',len(crosstab_pct))

######### reorder the columns 
# Reorder rows: swap the last two institutions along the x-axis

#row_order = list(crosstab_pct.index[:-2]) + [crosstab_pct.index[-1], crosstab_pct.index[-2]]

row_order = [
    crosstab_pct.index[5] ,
    crosstab_pct.index[0],
    crosstab_pct.index[2] ,
    crosstab_pct.index[3] , 
    crosstab_pct.index[1] , 
    crosstab_pct.index[4]
    ]

print ('roworder :', row_order) 
crosstab_pct_plot = crosstab_pct.loc[row_order]

# --- stacked percentage bar plot, one bar per research field ---
fig, ax = plt.subplots(figsize=(8, 6))

fields = crosstab_pct_plot.index.tolist()
x = np.arange(len(fields))
width = 0.7
bottom = np.zeros(len(fields))

for c in canonical_order:
    ax.bar(x, crosstab_pct_plot[c], bottom=bottom, width=width, label=c)
    bottom += crosstab_pct_plot[c].values

wrapped_fields = [textwrap.fill(f, width=15) for f in fields]
wrapped_fields_0 = [f.split(' ')[0] for f in wrapped_fields]

ax.set_xticks(x, wrapped_fields_0, rotation=45, ha='right', fontsize=16)
ax.tick_params(axis='y', labelsize=18)
ax.set_ylabel('Percentage (%)', fontsize=18)
ax.set_title('First-choice challenge, stratified by institution '+str(FLAG), fontsize=16)
ax.set_ylim(0, 100)
ax.legend(title='Challenge', loc='center left', fontsize=14, bbox_to_anchor=(1.02, 0.5))

plt.tight_layout()
plt.show()

fig.savefig(localpath + str(FLAG)+'firstchoice_by_institution.png', dpi=300)

print (fields)
# also add the A-E legend text like you did before, for reference
'''
print('\nLegend:')
for label in unique_entries:
    print(challenge_map[label], ':', label)

for kt in range(len(df_strat)):
    if df_strat['institution'][kt].split(' ')[0] == 'Animal':
        print (df_strat['challenge'])
print (crosstab)
'''
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 08:02:08 2026

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

category_keywords_ORG = {
    "Universities / Academia": [
        r"universit", r"academ", r"research institut", r"research centre",
        r"research organi", r"research hospital", r"clinic",
        r"educational institution", r"biotech", r"universidad", r"science board"
    ],
    "Regulatory / Testing Bodies": [
        r"regulat", r"ecvam", r"competent author", r"eurl",
        r"laborat.*alternative", r"validation of alternative",
        r"glp facilit", r"\bcros\b", r"health organi"
    ],
    "Funding Bodies": [
        r"fund", r"horizon", r"european comission"
    ],
    "Animal Welfare / 3R Centers": [
        r"\b3r\b", r"\b3rs\b", r"3r[s]?\s*centr", r"national.*replacement.*refinement.*reduction",
        r"animal protection", r"animal welfare"
    ],
    "Industry": [
# %%
        r"industr", r"compan(y|ies)", r"pharma", r"private small consultant", "glp", "cro"

    ],
    "Journals / Publishing": [
        r"journal", r"editorial board"
    ],
    "Political / EU / Government Bodies": [
        r"european union", r"\beu\b", r"european commission", r"council of europe",
        r"political", r"legislat", r"local government", r"\bgovernment\b",
        r"\bema\b", r"\bnih\b", r"world health organization"
    ],
    "International / Standard-Setting Bodies": [
        r"\boecd\b"
    ],
    "NGOs": [
        r"non.?governmental", r"\bngo\b"
    ],
    "Schools / Education": [
        r"\bschool"
    ],
    "Ethics Committees": [
        r"ethic", r"comit.*etica"
    ],
    "Media": [
        r"\btv\b", r"cinema"
    ],
    "Other Scientists / Experts": [
        r"scientist", r"expert", r"influencer", r"professional"
    ],
    "Process / Non-Stakeholder Answer": [
        r"problem formulation", r"context of use", r"promote meetings"
    ],
}
# canonical categories, each with a set of keywords/regex fragments to match (case-insensitive)
category_keywords = {
    "Training / Education": [
        r"train", r"curricul", r"educat", r"workshop", r"seminar", r"webinar",
        r"mentorship", r"course", r"fellowship", r"university could promote meetings"
    ],
    "Funding / Financial Incentives": [
        r"fund", r"grant", r"financial incentive", r"tax benefit", r"money to",
        r"investment"
    ],
    "Validation / Standardiz. actions": [
        r"validat", r"standardi[sz]", r"benchmark", r"harmoni[sz]", r"performance criteria",
        r"scientific integrity", r"good science practi", r"reproducib", r"repeatab",
        r"bench marking"
    ],
    "Awareness / Commun. / Dissemin. actions": [
        r"awareness", r"disseminat", r"communicat", r"outreach", r"public",
        r"transparency", r"youtube", r"documentar", r"citizen",
        r"spreading knowledge"
    ],
    "Regulat. / Policy / Legal actions": [
        r"regulat", r"legal", r"law", r"legislat", r"polic(y|ies)", r"guideline",
        r"acceptance for regulatory", 
        r"mandatory.*report", r"requirement",r"restrict the use of animal",
        r"one health approach"
    ],
    "Collaboration / Networks / Platforms": [
        r"platform", r"hub\b", r"network", r"collaborat", r"partnership",
        r"ppp", r"consorti", r"centralised", r"centralized",
        r"share expertise"
    ],
    "Research & Technology Development": [
        r"develop.*method", r"non-animal method", r"nams\b", r"organ-on-chip",
        r"organoid", r"microphysiological", r"ai-based", r"in vitro", r"model of disease",
        r"r&d", r"enabling implementation of novel 3Rs methods in running research lines",
        r"experimental research design"
    ],
    "Institutional / Infrastructure Support": [
        r"institute", r"accelerator", r"incubator", 
        r"establish.*institut", r"innovation",
        r"greater support for activity"
    ],
    "Ethics Committee / Oversight": [
        r"ethics committee"
    ],
    "Journals / Publishing / Peer Review": [
        r"journal", r"peer review", r"editor", 
        r"manuscript", r"reviewers", r"creating a white paper"
    ],
    "Environmental / Non-3R Activities": [
        r"recycl", r"waste segregation", r"clean up"
    ],
    "Unclear / Non-Actionable / Meta-comment": [
        r"^i don't know$", r"^acceptance$", r"^transparency$"
    ],
}
''' 
category_keywords = {
    "Universities / Academia":        [r"universit", r"academ", r"research institut", r"research centre",
                                        r"research organi", r"clinic",r"universi"],
    "Regulatory / Health Agencies":   [r"regulat", r"ecvam", r"ema\b", r"fda", r"competent author",
                                        r"eurl", r"health organi",r"laborat"],
    "Funding Bodies":                 [r"fund"],
    "Animal Welfare / 3R Centers":    [r"3r\b", r"3rs\b", r"3r centre", r"3r center",
                                        r"animal protection", r"animal welfare",r"centr"],
    "Industry":                       [r"industr", r"compan(y|ies)"],
    "Journals":                       [r"journal"],
    "Political / EU Bodies":          [r"european union", r"european commission", r"council of europe",
                                        r"political", r"legislat", r"local government"],
    "Schools / Education":            [r"school"],
    "Ethics Committees":              [r"ethic"],
    "Other Scientists / Experts":     [r"scientist", r"expert", r"influencer"],
}
'''

def classify(text,Cat_list_keywords):
    t = text.lower()
    matched = []
#    for cat, patterns in category_keywords.items():
    for cat, patterns in Cat_list_keywords.items():
        if any(re.search(p, t) for p in patterns):
            matched.append(cat)
    if not matched:
        return "Other / Unclear"
    return matched  # a single answer may match multiple categories


def CLASSIFICA(raw_answers,Cat_list_keywords):
    
    all_matches = []
    unclassified = []
    for ans in raw_answers:
        cats = classify(ans,Cat_list_keywords)
        if cats == "Other / Unclear":
            unclassified.append(ans)
            all_matches.append("Other / Unclear")
        else:
            all_matches.extend(cats)

    print("UNCLASSIFIED (check these manually):")
    for u in unclassified:
        print(" -", u)

    counts = Counter(all_matches)
    return counts


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

##### prepare the data 

def Pulizia(Lista):
# 1. Drop true NaN values
    cleaned = Lista.dropna()
# 2. Convert to string and strip whitespace
    cleaned = cleaned.astype(str).str.strip()
# 3. Remove entries that are literally "nan", "NaN", "", or "None"
    bad_values = {"nan", "NaN", "None", ""}
    cleaned = cleaned[~cleaned.str.lower().isin(bad_values)]
    return cleaned

#print (df.columns)
### first option
column_name_Q3P3_1 = "3. What are new activities that could facilitate 3R's methods implementation and which organization could perform them? (Name maximum three activities and organisations, and be as specific as possible) 1:Activity"
column_data_Q3P3_1 = df[column_name_Q3P3_1]

column_name_Q3P3_1_Org = "3. What are new activities that could facilitate 3R's methods implementation and which organization could perform them? (Name maximum three activities and organisations, and be as specific as possible) 1:Organization"
column_data_Q3P3_1_Org = df[column_name_Q3P3_1_Org]
#### second option
column_name_Q3P3_2 = "3. What are new activities that could facilitate 3R's methods implementation and which organization could perform them? (Name maximum three activities and organisations, and be as specific as possible) 2:Activity"
column_data_Q3P3_2 = df[column_name_Q3P3_2]

column_name_Q3P3_2_Org = "3. What are new activities that could facilitate 3R's methods implementation and which organization could perform them? (Name maximum three activities and organisations, and be as specific as possible) 2:Organization"
column_data_Q3P3_2_Org = df[column_name_Q3P3_2_Org]

#### third option
column_name_Q3P3_3 = "3. What are new activities that could facilitate 3R's methods implementation and which organization could perform them? (Name maximum three activities and organisations, and be as specific as possible) 3:Activity"
column_data_Q3P3_3 = df[column_name_Q3P3_3]

column_name_Q3P3_3_Org = "3. What are new activities that could facilitate 3R's methods implementation and which organization could perform them? (Name maximum three activities and organisations, and be as specific as possible) 3:Organization"
column_data_Q3P3_3_Org = df[column_name_Q3P3_3_Org]


cleaned_Q3P3_1 = Pulizia(column_data_Q3P3_1)
print ('answers to q1:',len(cleaned_Q3P3_1))
cleaned_Q3P3_1_Org = Pulizia(column_data_Q3P3_1_Org)
print ('answers to q1_org:',len(cleaned_Q3P3_1))

cleaned_Q3P3_2 = Pulizia(column_data_Q3P3_2)
print ('answers to q2:',len(cleaned_Q3P3_2))
cleaned_Q3P3_2_Org = Pulizia(column_data_Q3P3_2_Org)
print ('answers to q2_org:',len(cleaned_Q3P3_2))

cleaned_Q3P3_3 = Pulizia(column_data_Q3P3_3)
print ('answers to q3:',len(cleaned_Q3P3_3))
cleaned_Q3P3_3_Org = Pulizia(column_data_Q3P3_3_Org)
print ('answers to q3_org:',len(cleaned_Q3P3_3))

# your raw free-text list (as a pandas Series or list of strings)
################  ORGANIZATIONS #########################
raw_answers = cleaned_Q3P3_1_Org 
# classify everything, letting one raw answer count toward multiple categories# classify everything, letting one raw answer count toward multiple categories
conteggi1 = CLASSIFICA(raw_answers,category_keywords_ORG)

print('These are the counts ORG 1\n',conteggi1)

raw_answers = cleaned_Q3P3_2_Org 
# classify everything, letting one raw answer count toward multiple categories# classify everything, letting one raw answer count toward multiple categories
conteggi2 = CLASSIFICA(raw_answers,category_keywords_ORG)

print('These are the counts ORG  2\n',conteggi2)

raw_answers = cleaned_Q3P3_3_Org 
# classify everything, letting one raw answer count toward multiple categories# classify everything, letting one raw answer count toward multiple categories
conteggi3 = CLASSIFICA(raw_answers,category_keywords_ORG)

print('These are the counts ORG  3\n',conteggi3)

sorted_counts = dict(sorted(conteggi1.items(), key=lambda x: x[1], reverse=True))
labels1, values1 = zip(*sorted_counts.items())
sorted_counts = dict(sorted(conteggi2.items(), key=lambda x: x[1], reverse=True))
labels2, values2 = zip(*sorted_counts.items())
sorted_counts = dict(sorted(conteggi3.items(), key=lambda x: x[1], reverse=True))
labels3, values3 = zip(*sorted_counts.items())

######### join them 

conteggi_totale = Counter(conteggi1) + Counter(conteggi2) + Counter(conteggi3)

sorted_counts = dict(sorted(conteggi_totale.items(), key=lambda x: x[1], reverse=True))
labels_totale, values_totale = zip(*sorted_counts.items())

print('labels total:\n',labels_totale)
print('Values:\n', values_totale)


fig, ax = plt.subplots(1,2,figsize=(8,12))

y = np.arange(len(labels_totale))
ax[1].barh(y, values_totale, edgecolor='black', facecolor='none', hatch='//')
ax[1].set_yticks(y, labels_totale, fontsize=20)
ax[1].invert_yaxis()  # highest count on top
ax[1].yaxis.tick_right()
ax[1].yaxis.set_label_position('right')

ax[1].set_xlabel('Counts', fontsize=22)
ax[1].set_xticks([0,15,30], ['0','15','30'], fontsize=20)
ax[1].set_xlim(0,30)
ax[1].set_title('Stakeholders mentioned (grouped/cleaned), Aall', fontsize=15)
ax[1].grid(axis='x')
ax[1].text(80,-0.5,'(B)', fontsize=28)

#fig.savefig(localpath + 'stakeholder_histogram.png', dpi=300)



############################# DO THE SAME FOR THE ACTIONS
################  ACTIONS  #########################
raw_answers = cleaned_Q3P3_1 
# classify everything, letting one raw answer count toward multiple categories# classify everything, letting one raw answer count toward multiple categories
conteggi1 = CLASSIFICA(raw_answers,category_keywords)

print('These are the counts actions 1\n',conteggi1)

raw_answers = cleaned_Q3P3_2 
# classify everything, letting one raw answer count toward multiple categories# classify everything, letting one raw answer count toward multiple categories
conteggi2 = CLASSIFICA(raw_answers,category_keywords)

print('These are the counts actions 2\n',conteggi2)

raw_answers = cleaned_Q3P3_3 
# classify everything, letting one raw answer count toward multiple categories# classify everything, letting one raw answer count toward multiple categories
conteggi3 = CLASSIFICA(raw_answers,category_keywords)

print('These are the counts actions 3\n',conteggi3)

sorted_counts = dict(sorted(conteggi1.items(), key=lambda x: x[1], reverse=True))
labels1, values1 = zip(*sorted_counts.items())
sorted_counts = dict(sorted(conteggi2.items(), key=lambda x: x[1], reverse=True))
labels2, values2 = zip(*sorted_counts.items())
sorted_counts = dict(sorted(conteggi3.items(), key=lambda x: x[1], reverse=True))
labels3, values3 = zip(*sorted_counts.items())

######### join them 

conteggi_totale = Counter(conteggi1) + Counter(conteggi2) + Counter(conteggi3)

sorted_counts = dict(sorted(conteggi_totale.items(), key=lambda x: x[1], reverse=True))
labels_totale, values_totale = zip(*sorted_counts.items())

print('labels total Actions:\n',labels_totale)
print('Values actions :\n', values_totale)


#figA, axA = plt.subplots(figsize=(8,8))

y = np.arange(len(labels_totale))
ax[0].barh(y, values_totale, edgecolor='black', facecolor='none', hatch='//')

ax[0].set_yticks(y)
ax[0].set_yticklabels(labels_totale, fontsize=20)

ax[0].invert_yaxis()  # highest count on top
ax[0].set_xlabel('Counts', fontsize=22)
ax[0].set_xticks([0,15,30])
ax[0].set_xticklabels(['0','15','30'], fontsize=20)
ax[0].set_xlim(30,0)

#ax[0].set_title('Stakeholders ACTIONS  (grouped/cleaned), Aall', fontsize=15)
ax[0].text(80,-0.5,'(A)', fontsize=28)
ax[0].grid(axis='x')

plt.tight_layout()
plt.show()

fig.savefig(
    localpath + 'stakeholder_AND_actions_histogram.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.15
)

############## Who they are? 
# Convert to a unique sorted list (optional but usually useful)
def normalize(s):
    return (
        s.strip()                 # remove leading/trailing spaces
         .lower()                 # normalize case
         .replace("  ", " ")      # collapse double spaces
         .replace('"', '')            # remove quotation marks
         .replace("\u00a0", " ")  # remove non-breaking spaces
    )

all_strings = pd.concat([
    cleaned_Q3P3_1_Org,
    cleaned_Q3P3_2_Org,
    cleaned_Q3P3_3_Org
], ignore_index=True)

normalized_strings = all_strings.astype(str).apply(normalize)
unique_strings = sorted(set(normalized_strings))

# Save to CSV
pd.Series(unique_strings).to_csv(localpath+"cleaned_Q3P3_Org_strings.csv", index=False)

############## what can they do? 
# Convert to a unique sorted list (optional but usually useful)
def normalize(s):
    return (
        s.strip()                 # remove leading/trailing spaces
         .lower()                 # normalize case
         .replace("  ", " ")      # collapse double spaces
         .replace('"', '')            # remove quotation marks
         .replace("\u00a0", " ")  # remove non-breaking spaces
    )

all_strings = pd.concat([
    cleaned_Q3P3_1,
    cleaned_Q3P3_2,
    cleaned_Q3P3_3
], ignore_index=True)

normalized_strings = all_strings.astype(str).apply(normalize)
unique_strings = sorted(set(normalized_strings))

# Save to CSV
pd.Series(unique_strings).to_csv(localpath+"cleaned_Q3P3_What_strings.csv", index=False)

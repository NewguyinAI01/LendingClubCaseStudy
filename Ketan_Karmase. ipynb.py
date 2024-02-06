#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd # Importing the pandas in python


# In[19]:


LC = pd.read_csv('loan.csv')  # Fetching the csv file in python to analyze

# df = pd.read_csv('nba.csv', low_memory=False)


# In[20]:


LC = pd.read_csv('loan.csv', low_memory =False) # As memory error got so low_memory = False syntax used


# In[21]:


LC # Loan Calculation # Displaying the file to make sure correctly imported.


# In[22]:


LC.shape # Total rows and columns


# In[23]:


len(LC)


# In[24]:


LC.isna().sum()


# In[25]:


LC.term.value_counts() # value_counts to check how many entries are in each term value.


# In[26]:


LC.application_type.value_counts() # All the applications are of individual


# In[27]:


LC.grade.value_counts() # Nothing to check here.


# In[28]:


LC.int_rate.value_counts() 


# In[29]:


LC.last_pymnt_amnt.value_counts()


# In[30]:


LC.home_ownership.value_counts()


# In[31]:


LC.dtypes


# In[32]:


import seaborn as sns # seaborn lib imported


# In[33]:


import warnings


# In[34]:


#df['values'] = df['values'].apply(lambda x: float(''.join(filter(str.isdigit, x))) if not x.

LC ['values'] = LC['values'].apply(lambda x: float(''.join(filter(str.isdigit, x)))) if not x


# In[35]:


LC.drop(['id', 'member_id', 'loan_amnt','funded_amnt', 'funded_amnt_inv', 'tax_liens'], axis = 1)


# In[36]:


LC1 = LC.drop(['tot_hi_cred_lim', 'total_bal_ex_mort', 'total_bc_limit','total_il_high_credit_limit' ], axis = 1)


# In[37]:


LC1 # From LC to LC10 all new variables used to remove certain fields. Finally LC11 is being used.


# In[38]:


LC2 = LC1.drop(['grade','num_rev_tl_bal_gt_0', 'num_sats','num_tl_120dpd_2m','num_tl_30dpd','num_tl_90g_dpd_24m','num_tl_op_past_12m','pct_tl_nvr_dlq','percent_bc_gt_75',], axis = 1)


# In[39]:


LC2


# In[40]:


LC3 = LC2.drop(['sub_grade','num_accts_ever_120_pd','num_actv_bc_tl','num_actv_rev_tl','num_bc_sats','num_bc_tl','num_il_tl','num_op_rev_tl','num_rev_accts',], axis = 1)


# In[41]:


LC3


# In[42]:


LC4 = LC3.drop(['mo_sin_old_rev_tl_op', 'mo_sin_rcnt_rev_tl_op', 'mo_sin_rcnt_tl','mort_acc', 'mths_since_recent_bc','mths_since_recent_bc_dlq', 'mths_since_recent_inq', 'mths_since_recent_revol_delinq'], axis = 1)


# In[43]:


LC4


# In[44]:


LC5 = LC4.drop(['inq_last_12m','acc_open_past_24mths','avg_cur_bal','bc_open_to_buy','bc_util','mo_sin_old_il_acct'], axis = 1)


# In[45]:


LC5


# In[46]:


LC6 = LC5.drop(['open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl',], axis = 1)


# In[47]:


LC6


# In[48]:


LC7 = LC6.drop(['open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m' ], axis = 1)


# In[49]:


LC7


# In[50]:


LC8 = LC7.drop(['verification_status_joint', 'acc_now_delinq', 'tot_coll_amt', 'tot_cur_bal', 'open_acc_6m', 'open_il_6m' ], axis = 1)


# In[51]:


LC8


# In[52]:


LC9 = LC8.drop(['mths_since_last_major_derog', 'annual_inc_joint', 'dti_joint', 'pub_rec_bankruptcies', 'tax_liens','chargeoff_within_12_mths' ], axis = 1)


# In[53]:


LC9


# In[54]:


LC10 = LC9.drop([ 'delinq_amnt', 'collections_12_mths_ex_med', 'policy_code', 'application_type'], axis = 1)


# In[55]:


LC10


# In[56]:


LC10 = LC9.drop(['next_pymnt_d', 'collection_recovery_fee' ], axis = 1)


# In[57]:


LC10


# In[58]:


LC11 = LC10.drop(['member_id', 'id' ], axis = 1)


# In[59]:


LC11


# In[60]:


pd.set_option('display.max_columns', None)


# In[61]:


LC11.head(2)


# In[62]:


LC11.describe()


# In[63]:


LC11.head(4)


# In[64]:


pd.crosstab(LC11['loan_status'], LC11['emp_title'])

# Analyzed what is the trend depend on employeers for loan repayment.


# In[65]:


pd.crosstab(LC11['loan_status'], LC11['verification_status'])

# Some employeers have higher number in fully paid for as follows: Accenture, Bank of America, Best Buy, Citigroup, 
# comcast. 
# Bank of America employees are among a category of charged off and fully paid. Need to check what is the cause.
# People from the employeers who are fully paying loans should be given preference over others, also there can be
# some plan introduced to increase customer base.


# In[66]:


import pandas as pd


# In[67]:


LC11


# In[68]:


pd.crosstab(LC11['loan_status'], LC11['term']) 
# Term of repayment has shows that more people are opting for lesser duration for loan repayment.
# Reason can be less interest


# In[69]:


pd.crosstab(LC11['loan_status'], LC11['term'])


# In[70]:





# In[72]:


pd.crosstab(LC11['term'], LC11['emp_title'])


# In[73]:


# This employeer wise analysis for loan repayment duration also proves that more people are option for lesser
# duration of loan repayment


# In[74]:


pd.set_option('display.max_columns', None)


# In[75]:


import matplotlib.pyplot as plt


# In[76]:


LC11['code']= pd.factorize(LC11.emp_title)[0]


# In[80]:


# New special schemes for loan can be introduced for US amry, Bank of America and IBM considering highest number
# of people repaid loan from these companies.


# In[81]:


pd.crosstab(LC11['loan_status'], LC11['annual_inc'])

# This shows that higher income of applicant has clear impact on loan repayment.


# In[82]:


pd.crosstab(LC11['loan_status'], LC11['purpose'])


# In[83]:


# Highest number of charged off is in debt_consolidation purpose. Strict background check is required in these cases.


# In[84]:


import numpy as np


# In[85]:


LC11.dtypes


# In[86]:


x = LC11['loan_status']
y = LC11['purpose']


plt.xlabel('loan_status', fontsize = 30)
plt.ylabel('purpose', fontsize = 30)
plt.bar(x,y)

plt.show()


# In[87]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[89]:


sns.scatterplot(data=LC11, x = index, y = 'purpose', hue = LC11('last_credit_pull_d'))


# In[90]:


LC11.loc[0:10, 'term']


# In[92]:


LC11.loc[LC11['purpose']== 'debt_consolidation','loan_status']


# In[98]:


LC11['annual_inc'].median()


# In[104]:


LC11['total_acc'].median()


# In[106]:


LC11['term'].value_counts()


# In[107]:


LC11['loan_status'].value_counts()


# In[108]:


LC11['purpose'].value_counts() # highest number of loans were taken to pay of earlier loans followed by credit card


# In[109]:


LC11['emp_title'].value_counts() # largest employeer to whom loans were given is US army followed by Bank of America.
# Bank of America also has highest number who paid the loan correctly. So this employeer can be focused to give
# more loans. 


# In[110]:


LC11['purpose'].value_counts(normalize=True)


# In[112]:


Loan_Grp = LC11.groupby(['loan_status'])


# In[114]:


Loan_Grp.get_group('Charged Off')


# In[116]:


filt = LC11['loan_status'] =='Charged Off'
LC11.loc[filt]


# In[126]:


filt = LC11['loan_status'] =='Charged Off'
LC11.loc[filt]['emp_title'].value_counts(normalize=True)


# In[125]:


filt = LC11['loan_status'] =='Charged Off'
LC11.loc[filt]['purpose'].value_counts(normalize=True)


# In[123]:


filt = LC11['purpose'] =='debt_consolidation'
LC11.loc[filt]['loan_status'].value_counts(normalize=True)


# In[122]:


filt = LC11['purpose'] =='other'
LC11.loc[filt]['loan_status'].value_counts(normalize=True)


# In[128]:


filt = LC11['purpose'] =='small_business'
LC11.loc[filt]['loan_status'].value_counts(normalize=True)
# In case of small businesses 25 percent loans are charged off.Take care while giving loans to small businesses.


# In[129]:


filt = LC11['purpose'] =='major_purchase'
LC11.loc[filt]['loan_status'].value_counts(normalize=True)


# In[130]:


filt1= LC11['purpose'] =='other'
LC11.loc[filt1]


# In[133]:


filt1 = LC11['purpose'] =='other'
LC11.loc[filt]['title'].value_counts(normalize=True)

# Major purchase loans in other purpose loans has highest number of loan takers, so the uncategorized 15 percent
# of charged off loans has most number of major purchase loans which can be checked. 


# In[146]:


#home_ownership

filt = LC11['loan_status'] =='Charged Off'
LC11.loc[filt]['home_ownership'].value_counts(normalize =True)


# In[168]:


pd.crosstab(LC11['loan_status'], LC11['verification_status'])
# Applications who are verified have more charged offs and lesser fully paid compare to applications who are 
# not verified.


# In[170]:


pd.crosstab(LC11['purpose'], LC11['loan_status'])

# Highest number of charged_off are in small businesses.


# In[171]:


from matplotlib import style


# In[177]:


pd.crosstab(LC11['home_ownership'], LC11['loan_status'])

# Here almost all type of people have same percentage of defaulters.


# In[178]:


pd.crosstab(LC11['emp_length'], LC11['loan_status'])

# People whose employment length is more than 10 years have the highest number of charged offs.


# In[182]:


#annual_inc

pd.crosstab(LC11['term'], LC11['loan_status'])


# In[ ]:


# For the period of 60 months charged offs are more compare to ratio of fully pais and current figures of 36 months


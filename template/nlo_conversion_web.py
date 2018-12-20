# define dates & granularity
# dynamic dates ie 1 day 

start_date = (datetime.today() - timedelta(1)).strftime(format='%Y-%m-%d')
end_date = (datetime.today() - timedelta(1)).strftime(format='%Y-%m-%d')
granularity = 'day'



################## TOTAL WEB STARTS & COMPLETES

# App Starts
tot_nlo_start_rep = ReportDefinition(
    dimensions=[],
    metrics=[app_starts],
    segments=[web_hist, nlo_seg],
    date_from=start_date,
    date_to=end_date,
    granularity=granularity
)

# App Completes
tot_app_comp_rep = ReportDefinition(
    dimensions=[],
    metrics=[app_comp_corrected],
    segments=[web_hist],
    date_from=start_date,
    date_to=end_date,
    granularity=granularity
)
print('Total Web App Start/Complete reports created')

################## DESKTOP WEB 

# App Starts
dsk_nlo_start_rep = ReportDefinition(
    dimensions=[],
    metrics=[app_starts],
    segments=[web_hist, nlo_seg, desktop_devices, hist_corr_desk],
    date_from=start_date,
    date_to=end_date,
    granularity=granularity
)

# App Completes
dsk_app_comp_rep = ReportDefinition(
    dimensions=[],
    metrics=[app_comp_corrected],
    segments=[web_hist, desktop_devices, hist_corr_desk],
    date_from=start_date,
    date_to=end_date,
    granularity=granularity
)
print('Desktop Web App Start/Complete reports created')

################## MOBILE WEB

# App Starts
mob_nlo_start_rep = ReportDefinition(
    dimensions=[],
    metrics=[app_starts],
    segments=[web_hist, nlo_seg, mobile_devices],
    date_from=start_date,
    date_to=end_date,
    granularity=granularity
)

# App Completes
mob_app_comp_rep = ReportDefinition(
    dimensions=[],
    metrics=[app_comp_corrected],
    segments=[web_hist, mobile_devices],
    date_from=start_date,
    date_to=end_date,
    granularity=granularity
)
print('Mobile Web App Start/Complete reports created')





############## DOWNLOAD REPORT REQUESTS

#### TOTAL WEB

# App Starts
tot_nlo_start = dsk_suite.download(tot_nlo_start_rep)
# App completes
tot_app_comp = dsk_suite.download(tot_app_comp_rep)

# merge requests together
total_web_nlo = pd.merge(tot_nlo_start, tot_app_comp, how='left', on='Date')

# create % col
total_web_nlo['nlo_onversion'] = total_web_nlo['Application Complete (event43) - corrected'].astype(int) / total_web_nlo['App Starts'].astype(int)
total_web_nlo['report_type'] = 'total_web'

total_web_nlo.columns = ['date', 'app_starts', 'app_completes', 'nlo_conversion', 'report_type']

print('Total Web App Start/Complete Reports Downloaded')






#### DESKTOP WEB

# App Starts
dsk_nlo_start = dsk_suite.download(dsk_nlo_start_rep)
# App Completes
dsk_app_comp = dsk_suite.download(dsk_app_comp_rep)

# merge dfs together
dsk_web_nlo = pd.merge(dsk_nlo_start, dsk_app_comp, how='left', on='Date')

# create % col
dsk_web_nlo['nlo_onversion'] = dsk_web_nlo['Application Complete (event43) - corrected'].astype(int)/dsk_web_nlo['App Starts'].astype(int)
dsk_web_nlo['report_type'] = 'desktop_web'

dsk_web_nlo.columns = ['date', 'app_starts', 'app_completes', 'nlo_conversion', 'report_type']

print('Desktop Web App Start/Complete Reports Downloaded')





#### MOBILE WEB

# App Starts
mob_nlo_start = dsk_suite.download(mob_nlo_start_rep)
# App Completes
mob_app_comp = dsk_suite.download(mob_app_comp_rep)

# merge dfs together
mob_web_nlo = pd.merge(mob_nlo_start, mob_app_comp, how='left', on='Date')

# create % col
mob_web_nlo['nlo_onversion'] = mob_web_nlo['Application Complete (event43) - corrected'].astype(int)/mob_web_nlo['App Starts'].astype(int)
mob_web_nlo['report_type'] = 'mobile_web'

mob_web_nlo.columns = ['date', 'app_starts', 'app_completes', 'nlo_conversion', 'report_type']

print('Mobile Web App Start/Complete Reports Downloaded')

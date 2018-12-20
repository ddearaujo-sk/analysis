# iOS Suite
ios_suite = client.suites()['seekskiphoneprd']

# Android Suite
android_suite = client.suites()['vrs_seek1_androidwithlifecycle']



##### METRICS #####
# iOS

# iOS app starts
ios_app_start = ios_suite.metrics()['event5']

# 'NLO app start => app complete (iOS only)'
ios_app_cr = ios_suite.metrics()['cm200000660_58a232ba4f278f7e20c7029c']

# iOS app complete
ios_app_comp = ios_suite.metrics()['event1']

# Visits
ios_visit = ios_suite.metrics()['visits']

# Unique Visitors
ios_unique_visitor = ios_suite.metrics()['uniquevisitors']




# ANDROID

# event42 - Application Start Android
android_app_start = android_suite.metrics()['event42']

# 'Apps Completed (NonLinkOut) (event43)'
android_app_comp = android_suite.metrics()['event43']

# Visits (android adjusted) (Nov/Dec17) [Monthly]
android_visit = android_suite.metrics()['cm200000660_5a582fc35908010020890172']

# Unique Visitors
android_unique_visitor = android_suite.metrics()['uniquevisitors']



##### SEGMENTS #####
# iOS

# iOS NLO segment
ios_nlo_seg = ios_suite.segments()['s200000660_56f1ec73e4b0ff1f7e31de74']

# iOS: Historical data corrected
ios_hist_corrected = ios_suite.segments()['s200000660_5750043ee4b0761a9983e918']

# iOS: Logged in visits v2
ios_logged_in_visit = ios_suite.segments()['s200000660_5656852fe4b0491c0725c49b']



# ANDROID

# NLO segment
android_nlo_seg = android_suite.segments()['s200000660_572059a2e4b0031e240a6474']

# Android: Logged in visits
android_logged_in_visit = android_suite.segments()['s200000660_5656833fe4b080432935e359']

# Includes lifecycle
android_inc_lifecycle = android_suite.segments()['s200000660_590812e8e4b060c2f344ae77']
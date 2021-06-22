import subprocess,os,re

pattern_date = re.compile(r'^\d{4}.\d{2}.\d{2}')
pattern_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
pattern_time = re.compile("(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])")
pattern_on_preproc_headers = re.compile(r"[A-Z]{1}[a-z]{1}[A-Z]{1}[a-z]{3,9}[A-Z]{1}[a-z]{1,9}")
pattern_on_send_raw_data = re.compile(r"[A-Z]{1}[a-z]{1}[A-Z]{1}[a-z]{3,9}[A-Z]{1}[a-z]{1,9}[A-Z]{1}[a-z]{3}")
pattern_on_pass_through = re.compile(r"[A-Z]{1}[a-z]{1}[A-Z]{1}[a-z]{3}[A-Z]{1}[a-z]{6}")
pattern_on_send_raw_data = re.compile(r"[A-Z]{1}[a-z]{1}[A-Z]{1}[a-z]{3}[A-Z]{1}[a-z]{2}[A-Z]{1}[a-z]{3}")
pattern_on_url_map = re.compile(r"[A-Z]{1}[a-z]{1}[A-Z]{1}[a-z]{2}[A-Z]{1}[a-z]{2}")
pattern_method = re.compile(r"(\s[A-Z]{3,5}\s[;])")
pattern_post_method = re.compile(r"\s[P]{1}[A-Z]{3}\s")
pattern_head_method = re.compile(r"\s[H]{1}[A-Z]{3}\s")
pattern_stie_url = re.compile(r"\s[a-z]{3,10}\.[a-r]{1,20}\.[a-z]{3}\s")
pattern_resource_url =  re.compile(r"(\s[/]{1}.{1,25}.{1}.{1,10}.{1}[a-z]*[.][a-z]{1,10}\s)")
pattern_search_parameter_url = re.compile(r"\s\w{1,20}\S\W{1}\w{1,20}\W{1}\w{1,20}\S\w{1,20}\W[A-Z]{1}[a-z]{1,20}[A-I]{1,3}[=]\d{1,30}")
pattern_waf_action = re.compile(r"\s[A-Z]{1,10}[:]\s")
pattern_attack_alert = re.compile(r"(([A-Z]{1,20}[:])\s.{1,30}\s[;])")

log_file_1 = open('C:/Users/grayp/Desktop/Logs/SyslogCatchAll-2021-06-19.txt', 'r')
lines = log_file_1.readlines()
for line in lines:
    date = re.findall(pattern_date,line)
    time = re.findall(pattern_time,line)
    
    ip = re.findall(pattern_ip,line)
    print([date[0], ip[1]])
log_file_1.close()

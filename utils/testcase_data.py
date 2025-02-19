# Group post content/Discussion post content
import pathlib
from utils.openpyxlfunction import *

filepath = pathlib.Path(__file__).parent / "FacebookConfigFile.xlsx"
People_list_file_path = pathlib.Path(__file__).parent / "people_list.xlsx"
MessageFromExcel_sheet = "Messages"
People_list = "Peoplelist"
log = "log"
SearchKeyword_sheet = "searchkeywordforPeople"

# counterPath
counter_path = pathlib.Path(__file__).parent.parent / "testconf/counter.txt"

# conf file
group_post_message = readData(filepath, MessageFromExcel_sheet, 2, 2)
print(group_post_message)

# Search Keyword
SearchKeyword = readData(filepath, SearchKeyword_sheet, 6, 3)
# credential
account = ""
password = ""

# all sheet Name
others_portal = "Others"
job_portal = "Jobs"
internship_portal = "Internship"
php_portal = "Php"
ruby_portal = "Ruby"
Laravel_portal = "Laravel"
gcp_portal = "GCP"
redhat_portal = "Redhat"
aws_portal = "AWS"
django_portal = "Django"
devops_portal = "DevOps"
vacancy_portal = "Vacancy"
vue_portal = "Vue.JS"
python_portal = "Python"
react_portal = "ReactJS"
javascript_portal = "JavaScript"
node_portal = "NODE"
nodejs_portal = "NODEJS"
log = "Historyandlog"

from info import Info
from find import solution_number
from datetime import datetime
from data_handle import load_data_from_json
import pytz
from os.path import join,dirname


url_text_path = join(dirname(__file__),"url.txt")
with open(url_text_path,"r") as file:
    url = file.read()
time_zone = pytz.timezone("Asia/Dhaka")


def update_current_info():
    current_info = Info(solution_number(url),datetime.now(time_zone).strftime("%B"),datetime.now(time_zone).strftime("%d-%m-%Y %H:%M:%S"))
    return current_info

def update_previous_info(current_info):
    data = load_data_from_json()
    if "previous_info" not in data.keys() or data["previous_info"]["month"] != current_info.info["month"]:
        previous_info = Info(**current_info.info)
        return previous_info
    return Info(**data["previous_info"])
    
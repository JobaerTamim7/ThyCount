from rich.pretty import pprint
from update_info import update_current_info, update_previous_info,time_zone
from data_handle import dump_data_to_json
from datetime import datetime

def main():
    dumping_obj = {}
    info_currrent = update_current_info()
    info_prev = update_previous_info(info_currrent)
    dumping_obj.update({
    "current_info": info_currrent.info,
    "previous_info": info_prev.info,
    "mothly_solve_count": str(int(info_currrent.count) - int(info_prev.count)),
    "script_last_executed": str(datetime.now(time_zone))
    })
    dump_data_to_json(dumping_obj)
    pprint("Successfully wrote the JSON")
        
if __name__ == "__main__":
    main()

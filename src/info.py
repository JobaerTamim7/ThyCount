class Info:
 
    def __init__(self,count:int,month:str,time_stamp) -> None:
        self.count = count
        self.month = month
        self.time_stamp = time_stamp
        self.info = self._set_info()

    def _set_info(self):
        return {
            "month" : self.month,
            "count" : self.count,
            "time_stamp" : self.time_stamp
        }
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_t = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if not message in self.msg_t:
            self.msg_t[message] = timestamp
            return True
        else:
            if timestamp >= self.msg_t[message] + 10:
                self.msg_t[message] = timestamp
                return True
            else:
                return False


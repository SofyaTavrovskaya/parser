#!/usr/bin/python3


class LogEntry:
    def __init__(self, asctime, msecs, process, levelname, name, request_id, user_identitys, instance, message):
        """
        Create class LogEntry
        :param asctime:
        :param msecs:
        :param process:
        :param levelname:
        :param name:
        :param request_id:
        :param user_identitys:
        :param instance:
        :param message:
        """
        self.asctime = asctime
        self.msecs = msecs
        self.process = process
        self.levelname = levelname
        self.name = name
        self.request_id = request_id
        self.user_identitys = user_identitys
        self.instance = instance
        self.message = message

    def __repr__(self):
        return "Log object: asctime is %s, msecs is %s, process is %s, levelname is %s, " \
               "name is %s, request_id is %s, user_identitys is %s, instance is %s, message is %s" % \
               (self.asctime, self.msecs, self.process, self.levelname, self.name, self.request_id,
                self.user_identitys, self.instance, self.message)






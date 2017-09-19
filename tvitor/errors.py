class TRequestError(Exception):
    pass

class TUnsupportedError(Exception):
    pass

class TTwitterError(Exception):
    pass

class TConnectionError(Exception):
    pass

class TRCFileError(Exception):
    pass

class TError(Exception):
    """ Some unknown generic error. TODO something with it."""


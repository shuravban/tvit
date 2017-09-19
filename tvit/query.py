#!/usr/bin/python3

# standard modules
import sys
import os
import time

# logging
import logging as L
L.basicConfig(
    format='%(levelname)s: %(message)s')
# TODO
if os.environ.get('DEBUG', False):
    L.getLogger().setLevel(L.INFO)

# TwitterAPI
sys.path.insert(0, '../TwitterAPI')
import TwitterAPI as T

# my modules
import keys
# only exceptions are here
from error import *

class Query:
    def __init__(self, endpoint, params, user=None, rcfile=None, times=1):
        self.endpoint = endpoint
        self.params = params
        self.api = T.TwitterAPI(*keys.keys(user, rcfile))
        self.times = times

    def timed_query(self):
    # try execute the query and sleep 2^i seconds after Connection Error
    # (assume it is timed out), where i = 0, 1, 2... TIMES
        for i in range(self.times-1):
            try:
                return self.query()
            except TConnectionError:
                L.info('Sleeping ' + str(2**i) + ' seconds')
                time.sleep(2**i)
        # the last attempt (it executes with any value of times)
        return self.query()

    def query(self):
        try:
            rst = self.api.request(self.endpoint, self.params)

            if rst.text.startswith('{"errors":'):
                err = rst.json()['errors'][0]
                raise TTwitterError('[%s]: %s' % (err['code'], err['message']))
            return rst

        # ???
        except TTwitterError as e:
            raise e from None

        except T.TwitterRequestError as e:
            raise(TRequestError(*e.args)) from None

        except T.TwitterConnectionError as e:
            raise(TConnectionError(*e.args)) from None

        except Exception as e:
            s = str(e.args[0])
            if 'Endpoint' in s and 'unsupported' in s:
                raise TUnsupportedError(s)  from None
            else:
                raise e


if __name__ == '__main__':
    # just some testing code TODO remove
    e = 'account/verify_credentials'
    p = {}
    q = Query(e,p)
    L.info('start: ' + time.asctime())
    r = q.timed_query()
    print(r.json())

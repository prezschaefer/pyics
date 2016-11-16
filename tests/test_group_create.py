# Copyright 2016 Mathew Odden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import getpass
import logging

import pyics

try:
    import httplib
except ImportError:
    import http.client as httplib

# super debug mode - print all HTTP requests/responses
#httplib.HTTPConnection.debuglevel = 1


TEST_GROUP_NAME = 'pyics-test-group'


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--user', '-u',
                   required=True)
    p.add_argument('--space-id', '-s',
                   required=True)
    return p.parse_args()


def get_client():
    args = parse_args()
    passwd = getpass.getpass()
    client = pyics.Client(args.user, passwd, space_id=args.space_id)
    return client


def main():
    svc = get_client()

    try:
        group = svc.groups.show(TEST_GROUP_NAME)
    except Exception as ex:
        if ex.response.status_code == 404:
            group = None
        else:
            raise

    if group is None:
        print "Creating group '{0}'".format(TEST_GROUP_NAME)
        try:
            resp = svc.groups.create(
                name=TEST_GROUP_NAME,
                image='ibmliberty',
                port=9080,
                memory=128,
                number_instances={'Desired': 1,'Min': 1, 'Max': 2})
        except Exception as ex:
            print str(ex)
            print ex.response.text
            raise

        print resp

    print 'Listing groups...'
    print svc.groups.list()
    print "Finding group %s" % TEST_GROUP_NAME
    print svc.groups.show(TEST_GROUP_NAME)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()

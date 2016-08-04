# pyics
A pythonic API for interacting with the IBM Containers Service

[![Build Status](https://travis-ci.org/locke105/pyics.svg?branch=master)](https://travis-ci.org/locke105/pyics)

# Using

The main entity in the API is the `Client` object in the `pyics` module.

The following example shows how to get a `Client` and do some group manipulation.

```python
>>> import pyics
>>> client = pyics.Client(
...    username='some.bluemix.user@example.org',
...    passwd='supersecretpassword',
...    space_id='deadbeefabc123415123')
>>> client.groups.list()
[]
>>> client.groups.create(
...     name='mygroup',
...     image='ibmliberty',
...     port=9080,
...     memory=128,
...     number_instances={'Desired': 1, 'Min': 1, 'Max': 2})
>>> client.groups.list()
[{u'Status': u'CREATE_COMPLETE', u'Name': u'mygroup', u'Port': 9080, ...}]
>>> client.groups.show('mygroup')
{u'AntiAffinity': False, u'Status': u'CREATE_COMPLETE', ...}
>>> client.groups.delete('mygroup')
```

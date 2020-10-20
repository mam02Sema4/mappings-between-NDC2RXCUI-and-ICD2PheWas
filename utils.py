# !/usr/bin/python
# -*- coding: utf-8 -*-
import pickle as pkl
import json


def text_load(ifn):
    with open(ifn, "r") as f:
        text = f.read()
    return text


def text_dump(text, ofn):
    with open(ofn, "w") as f:
        f.write(text)


def pkl_load(ifn):
    with open(ifn, "rb") as f:
        pdata = pkl.load(f)
    return pdata


def pkl_dump(pdata, ofn):
    with open(ofn, "wb") as f:
        pkl.dump(pdata, f, protocol=pkl.HIGHEST_PROTOCOL)


def json_load(ifn):
    with open(ifn, "r") as f:
        jdata = json.load(f)
    return jdata


def json_dump(jdata, ofn):
    with open(ofn, "w") as f:
        json.dump(jdata, f, indent=2)

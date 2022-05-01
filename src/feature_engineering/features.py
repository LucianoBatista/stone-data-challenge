import pandas as pd


def total_success_dsp5(data: pd.Series):
    # your data must have the dsp column
    dsp_list = data.to_list()

    success_dsp5 = 0
    total_dsp5 = 0

    for i, item in enumerate(dsp_list):
        if item == 5:
            total_dsp5 += 1
            new_list = dsp_list[i : i + 6]
            for j, item in enumerate(new_list):
                try:
                    if new_list[j + 1] == 0:
                        success_dsp5 += 1
                        break
                except IndexError:
                    continue

    if total_dsp5 != 0:
        prop_dsp5 = success_dsp5 / total_dsp5
    else:
        prop_dsp5 = None

    return prop_dsp5


def total_success_dsp10(data: pd.Series):
    # your data must have the dsp column
    dsp_list = data.to_list()

    success_dsp10 = 0
    total_dsp10 = 0

    for i, item in enumerate(dsp_list):
        if item == 10:
            total_dsp10 += 1
            new_list = dsp_list[i : i + 11]
            for j, item in enumerate(new_list):
                try:
                    if new_list[j + 1] == 0:
                        success_dsp10 += 1
                        break
                except IndexError:
                    continue

    if total_dsp10 != 0:
        prop_dsp10 = success_dsp10 / total_dsp10
    else:
        prop_dsp10 = None

    return prop_dsp10


def total_success_dsp15(data: pd.Series):
    # your data must have the dsp column
    dsp_list = data.to_list()

    success_dsp15 = 0
    total_dsp15 = 0

    for i, item in enumerate(dsp_list):
        if item == 15:
            total_dsp15 += 1
            new_list = dsp_list[i : i + 16]
            for j, item in enumerate(new_list):
                try:
                    if new_list[j + 1] == 0:
                        success_dsp15 += 1
                        break
                except IndexError:
                    continue

    if total_dsp15 != 0:
        prop_dsp15 = success_dsp15 / total_dsp15
    else:
        prop_dsp15 = None

    return prop_dsp15


def total_success_dsp30(data: pd.Series):
    # your data must have the dsp column
    dsp_list = data.to_list()

    success_dsp30 = 0
    total_dsp30 = 0

    for i, item in enumerate(dsp_list):
        if item == 30:
            total_dsp30 += 1
            new_list = dsp_list[i : i + 31]
            for j, item in enumerate(new_list):
                try:
                    if new_list[j + 1] == 0:
                        success_dsp30 += 1
                        break
                except IndexError:
                    continue

    if total_dsp30 != 0:
        prop_dsp30 = success_dsp30 / total_dsp30
    else:
        prop_dsp30 = None

    return prop_dsp30


def total_success_dsp60(data: pd.Series):
    # your data must have the dsp column
    dsp_list = data.to_list()

    success_dsp60 = 0
    total_dsp60 = 0

    for i, item in enumerate(dsp_list):
        if item == 60:
            total_dsp60 += 1
            new_list = dsp_list[i : i + 61]
            for j, item in enumerate(new_list):
                try:
                    if new_list[j + 1] == 0:
                        success_dsp60 += 1
                        break
                except IndexError:
                    continue

    if total_dsp60 != 0:
        prop_dsp60 = success_dsp60 / total_dsp60
    else:
        prop_dsp60 = None

    return prop_dsp60


def total_success_dsp90(data: pd.Series):
    # your data must have the dsp column
    dsp_list = data.to_list()

    success_dsp90 = 0
    total_dsp90 = 0
    for i, item in enumerate(dsp_list):
        if item == 90:
            total_dsp90 += 1
            new_list = dsp_list[i:]
            for j, item in enumerate(new_list):
                try:
                    if new_list[j + 1] == 0:
                        success_dsp90 += 1
                        break
                except IndexError:
                    continue

    # cases where we don't have communication
    if total_dsp90 != 0:
        prop_dsp90 = success_dsp90 / total_dsp90
    else:
        prop_dsp90 = None

    return prop_dsp90

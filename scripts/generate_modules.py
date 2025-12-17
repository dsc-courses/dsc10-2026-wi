# generate_modules.py
# Use this to convert from the course calendar spreadsheet to modules that work with the course website template.
# Only run it on the weeks that haven't occurred yet, otherwise it'll erase any manual work.
# Run from the scripts folder.

import pandas as pd
import os
import sys
import numpy as np

# Edit these variables before running script
CSV_PATH = "/Users/katefeng/Desktop/dsc10-2025-fa/scripts/Lecture Schedule – DSC 10, Fall 2025 - fa25.csv"  #CHANGE CSV PATH for your computer
DATE_FORMAT = "DATE MONTH/DAY"
YEAR = 2025
START_FROM_WEEK = 0 #only future weeks!


def fill_missing_vals(df):
    df["Week"] = df["Week"].fillna(method="ffill").astype(int)
    df["Title"] = df["Title"].fillna(method="ffill").astype(str)
    df["LectureNum"] = df["LectureNum"].fillna(0).astype(int)
    df["Lecture"] = df["Lecture"].fillna("").astype(str)
    df["Lab"] = df["Lab"].fillna("").astype(str)
    df["Homework"] = df["Homework"].fillna("").astype(str)
    df["Readings"] = df["Readings"].fillna("").astype(str)
    df["Links"] = df["Links"].fillna("").astype(str)
    df["Keywords"] = df["Keywords"].fillna("").astype(str)
    df["Discussion"] = df["Discussion"].fillna("").astype(str)
    df["Quiz"] = df["Quiz"].fillna("").astype(str)
    df["Survey"] = df["Survey"].fillna("").astype(str)
#    df["Practice"] = df["Practice"].fillna("").astype(str)
    return df


df = pd.read_csv(CSV_PATH).rename(columns={"#": "LectureNum"}).pipe(fill_missing_vals)
df


month_map = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sept": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def round_format(i):
    return "0" + str(i) if int(i) <= 9 else str(i)


def date_conv(date):
    if DATE_FORMAT == "DATE. MONTH. DAY":
        try:
            _, month, day = date.split(" ")
        except TypeError:
            print(date)

        month = month_map[month]
        month = round_format(month)
        day = round_format(day)

    elif DATE_FORMAT == "MONTH/DAY":
        try:
            month, day = date.split("/")
        except TypeError:
            print(date)

    elif DATE_FORMAT == "DATE MONTH/DAY":
        date = date.split(" ")[1]
        try:
            month, day = date.split("/")
        except TypeError:
            print(date)

    elif DATE_FORMAT == "MONTH/DAY/YEAR":
        try:
            [month, day, _] = date.split("/")
        except TypeError:
            print(date)

    return f"{YEAR}-{month}-{day}"


def has_content(row):
    return row.loc[["Lecture", "Homework", "Lab", "Discussion", "Quiz"]].any() != ''

# for a single week
def write_week(i, dest="/Users/katefeng/Desktop/dsc10-2025-fa/_modules", write=True):  #CHANGE dest to path where "_modules" is on your computer
    week = df.query("Week == @i")
    week = week[week.apply(has_content, axis=1)] 

    outstr = f"""---
title: Week {i} – {week["Title"].iloc[0]}
weekNumber: {i}
days:"""

    for day in week.itertuples(index=False):
        date = day.Date
        lec_num = day.LectureNum
        lecture = day.Lecture
        homework = day.Homework
        lab = day.Lab
        readings = day.Readings
        links = day.Links
        keywords=day.Keywords
        discussion = day.Discussion
        quiz = day.Quiz
        survey = day.Survey
        #practice = day.Practice

        date_formatted = date_conv(date)

        outstr = outstr.rstrip()
        outstr += f"""
    - date: {date_formatted}
      events: """

        # Lecture number
        if lec_num != 0:
            outstr += f"""
        - name: LEC {lec_num}
          type: lecture
          title: {lecture}
          url:
          html:
          podcast:
          readings: """

            outstr = outstr.rstrip()
            read_str = "\n"
            if readings:
                readings_list = readings.split(", ")
                links_list = links.split(", ")
                num_readings = len(readings_list)
                for j in range(num_readings):
                    read_str += f"""            - name: {readings_list[j]}\n"""
                    read_str += f"""              url: {links_list[j].strip('#')}\n"""
                outstr += f"""{read_str}"""
                
            if keywords:
                outstr += f"""          keywords: {keywords}"""
                
        else:
            if lab:
                lab_num, lab_name = lab.split(". ")
                outstr = outstr.rstrip()
                outstr += f"""
        - name: LAB {lab_num}
          type: lab
          title: {lab_name}
          url: """

            elif "Exam" in lecture:
                outstr += f"""
        - name: EXAM
          type: exam
          title: <b>{lecture}</b>"""
            elif lecture:  # we reach this when we have holidays, like July 4
                outstr += f"""
        - markdown_content: <b>{lecture}</b>"""

        if homework:
            outstr = outstr.rstrip()
            if "Project" in homework:
                outstr += f"""
        - name: PROJ
          type: proj
          title: {homework.strip()}
          url: """
            else:
                hw_num, hw_name = homework.split(". ", 1)
                outstr += f"""
        - name: HW {hw_num}
          type: hw
          title: {hw_name.strip()}
          url: """

        if discussion:
            disc_num, disc_name = discussion.split(". ")
            outstr = outstr.rstrip()
            outstr += f"""
        - name: DISC {disc_num}
          type: disc
          title: {disc_name}
          url: """
            
        if survey:
            if '[' in survey and ']' in survey:
                survey_name, survey_link = survey.split('](')
                survey_name = survey_name[1:]
                survey_link = survey_link[:-1]
                outstr += f"""
        - name: SUR
          type: survey
          title: {survey_name}
          url: {survey_link}"""
            else: 
                outstr += f"""
        - name: SUR
          type: survey
          title: {survey}
          url: """
            
        #if practice:
        #    outstr += f"""
        #  "**PRAC**{{: .label .label-practice }} [Extra Practice Session](http://practice.dsc10.com)":"""
            
        if quiz:
            quiz_num, quiz_description = quiz.split(". ", 1)
            outstr += f"""
        - name: QUIZ {quiz_num}
          type: quiz
          title: {quiz_description}"""

    outstr = outstr.rstrip()
    outstr += "\n---"

    if write:
        # if not dest in os.listdir():
        #     os.system(f'mkdir {dest}')

        # print(dest + '/week-' + round_format(i) + '.md')

        f = open(dest + "/week-" + round_format(i) + ".md", "w")
        f.write(outstr)
        f.close()
    else:
        return outstr


for i in range(START_FROM_WEEK, 11):
    write_week(i)





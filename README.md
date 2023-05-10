# jotb-2023-hackathon
Repository for the [2023 JOTB InterSystems ML Hackathon](https://2023.jonthebeach.com/workshops/Intersystems-Hackathon).

Team 3: **Corner Squad Wizards**

Project name: **Loan_Approval**

## Description
This tool aims to predict whether to give loans to people, based on historical records.

## Model
We trained logistic model using [InterSystems IRIS Data Platform](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls)

## Dataset
We fed our model using the Kaggle [All Lending Club loan dataset](https://www.kaggle.com/code/faressayah/lending-club-loan-defaulters-prediction/input?select=lending_club_loan_two.csv)

## Installing
run the command
```
pip install -r requirements.txt
```

## Running
```
streamlit run src/Loan_Approval.py
```
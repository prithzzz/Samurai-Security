# SentinalAI

## **_Problem statemement_** 
_A scanning tool that audits AI/ML models and pipelines for security flaws, privacy risks, and bias issues. It produces a risk score and actionable remediation report for each model._

## **_Problem Solution_**

An AI model with _security flaws_ refers to all those vulnerabilities which a AI/ML Model faces , for instance 

1. **_Adversarial Attacks_** : where inputs from users are crafted in such a way so as to fool a model , 

2. **_Model Inversion_** : An attacker asks the model repeatedly to reverse engineer or revert its training data , these cases are extremely dangerous if the Model was trained on private and confidential records , someone can extract these by cleverly playing around a model. 

3. **_Data Poisoning_** : Where an attacker injects certain malicious data that creates anomalities in your own data 

4. **_Prompt Injections_** : where an attacker embedds instrutions inside inputs which override the model's intended behavior

5. **_Privacy Risks_** : where an attacker can basically determine everything about a user or about the model's training data , which may include confidential information 

6. **_Bias Issues_** : Training data bias to check if theres any sort of discrimination or hatred against a said community , Label bias from attackers where an attacker labels a certain community with a certain label etc

A **_ML Pipeline_** is in essence an end to end system around any given model , which starts all the way from taking in ```data-> preprocessing -> training over said data -> evaluation -> deployment..``` . And in all these stages , some kind of flaws or mis-information my persist!

## **_Project Proposal_** : **_SentinelAI_** 

 **_Sentinel_** is a _Security testing framework for AI-Models_ . 

 Sentinel looks for ```flaws in security``` of a said AI Model , it checks for ```Risks in Privacy``` , checking how ```Biased``` the model is , and etc.. 

 In general Sentinel is a _AI Tool_ that stress-tests AI Models for certain malicious or ```harmful prompt injections , data leakages and bias```. 

## **_Tech Stack_** 
1. **_Backend_** : _Flask_
2. **_AI_** : _OpenAI_
3. **_Frontend_** : _React_

## **_Project Architecture_** 
```
SentinelAI/
│
├── frontend/                  ← Person A (Frontend)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── InputBox.jsx
│   │   │   ├── AttackResults.jsx
│   │   │   ├── RiskDashboard.jsx
│   │   │   └── Loader.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   └── package.json
│
├── backend/                   ← Person B (Backend)
│   ├── app.py
│   ├── routes/
│   │   └── analyze.py
│   │
│   ├── services/
│   │   ├── attack_engine.py   ← Person C (AI)
│   │   ├── scoring.py         ← Person D
│   │   └── report.py          ← Person D
│   │
│   ├── models/
│   │   └── schema.py
│   │
│   └── requirements.txt
│
├── data/                      ← Person C
│   └── attack_prompts.json
│
├── docs/                      ← Person D
│   └── evaluation_metrics.md
│
└── README.md
```

## **_Project Implementation Schema_** 

### 1. **_Frontend UI_** : 
- **_Input Page_** : 
- **_Results Page_** : 
- **_DashBoard Page_** : 

### 2. **_Backend API_** : 
- 

### 3. **_Attack/Defense Logic_** : 






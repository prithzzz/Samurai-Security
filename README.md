# Samurai Security

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
model-scanner/
│
├── frontend/                          # 🟣 MEMBER A (UI Layer)
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   ├── icons/
│   │   │   └── images/
│   │   │
│   │   ├── components/                # Reusable UI
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── RiskCard.jsx
│   │   │   ├── AttackCard.jsx
│   │   │   ├── Chart.jsx
│   │   │   ├── Loader.jsx
│   │   │   └── Modal.jsx
│   │   │
│   │   ├── pages/                     # Screens
│   │   │   ├── Dashboard.jsx
│   │   │   ├── ScanPage.jsx
│   │   │   ├── Simulation.jsx
│   │   │   ├── Comparison.jsx
│   │   │   └── Report.jsx
│   │   │
│   │   ├── services/                  # API calls
│   │   │   └── api.js
│   │   │
│   │   ├── hooks/
│   │   │   └── useScan.js
│   │   │
│   │   ├── context/
│   │   │   └── ScanContext.jsx
│   │   │
│   │   ├── utils/
│   │   │   └── helpers.js
│   │   │
│   │   ├── styles/
│   │   │   └── global.css
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── backend/                           # 🔴 CORE BACKEND SYSTEM
│   │
│   ├── app/
│   │   ├── main.py                    # FastAPI entry
│   │   ├── config.py                  # Configs
│   │   │
│   │   ├── routes/                    # API Layer (Integration)
│   │   │   ├── scan_routes.py
│   │   │   ├── report_routes.py
│   │   │   └── health_routes.py
│   │   │
│   │   ├── core/                      # 🔴 PERSON B
│   │   │   ├── input_layer/
│   │   │   │   └── model_loader.py
│   │   │   │
│   │   │   ├── attack_generator/
│   │   │   │   ├── prompt_templates.py
│   │   │   │   ├── multi_agent.py
│   │   │   │   └── attack_builder.py
│   │   │   │
│   │   │   ├── adversarial_engine/
│   │   │   │   ├── mutation_engine.py
│   │   │   │   └── evolution.py
│   │   │   │
│   │   │   ├── simulator/
│   │   │   │   ├── conversation_simulator.py
│   │   │   │   └── memory_handler.py
│   │   │   │
│   │   │   ├── execution/
│   │   │   │   └── model_executor.py
│   │   │   │
│   │   │   └── pipeline_B.py            # 🔥 Person B orchestrator
│   │   │
│   │   ├── evaluation/                # 🔵 PERSON C
│   │   │   ├── judge/
│   │   │   │   └── llm_judge.py
│   │   │   │
│   │   │   ├── leakage/
│   │   │   │   ├── embedding_model.py
│   │   │   │   └── leakage_detector.py
│   │   │   │
│   │   │   ├── bias/
│   │   │   │   └── bias_detector.py
│   │   │   │
│   │   │   ├── memory_attack/
│   │   │   │   └── memory_detector.py
│   │   │   │
│   │   │   ├── jailbreak/
│   │   │   │   └── jailbreak_detector.py
│   │   │   │
│   │   │   └── pipeline_C.py            # 🔥 Person C orchestrator
│   │   │
│   │   ├── risk/                      # 🟢 PERSON D
│   │   │   ├── scoring/
│   │   │   │   └── risk_engine.py
│   │   │   │
│   │   │   ├── breakdown/
│   │   │   │   └── risk_breakdown.py
│   │   │   │
│   │   │   ├── owasp/
│   │   │   │   └── owasp_mapper.py
│   │   │   │
│   │   │   ├── consistency/
│   │   │   │   └── consistency_checker.py
│   │   │   │
│   │   │   ├── reporting/
│   │   │   │   └── report_generator.py
│   │   │   │
│   │   │   └── pipeline_D.py            # 🔥 Person D orchestrator
│   │   │
│   │   ├── schemas/                   # Shared contracts
│   │   │   ├── attack_schema.py
│   │   │   ├── evaluation_schema.py
│   │   │   └── report_schema.py
│   │   │
│   │   ├── database/                  # (Optional but impressive)
│   │   │   ├── db.py
│   │   │   └── models.py
│   │   │
│   │   ├── utils/
│   │   │   ├── logger.py
│   │   │   ├── helpers.py
│   │   │   └── constants.py
│   │
│   ├── tests/
│   │   ├── test_core.py
│   │   ├── test_evaluation.py
│   │   └── test_risk.py
│   │
│   ├── requirements.txt
│   └── run.sh
│
├── datasets/                          # 📊 SHARED (ALL MEMBERS)
│   ├── owasp_llm_top10.json
│   ├── prompt_templates.json
│   └── sample_sensitive_data.json
│
├── docs/                              # 📄 Documentation
│   ├── architecture.md
│   ├── api_docs.md
│   └── workflow.md
│
├── .env
├── .gitignore
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






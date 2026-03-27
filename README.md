# PRAXIS 2026

> [Problem Statement]: 
> Develop a Model Scanner that inspects AI/ML models, configurations, and pipelines to detect security vulnerabilities, privacy risks, bias issues, and compliance gaps. The tool should generate a comprehensive risk assessment for each model.

>[Key Objectives] : 
> - Detect data leakage and prompt-injection risks
> - Identify insecure dependencies and configurations
> - Generate actionable risk mitigation recommendations 

>[Expected Output : ]
> - Model risk and vulnerability score 
> - Detailed Scan Report
______________________________________________________________
# Solution 

**_Introduction_** : LLM's are used in multiple field this day, 
We find them in Finance , we find them in Law , we find them in our own tech fields , we find them in Automobiles , in medicine and it is STILL expanding into a lot more fields. 

AI here acts as a personal assistant - it assists them in their day to day tasks , people ask questions , learn from the answers , people ask tasks , learn through the implementation , some people blindly use those implementations without any further research or clarification from their own end. 

Because of how widely AI and LLM's are used today , its also really easy for people to target it . Manipulate and Prompt an AI in harmful ways that it gives its users the wrong , biased , false and inaccurate outputs. 

## How is AI Being Manipulated and Altered : 
### **_1. Prompt Injections_**
  People inject Malicious prompts and codes into their inputs - which alter the whole working of a LLM , it starts behaving weirdly This is really really a alarming situation because it causes an AI to : 
    1. Violate their own guidelines 
    2. Enable unauthorized access
    3. generate harmful content
    4. influece critical decisions

Solutions for the same being: 
1. Constraining Model behavior
2. Define and validate expected output formats
3. Implement input and ouput filters
4. Require human approvals
5. Segregate and identify external content

## **_2. Sensitive Information Disclosure_** 

Sensitive information can affect both the LLM and its application context , this includes your personal information , financial , confidential data etc etc.

Common examples being : 
1. Personal information leakage
2. Proprietary algorithm exposure
3. sensitive data disclosure 

## **_3. Supply Chain_** 
 supply chains are also susceptible to various vulnerabilities , which can effect the training of data models , and deployment etc etc.

 ## **_4. Data and Model Poisoning_**
data poisoning occurs when pre-training, fine-tuning, or embedding data is manipulated to introduce vulnerabilities, backdoors, or biases

Thus Compromising your model's security , performance or ethical behavior leading to harmful outputs

## **_5.Vector and Embedding Weaknesses_** 

Vectors and Embedding vulnerabilities present a huge security risk in systems.

Risks in how vectors and embeddings are generated , stored or retreived can be exploited by malicious actions to inject harmful content and generate unsafe and sensitive information as output


## **_And the list just goes onn and onn and onn.._** 

Well then , whats a solution to this? 
An Antivirus , yes an antivirus but for LLM's that help us detect these issues in them early on before they head into the public and into the people, and so , we present to you 
 
# **_Samurai Secrity_**
## **_AI Security Testing & Risk Analysis Platform for LLMs_**

**_Samurai_** is an advanced system designed to ``test, evaluate, and secure Large Language Models (LLMs) against real-world vulnerabilities`` such as:

- Prompt Injection
- Data Leakage
- Jailbreak Attacks
- Bias & Unsafe Outputs
- Multi-turn Exploits

It simulates adversarial attacks, evaluates model behavior, and generates comprehensive risk reports , graphs , comparison analysis between the LLM's

## **_Key Features_** : 
### **_Core Attack Engine_**
- Multi-agent attack generation
- Prompt injection simulation
- Adversarial prompt evolution
- Multi-turn conversation simulation
- Model execution engine

### **_Evaluation Engine_**
- LLM-as-a-Judge evaluation
- Data leakage detection (embeddings)
- Bias detection system
- Memory attack detection
- Jailbreak detection

### **_Risk & Reporting_**
- Hybrid risk scoring
- Risk breakdown (Leakage, Bias, Jailbreak)
- OWASP LLM Top 10 mapping
- Response consistency testing
- Detailed scan reports

## **_System Architecture:_**
```
User Input
    ↓
Attack Generator (Core Engine)
    ↓
Conversation Simulator
    ↓
Model Execution
    ↓
Evaluation Engine
    ↓
Risk Scoring Engine
    ↓
Report Generation
    ↓
Frontend Dashboard
```
### **_Sample Output:_**
```
{
  "model": "llama2",
  "risk_score": 8.2,
  "status": "HIGH RISK",
  "issues": [
    "Prompt Injection",
    "Data Leakage"
  ],
  "recommendations": [
    "Add input validation",
    "Implement output filtering"
  ]
}
```





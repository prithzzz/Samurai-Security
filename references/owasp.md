# 1.Prompt Injection! 

A Prompt Injection Vulnerability occurs when a user gives weird prompts , those kinds of prompts which make the LLM act or respond in a unintended ways...basically like a super toxic friend...you knoww...like how his toxic statements kinda start impacting how you take decisions...similar way...

Now now , When it comes to AI , there prompts not necessarily be human readable , they can also be contents which **_only the model can understand_**

This is really really a alarming situation because it causes an AI to 
 1. Violate their own guidelines 
 2. Enable unauthorized access 
 3. genrate harmful content 
 4. influence critical decisions 

 While techniques like RAG (Retrieval-Augmented Generation) and other "fine tuning" process do take place , this still doesnt totally ignore the prompt injection vulnerabilities 

 If you'd ask me a "Book specific definition" , i'd say: 

 ```Prompt Injection``` -  involves manipulating model responses through specific inputs to alter its behavior

 ```JailBreaking``` -  is a form of prompt injection where the attacker provides inputs that cause the model to disregard its safety protocols entirely

 ## Types of Prompt Injection Vulnerabilities! 
 1. ``Direct Prompt Injections``
 2. ``Indirect Prompt Injections`` (LLM accepts input from external sources, such as websites or files.)
 
 ## Prevention and Mitigation Strategies 

1. ``Constrain Model Behavior`` : Provide specific instructions about the model's role and abilities . Enforce strict rules and context adherence and limit responses. Train and instruct it to ignore attempts to modify core instructions

2. ``Define and Validate expected output formats`` : 

3. ``Implement input and output filtering`` : 

4. ``Require human approval for high-risk actions``

5. ``Segregate and identify external content``

# 2. Sensitive Information Disclosure

Sensitive information can affect both the LLM and its application context , this includes your personal information , financial , confidential data etc etc. 

## Common examples includes : 

1. ``Personal Information Leakage``
2. `` Proprietary algorithm exposure`` 
3. ``Sensitive Data disclosure``

## Prevention And Mitigation Strategies! 
1. ``Integrate Data Sanitization Techniques`` - so as to prevent user data entering training model! , doing so by masking sensitive content before its used in training
2. ``Robust input validation``- applying struct methods and filters on inputs to remove all the harmful bits of it. 
3. ``restriction of Data sources and enforcing strict access controls``
4. ``Utilize Federated learning and incorporate differential policy`` - training models using decentralized data stored across multiple servers , reducing exposure risk , and applying techniques that add noise to data making it difficult for attackers to reverse engineer individual data points! 
5. ``LLM Transparency and educating users on safe LLM Useage``
6. ``Homomorphic encryption and tokenization and redaction`` - to enable secure data analysis and privacy preserving machine learning. Tokenization to preprocess and sanitize sensitive information. 

# 3. Supply Chain

LLM Supply chain (uhm , think this of like a series of steps that are done in order to make an LLM , starting from )
```
Gathering Data 
      |
      v
Model Training
      |
      v
Fine tuning 
      |
      v
   Hosting 
```

**OKAY COMING BACK** , these supply chains are also susceptible to various vulnerabilities , which can effect the training of data models , and deployment etc etc. 

These risks can later result into ```Biased outputs , security breaches or system failures``` 

Creating LLM's often depend on third party models..now if these models in itself have corrupted data ...then its ggs for the LLM 

Alongside this the rise of open access LLM's and and new ``"fine tuning"`` methods , on platforms like hugging face intoduces even more supply chain risks. 

## Common examples of Risks
1. ``Traditional Third-Party Package Vulnerabilities`` - using outdated or deprecated components which are easily you know prey to such exploits compromising LLM's

2. ```Licensing Risks``` - having strict useage , distribution and commercialization 

3. ``Vulnerable Pre-Trained Model`` - these can have hidden biases , backdoor's or other malicious features **NOT** identified through safety evaluations. 

## Prevention and Mitigation Strategies 
1. ``Carefully get your sources and data which you use to train your LLM``

2. ``Apply comprehensive AI Red Teaming and Evaluations when selecting a third party model`` - Basically stress testing a model yourself to see how long it takes it to go crazy lol 

3. ``Only use models from verifiable sources and use third-party model integrity checks ``

4. ``Implement strict monitoring and auditing practices for collaborative model development``

# Data and Model Poisoning 
_Soooooooooooo_ data poisoning occurs when  ```pre-training, fine-tuning, or embedding data``` is **_manipulated_** to introduce vulnerabilities, backdoors, or biases

Thus Compromising your model's security , performance or ethical behavior leading to harmful outputs 

### Data Poisoning can target the following LLM Stages : 
1. ```Pre-training```
2. ```Fine Tuning```
3. ``` embedding(text to numericals)``` 

Data poisoning is considered an integrity attack since tampering with training data impacts the model’s ability to make accurate predictions

## Common Examples of Vulnerabilities 

1. ```Malicious actors introduing harmful data during training leading to bias```

2. ```Attckers injecting harmful stfff directly```

3. ```Unverified training data```

```editors note : these are soo duhh like breh smh obvisouly dont use sus data```

## Prevention and Mitigation Strategies 

1. ```Track your data using tools like owasp and ml-bom , verify their legitimacy ```

2. ```Vet data vendors rigorously, and validate model outputs against trusted sources to detect signs of poisoning.```

3. ```strict sandboxing to limit model exposure to unverified data sources```

4. ```Tailor models for different use cases by using specific data sets```

5. ```Ensure sufficient controls to prevet model from accessing sus data```

6. ```Store user-supplied information in a vector database```

# 5. Improper Output Handling
Like the title says , not taking care of your LLM's output 

```Taking care``` as in insufficient validaton , sanitization and handling of the outputs generated by LLM before they are passed to other components and systems...

since LARGE portion of LLM generated content can be controlled by prompt input , this is similar to providng users an indirect access to additional functionality. 

Successful exploitation of an Improper Output Handling vulnerability can result in: 

**_XSS (cross site scripting eg stealing cookies)_**

**_CSRF(cross sit request forgery tricking browser to perform unwanted actions on different logged in website) web browsers as well as SSRF(same but on server side...)_**

**_privilege escalation, or remote code execution on backend systems_**

## Common Examples of Vulnerability 

1. ``LLM output is entered directly into system shell or similar , resulting in remote code execution``

2. ``JS or markdown is generated by LLM and returned to a sure , then interpreted by browser resulting in XSS``

3. ``LLM SQL Injections``

4. ``LLM Ouput is used to construct file paths without proper sanitization , resulting in path traversal vulnerabilities``

5. ``LLM-generated content is used in email templates without proper escaping, potentially leading to phishing attacks.``

## Prevention and Mitigation Strategies 

1. ``Treat the model like any other use , dont trust it , apply prper input validation on responses``

2. ``Follow OWASP to ensure secure input validation``

3. ``Encode model output back to users to mitigate undesired code by js or md``

4. ``implement context aware output encoding where LLM outout will be used``

5. ``Using parameterized queries and prepared statements``

6. ``Employ Strict Content Security Polices``

7. ``Implement robust logging and monitoring system to track unusual patterns in LLM``


# 6. Excessive Agency 
An LLM Based system is often granted a degree of agency by its developer , like an ability to call functions or interface with other systems via extensions to undertake actions in response to a prompt.

`` Example `` :  Agent-based systems will typically make repeated calls to an LLM using output from previous invocations to ground and direct subsequent invocations.

Excessive Agency is the vulnerability that enables damaging actions..to be performed in response to a manipulated output from an LLM

## Common Examples of Risks 

1. ``Excessive Functionality`` - LLM agent having access to a lot of extensions which include functions that are not needed for the intended operation. 

2. ``Excessive Permissions`` :
LLM extension that is designed to perform operations in the context of an individual user accesses downstream systems with a generic high-privileged identity

## Prevention and Mitigation Strategies 

1. ``Minimize extensions`` - Limit the extensions that LLM agents are allowed to call , make it as minimum and restricted to only necessary conditions 

2. ``Minimize extension functionality`` - Limit the functions that are implemented in LLM to the minimum necessary

3. ``Avoid Open Ended Extensions``

4. ``Minimize extension Permissions``

5. ``Execute extensions in users context``

6. ``Require User Approval``

# 7. System Prompt Leakage
Refers to the risk that the system prompts used to steer the behavior of the model can contain sensitive infomation that was not intended to be discovered. 

`` System prompts are designed to guide the model’s output based on the requirements of the application, but may inadvertently contain secrets. When discovered, this information can be used to facilitate other attacks.``

``Even if the exact wording is not disclosed, attackers interacting with the system will almost certainly be able to determine many of the guardrails and formatting restrictions that are present in system prompt language in the course of using the application, sending utterances to the model, and observing the results.``

## Common Examples of Risk

1. ``Exposure of Sensitive Functionality`` : The system prompt of the application , _may_ reveal sensitibe information or functionality that is meant to be kept confidential...these can be extracted by attackers to uk gain access into your application.

2. ``Exposing internal rules`` : again , comes under revealing information with respect to rules , especially rules of decision making processes which shud be kept confidential. 

3. ``Revealing of filtering criteria`` 

4. ``Disclosure of permissions and user roles`` : about inteernal role structures or permission levels of the application. 

## Prevention and Mitigation Strategies 
1. ``Separate sensitive data from systems prompts`` 

2. ``Avoid Reliance on System Prompts for Strict Behavior Control`` 

3. ``implement guardrails`` : train it in order to not reveal its system prompts , by implementing a system of guardrails 

# 8. Vector and Embedding Weaknesses 
Vectors and Embedding vulnerabilities present a huge security risk in systems. 

Risks in how vectors and embeddings are generated , stored or retreived can be exploited by malicious actions to inject harmful content and generate unsafe and sensitive information as output 

RAG is a model adaptation technique that enchances performance and contexttial revelance of responses from LLM's bycombining pre trained LLM with external knowledge sources 

## Common examples of risks
1. ``Unauthorized Access & Data Leakage``

2. ``Cross Context information leaks``

3. ``Embedding inversion attacks`` to recover significant amts of information , compromising data confidentiality 

4. ``Data Poisoning attacks``

5. ``Behavior attention``

## Prevention and Mitigation 

1. ``Permission and access control`` : fine-grained access controls and permission aware vector and embedding stores

2. ``Data validation and source authentication`` 

3. ``data reviewing``

4. ``Monitoring and Logging``


# 9. Misinformation 
This poses a core vulnerability for applications relying on these models. 

Misinformation occurs when an LLM produces false or misleading infomation that appears real , thus leading to risks like security breaches , reputational damage and legal liability 

One of the major causes of misinformation is hallucination - As in when the LLM generates conten tthat seems accurate but is fake and fabricated . Hallucinations occur when LLM's fill gaps in their training data using statistical patterns without understanding the content , which results in answers that sound correct but arent accurate or factual. 

Anothing related issue is ``overreliance`` , which occurs when the user places excessive trust in LLM Generated content , failing to verify its accuracy , this exacerbates the impact of misinformation , as users may integrate incorrect data into making important decisions without sufficient background


## Common examples of risk
1. ``Factual Inaccuracies`` : LLM gives you inaccurate outputs which you use to make super important decisions

2. ``unsupported claims`` : model generates baseless assumptionswhich can be harmful in sensitive contexts leading to legal / other issues 

3. ``misrepresentation of expertise`` : the model gives the illusion of understanding complex topics , misleading users regarding its level of expertise

4. ``Unsafe code generation`` : insecure or non existent code libraries are given as output which can introduce vulnerabilities when integrated with software systems. 

## Prevention and Mitigation Strategies : 

1. ``RAG's (Retrieval-Augmented Generation )`` : to enhance reliability of the model outputs but retreiving revelant and verified and accurate information from trusted sources 

2. `` Model Fine-Tuning`` : enchance the model with fine-tuning or embeddings to improve output quality , like PET (Parameter efficient tuning) and chain of thought prompting can help with reducing misinformation 

3. ``Cross Verification and Human Oversight`` : encouraging users to cross check LLM outputs with trust external sources to ensure the accuracy of information 

4. ``Automatic validation mechanisms`` : 

5. ``secure coding practices``

6. ``Training and education``

# 10. Unbounded Consumption 

The process where an LLM generates outputs based on input queries or prompts , by inferencing , which involves LLM to apply learned pattenrs of knowledge to produces revelannt responses or predictions 

## Common Examples of Vulnerability 

1. ``Variable Length Input Flood`` : attackers overload the LLM with multiple inputs of varying lengths , exploiting provessing inefficienes. This deplets resources and potentially render the system unresponsive. 

2. ``Denial of wallet`` : high volume operations , attackers exploit the cost per use model of cloud based AI models , leading to financial burdens on the provider 

3. ``Continuous flow overflow`` : sending inputs continuously that exceed the LLM's context window can lead to excessive resource use , leading to service degradation 

4. ``resource intensive queries`` : submitting unusually demanding queries involving complex sequences or intricate language patterns can drain system resources 

5. ``Model extraction via API , and functional Model replication `` 

## Prevention and Mitigation Strategies 

1. ``Input Validation``

2. ``Limit exposure of logits`` in api responses , provide only necessary information 

3. ``rate limiting`` : restrict the number of requests in a single source 

4. ``Resource allocation management`` : monitor and manage resources allocation dynamically t

5. ``Timeouts and throttling``

6. ``sandboxing``

7. ``access controls``










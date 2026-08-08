# NCLEX Ready, 10-Week Study and Content Plan

**70 topics. 7 posts a week. Mapped to the 2026 NCLEX-RN Test Plan, effective April 2026.**

Topic counts follow the blueprint's percentage midpoints, so the teaching schedule mirrors
what the exam weights. Every topic states Australian practice directly and carries a
verified free resource.

This file is generated. Edit `content/topics.py` and run `python3 build_calendar.py`.

## The eight templates, and the look each one wears

Art direction is assigned rather than rotated at random. Consistency builds recognition
faster than variety does, so a reference card always looks like a reference card and a
carousel always reads as one piece. The rule that matters most: never switch art
direction inside a carousel. Every slide in a single post must match.

| Template | Code | Art direction | Primary goal |
|---|---|---|---|
| Single-fact card | `fact` | Editorial | REACH |
| Question of the day | `qotd` | Midnight | COMMENT |
| Mnemonic card | `mnemonic` | Study Card | SAVE |
| Reference card | `ref` | Clinical Chart | SAVE |
| Comparison card | `compare` | Clinical Chart | SAVE |
| Drug card | `drug` | Study Card | SAVE |
| Australian practice card | `auvs` | Editorial | SHARE |
| Carousel (1 post, 5 slides) | `carousel` | Colour Block | SAVE + SHARE |

## Why the art directions are assigned this way

There are five art directions in `design/themes.py`. Two sensible ways to use them exist,
and this plan takes the second.

*Pick one and own it.* Consistency builds recognition fastest. Editorial or Study Card are
the most sustainable for daily posting, and if a week ever gets away from you, falling back
to a single theme is the safe move.

*Assign by purpose.* Midnight opens and carries anything you want to travel, because a dark
card in a feed of white ones stops a thumb. Clinical Chart takes reference and lab-value
content, since it is literally built from the observation chart. Colour Block takes the
carousel, where a solid field holds a five-slide set together. Editorial carries everyday
teaching, and Study Card carries the memory aids and drug cards because it looks like the
thing your audience already writes by hand.

That gives a feed rhythm without looking scattered, and it removes a decision from every
posting day. The mapping lives in `THEME_FOR_TEMPLATE` in `content/topics.py`, so the
generator picks it up with no flag needed:

```bash
python3 build_social.py --week 3            # a full week, each post in its assigned look
python3 build_social.py --week 3 --theme chart   # force one look, for a themed week
```

Across a typical week this produces roughly four Editorial cards, one or two Study Cards,
one Chart, and either a Midnight question or a Block carousel. Enough variety to keep a
grid interesting. Not so much that it stops looking like one account.

---

## Week 1: Thinking like a nurse, prioritisation and professional practice

*Funnel stage: TRUST. Sunday story: Introduce the 10-week syllabus and ask people to comment 'in' if they are starting with you. No link.*

### Monday · #1 · Mnemonic card · Study Card
**Prioritisation: why ABC beats everything else**

> When two patients both need you, the order is not a judgement call.

- Airway, then Breathing, then Circulation, ABC overrides Maslow whenever both apply.
- Unstable beats stable. A change in condition outranks an abnormal but stable baseline.
- Actual problems generally outrank potential ones, unless the potential problem is airway.
- Read the stem carefully: 'first' action and 'best' action are different questions.

**In Australia:** Australian emergency departments triage on the Australasian Triage Scale (ATS 1-5).

**Common trap:** Choosing the most thorough action when the question asked for the first action.

**Resource:** [ACSQHC: Recognising and responding to acute deterioration](https://www.safetyandquality.gov.au/our-work/recognising-and-responding-to-acute-deterioration)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 1`*

### Tuesday · #2 · Carousel (1 post, 5 slides) · Colour Block
**Delegation: what you can and cannot hand over**

> You can delegate the task. You can never delegate the accountability.

- Delegate only what sits inside the other person's role and competence, and needs no nursing judgement.
- Never delegate assessment, initial patient education, or a clinical judgement call.
- The RN stays accountable for the decision to delegate and for the supervision.
- Check the five rights: right task, circumstance, person, direction, supervision.

**In Australia:** Australia's skill mix is RN, Enrolled Nurse and Assistant in Nursing. An EN works under the direction of an RN and is implementation-focused, so an EN does not independently assess or plan care.

**Common trap:** Assuming an Enrolled Nurse can do an initial assessment because they are registered.

**Resource:** [NMBA: Enrolled Nurse Standards for Practice](https://www.nursingmidwiferyboard.gov.au/Codes-Guidelines-Statements/Professional-standards/enrolled-nurse-standards-for-practice.aspx)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 2`*

### Wednesday · #3 · Australian practice card · Editorial
**Scope of practice: the question to ask before you act**

> Scope is set by your education and competence, not by your job title.

- Scope of practice comes from education, competence, context and law together.
- If you are unsure whether something is in scope, seek supervision before acting, not after.
- 'I have seen other nurses do it' is never the test of whether you are authorised.
- Document the decision and who you consulted.

**In Australia:** Australia uses the NMBA's national Decision-Making Framework, a set of structured questions you work through before performing an activity, covering education, competence, authorisation and evidence.

**Common trap:** Treating a local ward habit as authorisation.

**Resource:** [NMBA: Decision-Making Framework](https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/frameworks.aspx)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 3`*

### Thursday · #4 · Mnemonic card · Study Card
**ISBAR: the handover structure that is mandated here**

> Most handover failures are missing the last letter.

- Identify, yourself, your role and the patient.
- Situation, why you are calling, right now, in one sentence.
- Background, only the history that bears on this problem.
- Assessment, your findings and observations.
- Recommendation, what you are actually asking for. Say it out loud.

**In Australia:** ISBAR is mandated nationally under NSQHS Standard 6 (Communicating for Safety) and is an accreditation requirement in Australian hospitals, so it is the expected structure for every escalation call.

**Common trap:** Leaving out the Recommendation and hoping the other person infers what you need.

**Resource:** [ACSQHC: ISBAR resources](https://www.safetyandquality.gov.au/publications-and-resources/resource-library/isbar-poster)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 4`*

### Friday · #5 · Single-fact card · Editorial
**Informed consent: whose job is it**

> The nurse witnesses consent. The nurse does not obtain it.

- Valid consent needs capacity, voluntariness, enough information, and it must be specific to the procedure.
- The person performing the procedure is responsible for obtaining consent.
- The nurse's role is to verify understanding and that the form is complete.
- Consent can be withdrawn at any time, including after the form is signed.

**In Australia:** There is no single national consent law in Australia. Each state and territory has its own guardianship and consent legislation, so capacity and substitute consent processes vary by jurisdiction.

**Common trap:** Proceeding because the form is signed, when the patient no longer understands what is planned.

**Resource:** [End of Life Law in Australia: Capacity and consent](https://end-of-life.qut.edu.au/treatment-decisions/adults/state-and-territory-laws)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 5`*

### Saturday · #6 · Question of the day · Midnight
**Advance care directives and who decides**

> The family disagrees with the directive. What happens?

- A valid advance care directive made while the person had capacity overrides family preference.
- With no directive, decisions pass to the legally recognised substitute decision-maker in order.
- A substitute decision-maker must act on the person's known wishes, not their own view.
- Next of kin is not automatically the legal decision-maker.

**In Australia:** Terminology is state-based: 'Person Responsible' in NSW, 'Medical Treatment Decision Maker' in Victoria, 'Enduring Guardian' elsewhere. There is no single national living-will equivalent.

**Common trap:** Following the loudest family member instead of the correctly ranked decision-maker.

**Resource:** [End of Life Law in Australia: State and territory laws](https://end-of-life.qut.edu.au/treatment-decisions/adults/state-and-territory-laws)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 6`*

### Sunday · #7 · Single-fact card · Editorial
**Advocacy: representing their wishes, not your opinion**

> Advocacy means their choice, even when you would choose differently.

- Advocacy is representing what the patient wants, not what you think is best for them.
- Support a competent adult's right to refuse treatment, and document it.
- Escalate unresolved safety concerns up the chain of command rather than working around them.
- Cultural safety is judged by the patient, not by the clinician.

**In Australia:** Cultural safety is an explicit obligation in the NMBA Code of Conduct, including a specific requirement to provide culturally safe care for Aboriginal and Torres Strait Islander Peoples.

**Common trap:** Overriding an informed refusal because you believe you are advocating for their health.

**Resource:** [NMBA: Code of Conduct for Nurses](https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/code-of-conduct.aspx)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 7`*

## Week 2: Legal, ethical and professional obligations

*Funnel stage: TRUST. Sunday story: Recap the week's four legal and professional posts in one frame. Ask what topic they want covered next. No link.*

### Monday · #8 · Single-fact card · Editorial
**Confidentiality: need-to-know, every time**

> No names in the lift. No details in the tearoom.

- Share information only with those involved in the person's care, only as far as needed.
- De-identified is not the same as unidentifiable, a detailed story can still identify someone.
- Never discuss patients on social media, even without a name.
- Patients generally have a right to access their own health record.

**In Australia:** Australia is governed by the Privacy Act 1988 and the Australian Privacy Principles, plus state health records legislation. My Health Record has its own access and consent rules.

**Common trap:** Assuming family have a right to information because they are next of kin.

**Resource:** [OAIC, Australian Privacy Principles](https://www.oaic.gov.au/privacy/australian-privacy-principles)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 8`*

### Tuesday · #9 · Comparison card · Clinical Chart
**Who to refer to, and when**

> Coordinating care is a skill the exam tests directly.

- Dietitian, nutrition risk, enteral feeding, malnutrition screening.
- Social worker, psychosocial need, housing, financial and discharge support.
- Physiotherapist and occupational therapist, mobility, function, equipment and home assessment.
- Pharmacist, medication reconciliation, interactions, discharge medicines.

**In Australia:** Community allied health is often accessed through a GP Chronic Disease Management Plan, which attracts Medicare rebates for a set number of sessions.

**Common trap:** Managing it yourself when a scope-appropriate referral is clearly indicated.

**Resource:** [Australian Government: My Health Record](https://www.myhealthrecord.gov.au)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 9`*

### Wednesday · #10 · Single-fact card · Editorial
**Discharge planning starts on admission**

> If discharge planning starts on discharge day, it has already failed.

- Begin planning at admission, not on the morning of discharge.
- Confirm the person understands medicines, follow-up and the red flags that mean 'come back'.
- Use teach-back, ask them to explain it to you, rather than asking 'do you understand?'.
- Check equipment and supports are actually in place before they leave.

**In Australia:** Aged care and disability supports are arranged through My Aged Care and the NDIS, with ACAT assessment determining aged-care eligibility.

**Common trap:** Recording education as complete because a pamphlet was handed over.

**Resource:** [My Aged Care](https://www.myagedcare.gov.au)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 10`*

### Thursday · #11 · Question of the day · Midnight
**Ethical conflict and conscientious objection**

> You object to the procedure. Can you step away?

- Autonomy generally prevails for a competent adult, even when the team disagrees.
- You may conscientiously object, but you must not abandon the patient, arrange handover of care.
- Resolve conflict through documented escalation, never unilateral action.
- Personal discomfort is not the same as a clinical reason to withhold care.

**In Australia:** Ethical obligations are codified nationally in the NMBA Code of Conduct, which applies in every state and territory.

**Common trap:** Withdrawing care without ensuring someone else has taken it over.

**Resource:** [NMBA: Code of Conduct for Nurses](https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/code-of-conduct.aspx)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 11`*

### Friday · #12 · Australian practice card · Editorial
**Mandatory notification: an obligation unique to here**

> In Australia, reporting an impaired colleague can be a legal duty.

- Notifiable conduct includes practising while intoxicated, sexual misconduct, significant departure from accepted standards, and impairment placing the public at substantial risk.
- This sits alongside, not instead of, state child protection reporting laws.
- Document objectively and factually. Never alter a record after an incident.
- Notification is about public risk, not punishment.

**In Australia:** AHPRA mandatory notification is a defined legal obligation on every registered practitioner in Australia, made directly to the regulator.

**Common trap:** Treating an impaired colleague as an internal HR matter only.

**Resource:** [AHPRA: Mandatory notifications](https://www.ahpra.gov.au/Notifications/mandatorynotifications.aspx)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 12`*

### Saturday · #13 · Single-fact card · Editorial
**Open disclosure: saying sorry is not admitting liability**

> Something went wrong. The patient is told, promptly, and honestly.

- Report incidents and near-misses regardless of whether harm occurred.
- Root cause analysis looks for system causes, not someone to blame.
- Open disclosure means an honest explanation, an apology, and what will change.
- Near-misses are reported precisely because no one was hurt this time.

**In Australia:** Open disclosure is a formal national requirement under the NSQHS Standards and the Australian Open Disclosure Framework. Under most state Civil Liability Acts an apology is not an admission of liability.

**Common trap:** Staying silent about a near-miss because the patient was not harmed.

**Resource:** [ACSQHC, Australian Open Disclosure Framework](https://www.safetyandquality.gov.au/our-work/open-disclosure/the-open-disclosure-framework)

*NCLEX category: Management of Care · practise in: Professional practice · generate: `--id 13`*

### Sunday · #14 · Mnemonic card · Study Card
**The 5 Moments for Hand Hygiene**

> Five moments. Most missed is the one after touching the surroundings.

- 1, before touching a patient.
- 2, before a clean or aseptic procedure.
- 3, after a body fluid exposure risk.
- 4, after touching a patient.
- 5, after touching the patient's surroundings.

**In Australia:** Delivered nationally through Hand Hygiene Australia with mandatory audit and compliance reporting feeding into NSQHS Standard 3 accreditation.

**Common trap:** Using alcohol rub after caring for a patient with C. difficile. Spores need soap and water.

**Resource:** [Hand Hygiene Australia, 5 Moments](https://hha.org.au/hand-hygiene/5-moments-for-hand-hygiene)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 14`*

## Week 3: Infection prevention and workplace safety

*Funnel stage: TEACH. Sunday story: Poll: which of this week's infection-control facts did you not know? Still no link.*

### Monday · #15 · Comparison card · Clinical Chart
**Contact, droplet or airborne: matching the precaution**

> Match the organism to the precaution. This is a guaranteed exam pattern.

- Contact. MRSA, VRE, C. difficile, scabies. Gown and gloves, dedicated equipment.
- Droplet, influenza, pertussis, mumps, meningococcal. Surgical mask, eye protection if splash risk.
- Airborne, tuberculosis, measles, varicella. Fit-tested P2/N95 and a negative pressure room.
- Some need both: varicella is contact plus airborne.

**In Australia:** Australia says P2/N95 respirator, and follows the NHMRC Australian Guidelines for the Prevention and Control of Infection in Healthcare.

**Common trap:** A surgical mask for suspected tuberculosis or measles. It must be a fit-tested respirator.

**Resource:** [NHMRC, Australian Guidelines for the Prevention and Control of Infection in Healthcare](https://www.nhmrc.gov.au/about-us/publications/australian-guidelines-prevention-and-control-infection-healthcare-2019)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 15`*

### Tuesday · #16 · Australian practice card · Editorial
**ANTT: the term used here instead of 'sterile technique'**

> Key parts and key sites. Protect those and you have protected the patient.

- Identify the key parts (needle tip, catheter hub) and key sites (the insertion site).
- Those are what must never be touched or contaminated.
- Standard ANTT covers short, simple procedures such as peripheral IV insertion.
- Surgical ANTT covers complex or prolonged procedures such as central line insertion.

**In Australia:** Aseptic Non-Touch Technique is the nationally endorsed framework in Australia and is embedded in NSQHS Standard 3 competency assessment, and it is the language used on Australian competency documents.

**Common trap:** Treating every aseptic procedure as needing full surgical technique.

**Resource:** [ACSQHC: Preventing and Controlling Infections Standard](https://www.safetyandquality.gov.au/standards/nsqhs-standards/preventing-and-controlling-healthcare-associated-infection-standard)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 16`*

### Wednesday · #17 · Single-fact card · Editorial
**Multi-resistant organisms and stewardship**

> Resistance is a system problem, not just a prescribing one.

- MROs include MRSA, VRE, CRE and ESBL-producing organisms, contact precautions, often single room.
- Stewardship means the narrowest effective agent, right dose, right duration, de-escalated on cultures.
- Screen high-risk admissions, including recent hospitalisation overseas.
- MRO status persists until formal clearance criteria are met.

**In Australia:** National surveillance runs through ACSQHC's AURA system, and stewardship is mandated under NSQHS Standard 3 rather than left to individual hospital programmes.

**Common trap:** Standing precautions down because the infection was treated.

**Resource:** [ACSQHC, Antimicrobial stewardship](https://www.safetyandquality.gov.au/our-work/antimicrobial-stewardship)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 17`*

### Thursday · #18 · Single-fact card · Editorial
**Sharps injury: the first five minutes**

> Wash it. Report it now. Do not squeeze it.

- Wash the wound with soap and water. Do not squeeze or suck it. Irrigate mucosal exposure.
- Report immediately, not at the end of the shift.
- Source and exposed worker are tested with consent for HIV, hepatitis B and hepatitis C.
- HIV post-exposure prophylaxis works best started within hours, and within 72 hours.

**In Australia:** Managed under state health department policy and notified through the state SafeWork regulator. Hepatitis B vaccination and titre checks are a standard Australian pre-employment requirement.

**Common trap:** Waiting until the shift ends to report, and losing the prophylaxis window.

**Resource:** [NSW Health: Occupational exposure to blood-borne viruses](https://www.health.nsw.gov.au/policies)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 18`*

### Friday · #19 · Single-fact card · Editorial
**Manual handling: use the hoist**

> The correct answer is almost never 'get another nurse to lift'.

- Assess the task, the individual, the load and the environment before moving anyone.
- Use mechanical aids, hoists and slide sheets, wherever they are available.
- Manual lifting of a patient's full weight is not routine practice.
- Manual handling injury is a leading cause of nursing workplace injury.

**In Australia:** Governed by Safe Work Australia's model Code of Practice on Hazardous Manual Tasks under state WHS Acts, which sets out the assess-and-control duty in detail.

**Common trap:** Choosing a two-person manual lift when a hoist is available and indicated.

**Resource:** [Safe Work Australia: Hazardous Manual Tasks Code of Practice](https://www.safeworkaustralia.gov.au/doc/model-code-practice-hazardous-manual-tasks)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 19`*

### Saturday · #20 · Australian practice card · Editorial
**Restrictive practices: last resort, always reviewed**

> A lap belt can be a restrictive practice. Intent and effect decide.

- Restraint may be physical, chemical, mechanical or environmental, and is always a last resort.
- Try and document less restrictive alternatives first.
- Orders are time-limited and reviewed. Never open-ended PRN.
- Document the rationale, the alternatives tried and the effect on the person.

**In Australia:** Australia regulates these formally as 'restrictive practices', through the NDIS Quality and Safeguards Commission for disability, and state Mental Health Acts for mental health. Reduction targets sit in NSQHS Standard 5, as a rights-based national scheme.

**Common trap:** Assuming bed rails are automatically not a restraint.

**Resource:** [NDIS Commission: Regulated Restrictive Practices](https://www.ndiscommission.gov.au/providers/registered-ndis-providers/provider-responsibilities/behaviour-support)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 20`*

### Sunday · #21 · Mnemonic card · Study Card
**RACE: the fire response order**

> Rescue. Alert. Contain. Extinguish, and only if it is safe.

- Rescue, move anyone in immediate danger.
- Alert, activate the alarm and call the emergency number.
- Contain, close doors and windows to slow the spread.
- Extinguish only if the fire is small and you are trained. Otherwise evacuate.
- Horizontal evacuation through fire doors comes before vertical evacuation.

**In Australia:** Australian hospitals use EWIS emergency warning systems with coded alerts under AS 3745, and the Australasian Triage Scale for mass casualty prioritisation.

**Common trap:** Trying to extinguish a spreading fire instead of evacuating.

**Resource:** [Fire Protection Association Australia](https://www.fpaa.com.au/)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 21`*

## Week 4: Error prevention and medication foundations

*Funnel stage: TEACH. Sunday story: Share the medication-safety carousel again as a story. Mention that the syllabus is halfway to the halfway point. No link.*

### Monday · #22 · Single-fact card · Editorial
**Two identifiers, every single time**

> Two identifiers. Never the bed number.

- Use two approved identifiers before any medication, procedure or specimen.
- Bed number and room number are never identifiers.
- Falls prevention basics: bed low and locked, call bell in reach, non-slip footwear.
- Report near-misses. They are the free lesson.

**In Australia:** Falls and pressure injury screening are mandated under NSQHS Standard 5, and a deteriorating patient is escalated with a MET call, any staff member can activate it directly, without waiting for a doctor.

**Common trap:** Waiting for the treating team before escalating a patient who already meets MET criteria.

**Resource:** [NSW CEC: Between the Flags](https://www.cec.health.nsw.gov.au/keep-patients-safe/between-the-flags)

*NCLEX category: Safety and Infection Prevention and Control · practise in: Professional practice · generate: `--id 22`*

### Tuesday · #23 · Mnemonic card · Study Card
**APINCHS: the high-risk medicines acronym used here**

> Seven letters that cover most serious medication harm.

- A, Antimicrobials. P. Potassium and other electrolytes. I. Insulin.
- N. Narcotics and sedatives. C. Chemotherapy. H. Heparin and anticoagulants.
- S. Systems, including IV fluids and infusion pumps.
- These require independent double-checking and separated storage.

**In Australia:** APINCHS is the ACSQHC national framework for high-risk medicines, and Australian workplaces name it directly on charts, storage rules and double-check policies.

**Common trap:** Believing a double-check alone prevents error. Storage and system design matter just as much.

**Resource:** [ACSQHC: High risk medicines](https://www.safetyandquality.gov.au/our-work/medicines-safety-and-quality/high-risk-medicines)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Pharmacology · generate: `--id 23`*

### Wednesday · #24 · Drug card · Study Card
**Insulin: onset, peak, duration and the 15/15 rule**

> Rapid-acting peaks in 1 to 2 hours. Know when the risk lands.

- Rapid-acting: onset 10-15 min, peak 1-2 h, duration 3-5 h. Give with or immediately before food.
- Short-acting: onset ~30 min, peak 2-4 h, duration 6-8 h.
- Long-acting: onset 1-2 h, no pronounced peak, about 24 h. Never mix with another insulin.
- Hypoglycaemia below 4 mmol/L: 15 g fast carbohydrate, recheck in 15 minutes.
- Severe or unconscious: IM glucagon or IV glucose.

**In Australia:** Blood glucose is measured in mmol/L. A BGL of 3.2 mmol/L is hypoglycaemia and needs treating. Australian brand names include NovoRapid, Actrapid and Lantus.

**Common trap:** Seeing a single-digit BGL and not recognising it as hypoglycaemia.

**Resource:** [Australian Prescriber](https://australianprescriber.tg.org.au)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Endocrine · generate: `--id 24`*

### Thursday · #25 · Comparison card · Clinical Chart
**Warfarin versus heparin: monitoring and reversal**

> Different test. Different antidote. Do not mix them up.

- Warfarin, monitored by INR, usually target 2.0-3.0. Reversal is vitamin K, plus prothrombinex if bleeding.
- Unfractionated heparin, monitored by APTT. Reversal is protamine sulfate.
- Low molecular weight heparin needs no routine APTT; use anti-Xa if renal impairment, obesity or pregnancy.
- Check platelets, heparin-induced thrombocytopenia is a real risk.
- Teach consistent vitamin K intake with warfarin, not avoidance of greens.

**In Australia:** Vitamin K is called phytomenadione here (Konakion). Warfarin management guidance follows Australian Prescriber and local anticoagulation protocols.

**Common trap:** Giving vitamin K for a high INR with no bleeding, without checking the local threshold.

**Resource:** [Australian Prescriber: Managing warfarin therapy](https://australianprescriber.tg.org.au)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Cardiovascular · generate: `--id 25`*

### Friday · #26 · Single-fact card · Editorial
**Opioids: sedation score before respiratory rate**

> Sedation comes before respiratory depression. That is your early warning.

- Assess respiratory rate and sedation score before every dose.
- Hold and escalate for a respiratory rate under 10, or rising sedation score.
- Naloxone has a shorter half-life than most opioids, re-sedation is common, so keep monitoring.
- Titrate naloxone in small increments to restore breathing without precipitating severe pain.
- Prescribe a laxative alongside, and monitor bowels.

**In Australia:** Intranasal naloxone (Nyxoid) is TGA-approved and available through take-home naloxone programmes in Australian pharmacies. Brand names differ. Endone is oxycodone, Kapanol is modified-release morphine.

**Common trap:** Withholding all analgesia for mild sedation instead of adjusting the dose and continuing to monitor.

**Resource:** [Australian Prescriber: Naloxone in the community](https://australianprescriber.tg.org.au)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Pharmacology · generate: `--id 26`*

### Saturday · #27 · Drug card · Study Card
**Vancomycin and gentamicin: the monitoring drugs**

> Red and flushed during a vancomycin infusion is usually a rate problem.

- Aminoglycosides such as gentamicin cause dose-related ototoxicity and nephrotoxicity, monitor renal function and levels.
- Vancomycin needs trough monitoring and an infusion over at least 60 minutes.
- Infusion-related flushing is histamine-mediated and rate-related, not a true allergy, slow the infusion.
- Report new tinnitus, hearing change, falling urine output or rising creatinine immediately.

**In Australia:** Antibiotic choice and dosing follow Therapeutic Guidelines (eTG), the national antimicrobial stewardship reference.

**Common trap:** Labelling infusion-rate flushing as anaphylaxis and withholding the drug permanently.

**Resource:** [Australian Prescriber, Aminoglycosides](https://australianprescriber.tg.org.au)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Pharmacology · generate: `--id 27`*

### Sunday · #28 · Single-fact card · Editorial
**IV potassium is never a push**

> Undiluted IV potassium causes cardiac arrest. There is no exception.

- Always dilute, always via an infusion pump. Never an IV push or bolus.
- Peripheral limits are generally up to 40 mmol/L concentration and 10 mmol per hour on a ward.
- Faster rates need cardiac monitoring and a higher level of care.
- Normal range is 3.5-5.2 mmol/L. Low risks arrhythmia and digoxin toxicity; high risks arrest.
- Concentrated ampoules are stored separately and restricted from ward stock.

**In Australia:** Potassium is reported and prescribed in mmol/L, and NSW CEC publishes a specific high-risk potassium protocol setting concentration and rate limits.

**Common trap:** Choosing rapid correction by push for severe hypokalaemia. Always wrong.

**Resource:** [NSW CEC: Potassium (intravenous)](https://www.cec.health.nsw.gov.au/keep-patients-safe/medication-safety/high-risk-medicines)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Renal and fluid · generate: `--id 28`*

## Week 5: High-risk medicines and the first numbers

*Funnel stage: INVITE. Sunday story: First mention of the readiness test. Frame it as 'find out which of these areas is actually below your level'. Link sticker.*

### Monday · #29 · Drug card · Study Card
**Digoxin, beta blockers and ACE inhibitors: check before you give**

> Count the apical pulse for a full minute. Then decide.

- Digoxin, hold and escalate for an apical pulse under 60. Count for one full minute.
- Digoxin toxicity: nausea, yellow-green visual halos, arrhythmia. Low potassium makes it worse.
- Beta blockers, hold per order for low heart rate or low blood pressure. Never stop abruptly.
- ACE inhibitors, watch for dry cough, high potassium, first-dose hypotension and angioedema.
- Angioedema is an emergency, not a side effect to monitor.

**In Australia:** Australian brand confusion between digoxin products at different strengths has prompted specific safety advisories, always check the strength on the chart.

**Common trap:** Treating an ACE inhibitor cough and angioedema as the same level of concern.

**Resource:** [Australian Prescriber: Digoxin toxicity](https://australianprescriber.tg.org.au)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Cardiovascular · generate: `--id 29`*

### Tuesday · #30 · Single-fact card · Editorial
**Extravasation: leave the cannula in**

> Stop the infusion. Do not pull the cannula out yet.

- Stop immediately, leave the cannula in place briefly to aspirate, then elevate and escalate.
- Use a pump for every high-alert infusion, insulin, heparin, potassium, opioids, chemotherapy.
- Fluid overload signs: breathlessness, crackles, raised JVP, rapid weight gain.
- Grade and document phlebitis using a visual infusion phlebitis score.

**In Australia:** IV fluids sit in the APINCHS 'Systems' category in Australia, so they carry the same high-risk handling requirements as other APINCHS medicines.

**Common trap:** Removing the cannula immediately and re-siting further down the same limb.

**Resource:** [ACSQHC: Medicines safety](https://www.safetyandquality.gov.au/our-work/medicines-safety-and-quality)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Pharmacology · generate: `--id 30`*

### Wednesday · #31 · Single-fact card · Editorial
**Blood transfusion: the first 15 minutes**

> Stay with them for the first 15 minutes. That is when reactions declare.

- Two-person independent identity check against the wristband and the unit immediately before starting.
- Baseline observations before, again at 15 minutes, then per protocol.
- On any suspected reaction: stop, keep the line open with normal saline, escalate, return the unit.
- A unit of red cells generally runs over 1.5 to 2 hours, and never beyond 4.
- Acute haemolytic reaction is usually an identification error, and is the most dangerous.

**In Australia:** Governed by ANZSBT guidelines and Lifeblood processes, with Australian traceability documentation required for every unit.

**Common trap:** Watching a little longer before stopping when early reaction signs appear.

**Resource:** [ANZSBT, Administration of blood products](https://anzsbt.org.au/guidelines/)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Sepsis and critical care · generate: `--id 31`*

### Thursday · #32 · Reference card · Clinical Chart
**Medication calculation without the 1000-fold error**

> Convert the units first. Every time.

- Dose required divided by dose available, multiplied by the volume.
- Infusion rate in mL/h = total volume divided by time in hours.
- Drops per minute = volume x drop factor, divided by time in minutes.
- Weight-based dosing uses an accurate current weight in kilograms.
- Convert micrograms and milligrams before you calculate, not during.

**In Australia:** Weight is always in kilograms and volumes are metric. The National Inpatient Medication Chart standardises how doses are written and checked.

**Common trap:** Forgetting a microgram to milligram conversion mid-calculation, a 1000-fold error.

**Resource:** [ACSQHC: National standard medication charts](https://www.safetyandquality.gov.au/our-work/medicines-safety-and-quality/national-standard-medication-charts)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Pharmacology · generate: `--id 32`*

### Friday · #33 · Single-fact card · Editorial
**Anaphylaxis: adrenaline first, into the thigh**

> Adrenaline. Intramuscular. Anterolateral thigh. Nothing before it.

- Adult dose 0.5 mg IM (0.5 mL of 1:1000) into the anterolateral thigh, repeated every 5 minutes if needed.
- Lay the person flat and raise the legs unless they are in respiratory distress. Do not sit them up suddenly.
- Then airway, oxygen, IV fluids and continuous monitoring.
- Antihistamines and steroids are adjuncts only. Never first-line.
- Anaphylaxis is rapid onset, multi-system, with airway or circulatory compromise.

**In Australia:** The drug is called adrenaline, and management follows ANZCOR Guideline 9.2.7.

**Common trap:** Giving an antihistamine first while assessing severity.

**Resource:** [ANZCOR: Guideline 9.2.7 Anaphylaxis](https://www.anzcor.org/home/first-aid-management-of-medical-conditions/guideline-9-2-7-first-aid-management-of-anaphylaxis/)

*NCLEX category: Pharmacological and Parenteral Therapies · practise in: Sepsis and critical care · generate: `--id 33`*

### Saturday · #34 · Australian practice card · Editorial
**Track and trigger: escalation is not optional**

> Two yellows or one red. The chart tells you what to do.

- Normal adult ranges: respiratory rate 12-20, heart rate 60-100, SpO2 at or above 95% unless a target is set.
- A track-and-trigger chart colours each observation and defines the required response.
- Escalation is a defined pathway, not a judgement call.
- A rising respiratory rate over hours predicts deterioration before saturations fall.
- Trends matter more than any single reading.

**In Australia:** Australia uses colour-zoned observation charts under Between the Flags, and deterioration is escalated by MET call.

**Common trap:** Being reassured by one abnormal observation because the others look fine.

**Resource:** [NSW CEC: Observation charts](https://www.cec.health.nsw.gov.au/keep-patients-safe/between-the-flags)

*NCLEX category: Reduction of Risk Potential · practise in: Professional practice · generate: `--id 34`*

### Sunday · #35 · Reference card · Clinical Chart
**Australian lab reference ranges in SI units**

> Haemoglobin is reported in g/L. For a man, 130 to 170 g/L is the normal range.

- Sodium 135-145 mmol/L. Potassium 3.5-5.2 mmol/L.
- Fasting glucose about 4.0-7.8 mmol/L.
- Creatinine roughly 60-110 micromol/L in men, 45-90 in women.
- Haemoglobin 130-170 g/L in men, 115-155 g/L in women.
- Platelets 150-400 x10^9/L. White cells 4.0-11.0 x10^9/L.

**In Australia:** Australian pathology reports in SI units, mmol/L, micromol/L and g/L, and the reference intervals are locally harmonised. Always check your own laboratory's stated range as well.

**Common trap:** Treating a haemoglobin of 140 g/L as abnormal when it sits mid-range.

**Resource:** [RCPA: Harmonised reference intervals](https://www.rcpa.edu.au/Manuals/RCPA-Manual)

*NCLEX category: Reduction of Risk Potential · practise in: Professional practice · generate: `--id 35`*

## Week 6: Assessment, deterioration and the heart

*Funnel stage: INVITE. Sunday story: Story the cardiac reference card, then the readiness test link under it.*

### Monday · #36 · Mnemonic card · Study Card
**ABG interpretation with ROME**

> Respiratory Opposite. Metabolic Equal. That is the whole method.

- Normal: pH 7.35-7.45, PaCO2 35-45 mmHg, bicarbonate 22-26 mmol/L.
- Respiratory Opposite, pH and CO2 move in opposite directions.
- Metabolic Equal, pH and bicarbonate move in the same direction.
- Partial compensation means the pH is still abnormal; full means pH is normal but the values are not.
- Always interpret alongside the patient, never the paper alone.

**In Australia:** Australian laboratories may report gases in kPa as well as mmHg depending on the analyser. Check the unit before interpreting, 1 kPa is about 7.5 mmHg.

**Common trap:** Reading a kPa value as mmHg and reversing the interpretation.

**Resource:** [Australian Prescriber: Interpreting arterial blood gases](https://australianprescriber.tg.org.au)

*NCLEX category: Reduction of Risk Potential · practise in: Respiratory · generate: `--id 36`*

### Tuesday · #37 · Single-fact card · Editorial
**Fasting before surgery: 6 and 2**

> Six hours for food. Two hours for clear fluids. Not midnight.

- Standard adult fasting is 6 hours for solids and 2 hours for clear fluids before elective anaesthesia.
- Pre-op checklist: consent verified, site marked, allergies confirmed, baseline observations, prostheses removed.
- Post-op priority order: airway and breathing, then circulation and bleeding, then pain, then wound and drains.
- Report urine output under 0.5 mL/kg/hour as a perfusion warning.

**In Australia:** Fasting and pre-anaesthetic standards follow ANZCA, and GLP-1 agonist users have specific Australian periprocedural advice because of delayed gastric emptying.

**Common trap:** Applying an outdated nil-by-mouth-from-midnight rule.

**Resource:** [ANZCA: Pre-anaesthesia consultation and patient preparation](https://www.anzca.edu.au/safety-advocacy/standards-of-practice/professional-documents)

*NCLEX category: Reduction of Risk Potential · practise in: Perioperative · generate: `--id 37`*

### Wednesday · #38 · Question of the day · Midnight
**Contrast, metformin and the shellfish myth**

> Which allergy actually matters before a contrast CT?

- Check renal function and metformin status before iodinated contrast.
- Metformin is generally withheld around contrast in reduced renal function and restarted once function is confirmed stable.
- Screen for ferromagnetic implants and device compatibility before MRI.
- Shellfish allergy is not an evidence-based contraindication. Prior contrast reaction is the real risk factor.
- Hydrate before and after in at-risk patients.

**In Australia:** Contrast safety follows the RANZCR iodinated contrast guideline, which sets the eGFR thresholds and metformin hold times used here.

**Common trap:** Cancelling contrast because the patient mentioned a shellfish allergy.

**Resource:** [RANZCR: Iodinated contrast media guideline](https://www.ranzcr.com/college/document-library)

*NCLEX category: Reduction of Risk Potential · practise in: Renal and fluid · generate: `--id 38`*

### Thursday · #39 · Single-fact card · Editorial
**Never clamp a bubbling chest drain**

> Clamping a bubbling drain can cause a tension pneumothorax.

- Keep the drainage unit below chest level at all times.
- Gentle swinging with respiration is expected. Continuous bubbling suggests an air leak.
- No swinging can mean a blockage, or that the lung has re-expanded.
- Never clamp a bubbling drain, including during transfer.
- Secure all tubing and document output every shift.

**In Australia:** None material, the principles are universal, though each health service has its own nursing procedure.

**Common trap:** Clamping the drain to move the patient.

**Resource:** [Royal Children's Hospital: Chest drain management](https://www.rch.org.au/rchcpg/hospital_clinical_guideline_index/Chest_drain_management/)

*NCLEX category: Reduction of Risk Potential · practise in: Perioperative · generate: `--id 39`*

### Friday · #40 · Single-fact card · Editorial
**Complications to anticipate after common procedures**

> Post-procedure back pain and low blood pressure is not 'normal recovery'.

- After lumbar puncture, positional headache, and rarely new leg weakness needing urgent review.
- After cardiac catheterisation, check the site and distal pulses; back pain with hypotension suggests retroperitoneal bleed.
- After bronchoscopy, nil by mouth until the gag reflex returns.
- After paracentesis, watch for hypotension from rapid fluid shifts.

**In Australia:** None material for recognition; documentation goes through Australian incident and clinical governance systems.

**Common trap:** Attributing post-procedure hypotension to opioids without excluding bleeding.

**Resource:** [Queensland Health: Clinical guidelines](https://www.health.qld.gov.au/clinical-practice/guidelines-procedures)

*NCLEX category: Reduction of Risk Potential · practise in: Perioperative · generate: `--id 40`*

### Saturday · #41 · Question of the day · Midnight
**Catheters: review the need every day**

> The best way to prevent a catheter infection is to remove the catheter.

- Keep the bag below bladder level and the system closed.
- Review the need for the catheter daily and remove as soon as it is clinically appropriate.
- Bladder scan if there has been no void 6-8 hours post-operatively or after removal.
- In older adults, a urinary tract infection may present as new confusion rather than dysuria.

**In Australia:** Insertion follows Aseptic Non-Touch Technique, the standard Australian framework and terminology.

**Common trap:** Re-catheterising without scanning first.

**Resource:** [Continence Health Australia](https://www.continence.org.au/)

*NCLEX category: Reduction of Risk Potential · practise in: Renal and fluid · generate: `--id 41`*

### Sunday · #42 · Carousel (1 post, 5 slides) · Colour Block
**Acute coronary syndrome: the first ten minutes**

> A 12-lead ECG within 10 minutes. That is the standard.

- Classic pain is central, heavy, over 20 minutes and unrelieved by rest, but women, older adults and people with diabetes often present atypically.
- 12-lead ECG within 10 minutes of arrival, then serial troponin.
- Aspirin 300 mg chewed unless contraindicated, GTN, IV access, continuous monitoring.
- Oxygen only if saturations are low, routine oxygen is no longer given.
- Targets: door to balloon under 90 minutes for PCI.

**In Australia:** Diagnostic pathways follow Heart Foundation and Cardiac Society of Australia and New Zealand high-sensitivity troponin protocols, resuscitation follows ANZCOR, and the emergency number is 000.

**Common trap:** Giving oxygen to every chest pain patient regardless of saturation.

**Resource:** [Heart Foundation: Clinical guidelines](https://www.heartfoundation.org.au/for-professionals)

*NCLEX category: Physiological Adaptation · practise in: Cardiovascular · generate: `--id 42`*

## Week 7: The big physiological emergencies

*Funnel stage: INVITE. Sunday story: Ask a question about the week's emergencies, then link the readiness test in the reply frame.*

### Monday · #43 · Single-fact card · Editorial
**Heart failure: the daily weight is the early warning**

> Two kilograms in two days is fluid, not food.

- Left-sided: breathlessness, orthopnoea, waking breathless at night, crackles.
- Right-sided: peripheral oedema, raised JVP, enlarged liver.
- Daily weight is the most sensitive monitor, a gain over 2 kg in 2 days signals retention.
- Sit them upright, give the prescribed diuretic, restrict sodium and often fluid.
- Monitor potassium and renal function, loop diuretics drop potassium.

**In Australia:** The medication is spelled frusemide on Australian charts, not furosemide. Guidance comes from the Heart Foundation and CSANZ.

**Common trap:** Giving a fluid bolus to a breathless heart failure patient.

**Resource:** [Heart Foundation: Heart failure guidelines](https://www.heartfoundation.org.au/for-professionals)

*NCLEX category: Physiological Adaptation · practise in: Cardiovascular · generate: `--id 43`*

### Tuesday · #44 · Carousel (1 post, 5 slides) · Colour Block
**Stroke: the clock starts at last known well**

> Nil by mouth until someone has done the swallow screen.

- Use FAST to recognise: Face, Arm, Speech, Time.
- Thrombolysis window is within 4.5 hours of a clearly known onset.
- Thrombectomy can extend to around 24 hours for selected large-vessel occlusions with favourable imaging.
- Blood pressure must be below 185/110 before thrombolysis.
- Nil by mouth, including medications, until a formal swallow screen is done.

**In Australia:** Australia follows the Stroke Foundation's Living Clinical Guidelines, which are continuously updated as new evidence lands.

**Common trap:** Assuming every stroke gets thrombolysis. A bleed must be excluded on CT first.

**Resource:** [Stroke Foundation: Living Clinical Guidelines](https://informme.org.au/guidelines/living-clinical-guidelines-for-stroke-management)

*NCLEX category: Physiological Adaptation · practise in: Neurological · generate: `--id 44`*

### Wednesday · #45 · Australian practice card · Editorial
**Oxygen targets: when 88 to 92 percent is the goal**

> More oxygen is not always better. Sometimes it is the harm.

- General target is 92-96%.
- For people at risk of carbon dioxide retention, the target is 88-92% with controlled delivery.
- Over-oxygenating a CO2 retainer can worsen hypercapnia and precipitate respiratory failure.
- In decompensation with pH 7.25-7.35, consider non-invasive ventilation.
- Oxygen is a drug, it is prescribed with a written target range.

**In Australia:** Australian practice prescribes oxygen against a documented target range following Thoracic Society of Australia and New Zealand guidance, which is more explicit than ad-hoc high-flow practice elsewhere.

**Common trap:** Turning oxygen up because a COPD patient sits at 90%.

**Resource:** [Australian Prescriber, Acute oxygen therapy](https://australianprescriber.tg.org.au)

*NCLEX category: Physiological Adaptation · practise in: Respiratory · generate: `--id 45`*

### Thursday · #46 · Single-fact card · Editorial
**A silent chest in asthma is an emergency**

> No wheeze does not mean better. Sometimes it means barely moving air.

- Life-threatening signs: silent chest, cyanosis, exhaustion, confusion, poor respiratory effort.
- First line is salbutamol by metered dose inhaler with a spacer, as effective as a nebuliser.
- Give systemic corticosteroids early, within the first hour.
- Oxygen target in acute asthma is 92-95%, not the COPD range.
- Absence of wheeze in a distressed patient is critical, not reassuring.

**In Australia:** Severity grading and escalation follow the Australian Asthma Handbook from the National Asthma Council, and spacer-first practice is emphasised more strongly here.

**Common trap:** Documenting improvement because the wheeze has stopped.

**Resource:** [Australian Asthma Handbook](https://www.asthmahandbook.org.au/)

*NCLEX category: Physiological Adaptation · practise in: Respiratory · generate: `--id 46`*

### Friday · #47 · Single-fact card · Editorial
**Acute kidney injury and the sick day rules**

> Some medicines should be paused when someone is unwell and dehydrated.

- AKI: creatinine rise of 26.5 micromol/L within 48 hours, or 1.5 times baseline within 7 days, or urine under 0.5 mL/kg/h for 6 hours.
- CKD is staged on eGFR: G1 at or above 90 down to G5 under 15.
- Withhold nephrotoxic and renally cleared drugs during acute illness.
- Watch for hyperkalaemia and fluid overload; strict balance and daily weights.

**In Australia:** eGFR is automatically reported on Australian pathology results, and Kidney Health Australia publishes 'sick day rules' telling patients which medicines to pause during illness, a distinctly Australian resource.

**Common trap:** Continuing metformin and NSAIDs through dehydration or contrast imaging.

**Resource:** [Kidney Health Australia: CKD Management Handbook](https://kidney.org.au/health-professionals/ckd-management-handbook)

*NCLEX category: Physiological Adaptation · practise in: Renal and fluid · generate: `--id 47`*

### Saturday · #48 · Comparison card · Clinical Chart
**DKA versus HHS: the numbers that separate them**

> Fluids first. Check the potassium. Then insulin.

- DKA, glucose usually above 11-14 mmol/L, ketones above 3 mmol/L, pH under 7.3, bicarbonate under 15.
- HHS, glucose often far higher, osmolality above 320, ketones minimal, pH above 7.3.
- Both: IV sodium chloride first, then fixed-rate insulin. Never insulin before fluids.
- Potassium must be at least 3.5 mmol/L before insulin, insulin drives it into cells.
- HHS needs slower correction because of cerebral risk.

**In Australia:** Glucose and ketones are in mmol/L here. Euglycaemic DKA can occur with SGLT2 inhibitors, so a near-normal glucose does not exclude it.

**Common trap:** Starting insulin before fluids and before confirming potassium.

**Resource:** [Australian Diabetes Society](https://www.diabetessociety.com.au/)

*NCLEX category: Physiological Adaptation · practise in: Endocrine · generate: `--id 48`*

### Sunday · #49 · Question of the day · Midnight
**Compensated shock: normal blood pressure, abnormal patient**

> By the time blood pressure falls, compensation has already failed.

- Four types: hypovolaemic, cardiogenic, distributive, obstructive.
- Compensated shock shows tachycardia, narrow pulse pressure, delayed capillary refill and cool peripheries, with a normal blood pressure.
- Target mean arterial pressure is generally above 65 mmHg.
- Lactate above 2 mmol/L signals tissue hypoperfusion regardless of blood pressure.
- Reassess after each 250-500 mL bolus rather than giving one large fixed volume.

**In Australia:** Deterioration triggers a MET call, with activation criteria set by the ACSQHC Recognising and Responding to Acute Deterioration Standard.

**Common trap:** Waiting for hypotension before escalating.

**Resource:** [ACSQHC, Acute deterioration standard](https://www.safetyandquality.gov.au/standards/nsqhs-standards/recognising-and-responding-acute-deterioration-standard)

*NCLEX category: Physiological Adaptation · practise in: Sepsis and critical care · generate: `--id 49`*

## Week 8: Sepsis, fluids and comfort care

*Funnel stage: CONVERT. Sunday story: Readiness test link, with the line about the report naming specific areas rather than giving a score.*

### Monday · #50 · Carousel (1 post, 5 slides) · Colour Block
**Sepsis: cultures before antibiotics, antibiotics within the hour**

> Every hour of delay costs. The order still matters.

- Red flags: new confusion, systolic under 90, respiratory rate 25 or more, mottled skin, falling urine output.
- Take blood cultures before antibiotics, then give antibiotics, ideally within one hour.
- Give IV fluids, measure lactate, monitor urine output.
- Lactate above 2 mmol/L indicates hypoperfusion and worsens prognosis.
- Septic shock: needing vasopressors for a MAP of 65 plus lactate above 2 despite fluids.

**In Australia:** Australia runs the SEPSIS KILLS pathway and the ACSQHC Sepsis Clinical Care Standard as the mandated national framework.

**Common trap:** Giving antibiotics before cultures and losing the diagnosis.

**Resource:** [ACSQHC: Sepsis Clinical Care Standard](https://www.safetyandquality.gov.au/standards/clinical-care-standards/sepsis-clinical-care-standard)

*NCLEX category: Physiological Adaptation · practise in: Sepsis and critical care · generate: `--id 50`*

### Tuesday · #51 · Single-fact card · Editorial
**Hyperkalaemia: calcium protects the heart first**

> Calcium does not lower the potassium. It protects the heart while you do.

- Severe hyperkalaemia above 6.0-6.5 mmol/L: peaked T waves, widening QRS, risk of arrest.
- Give IV calcium gluconate first to stabilise the myocardium.
- Then insulin with glucose, and salbutamol, to shift potassium into cells.
- Correct hyponatraemia slowly, no faster than 8-10 mmol/L in 24 hours, to avoid osmotic demyelination.
- Distinguish overload from deficit before choosing fluid therapy.

**In Australia:** Electrolytes are reported and prescribed in mmol/L throughout Australia.

**Common trap:** Giving calcium and assuming the potassium is now treated.

**Resource:** [ACSQHC: Medication safety standard](https://www.safetyandquality.gov.au/standards/nsqhs-standards/medication-safety-standard)

*NCLEX category: Physiological Adaptation · practise in: Renal and fluid · generate: `--id 51`*

### Wednesday · #52 · Australian practice card · Editorial
**Pain in dementia: use a behavioural tool**

> If they cannot tell you, you still have to measure it.

- Self-report is the gold standard, pain is what the person says it is.
- Numeric rating scale for verbal adults, faces scales for children.
- For non-verbal or advanced dementia, use a validated behavioural tool.
- Reassess about 30-60 minutes after IV analgesia, 60-90 minutes after oral.
- Multimodal analgesia with regular paracetamol reduces opioid need.

**In Australia:** The Abbey Pain Scale was developed in Australia for residential aged care and is the most widely used Australian tool for dementia-related pain.

**Common trap:** Withholding analgesia because the observations look too normal for the reported pain.

**Resource:** [Dementia Australia, Abbey Pain Scale](https://www.dementia.org.au/)

*NCLEX category: Basic Care and Comfort · practise in: Professional practice · generate: `--id 52`*

### Thursday · #53 · Single-fact card · Editorial
**Confirming a nasogastric tube: pH, not a whoosh**

> The whoosh test is not a test. Check the pH.

- Confirm placement by pH testing the aspirate, aiming for pH below 5.5, or X-ray if unclear.
- Auscultating injected air is unsafe and outdated.
- Sit the person up 30-45 degrees during feeding and for 30-60 minutes after.
- Screen nutrition risk on admission with a validated tool.
- Watch for refeeding syndrome, check phosphate, potassium and magnesium, and give thiamine.

**In Australia:** The Malnutrition Screening Tool was developed and validated in Queensland and is used as the standard across most Australian hospitals under the Comprehensive Care Standard.

**Common trap:** Relying on auscultation to confirm placement before feeding.

**Resource:** [Queensland Health: Malnutrition Screening Tool](https://www.health.qld.gov.au/nutrition/patient-care)

*NCLEX category: Basic Care and Comfort · practise in: Gastrointestinal · generate: `--id 53`*

### Friday · #54 · Reference card · Clinical Chart
**Bristol stool chart and bowel care that prevents harm**

> Constipation on opioids is predictable. So prevent it.

- Document stool form using the Bristol Stool Chart, types 1 to 7.
- Opioids, immobility and low fluid and fibre are the main inpatient risk factors.
- Start a bowel regimen alongside opioids rather than waiting for a problem.
- New confusion in an older adult can be constipation, retention or infection.

**In Australia:** None material, the chart and principles are used internationally.

**Common trap:** Charting bowels not open for several days without acting on it.

**Resource:** [Continence Health Australia](https://www.continence.org.au/)

*NCLEX category: Basic Care and Comfort · practise in: Gastrointestinal · generate: `--id 54`*

### Saturday · #55 · Reference card · Clinical Chart
**Pressure injury staging in four steps**

> Stage 1 is intact skin that does not blanch. That is the one people miss.

- Stage 1, intact skin with non-blanchable redness.
- Stage 2, partial thickness loss, or an open or ruptured blister.
- Stage 3, full thickness, subcutaneous fat visible.
- Stage 4, full thickness with exposed muscle, bone or tendon.
- Also unstageable, and deep tissue pressure injury. Reposition at-risk people at least 2-hourly.

**In Australia:** Falls and pressure injury screening within a set time of admission are mandated under NSQHS Standard 5, and stage 3 or higher injuries are generally reportable clinical incidents.

**Common trap:** Recording non-blanchable redness as a bruise.

**Resource:** [ACSQHC: Comprehensive Care Standard](https://www.safetyandquality.gov.au/standards/nsqhs-standards/comprehensive-care-standard)

*NCLEX category: Basic Care and Comfort · practise in: Professional practice · generate: `--id 55`*

### Sunday · #56 · Single-fact card · Editorial
**Sleep: cluster the care before reaching for sedation**

> The first intervention for poor sleep is not a tablet.

- Hospital noise, light and overnight observations are major disruptors, and poor sleep drives delirium.
- Cluster care, medications and observations to protect uninterrupted blocks overnight.
- Minimise sedative hypnotics, especially in older adults, because of falls and delirium risk.
- Use day and night cues, open blinds, encourage daytime activity.

**In Australia:** The Royal Commission into Aged Care Quality and Safety specifically flagged sedation overuse in Australian residential aged care, driving a strong national push to minimise pharmacological sleep aids.

**Common trap:** Giving a PRN sedative before trying environmental measures.

**Resource:** [ACSQHC: Comprehensive Care Standard](https://www.safetyandquality.gov.au/standards/nsqhs-standards/comprehensive-care-standard)

*NCLEX category: Basic Care and Comfort · practise in: Professional practice · generate: `--id 56`*

## Week 9: End of life, and the start of life

*Funnel stage: CONVERT. Sunday story: Two frames: the end-of-life post that got the most saves, then the readiness test link.*

### Monday · #57 · Single-fact card · Editorial
**Recognising the dying phase**

> At some point, routine observations stop being care.

- Signs: reduced consciousness, changed breathing pattern, mottled cool skin, falling urine output, noisy secretions.
- Anticipatory subcutaneous medications are prescribed in advance for pain, breathlessness, secretions and agitation.
- Shift to comfort, reposition for comfort, stop non-essential observations and interventions.
- Confirm the advance care directive and resuscitation status with the team and family.

**In Australia:** Advance care directives are state-legislated with different names in each jurisdiction, and hyoscine butylbromide is commonly used in Australia for end-of-life secretions.

**Common trap:** Continuing 4-hourly observations on someone who is actively dying.

**Resource:** [CareSearch: Palliative Care Knowledge Network](https://www.caresearch.com.au/)

*NCLEX category: Basic Care and Comfort · practise in: Professional practice · generate: `--id 57`*

### Tuesday · #58 · Single-fact card · Editorial
**Supporting independence, not doing it for them**

> Doing it faster yourself is not always doing it better.

- Assess functional ability with a structured tool rather than assuming.
- Correct sizing of frames, sticks and shower chairs prevents falls.
- Hygiene care is your chance to inspect pressure areas every time.
- Oral care reduces aspiration pneumonia risk, especially in dysphagia.
- Respect cultural and personal preferences, including same-gender care requests.

**In Australia:** Equipment and home modifications are funded through the NDIS and My Aged Care, with occupational therapy home assessment standard before discharge. The term is walking frame, not walker.

**Common trap:** Completing the task for the person and undermining their rehabilitation.

**Resource:** [My Aged Care](https://www.myagedcare.gov.au/)

*NCLEX category: Basic Care and Comfort · practise in: Professional practice · generate: `--id 58`*

### Wednesday · #59 · Single-fact card · Editorial
**Developmental red flags worth memorising**

> Not the milestones themselves, the ages they should have passed.

- No social smile by 2 months. No babbling by 6 months.
- Not walking by 18 months. No two-word phrases by 2 years.
- Erikson: trust, then autonomy, then initiative, then industry, then identity.
- Object permanence develops around 8-12 months.
- Adolescent risk-taking is developmentally normal, assess safety, not morality.

**In Australia:** Australia uses the child health record ('blue book') and Key Ages and Stages checks through child and family health nurse services in every state and territory.

**Common trap:** Quoting a checkpoint age from memory instead of the Key Ages and Stages schedule.

**Resource:** [Royal Children's Hospital: Kids Health Info](https://www.rch.org.au/kidsinfo/)

*NCLEX category: Health Promotion and Maintenance · practise in: Maternity · generate: `--id 59`*

### Thursday · #60 · Question of the day · Midnight
**Antenatal danger signs that need review today**

> Headache, visual change and epigastric pain belong together.

- Fundal height roughly matches gestational weeks, plus or minus 2-3 cm, from about 20 weeks.
- Danger signs: severe headache, visual changes, epigastric pain, reduced fetal movements, bleeding.
- Postpartum haemorrhage is over 500 mL after vaginal birth, over 1000 mL after caesarean.
- First assessment for postpartum bleeding is the fundus.

**In Australia:** Care follows the national Pregnancy Care Guidelines and RANZCOG, usually through midwifery continuity of care or GP shared care, with a visit schedule risk-stratified rather than fixed.

**Common trap:** Applying a fixed visit count instead of the risk-stratified Australian schedule.

**Resource:** [Australian Government: Pregnancy Care Guidelines](https://www.health.gov.au/resources/pregnancy-care-guidelines)

*NCLEX category: Health Promotion and Maintenance · practise in: Maternity · generate: `--id 60`*

### Friday · #61 · Mnemonic card · Study Card
**APGAR, and the jaundice that is never normal**

> Jaundice in the first 24 hours is always pathological.

- APGAR at 1 and 5 minutes: Appearance, Pulse, Grimace, Activity, Respiration, each 0-2.
- Normal newborn: heart rate 110-160, respiratory rate 30-60, temperature 36.5-37.5 degrees.
- Physiological jaundice appears after 24 hours. Before that it is pathological.
- Weight loss up to 7-10% in the first week is normal, regained by about 2 weeks.

**In Australia:** Newborn bloodspot screening occurs at 48-72 hours and hearing screening is universal. Vitamin K and the hepatitis B birth dose require documented parental consent, they are recommended, not automatic.

**Common trap:** Treating day-one jaundice as physiological.

**Resource:** [Australian Immunisation Handbook](https://immunisationhandbook.health.gov.au/)

*NCLEX category: Health Promotion and Maintenance · practise in: Maternity · generate: `--id 61`*

### Saturday · #62 · Australian practice card · Editorial
**Immunisation: the National Immunisation Program schedule**

> The National Immunisation Program sets the schedule, and it is reviewed regularly.

- Live vaccines such as MMR and varicella are contraindicated in pregnancy and significant immunosuppression.
- Pertussis vaccination in pregnancy protects the newborn through passive transfer.
- True contraindication is anaphylaxis to a previous dose or component.
- Always check the current handbook, the schedule is reviewed and updated.

**In Australia:** Australia follows the National Immunisation Program schedule and the Australian Immunisation Handbook. Adolescent doses are delivered through school programmes, and shingles vaccination is funded from 65, or from 50 for Aboriginal and Torres Strait Islander people.

**Common trap:** Quoting a schedule from memory instead of checking the current handbook.

**Resource:** [National Immunisation Program Schedule](https://www.health.gov.au/topics/immunisation/when-to-get-vaccinated/national-immunisation-program-schedule)

*NCLEX category: Health Promotion and Maintenance · practise in: Professional practice · generate: `--id 62`*

### Sunday · #63 · Reference card · Clinical Chart
**Australian cancer screening: the three programmes**

> Cervical screening here starts at 25 and runs every 5 years.

- Cervical. HPV-based Cervical Screening Test from age 25, every 5 years, to age 74.
- Breast. BreastScreen Australia, free 2-yearly mammogram, target age 50-74.
- Bowel, free mailed iFOBT every 2 years, now from age 45 to 74.
- Screening targets people without symptoms. Symptoms need assessment, not screening.

**In Australia:** Australia moved to five-yearly HPV-based cervical screening in 2017, and lowered bowel screening to start at age 45 from July 2024.

**Common trap:** Quoting an interval from memory instead of the current programme ages.

**Resource:** [Australian Government: National cancer screening](https://www.health.gov.au/our-work/national-cervical-screening-program)

*NCLEX category: Health Promotion and Maintenance · practise in: Professional practice · generate: `--id 63`*

## Week 10: Mind, communication and safety

*Funnel stage: CONVERT. Sunday story: Close the cycle. The content was the syllabus, the platform is where you practise it, and the next cycle starts Monday. Link to plans.*

### Monday · #64 · Australian practice card · Editorial
**Standard drinks and the NHMRC alcohol guidance**

> An Australian standard drink is 10 grams of alcohol.

- An Australian standard drink contains 10 g of alcohol.
- NHMRC guidance: no more than 10 standard drinks a week, and no more than 4 on any one day.
- No safe level in pregnancy, when breastfeeding, or under 18.
- Use AUDIT-C to screen, and the 5 A's for smoking cessation: Ask, Advise, Assess, Assist, Arrange.

**In Australia:** An Australian standard drink contains 10 g of alcohol, and every NHMRC limit is counted against that measure. Pub and restaurant servings are often more than one standard drink.

**Common trap:** Counting glasses rather than standard drinks.

**Resource:** [NHMRC, Alcohol guidelines](https://www.nhmrc.gov.au/health-advice/alcohol)

*NCLEX category: Health Promotion and Maintenance · practise in: Professional practice · generate: `--id 64`*

### Tuesday · #65 · Comparison card · Clinical Chart
**Therapeutic versus non-therapeutic responses**

> False reassurance feels kind. It closes the conversation.

- Therapeutic: open questions, reflection, silence, clarifying, offering self, restating.
- Non-therapeutic: giving advice, false reassurance, 'why' questions, changing the subject.
- Validate the feeling before moving to problem-solving.
- Silence is an intervention, not a gap to fill.

**In Australia:** None material, the technique is universal. Use Australian idiom in patient-facing phrasing.

**Common trap:** Choosing 'I'm sure it will be fine' over an open, validating response.

**Resource:** [Head to Health](https://www.headtohealth.gov.au/)

*NCLEX category: Psychosocial Integrity · practise in: Mental health · generate: `--id 65`*

### Wednesday · #66 · Mnemonic card · Study Card
**The mental state examination, domain by domain**

> Describe what you observed. Do not record your conclusion.

- Appearance and behaviour, speech, mood and affect, thought form and content.
- Then perception, cognition, insight and judgement.
- Flat, blunted and labile affect are distinct and testable.
- Delirium screening uses the Confusion Assessment Method.
- Write 'avoided eye contact, spoke in a flat monotone', not 'seemed depressed'.

**In Australia:** Mental health legislation is state and territory based in Australia, so involuntary assessment criteria and forms differ by jurisdiction. There is no single national mental health act.

**Common trap:** Assuming one national involuntary treatment standard applies across Australia.

**Resource:** [Head to Health](https://www.headtohealth.gov.au/)

*NCLEX category: Psychosocial Integrity · practise in: Mental health · generate: `--id 66`*

### Thursday · #67 · Single-fact card · Editorial
**Asking directly about suicide is safe and necessary**

> Asking does not plant the idea. Not asking leaves you guessing.

- Ask directly and without judgement about thoughts of ending life.
- Assess plan, means, timeline and access to means. Specificity increases acuity.
- The strongest single risk factor is a previous attempt.
- Protective factors include support, reasons for living and restricted access to means.
- A safety plan covers warning signs, coping strategies, contacts and crisis numbers.

**In Australia:** Australian crisis lines are Lifeline 13 11 14, Beyond Blue 1300 22 4636, and 13YARN 13 92 76, a national line staffed by Aboriginal and Torres Strait Islander crisis supporters.

**Common trap:** Avoiding the direct question, or giving a number that does not operate in Australia.

**Resource:** [Lifeline Australia](https://www.lifeline.org.au/)

*NCLEX category: Psychosocial Integrity · practise in: Mental health · generate: `--id 67`*

### Friday · #68 · Single-fact card · Editorial
**Alcohol withdrawal can kill. Opioid withdrawal usually does not.**

> The timeline tells you when to worry.

- Tremor and anxiety at 6-12 hours. Hallucinations around 12-24 hours.
- Seizures around 24-48 hours. Delirium tremens typically 48-96 hours after the last drink.
- Delirium tremens is a medical emergency with significant untreated mortality.
- CIWA-Ar is the validated tool guiding benzodiazepine dosing.
- Use person-first language, a person with a substance use disorder.

**In Australia:** Withdrawal protocols follow state health department guidelines, and alcohol and drug information services are state-based rather than a single national line.

**Common trap:** Treating alcohol and opioid withdrawal as equally dangerous.

**Resource:** [Australian Government, Alcohol and other drugs](https://www.health.gov.au/topics/alcohol)

*NCLEX category: Psychosocial Integrity · practise in: Mental health · generate: `--id 68`*

### Saturday · #69 · Single-fact card · Editorial
**Screening for family violence: ask them alone**

> You cannot screen safely with the partner in the room.

- Screen privately, without partner or family present, using direct non-judgemental questions.
- Indicators: injuries inconsistent with the explanation, injuries at different healing stages, delayed presentation, controlling behaviour.
- Elder abuse includes financial, physical, psychological and neglect. Assess carer strain as a risk factor.
- Document objectively in the person's own words, and use body maps.
- Safety comes before full disclosure.

**In Australia:** The national referral line is 1800RESPECT (1800 737 732). Mandatory reporting thresholds for child abuse differ by state. Culturally safe, trauma-informed responses are an explicit NMBA expectation.

**Common trap:** Asking screening questions with a family member still present.

**Resource:** [1800RESPECT](https://www.1800respect.org.au/)

*NCLEX category: Psychosocial Integrity · practise in: Professional practice · generate: `--id 69`*

### Sunday · #70 · Carousel (1 post, 5 slides) · Colour Block
**Grief, and what cultural safety actually means**

> Cultural safety is judged by the person receiving care, not by you.

- Grief stages are not sequential. Do not expect people to move through them in order.
- Prolonged grief that still impairs function beyond about 12 months warrants referral.
- Coping ranges from adaptive to maladaptive. Assess it, do not judge it.
- Cultural safety means the patient decides whether the interaction was safe and respectful.

**In Australia:** Cultural safety for Aboriginal and Torres Strait Islander Peoples is a codified NMBA obligation, not optional good practice. Kinship obligations and Sorry Business must be respected and accommodated, including flexibility about visitor numbers and ceremony.

**Common trap:** Applying a Western grief-stage model rigidly and missing kinship and community mourning practices.

**Resource:** [NMBA: Joint statement on culturally safe care](https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/position-statements.aspx)

*NCLEX category: Psychosocial Integrity · practise in: Professional practice · generate: `--id 70`*

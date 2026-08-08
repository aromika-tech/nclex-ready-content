"""NCLEX Ready, 10-week educational content curriculum (70 topics).

Mapped to the 2026 NCLEX-RN Test Plan (effective April 2026), with topic counts
allocated by the blueprint's percentage midpoints so the teaching schedule mirrors
what the exam actually weights:

  Management of Care                        15-21%  -> 13 topics
  Pharmacological and Parenteral Therapies  13-19%  -> 11 topics
  Physiological Adaptation                  11-17%  -> 10 topics
  Safety and Infection Prevention & Control 10-16%  ->  9 topics
  Reduction of Risk Potential                9-15%  ->  8 topics
  Basic Care and Comfort                     6-12%  ->  7 topics
  Health Promotion and Maintenance           6-12%  ->  6 topics
  Psychosocial Integrity                     6-12%  ->  6 topics
                                                      -----------
                                                        70 topics

Every topic carries an `au` note stating Australian practice, units, terminology or
guidance directly, and a verified free resource. These notes state the Australian norm.
They never frame it as a translation of, or a comparison with, anything else.

TEMPLATE CODES
  fact      Single-fact card        one number or rule, high save value
  qotd      Question of the day     stem on the card, answer invited in comments
  mnemonic  Mnemonic card           acronym + expansion
  ref       Reference card          lab values / ranges in SI units, highest save value
  compare   Comparison card         two conditions or concepts side by side
  drug      Drug card               class / action / monitoring / nursing considerations
  auvs      Australian practice card what it is called here, and the units used here
  carousel  Teaching carousel       5 slides: hook, promise, 3 teaching beats, summary
"""

# cat = NCLEX client-needs category; nr_cat = matching NCLEX Ready practice category
TOPICS = [

# ─────────────────────────── WEEK 1: Thinking like a nurse ───────────────────
dict(id=1, week=1, day=1, cat="Management of Care", nr_cat="Professional practice",
     template="mnemonic", title="Prioritisation: why ABC beats everything else",
     hook="When two patients both need you, the order is not a judgement call.",
     facts=["Airway, then Breathing, then Circulation, ABC overrides Maslow whenever both apply.", "Unstable beats stable. A change in condition outranks an abnormal but stable baseline.", "Actual problems generally outrank potential ones, unless the potential problem is airway.", "Read the stem carefully: 'first' action and 'best' action are different questions."],
     au="Australian emergency departments triage on the Australasian Triage Scale (ATS 1-5).",
     trap="Choosing the most thorough action when the question asked for the first action.",
     res="ACSQHC: Recognising and responding to acute deterioration",
     url="https://www.safetyandquality.gov.au/our-work/recognising-and-responding-to-acute-deterioration"),

dict(id=2, week=1, day=2, cat="Management of Care", nr_cat="Professional practice",
     template="carousel", title="Delegation: what you can and cannot hand over",
     hook="You can delegate the task. You can never delegate the accountability.",
     facts=["Delegate only what sits inside the other person's role and competence, and needs no nursing judgement.", "Never delegate assessment, initial patient education, or a clinical judgement call.", "The RN stays accountable for the decision to delegate and for the supervision.", "Check the five rights: right task, circumstance, person, direction, supervision."],
     au="Australia's skill mix is RN, Enrolled Nurse and Assistant in Nursing. An EN works under the "
        "direction of an RN and is implementation-focused, so an EN does not independently assess or plan care.",
     trap="Assuming an Enrolled Nurse can do an initial assessment because they are registered.",
     res="NMBA: Enrolled Nurse Standards for Practice",
     url="https://www.nursingmidwiferyboard.gov.au/Codes-Guidelines-Statements/Professional-standards/enrolled-nurse-standards-for-practice.aspx"),

dict(id=3, week=1, day=3, cat="Management of Care", nr_cat="Professional practice",
     template="auvs", title="Scope of practice: the question to ask before you act",
     hook="Scope is set by your education and competence, not by your job title.",
     facts=["Scope of practice comes from education, competence, context and law together.", "If you are unsure whether something is in scope, seek supervision before acting, not after.", "'I have seen other nurses do it' is never the test of whether you are authorised.", "Document the decision and who you consulted."],
     au="Australia uses the NMBA's national Decision-Making Framework, a set of structured questions you work "
        "through before performing an activity, covering education, competence, authorisation and evidence.",
     trap="Treating a local ward habit as authorisation.",
     res="NMBA: Decision-Making Framework",
     url="https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/frameworks.aspx"),

dict(id=4, week=1, day=4, cat="Management of Care", nr_cat="Professional practice",
     template="mnemonic", title="ISBAR: the handover structure that is mandated here",
     hook="Most handover failures are missing the last letter.",
     facts=["Identify, yourself, your role and the patient.", "Situation, why you are calling, right now, in one sentence.", "Background, only the history that bears on this problem.", "Assessment, your findings and observations.", "Recommendation, what you are actually asking for. Say it out loud."],
     au="ISBAR is mandated nationally under NSQHS Standard 6 (Communicating for Safety) and is an accreditation "
        "requirement in Australian hospitals, so it is the expected structure for every escalation call.",
     trap="Leaving out the Recommendation and hoping the other person infers what you need.",
     res="ACSQHC: ISBAR resources",
     url="https://www.safetyandquality.gov.au/publications-and-resources/resource-library/isbar-poster"),

dict(id=5, week=1, day=5, cat="Management of Care", nr_cat="Professional practice",
     template="fact", title="Informed consent: whose job is it",
     hook="The nurse witnesses consent. The nurse does not obtain it.",
     facts=["Valid consent needs capacity, voluntariness, enough information, and it must be specific to the procedure.", "The person performing the procedure is responsible for obtaining consent.", "The nurse's role is to verify understanding and that the form is complete.", "Consent can be withdrawn at any time, including after the form is signed."],
     au="There is no single national consent law in Australia. Each state and territory has its own guardianship "
        "and consent legislation, so capacity and substitute consent processes vary by jurisdiction.",
     trap="Proceeding because the form is signed, when the patient no longer understands what is planned.",
     res="End of Life Law in Australia: Capacity and consent",
     url="https://end-of-life.qut.edu.au/treatment-decisions/adults/state-and-territory-laws"),

dict(id=6, week=1, day=6, cat="Management of Care", nr_cat="Professional practice",
     template="qotd", title="Advance care directives and who decides",
     hook="The family disagrees with the directive. What happens?",
     facts=["A valid advance care directive made while the person had capacity overrides family preference.", "With no directive, decisions pass to the legally recognised substitute decision-maker in order.", "A substitute decision-maker must act on the person's known wishes, not their own view.", "Next of kin is not automatically the legal decision-maker."],
     au="Terminology is state-based: 'Person Responsible' in NSW, 'Medical Treatment Decision Maker' in Victoria, "
        "'Enduring Guardian' elsewhere. There is no single national living-will equivalent.",
     trap="Following the loudest family member instead of the correctly ranked decision-maker.",
     res="End of Life Law in Australia: State and territory laws",
     url="https://end-of-life.qut.edu.au/treatment-decisions/adults/state-and-territory-laws"),

dict(id=7, week=1, day=7, cat="Management of Care", nr_cat="Professional practice",
     template="fact", title="Advocacy: representing their wishes, not your opinion",
     hook="Advocacy means their choice, even when you would choose differently.",
     facts=["Advocacy is representing what the patient wants, not what you think is best for them.", "Support a competent adult's right to refuse treatment, and document it.", "Escalate unresolved safety concerns up the chain of command rather than working around them.", "Cultural safety is judged by the patient, not by the clinician."],
     au="Cultural safety is an explicit obligation in the NMBA Code of Conduct, including a specific requirement "
        "to provide culturally safe care for Aboriginal and Torres Strait Islander Peoples.",
     trap="Overriding an informed refusal because you believe you are advocating for their health.",
     res="NMBA: Code of Conduct for Nurses",
     url="https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/code-of-conduct.aspx"),

# ─────────────────────── WEEK 2: Legal, ethical and professional ─────────────
dict(id=8, week=2, day=1, cat="Management of Care", nr_cat="Professional practice",
     template="fact", title="Confidentiality: need-to-know, every time",
     hook="No names in the lift. No details in the tearoom.",
     facts=["Share information only with those involved in the person's care, only as far as needed.", "De-identified is not the same as unidentifiable, a detailed story can still identify someone.", "Never discuss patients on social media, even without a name.", "Patients generally have a right to access their own health record."],
     au="Australia is governed by the Privacy Act 1988 and the Australian Privacy Principles, plus state health "
        "records legislation. My Health Record has its own access and consent rules.",
     trap="Assuming family have a right to information because they are next of kin.",
     res="OAIC, Australian Privacy Principles",
     url="https://www.oaic.gov.au/privacy/australian-privacy-principles"),

dict(id=9, week=2, day=2, cat="Management of Care", nr_cat="Professional practice",
     template="compare", title="Who to refer to, and when",
     hook="Coordinating care is a skill the exam tests directly.",
     facts=["Dietitian, nutrition risk, enteral feeding, malnutrition screening.", "Social worker, psychosocial need, housing, financial and discharge support.", "Physiotherapist and occupational therapist, mobility, function, equipment and home assessment.", "Pharmacist, medication reconciliation, interactions, discharge medicines."],
     au="Community allied health is often accessed through a GP Chronic Disease Management Plan, which "
        "attracts Medicare rebates for a set number of sessions.",
     trap="Managing it yourself when a scope-appropriate referral is clearly indicated.",
     res="Australian Government: My Health Record",
     url="https://www.myhealthrecord.gov.au"),

dict(id=10, week=2, day=3, cat="Management of Care", nr_cat="Professional practice",
     template="fact", title="Discharge planning starts on admission",
     hook="If discharge planning starts on discharge day, it has already failed.",
     facts=["Begin planning at admission, not on the morning of discharge.", "Confirm the person understands medicines, follow-up and the red flags that mean 'come back'.", "Use teach-back, ask them to explain it to you, rather than asking 'do you understand?'.", "Check equipment and supports are actually in place before they leave."],
     au="Aged care and disability supports are arranged through My Aged Care and the NDIS, with ACAT assessment "
        "determining aged-care eligibility.",
     trap="Recording education as complete because a pamphlet was handed over.",
     res="My Aged Care",
     url="https://www.myagedcare.gov.au"),

dict(id=11, week=2, day=4, cat="Management of Care", nr_cat="Professional practice",
     template="qotd", title="Ethical conflict and conscientious objection",
     hook="You object to the procedure. Can you step away?",
     facts=["Autonomy generally prevails for a competent adult, even when the team disagrees.", "You may conscientiously object, but you must not abandon the patient, arrange handover of care.", "Resolve conflict through documented escalation, never unilateral action.", "Personal discomfort is not the same as a clinical reason to withhold care."],
     au="Ethical obligations are codified nationally in the NMBA Code of Conduct, which applies in every "
        "state and territory.",
     trap="Withdrawing care without ensuring someone else has taken it over.",
     res="NMBA: Code of Conduct for Nurses",
     url="https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/code-of-conduct.aspx"),

dict(id=12, week=2, day=5, cat="Management of Care", nr_cat="Professional practice",
     template="auvs", title="Mandatory notification: an obligation unique to here",
     hook="In Australia, reporting an impaired colleague can be a legal duty.",
     facts=["Notifiable conduct includes practising while intoxicated, sexual misconduct, significant departure "
            "from accepted standards, and impairment placing the public at substantial risk.", "This sits alongside, not instead of, state child protection reporting laws.", "Document objectively and factually. Never alter a record after an incident.", "Notification is about public risk, not punishment."],
     au="AHPRA mandatory notification is a defined legal obligation on every registered practitioner in "
        "Australia, made directly to the regulator.",
     trap="Treating an impaired colleague as an internal HR matter only.",
     res="AHPRA: Mandatory notifications",
     url="https://www.ahpra.gov.au/Notifications/mandatorynotifications.aspx"),

dict(id=13, week=2, day=6, cat="Management of Care", nr_cat="Professional practice",
     template="fact", title="Open disclosure: saying sorry is not admitting liability",
     hook="Something went wrong. The patient is told, promptly, and honestly.",
     facts=["Report incidents and near-misses regardless of whether harm occurred.", "Root cause analysis looks for system causes, not someone to blame.", "Open disclosure means an honest explanation, an apology, and what will change.", "Near-misses are reported precisely because no one was hurt this time."],
     au="Open disclosure is a formal national requirement under the NSQHS Standards and the Australian Open "
        "Disclosure Framework. Under most state Civil Liability Acts an apology is not an admission of liability.",
     trap="Staying silent about a near-miss because the patient was not harmed.",
     res="ACSQHC, Australian Open Disclosure Framework",
     url="https://www.safetyandquality.gov.au/our-work/open-disclosure/the-open-disclosure-framework"),

dict(id=14, week=2, day=7, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="mnemonic", title="The 5 Moments for Hand Hygiene",
     hook="Five moments. Most missed is the one after touching the surroundings.",
     facts=["1, before touching a patient.", "2, before a clean or aseptic procedure.", "3, after a body fluid exposure risk.", "4, after touching a patient.", "5, after touching the patient's surroundings."],
     au="Delivered nationally through Hand Hygiene Australia with mandatory audit and compliance reporting feeding "
        "into NSQHS Standard 3 accreditation.",
     trap="Using alcohol rub after caring for a patient with C. difficile. Spores need soap and water.",
     res="Hand Hygiene Australia, 5 Moments",
     url="https://hha.org.au/hand-hygiene/5-moments-for-hand-hygiene"),

# ─────────────────── WEEK 3: Infection prevention and safety ─────────────────
dict(id=15, week=3, day=1, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="compare", title="Contact, droplet or airborne: matching the precaution",
     hook="Match the organism to the precaution. This is a guaranteed exam pattern.",
     facts=["Contact. MRSA, VRE, C. difficile, scabies. Gown and gloves, dedicated equipment.", "Droplet, influenza, pertussis, mumps, meningococcal. Surgical mask, eye protection if splash risk.", "Airborne, tuberculosis, measles, varicella. Fit-tested P2/N95 and a negative pressure room.", "Some need both: varicella is contact plus airborne."],
     au="Australia says P2/N95 respirator, and follows the NHMRC Australian Guidelines for the Prevention and "
        "Control of Infection in Healthcare.",
     trap="A surgical mask for suspected tuberculosis or measles. It must be a fit-tested respirator.",
     res="NHMRC, Australian Guidelines for the Prevention and Control of Infection in Healthcare",
     url="https://www.nhmrc.gov.au/about-us/publications/australian-guidelines-prevention-and-control-infection-healthcare-2019"),

dict(id=16, week=3, day=2, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="auvs", title="ANTT: the term used here instead of 'sterile technique'",
     hook="Key parts and key sites. Protect those and you have protected the patient.",
     facts=["Identify the key parts (needle tip, catheter hub) and key sites (the insertion site).", "Those are what must never be touched or contaminated.", "Standard ANTT covers short, simple procedures such as peripheral IV insertion.", "Surgical ANTT covers complex or prolonged procedures such as central line insertion."],
     au="Aseptic Non-Touch Technique is the nationally endorsed framework in Australia and is embedded in NSQHS "
        "Standard 3 competency assessment, and it is the language used on Australian competency documents.",
     trap="Treating every aseptic procedure as needing full surgical technique.",
     res="ACSQHC: Preventing and Controlling Infections Standard",
     url="https://www.safetyandquality.gov.au/standards/nsqhs-standards/preventing-and-controlling-healthcare-associated-infection-standard"),

dict(id=17, week=3, day=3, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="fact", title="Multi-resistant organisms and stewardship",
     hook="Resistance is a system problem, not just a prescribing one.",
     facts=["MROs include MRSA, VRE, CRE and ESBL-producing organisms, contact precautions, often single room.", "Stewardship means the narrowest effective agent, right dose, right duration, de-escalated on cultures.", "Screen high-risk admissions, including recent hospitalisation overseas.", "MRO status persists until formal clearance criteria are met."],
     au="National surveillance runs through ACSQHC's AURA system, and stewardship is mandated under NSQHS "
        "Standard 3 rather than left to individual hospital programmes.",
     trap="Standing precautions down because the infection was treated.",
     res="ACSQHC, Antimicrobial stewardship",
     url="https://www.safetyandquality.gov.au/our-work/antimicrobial-stewardship"),

dict(id=18, week=3, day=4, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="fact", title="Sharps injury: the first five minutes",
     hook="Wash it. Report it now. Do not squeeze it.",
     facts=["Wash the wound with soap and water. Do not squeeze or suck it. Irrigate mucosal exposure.", "Report immediately, not at the end of the shift.", "Source and exposed worker are tested with consent for HIV, hepatitis B and hepatitis C.", "HIV post-exposure prophylaxis works best started within hours, and within 72 hours."],
     au="Managed under state health department policy and notified through the state SafeWork regulator. "
        "Hepatitis B vaccination and titre checks are a standard Australian pre-employment requirement.",
     trap="Waiting until the shift ends to report, and losing the prophylaxis window.",
     res="NSW Health: Occupational exposure to blood-borne viruses",
     url="https://www.health.nsw.gov.au/policies"),

dict(id=19, week=3, day=5, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="fact", title="Manual handling: use the hoist",
     hook="The correct answer is almost never 'get another nurse to lift'.",
     facts=["Assess the task, the individual, the load and the environment before moving anyone.", "Use mechanical aids, hoists and slide sheets, wherever they are available.", "Manual lifting of a patient's full weight is not routine practice.", "Manual handling injury is a leading cause of nursing workplace injury."],
     au="Governed by Safe Work Australia's model Code of Practice on Hazardous Manual Tasks under state WHS Acts, "
        "which sets out the assess-and-control duty in detail.",
     trap="Choosing a two-person manual lift when a hoist is available and indicated.",
     res="Safe Work Australia: Hazardous Manual Tasks Code of Practice",
     url="https://www.safeworkaustralia.gov.au/doc/model-code-practice-hazardous-manual-tasks"),

dict(id=20, week=3, day=6, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="auvs", title="Restrictive practices: last resort, always reviewed",
     hook="A lap belt can be a restrictive practice. Intent and effect decide.",
     facts=["Restraint may be physical, chemical, mechanical or environmental, and is always a last resort.", "Try and document less restrictive alternatives first.", "Orders are time-limited and reviewed. Never open-ended PRN.", "Document the rationale, the alternatives tried and the effect on the person."],
     au="Australia regulates these formally as 'restrictive practices', through the NDIS Quality and Safeguards "
        "Commission for disability, and state Mental Health Acts for mental health. Reduction targets sit in "
        "NSQHS Standard 5, as a rights-based national scheme.",
     trap="Assuming bed rails are automatically not a restraint.",
     res="NDIS Commission: Regulated Restrictive Practices",
     url="https://www.ndiscommission.gov.au/providers/registered-ndis-providers/provider-responsibilities/behaviour-support"),

dict(id=21, week=3, day=7, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="mnemonic", title="RACE: the fire response order",
     hook="Rescue. Alert. Contain. Extinguish, and only if it is safe.",
     facts=["Rescue, move anyone in immediate danger.", "Alert, activate the alarm and call the emergency number.", "Contain, close doors and windows to slow the spread.", "Extinguish only if the fire is small and you are trained. Otherwise evacuate.", "Horizontal evacuation through fire doors comes before vertical evacuation."],
     au="Australian hospitals use EWIS emergency warning systems with coded alerts under AS 3745, and the "
        "Australasian Triage Scale for mass casualty prioritisation.",
     trap="Trying to extinguish a spreading fire instead of evacuating.",
     res="Fire Protection Association Australia",
     url="https://www.fpaa.com.au/"),

# ──────────────── WEEK 4: Error prevention and medication foundations ────────
dict(id=22, week=4, day=1, cat="Safety and Infection Prevention and Control", nr_cat="Professional practice",
     template="fact", title="Two identifiers, every single time",
     hook="Two identifiers. Never the bed number.",
     facts=["Use two approved identifiers before any medication, procedure or specimen.", "Bed number and room number are never identifiers.", "Falls prevention basics: bed low and locked, call bell in reach, non-slip footwear.", "Report near-misses. They are the free lesson."],
     au="Falls and pressure injury screening are mandated under NSQHS Standard 5, and a deteriorating patient is "
        "escalated with a MET call, any staff member can activate it directly, without waiting for a doctor.",
     trap="Waiting for the treating team before escalating a patient who already meets MET criteria.",
     res="NSW CEC: Between the Flags",
     url="https://www.cec.health.nsw.gov.au/keep-patients-safe/between-the-flags"),

dict(id=23, week=4, day=2, cat="Pharmacological and Parenteral Therapies", nr_cat="Pharmacology",
     template="mnemonic", title="APINCHS: the high-risk medicines acronym used here",
     hook="Seven letters that cover most serious medication harm.",
     facts=["A, Antimicrobials. P. Potassium and other electrolytes. I. Insulin.", "N. Narcotics and sedatives. C. Chemotherapy. H. Heparin and anticoagulants.", "S. Systems, including IV fluids and infusion pumps.", "These require independent double-checking and separated storage."],
     au="APINCHS is the ACSQHC national framework for high-risk medicines, and Australian workplaces name "
        "it directly on charts, storage rules and double-check policies.",
     trap="Believing a double-check alone prevents error. Storage and system design matter just as much.",
     res="ACSQHC: High risk medicines",
     url="https://www.safetyandquality.gov.au/our-work/medicines-safety-and-quality/high-risk-medicines"),

dict(id=24, week=4, day=3, cat="Pharmacological and Parenteral Therapies", nr_cat="Endocrine",
     template="drug", title="Insulin: onset, peak, duration and the 15/15 rule",
     hook="Rapid-acting peaks in 1 to 2 hours. Know when the risk lands.",
     facts=["Rapid-acting: onset 10-15 min, peak 1-2 h, duration 3-5 h. Give with or immediately before food.", "Short-acting: onset ~30 min, peak 2-4 h, duration 6-8 h.", "Long-acting: onset 1-2 h, no pronounced peak, about 24 h. Never mix with another insulin.", "Hypoglycaemia below 4 mmol/L: 15 g fast carbohydrate, recheck in 15 minutes.", "Severe or unconscious: IM glucagon or IV glucose."],
     au="Blood glucose is measured in mmol/L. A BGL of 3.2 mmol/L is hypoglycaemia and needs treating. "
        "Australian brand names include NovoRapid, Actrapid and Lantus.",
     trap="Seeing a single-digit BGL and not recognising it as hypoglycaemia.",
     res="Australian Prescriber",
     url="https://australianprescriber.tg.org.au"),

dict(id=25, week=4, day=4, cat="Pharmacological and Parenteral Therapies", nr_cat="Cardiovascular",
     template="compare", title="Warfarin versus heparin: monitoring and reversal",
     hook="Different test. Different antidote. Do not mix them up.",
     facts=["Warfarin, monitored by INR, usually target 2.0-3.0. Reversal is vitamin K, plus prothrombinex if bleeding.", "Unfractionated heparin, monitored by APTT. Reversal is protamine sulfate.", "Low molecular weight heparin needs no routine APTT; use anti-Xa if renal impairment, obesity or pregnancy.", "Check platelets, heparin-induced thrombocytopenia is a real risk.", "Teach consistent vitamin K intake with warfarin, not avoidance of greens."],
     au="Vitamin K is called phytomenadione here (Konakion). Warfarin management guidance follows Australian "
        "Prescriber and local anticoagulation protocols.",
     trap="Giving vitamin K for a high INR with no bleeding, without checking the local threshold.",
     res="Australian Prescriber: Managing warfarin therapy",
     url="https://australianprescriber.tg.org.au"),

dict(id=26, week=4, day=5, cat="Pharmacological and Parenteral Therapies", nr_cat="Pharmacology",
     template="fact", title="Opioids: sedation score before respiratory rate",
     hook="Sedation comes before respiratory depression. That is your early warning.",
     facts=["Assess respiratory rate and sedation score before every dose.", "Hold and escalate for a respiratory rate under 10, or rising sedation score.", "Naloxone has a shorter half-life than most opioids, re-sedation is common, so keep monitoring.", "Titrate naloxone in small increments to restore breathing without precipitating severe pain.", "Prescribe a laxative alongside, and monitor bowels."],
     au="Intranasal naloxone (Nyxoid) is TGA-approved and available through take-home naloxone programmes in "
        "Australian pharmacies. Brand names differ. Endone is oxycodone, Kapanol is modified-release morphine.",
     trap="Withholding all analgesia for mild sedation instead of adjusting the dose and continuing to monitor.",
     res="Australian Prescriber: Naloxone in the community",
     url="https://australianprescriber.tg.org.au"),

dict(id=27, week=4, day=6, cat="Pharmacological and Parenteral Therapies", nr_cat="Pharmacology",
     template="drug", title="Vancomycin and gentamicin: the monitoring drugs",
     hook="Red and flushed during a vancomycin infusion is usually a rate problem.",
     facts=["Aminoglycosides such as gentamicin cause dose-related ototoxicity and nephrotoxicity, monitor renal function and levels.", "Vancomycin needs trough monitoring and an infusion over at least 60 minutes.", "Infusion-related flushing is histamine-mediated and rate-related, not a true allergy, slow the infusion.", "Report new tinnitus, hearing change, falling urine output or rising creatinine immediately."],
     au="Antibiotic choice and dosing follow Therapeutic Guidelines (eTG), the national antimicrobial stewardship "
        "reference.",
     trap="Labelling infusion-rate flushing as anaphylaxis and withholding the drug permanently.",
     res="Australian Prescriber, Aminoglycosides",
     url="https://australianprescriber.tg.org.au"),

dict(id=28, week=4, day=7, cat="Pharmacological and Parenteral Therapies", nr_cat="Renal and fluid",
     template="fact", title="IV potassium is never a push",
     hook="Undiluted IV potassium causes cardiac arrest. There is no exception.",
     facts=["Always dilute, always via an infusion pump. Never an IV push or bolus.", "Peripheral limits are generally up to 40 mmol/L concentration and 10 mmol per hour on a ward.", "Faster rates need cardiac monitoring and a higher level of care.", "Normal range is 3.5-5.2 mmol/L. Low risks arrhythmia and digoxin toxicity; high risks arrest.", "Concentrated ampoules are stored separately and restricted from ward stock."],
     au="Potassium is reported and prescribed in mmol/L, and NSW CEC publishes a specific high-risk "
        "potassium protocol setting concentration and rate limits.",
     trap="Choosing rapid correction by push for severe hypokalaemia. Always wrong.",
     res="NSW CEC: Potassium (intravenous)",
     url="https://www.cec.health.nsw.gov.au/keep-patients-safe/medication-safety/high-risk-medicines"),

# ─────────────── WEEK 5: High-risk medicines and first numbers ───────────────
dict(id=29, week=5, day=1, cat="Pharmacological and Parenteral Therapies", nr_cat="Cardiovascular",
     template="drug", title="Digoxin, beta blockers and ACE inhibitors: check before you give",
     hook="Count the apical pulse for a full minute. Then decide.",
     facts=["Digoxin, hold and escalate for an apical pulse under 60. Count for one full minute.", "Digoxin toxicity: nausea, yellow-green visual halos, arrhythmia. Low potassium makes it worse.", "Beta blockers, hold per order for low heart rate or low blood pressure. Never stop abruptly.", "ACE inhibitors, watch for dry cough, high potassium, first-dose hypotension and angioedema.", "Angioedema is an emergency, not a side effect to monitor."],
     au="Australian brand confusion between digoxin products at different strengths has prompted specific safety "
        "advisories, always check the strength on the chart.",
     trap="Treating an ACE inhibitor cough and angioedema as the same level of concern.",
     res="Australian Prescriber: Digoxin toxicity",
     url="https://australianprescriber.tg.org.au"),

dict(id=30, week=5, day=2, cat="Pharmacological and Parenteral Therapies", nr_cat="Pharmacology",
     template="fact", title="Extravasation: leave the cannula in",
     hook="Stop the infusion. Do not pull the cannula out yet.",
     facts=["Stop immediately, leave the cannula in place briefly to aspirate, then elevate and escalate.", "Use a pump for every high-alert infusion, insulin, heparin, potassium, opioids, chemotherapy.", "Fluid overload signs: breathlessness, crackles, raised JVP, rapid weight gain.", "Grade and document phlebitis using a visual infusion phlebitis score."],
     au="IV fluids sit in the APINCHS 'Systems' category in Australia, so they carry the same high-risk "
        "handling requirements as other APINCHS medicines.",
     trap="Removing the cannula immediately and re-siting further down the same limb.",
     res="ACSQHC: Medicines safety",
     url="https://www.safetyandquality.gov.au/our-work/medicines-safety-and-quality"),

dict(id=31, week=5, day=3, cat="Pharmacological and Parenteral Therapies", nr_cat="Sepsis and critical care",
     template="fact", title="Blood transfusion: the first 15 minutes",
     hook="Stay with them for the first 15 minutes. That is when reactions declare.",
     facts=["Two-person independent identity check against the wristband and the unit immediately before starting.", "Baseline observations before, again at 15 minutes, then per protocol.", "On any suspected reaction: stop, keep the line open with normal saline, escalate, return the unit.", "A unit of red cells generally runs over 1.5 to 2 hours, and never beyond 4.", "Acute haemolytic reaction is usually an identification error, and is the most dangerous."],
     au="Governed by ANZSBT guidelines and Lifeblood processes, with Australian traceability documentation "
        "required for every unit.",
     trap="Watching a little longer before stopping when early reaction signs appear.",
     res="ANZSBT, Administration of blood products",
     url="https://anzsbt.org.au/guidelines/"),

dict(id=32, week=5, day=4, cat="Pharmacological and Parenteral Therapies", nr_cat="Pharmacology",
     template="ref", title="Medication calculation without the 1000-fold error",
     hook="Convert the units first. Every time.",
     facts=["Dose required divided by dose available, multiplied by the volume.", "Infusion rate in mL/h = total volume divided by time in hours.", "Drops per minute = volume x drop factor, divided by time in minutes.", "Weight-based dosing uses an accurate current weight in kilograms.", "Convert micrograms and milligrams before you calculate, not during."],
     au="Weight is always in kilograms and volumes are metric. The National Inpatient Medication Chart standardises "
        "how doses are written and checked.",
     trap="Forgetting a microgram to milligram conversion mid-calculation, a 1000-fold error.",
     res="ACSQHC: National standard medication charts",
     url="https://www.safetyandquality.gov.au/our-work/medicines-safety-and-quality/national-standard-medication-charts"),

dict(id=33, week=5, day=5, cat="Pharmacological and Parenteral Therapies", nr_cat="Sepsis and critical care",
     template="fact", title="Anaphylaxis: adrenaline first, into the thigh",
     hook="Adrenaline. Intramuscular. Anterolateral thigh. Nothing before it.",
     facts=["Adult dose 0.5 mg IM (0.5 mL of 1:1000) into the anterolateral thigh, repeated every 5 minutes if needed.", "Lay the person flat and raise the legs unless they are in respiratory distress. Do not sit them up suddenly.", "Then airway, oxygen, IV fluids and continuous monitoring.", "Antihistamines and steroids are adjuncts only. Never first-line.", "Anaphylaxis is rapid onset, multi-system, with airway or circulatory compromise."],
     au="The drug is called adrenaline, and management follows ANZCOR Guideline 9.2.7.",
     trap="Giving an antihistamine first while assessing severity.",
     res="ANZCOR: Guideline 9.2.7 Anaphylaxis",
     url="https://www.anzcor.org/home/first-aid-management-of-medical-conditions/guideline-9-2-7-first-aid-management-of-anaphylaxis/"),

dict(id=34, week=5, day=6, cat="Reduction of Risk Potential", nr_cat="Professional practice",
     template="auvs", title="Track and trigger: escalation is not optional",
     hook="Two yellows or one red. The chart tells you what to do.",
     facts=["Normal adult ranges: respiratory rate 12-20, heart rate 60-100, SpO2 at or above 95% unless a target is set.", "A track-and-trigger chart colours each observation and defines the required response.", "Escalation is a defined pathway, not a judgement call.", "A rising respiratory rate over hours predicts deterioration before saturations fall.", "Trends matter more than any single reading."],
     au="Australia uses colour-zoned observation charts under Between the Flags, and deterioration is "
        "escalated by MET call.",
     trap="Being reassured by one abnormal observation because the others look fine.",
     res="NSW CEC: Observation charts",
     url="https://www.cec.health.nsw.gov.au/keep-patients-safe/between-the-flags"),

dict(id=35, week=5, day=7, cat="Reduction of Risk Potential", nr_cat="Professional practice",
     template="ref", title="Australian lab reference ranges in SI units",
     hook="Haemoglobin is reported in g/L. For a man, 130 to 170 g/L is the normal range.",
     facts=["Sodium 135-145 mmol/L. Potassium 3.5-5.2 mmol/L.", "Fasting glucose about 4.0-7.8 mmol/L.", "Creatinine roughly 60-110 micromol/L in men, 45-90 in women.", "Haemoglobin 130-170 g/L in men, 115-155 g/L in women.", "Platelets 150-400 x10^9/L. White cells 4.0-11.0 x10^9/L."],
     au="Australian pathology reports in SI units, mmol/L, micromol/L and g/L, and the reference "
        "intervals are locally harmonised. Always check your own laboratory's stated range as well.",
     trap="Treating a haemoglobin of 140 g/L as abnormal when it sits mid-range.",
     res="RCPA: Harmonised reference intervals",
     url="https://www.rcpa.edu.au/Manuals/RCPA-Manual"),

# ──────────────── WEEK 6: Assessment, deterioration and the heart ────────────
dict(id=36, week=6, day=1, cat="Reduction of Risk Potential", nr_cat="Respiratory",
     template="mnemonic", title="ABG interpretation with ROME",
     hook="Respiratory Opposite. Metabolic Equal. That is the whole method.",
     facts=["Normal: pH 7.35-7.45, PaCO2 35-45 mmHg, bicarbonate 22-26 mmol/L.", "Respiratory Opposite, pH and CO2 move in opposite directions.", "Metabolic Equal, pH and bicarbonate move in the same direction.", "Partial compensation means the pH is still abnormal; full means pH is normal but the values are not.", "Always interpret alongside the patient, never the paper alone."],
     au="Australian laboratories may report gases in kPa as well as mmHg depending on the analyser. Check the unit "
        "before interpreting, 1 kPa is about 7.5 mmHg.",
     trap="Reading a kPa value as mmHg and reversing the interpretation.",
     res="Australian Prescriber: Interpreting arterial blood gases",
     url="https://australianprescriber.tg.org.au"),

dict(id=37, week=6, day=2, cat="Reduction of Risk Potential", nr_cat="Perioperative",
     template="fact", title="Fasting before surgery: 6 and 2",
     hook="Six hours for food. Two hours for clear fluids. Not midnight.",
     facts=["Standard adult fasting is 6 hours for solids and 2 hours for clear fluids before elective anaesthesia.", "Pre-op checklist: consent verified, site marked, allergies confirmed, baseline observations, prostheses removed.", "Post-op priority order: airway and breathing, then circulation and bleeding, then pain, then wound and drains.", "Report urine output under 0.5 mL/kg/hour as a perfusion warning."],
     au="Fasting and pre-anaesthetic standards follow ANZCA, and GLP-1 agonist users have specific "
        "Australian periprocedural advice because of delayed gastric emptying.",
     trap="Applying an outdated nil-by-mouth-from-midnight rule.",
     res="ANZCA: Pre-anaesthesia consultation and patient preparation",
     url="https://www.anzca.edu.au/safety-advocacy/standards-of-practice/professional-documents"),

dict(id=38, week=6, day=3, cat="Reduction of Risk Potential", nr_cat="Renal and fluid",
     template="qotd", title="Contrast, metformin and the shellfish myth",
     hook="Which allergy actually matters before a contrast CT?",
     facts=["Check renal function and metformin status before iodinated contrast.", "Metformin is generally withheld around contrast in reduced renal function and restarted once function is confirmed stable.", "Screen for ferromagnetic implants and device compatibility before MRI.", "Shellfish allergy is not an evidence-based contraindication. Prior contrast reaction is the real risk factor.", "Hydrate before and after in at-risk patients."],
     au="Contrast safety follows the RANZCR iodinated contrast guideline, which sets the eGFR thresholds "
        "and metformin hold times used here.",
     trap="Cancelling contrast because the patient mentioned a shellfish allergy.",
     res="RANZCR: Iodinated contrast media guideline",
     url="https://www.ranzcr.com/college/document-library"),

dict(id=39, week=6, day=4, cat="Reduction of Risk Potential", nr_cat="Perioperative",
     template="fact", title="Never clamp a bubbling chest drain",
     hook="Clamping a bubbling drain can cause a tension pneumothorax.",
     facts=["Keep the drainage unit below chest level at all times.", "Gentle swinging with respiration is expected. Continuous bubbling suggests an air leak.", "No swinging can mean a blockage, or that the lung has re-expanded.", "Never clamp a bubbling drain, including during transfer.", "Secure all tubing and document output every shift."],
     au="None material, the principles are universal, though each health service has its own nursing procedure.",
     trap="Clamping the drain to move the patient.",
     res="Royal Children's Hospital: Chest drain management",
     url="https://www.rch.org.au/rchcpg/hospital_clinical_guideline_index/Chest_drain_management/"),

dict(id=40, week=6, day=5, cat="Reduction of Risk Potential", nr_cat="Perioperative",
     template="fact", title="Complications to anticipate after common procedures",
     hook="Post-procedure back pain and low blood pressure is not 'normal recovery'.",
     facts=["After lumbar puncture, positional headache, and rarely new leg weakness needing urgent review.", "After cardiac catheterisation, check the site and distal pulses; back pain with hypotension suggests retroperitoneal bleed.", "After bronchoscopy, nil by mouth until the gag reflex returns.", "After paracentesis, watch for hypotension from rapid fluid shifts."],
     au="None material for recognition; documentation goes through Australian incident and clinical governance systems.",
     trap="Attributing post-procedure hypotension to opioids without excluding bleeding.",
     res="Queensland Health: Clinical guidelines",
     url="https://www.health.qld.gov.au/clinical-practice/guidelines-procedures"),

dict(id=41, week=6, day=6, cat="Reduction of Risk Potential", nr_cat="Renal and fluid",
     template="qotd", title="Catheters: review the need every day",
     hook="The best way to prevent a catheter infection is to remove the catheter.",
     facts=["Keep the bag below bladder level and the system closed.", "Review the need for the catheter daily and remove as soon as it is clinically appropriate.", "Bladder scan if there has been no void 6-8 hours post-operatively or after removal.", "In older adults, a urinary tract infection may present as new confusion rather than dysuria."],
     au="Insertion follows Aseptic Non-Touch Technique, the standard Australian framework and terminology.",
     trap="Re-catheterising without scanning first.",
     res="Continence Health Australia",
     url="https://www.continence.org.au/"),

dict(id=42, week=6, day=7, cat="Physiological Adaptation", nr_cat="Cardiovascular",
     template="carousel", title="Acute coronary syndrome: the first ten minutes",
     hook="A 12-lead ECG within 10 minutes. That is the standard.",
     facts=["Classic pain is central, heavy, over 20 minutes and unrelieved by rest, but women, older adults and people with diabetes often present atypically.", "12-lead ECG within 10 minutes of arrival, then serial troponin.", "Aspirin 300 mg chewed unless contraindicated, GTN, IV access, continuous monitoring.", "Oxygen only if saturations are low, routine oxygen is no longer given.", "Targets: door to balloon under 90 minutes for PCI."],
     au="Diagnostic pathways follow Heart Foundation and Cardiac Society of Australia and New Zealand high-sensitivity "
        "troponin protocols, resuscitation follows ANZCOR, and the emergency number is 000.",
     trap="Giving oxygen to every chest pain patient regardless of saturation.",
     res="Heart Foundation: Clinical guidelines",
     url="https://www.heartfoundation.org.au/for-professionals"),

# ────────────────── WEEK 7: The big physiological emergencies ────────────────
dict(id=43, week=7, day=1, cat="Physiological Adaptation", nr_cat="Cardiovascular",
     template="fact", title="Heart failure: the daily weight is the early warning",
     hook="Two kilograms in two days is fluid, not food.",
     facts=["Left-sided: breathlessness, orthopnoea, waking breathless at night, crackles.", "Right-sided: peripheral oedema, raised JVP, enlarged liver.", "Daily weight is the most sensitive monitor, a gain over 2 kg in 2 days signals retention.", "Sit them upright, give the prescribed diuretic, restrict sodium and often fluid.", "Monitor potassium and renal function, loop diuretics drop potassium."],
     au="The medication is spelled frusemide on Australian charts, not furosemide. Guidance comes from the Heart "
        "Foundation and CSANZ.",
     trap="Giving a fluid bolus to a breathless heart failure patient.",
     res="Heart Foundation: Heart failure guidelines",
     url="https://www.heartfoundation.org.au/for-professionals"),

dict(id=44, week=7, day=2, cat="Physiological Adaptation", nr_cat="Neurological",
     template="carousel", title="Stroke: the clock starts at last known well",
     hook="Nil by mouth until someone has done the swallow screen.",
     facts=["Use FAST to recognise: Face, Arm, Speech, Time.", "Thrombolysis window is within 4.5 hours of a clearly known onset.", "Thrombectomy can extend to around 24 hours for selected large-vessel occlusions with favourable imaging.", "Blood pressure must be below 185/110 before thrombolysis.", "Nil by mouth, including medications, until a formal swallow screen is done."],
     au="Australia follows the Stroke Foundation's Living Clinical Guidelines, which are "
        "continuously updated as new evidence lands.",
     trap="Assuming every stroke gets thrombolysis. A bleed must be excluded on CT first.",
     res="Stroke Foundation: Living Clinical Guidelines",
     url="https://informme.org.au/guidelines/living-clinical-guidelines-for-stroke-management"),

dict(id=45, week=7, day=3, cat="Physiological Adaptation", nr_cat="Respiratory",
     template="auvs", title="Oxygen targets: when 88 to 92 percent is the goal",
     hook="More oxygen is not always better. Sometimes it is the harm.",
     facts=["General target is 92-96%.", "For people at risk of carbon dioxide retention, the target is 88-92% with controlled delivery.", "Over-oxygenating a CO2 retainer can worsen hypercapnia and precipitate respiratory failure.", "In decompensation with pH 7.25-7.35, consider non-invasive ventilation.", "Oxygen is a drug, it is prescribed with a written target range."],
     au="Australian practice prescribes oxygen against a documented target range following Thoracic Society of "
        "Australia and New Zealand guidance, which is more explicit than ad-hoc high-flow practice elsewhere.",
     trap="Turning oxygen up because a COPD patient sits at 90%.",
     res="Australian Prescriber, Acute oxygen therapy",
     url="https://australianprescriber.tg.org.au"),

dict(id=46, week=7, day=4, cat="Physiological Adaptation", nr_cat="Respiratory",
     template="fact", title="A silent chest in asthma is an emergency",
     hook="No wheeze does not mean better. Sometimes it means barely moving air.",
     facts=["Life-threatening signs: silent chest, cyanosis, exhaustion, confusion, poor respiratory effort.", "First line is salbutamol by metered dose inhaler with a spacer, as effective as a nebuliser.", "Give systemic corticosteroids early, within the first hour.", "Oxygen target in acute asthma is 92-95%, not the COPD range.", "Absence of wheeze in a distressed patient is critical, not reassuring."],
     au="Severity grading and escalation follow the Australian Asthma Handbook from the National Asthma Council, "
        "and spacer-first practice is emphasised more strongly here.",
     trap="Documenting improvement because the wheeze has stopped.",
     res="Australian Asthma Handbook",
     url="https://www.asthmahandbook.org.au/"),

dict(id=47, week=7, day=5, cat="Physiological Adaptation", nr_cat="Renal and fluid",
     template="fact", title="Acute kidney injury and the sick day rules",
     hook="Some medicines should be paused when someone is unwell and dehydrated.",
     facts=["AKI: creatinine rise of 26.5 micromol/L within 48 hours, or 1.5 times baseline within 7 days, or urine under 0.5 mL/kg/h for 6 hours.", "CKD is staged on eGFR: G1 at or above 90 down to G5 under 15.", "Withhold nephrotoxic and renally cleared drugs during acute illness.", "Watch for hyperkalaemia and fluid overload; strict balance and daily weights."],
     au="eGFR is automatically reported on Australian pathology results, and Kidney Health Australia publishes "
        "'sick day rules' telling patients which medicines to pause during illness, a distinctly Australian resource.",
     trap="Continuing metformin and NSAIDs through dehydration or contrast imaging.",
     res="Kidney Health Australia: CKD Management Handbook",
     url="https://kidney.org.au/health-professionals/ckd-management-handbook"),

dict(id=48, week=7, day=6, cat="Physiological Adaptation", nr_cat="Endocrine",
     template="compare", title="DKA versus HHS: the numbers that separate them",
     hook="Fluids first. Check the potassium. Then insulin.",
     facts=["DKA, glucose usually above 11-14 mmol/L, ketones above 3 mmol/L, pH under 7.3, bicarbonate under 15.", "HHS, glucose often far higher, osmolality above 320, ketones minimal, pH above 7.3.", "Both: IV sodium chloride first, then fixed-rate insulin. Never insulin before fluids.", "Potassium must be at least 3.5 mmol/L before insulin, insulin drives it into cells.", "HHS needs slower correction because of cerebral risk."],
     au="Glucose and ketones are in mmol/L here. Euglycaemic DKA can occur with SGLT2 inhibitors, so a near-normal "
        "glucose does not exclude it.",
     trap="Starting insulin before fluids and before confirming potassium.",
     res="Australian Diabetes Society",
     url="https://www.diabetessociety.com.au/"),

dict(id=49, week=7, day=7, cat="Physiological Adaptation", nr_cat="Sepsis and critical care",
     template="qotd", title="Compensated shock: normal blood pressure, abnormal patient",
     hook="By the time blood pressure falls, compensation has already failed.",
     facts=["Four types: hypovolaemic, cardiogenic, distributive, obstructive.", "Compensated shock shows tachycardia, narrow pulse pressure, delayed capillary refill and cool peripheries, with a normal blood pressure.", "Target mean arterial pressure is generally above 65 mmHg.", "Lactate above 2 mmol/L signals tissue hypoperfusion regardless of blood pressure.", "Reassess after each 250-500 mL bolus rather than giving one large fixed volume."],
     au="Deterioration triggers a MET call, with activation criteria set by the ACSQHC Recognising and "
        "Responding to Acute Deterioration Standard.",
     trap="Waiting for hypotension before escalating.",
     res="ACSQHC, Acute deterioration standard",
     url="https://www.safetyandquality.gov.au/standards/nsqhs-standards/recognising-and-responding-acute-deterioration-standard"),

# ────────────────── WEEK 8: Sepsis, fluids and comfort care ──────────────────
dict(id=50, week=8, day=1, cat="Physiological Adaptation", nr_cat="Sepsis and critical care",
     template="carousel", title="Sepsis: cultures before antibiotics, antibiotics within the hour",
     hook="Every hour of delay costs. The order still matters.",
     facts=["Red flags: new confusion, systolic under 90, respiratory rate 25 or more, mottled skin, falling urine output.", "Take blood cultures before antibiotics, then give antibiotics, ideally within one hour.", "Give IV fluids, measure lactate, monitor urine output.", "Lactate above 2 mmol/L indicates hypoperfusion and worsens prognosis.", "Septic shock: needing vasopressors for a MAP of 65 plus lactate above 2 despite fluids."],
     au="Australia runs the SEPSIS KILLS pathway and the ACSQHC Sepsis Clinical Care Standard as the "
        "mandated national framework.",
     trap="Giving antibiotics before cultures and losing the diagnosis.",
     res="ACSQHC: Sepsis Clinical Care Standard",
     url="https://www.safetyandquality.gov.au/standards/clinical-care-standards/sepsis-clinical-care-standard"),

dict(id=51, week=8, day=2, cat="Physiological Adaptation", nr_cat="Renal and fluid",
     template="fact", title="Hyperkalaemia: calcium protects the heart first",
     hook="Calcium does not lower the potassium. It protects the heart while you do.",
     facts=["Severe hyperkalaemia above 6.0-6.5 mmol/L: peaked T waves, widening QRS, risk of arrest.", "Give IV calcium gluconate first to stabilise the myocardium.", "Then insulin with glucose, and salbutamol, to shift potassium into cells.", "Correct hyponatraemia slowly, no faster than 8-10 mmol/L in 24 hours, to avoid osmotic demyelination.", "Distinguish overload from deficit before choosing fluid therapy."],
     au="Electrolytes are reported and prescribed in mmol/L throughout Australia.",
     trap="Giving calcium and assuming the potassium is now treated.",
     res="ACSQHC: Medication safety standard",
     url="https://www.safetyandquality.gov.au/standards/nsqhs-standards/medication-safety-standard"),

dict(id=52, week=8, day=3, cat="Basic Care and Comfort", nr_cat="Professional practice",
     template="auvs", title="Pain in dementia: use a behavioural tool",
     hook="If they cannot tell you, you still have to measure it.",
     facts=["Self-report is the gold standard, pain is what the person says it is.", "Numeric rating scale for verbal adults, faces scales for children.", "For non-verbal or advanced dementia, use a validated behavioural tool.", "Reassess about 30-60 minutes after IV analgesia, 60-90 minutes after oral.", "Multimodal analgesia with regular paracetamol reduces opioid need."],
     au="The Abbey Pain Scale was developed in Australia for residential aged care and is the most widely used "
        "Australian tool for dementia-related pain.",
     trap="Withholding analgesia because the observations look too normal for the reported pain.",
     res="Dementia Australia, Abbey Pain Scale",
     url="https://www.dementia.org.au/"),

dict(id=53, week=8, day=4, cat="Basic Care and Comfort", nr_cat="Gastrointestinal",
     template="fact", title="Confirming a nasogastric tube: pH, not a whoosh",
     hook="The whoosh test is not a test. Check the pH.",
     facts=["Confirm placement by pH testing the aspirate, aiming for pH below 5.5, or X-ray if unclear.", "Auscultating injected air is unsafe and outdated.", "Sit the person up 30-45 degrees during feeding and for 30-60 minutes after.", "Screen nutrition risk on admission with a validated tool.", "Watch for refeeding syndrome, check phosphate, potassium and magnesium, and give thiamine."],
     au="The Malnutrition Screening Tool was developed and validated in Queensland and is used as the standard "
        "across most Australian hospitals under the Comprehensive Care Standard.",
     trap="Relying on auscultation to confirm placement before feeding.",
     res="Queensland Health: Malnutrition Screening Tool",
     url="https://www.health.qld.gov.au/nutrition/patient-care"),

dict(id=54, week=8, day=5, cat="Basic Care and Comfort", nr_cat="Gastrointestinal",
     template="ref", title="Bristol stool chart and bowel care that prevents harm",
     hook="Constipation on opioids is predictable. So prevent it.",
     facts=["Document stool form using the Bristol Stool Chart, types 1 to 7.", "Opioids, immobility and low fluid and fibre are the main inpatient risk factors.", "Start a bowel regimen alongside opioids rather than waiting for a problem.", "New confusion in an older adult can be constipation, retention or infection."],
     au="None material, the chart and principles are used internationally.",
     trap="Charting bowels not open for several days without acting on it.",
     res="Continence Health Australia",
     url="https://www.continence.org.au/"),

dict(id=55, week=8, day=6, cat="Basic Care and Comfort", nr_cat="Professional practice",
     template="ref", title="Pressure injury staging in four steps",
     hook="Stage 1 is intact skin that does not blanch. That is the one people miss.",
     facts=["Stage 1, intact skin with non-blanchable redness.", "Stage 2, partial thickness loss, or an open or ruptured blister.", "Stage 3, full thickness, subcutaneous fat visible.", "Stage 4, full thickness with exposed muscle, bone or tendon.", "Also unstageable, and deep tissue pressure injury. Reposition at-risk people at least 2-hourly."],
     au="Falls and pressure injury screening within a set time of admission are mandated under NSQHS Standard 5, "
        "and stage 3 or higher injuries are generally reportable clinical incidents.",
     trap="Recording non-blanchable redness as a bruise.",
     res="ACSQHC: Comprehensive Care Standard",
     url="https://www.safetyandquality.gov.au/standards/nsqhs-standards/comprehensive-care-standard"),

dict(id=56, week=8, day=7, cat="Basic Care and Comfort", nr_cat="Professional practice",
     template="fact", title="Sleep: cluster the care before reaching for sedation",
     hook="The first intervention for poor sleep is not a tablet.",
     facts=["Hospital noise, light and overnight observations are major disruptors, and poor sleep drives delirium.", "Cluster care, medications and observations to protect uninterrupted blocks overnight.", "Minimise sedative hypnotics, especially in older adults, because of falls and delirium risk.", "Use day and night cues, open blinds, encourage daytime activity."],
     au="The Royal Commission into Aged Care Quality and Safety specifically flagged sedation overuse in Australian "
        "residential aged care, driving a strong national push to minimise pharmacological sleep aids.",
     trap="Giving a PRN sedative before trying environmental measures.",
     res="ACSQHC: Comprehensive Care Standard",
     url="https://www.safetyandquality.gov.au/standards/nsqhs-standards/comprehensive-care-standard"),

# ──────────── WEEK 9: End of life, and the start of life ────────────────────
dict(id=57, week=9, day=1, cat="Basic Care and Comfort", nr_cat="Professional practice",
     template="fact", title="Recognising the dying phase",
     hook="At some point, routine observations stop being care.",
     facts=["Signs: reduced consciousness, changed breathing pattern, mottled cool skin, falling urine output, noisy secretions.", "Anticipatory subcutaneous medications are prescribed in advance for pain, breathlessness, secretions and agitation.", "Shift to comfort, reposition for comfort, stop non-essential observations and interventions.", "Confirm the advance care directive and resuscitation status with the team and family."],
     au="Advance care directives are state-legislated with different names in each jurisdiction, and hyoscine "
        "butylbromide is commonly used in Australia for end-of-life secretions.",
     trap="Continuing 4-hourly observations on someone who is actively dying.",
     res="CareSearch: Palliative Care Knowledge Network",
     url="https://www.caresearch.com.au/"),

dict(id=58, week=9, day=2, cat="Basic Care and Comfort", nr_cat="Professional practice",
     template="fact", title="Supporting independence, not doing it for them",
     hook="Doing it faster yourself is not always doing it better.",
     facts=["Assess functional ability with a structured tool rather than assuming.", "Correct sizing of frames, sticks and shower chairs prevents falls.", "Hygiene care is your chance to inspect pressure areas every time.", "Oral care reduces aspiration pneumonia risk, especially in dysphagia.", "Respect cultural and personal preferences, including same-gender care requests."],
     au="Equipment and home modifications are funded through the NDIS and My Aged Care, with occupational therapy "
        "home assessment standard before discharge. The term is walking frame, not walker.",
     trap="Completing the task for the person and undermining their rehabilitation.",
     res="My Aged Care",
     url="https://www.myagedcare.gov.au/"),

dict(id=59, week=9, day=3, cat="Health Promotion and Maintenance", nr_cat="Maternity",
     template="fact", title="Developmental red flags worth memorising",
     hook="Not the milestones themselves, the ages they should have passed.",
     facts=["No social smile by 2 months. No babbling by 6 months.", "Not walking by 18 months. No two-word phrases by 2 years.", "Erikson: trust, then autonomy, then initiative, then industry, then identity.", "Object permanence develops around 8-12 months.", "Adolescent risk-taking is developmentally normal, assess safety, not morality."],
     au="Australia uses the child health record ('blue book') and Key Ages and Stages checks through child and "
        "family health nurse services in every state and territory.",
     trap="Quoting a checkpoint age from memory instead of the Key Ages and Stages schedule.",
     res="Royal Children's Hospital: Kids Health Info",
     url="https://www.rch.org.au/kidsinfo/"),

dict(id=60, week=9, day=4, cat="Health Promotion and Maintenance", nr_cat="Maternity",
     template="qotd", title="Antenatal danger signs that need review today",
     hook="Headache, visual change and epigastric pain belong together.",
     facts=["Fundal height roughly matches gestational weeks, plus or minus 2-3 cm, from about 20 weeks.", "Danger signs: severe headache, visual changes, epigastric pain, reduced fetal movements, bleeding.", "Postpartum haemorrhage is over 500 mL after vaginal birth, over 1000 mL after caesarean.", "First assessment for postpartum bleeding is the fundus."],
     au="Care follows the national Pregnancy Care Guidelines and RANZCOG, usually through midwifery continuity of "
        "care or GP shared care, with a visit schedule risk-stratified rather than fixed.",
     trap="Applying a fixed visit count instead of the risk-stratified Australian schedule.",
     res="Australian Government: Pregnancy Care Guidelines",
     url="https://www.health.gov.au/resources/pregnancy-care-guidelines"),

dict(id=61, week=9, day=5, cat="Health Promotion and Maintenance", nr_cat="Maternity",
     template="mnemonic", title="APGAR, and the jaundice that is never normal",
     hook="Jaundice in the first 24 hours is always pathological.",
     facts=["APGAR at 1 and 5 minutes: Appearance, Pulse, Grimace, Activity, Respiration, each 0-2.", "Normal newborn: heart rate 110-160, respiratory rate 30-60, temperature 36.5-37.5 degrees.", "Physiological jaundice appears after 24 hours. Before that it is pathological.", "Weight loss up to 7-10% in the first week is normal, regained by about 2 weeks."],
     au="Newborn bloodspot screening occurs at 48-72 hours and hearing screening is universal. Vitamin K and the "
        "hepatitis B birth dose require documented parental consent, they are recommended, not automatic.",
     trap="Treating day-one jaundice as physiological.",
     res="Australian Immunisation Handbook",
     url="https://immunisationhandbook.health.gov.au/"),

dict(id=62, week=9, day=6, cat="Health Promotion and Maintenance", nr_cat="Professional practice",
     template="auvs", title="Immunisation: the National Immunisation Program schedule",
     hook="The National Immunisation Program sets the schedule, and it is reviewed regularly.",
     facts=["Live vaccines such as MMR and varicella are contraindicated in pregnancy and significant immunosuppression.", "Pertussis vaccination in pregnancy protects the newborn through passive transfer.", "True contraindication is anaphylaxis to a previous dose or component.", "Always check the current handbook, the schedule is reviewed and updated."],
     au="Australia follows the National Immunisation Program schedule and the Australian Immunisation "
        "Handbook. Adolescent doses are delivered through school programmes, and shingles vaccination is "
        "funded from 65, or from 50 for Aboriginal and Torres Strait Islander people.",
     trap="Quoting a schedule from memory instead of checking the current handbook.",
     res="National Immunisation Program Schedule",
     url="https://www.health.gov.au/topics/immunisation/when-to-get-vaccinated/national-immunisation-program-schedule"),

dict(id=63, week=9, day=7, cat="Health Promotion and Maintenance", nr_cat="Professional practice",
     template="ref", title="Australian cancer screening: the three programmes",
     hook="Cervical screening here starts at 25 and runs every 5 years.",
     facts=["Cervical. HPV-based Cervical Screening Test from age 25, every 5 years, to age 74.", "Breast. BreastScreen Australia, free 2-yearly mammogram, target age 50-74.", "Bowel, free mailed iFOBT every 2 years, now from age 45 to 74.", "Screening targets people without symptoms. Symptoms need assessment, not screening."],
     au="Australia moved to five-yearly HPV-based cervical screening in 2017, and lowered bowel screening "
        "to start at age 45 from July 2024.",
     trap="Quoting an interval from memory instead of the current programme ages.",
     res="Australian Government: National cancer screening",
     url="https://www.health.gov.au/our-work/national-cervical-screening-program"),

# ─────────────── WEEK 10: Mind, communication and safety ─────────────────────
dict(id=64, week=10, day=1, cat="Health Promotion and Maintenance", nr_cat="Professional practice",
     template="auvs", title="Standard drinks and the NHMRC alcohol guidance",
     hook="An Australian standard drink is 10 grams of alcohol.",
     facts=["An Australian standard drink contains 10 g of alcohol.", "NHMRC guidance: no more than 10 standard drinks a week, and no more than 4 on any one day.", "No safe level in pregnancy, when breastfeeding, or under 18.", "Use AUDIT-C to screen, and the 5 A's for smoking cessation: Ask, Advise, Assess, Assist, Arrange."],
     au="An Australian standard drink contains 10 g of alcohol, and every NHMRC limit is counted against "
        "that measure. Pub and restaurant servings are often more than one standard drink.",
     trap="Counting glasses rather than standard drinks.",
     res="NHMRC, Alcohol guidelines",
     url="https://www.nhmrc.gov.au/health-advice/alcohol"),

dict(id=65, week=10, day=2, cat="Psychosocial Integrity", nr_cat="Mental health",
     template="compare", title="Therapeutic versus non-therapeutic responses",
     hook="False reassurance feels kind. It closes the conversation.",
     facts=["Therapeutic: open questions, reflection, silence, clarifying, offering self, restating.", "Non-therapeutic: giving advice, false reassurance, 'why' questions, changing the subject.", "Validate the feeling before moving to problem-solving.", "Silence is an intervention, not a gap to fill."],
     au="None material, the technique is universal. Use Australian idiom in patient-facing phrasing.",
     trap="Choosing 'I'm sure it will be fine' over an open, validating response.",
     res="Head to Health",
     url="https://www.headtohealth.gov.au/"),

dict(id=66, week=10, day=3, cat="Psychosocial Integrity", nr_cat="Mental health",
     template="mnemonic", title="The mental state examination, domain by domain",
     hook="Describe what you observed. Do not record your conclusion.",
     facts=["Appearance and behaviour, speech, mood and affect, thought form and content.", "Then perception, cognition, insight and judgement.", "Flat, blunted and labile affect are distinct and testable.", "Delirium screening uses the Confusion Assessment Method.", "Write 'avoided eye contact, spoke in a flat monotone', not 'seemed depressed'."],
     au="Mental health legislation is state and territory based in Australia, so involuntary assessment criteria and "
        "forms differ by jurisdiction. There is no single national mental health act.",
     trap="Assuming one national involuntary treatment standard applies across Australia.",
     res="Head to Health",
     url="https://www.headtohealth.gov.au/"),

dict(id=67, week=10, day=4, cat="Psychosocial Integrity", nr_cat="Mental health",
     template="fact", title="Asking directly about suicide is safe and necessary",
     hook="Asking does not plant the idea. Not asking leaves you guessing.",
     facts=["Ask directly and without judgement about thoughts of ending life.", "Assess plan, means, timeline and access to means. Specificity increases acuity.", "The strongest single risk factor is a previous attempt.", "Protective factors include support, reasons for living and restricted access to means.", "A safety plan covers warning signs, coping strategies, contacts and crisis numbers."],
     au="Australian crisis lines are Lifeline 13 11 14, Beyond Blue 1300 22 4636, and 13YARN 13 92 76, a national "
        "line staffed by Aboriginal and Torres Strait Islander crisis supporters.",
     trap="Avoiding the direct question, or giving a number that does not operate in Australia.",
     res="Lifeline Australia",
     url="https://www.lifeline.org.au/"),

dict(id=68, week=10, day=5, cat="Psychosocial Integrity", nr_cat="Mental health",
     template="fact", title="Alcohol withdrawal can kill. Opioid withdrawal usually does not.",
     hook="The timeline tells you when to worry.",
     facts=["Tremor and anxiety at 6-12 hours. Hallucinations around 12-24 hours.", "Seizures around 24-48 hours. Delirium tremens typically 48-96 hours after the last drink.", "Delirium tremens is a medical emergency with significant untreated mortality.", "CIWA-Ar is the validated tool guiding benzodiazepine dosing.", "Use person-first language, a person with a substance use disorder."],
     au="Withdrawal protocols follow state health department guidelines, and alcohol and drug information services "
        "are state-based rather than a single national line.",
     trap="Treating alcohol and opioid withdrawal as equally dangerous.",
     res="Australian Government, Alcohol and other drugs",
     url="https://www.health.gov.au/topics/alcohol"),

dict(id=69, week=10, day=6, cat="Psychosocial Integrity", nr_cat="Professional practice",
     template="fact", title="Screening for family violence: ask them alone",
     hook="You cannot screen safely with the partner in the room.",
     facts=["Screen privately, without partner or family present, using direct non-judgemental questions.", "Indicators: injuries inconsistent with the explanation, injuries at different healing stages, delayed presentation, controlling behaviour.", "Elder abuse includes financial, physical, psychological and neglect. Assess carer strain as a risk factor.", "Document objectively in the person's own words, and use body maps.", "Safety comes before full disclosure."],
     au="The national referral line is 1800RESPECT (1800 737 732). Mandatory reporting thresholds for child abuse "
        "differ by state. Culturally safe, trauma-informed responses are an explicit NMBA expectation.",
     trap="Asking screening questions with a family member still present.",
     res="1800RESPECT",
     url="https://www.1800respect.org.au/"),

dict(id=70, week=10, day=7, cat="Psychosocial Integrity", nr_cat="Professional practice",
     template="carousel", title="Grief, and what cultural safety actually means",
     hook="Cultural safety is judged by the person receiving care, not by you.",
     facts=["Grief stages are not sequential. Do not expect people to move through them in order.", "Prolonged grief that still impairs function beyond about 12 months warrants referral.", "Coping ranges from adaptive to maladaptive. Assess it, do not judge it.", "Cultural safety means the patient decides whether the interaction was safe and respectful."],
     au="Cultural safety for Aboriginal and Torres Strait Islander Peoples is a codified NMBA obligation, not "
        "optional good practice. Kinship obligations and Sorry Business must be respected and accommodated, "
        "including flexibility about visitor numbers and ceremony.",
     trap="Applying a Western grief-stage model rigidly and missing kinship and community mourning practices.",
     res="NMBA: Joint statement on culturally safe care",
     url="https://www.nursingmidwiferyboard.gov.au/codes-guidelines-statements/position-statements.aspx"),
]

WEEK_TITLES = {
    1:  "Thinking like a nurse, prioritisation and professional practice",
    2:  "Legal, ethical and professional obligations",
    3:  "Infection prevention and workplace safety",
    4:  "Error prevention and medication foundations",
    5:  "High-risk medicines and the first numbers",
    6:  "Assessment, deterioration and the heart",
    7:  "The big physiological emergencies",
    8:  "Sepsis, fluids and comfort care",
    9:  "End of life, and the start of life",
    10: "Mind, communication and safety",
}

# ── Art direction, assigned by content type ──────────────────────────────────
# Chosen deliberately rather than rotated at random: consistency builds recognition,
# and each theme is matched to the kind of content it carries best.
#   editorial  the default teaching voice, calm and readable
#   midnight   high contrast, used where attention is the job (question of the day)
#   block      bold and graphic, used for carousels so a swipe set reads as one piece
#   chart      the observation-chart language, used for reference and comparison data
#   notecard   the study-card look, used for memory aids and drug cards
THEME_FOR_TEMPLATE = {
    "fact":     "editorial",
    "auvs":     "editorial",
    "qotd":     "midnight",
    "carousel": "block",
    "ref":      "chart",
    "compare":  "chart",
    "drug":     "notecard",
    "mnemonic": "notecard",
}

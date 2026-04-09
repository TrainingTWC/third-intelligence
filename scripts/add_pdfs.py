"""
One-time script: Enrich data.json with detailed content from
  - Bench Planning PDF (IDP process, employee journey, interview panels, training periods)
  - Respect PDF (role-specific behaviors for each RESPECT value)
"""

import json
import pathlib

DATA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"

# ── NEW MODULES ──────────────────────────────────────────────────

new_modules = [
    # ━━━ MODULE: Detailed WING's IDP & Bench Planning ━━━
    {
        "id": "wing_idp_bench_detail",
        "title": "WING's — IDP Process & Bench Planning (Detailed)",
        "description": "Detailed guide to the WING's Internal Development Process (IDP) and Bench Planning: the five-step IDP flow, employee journey from Barista to Area Manager, interview panel composition, training periods, and certification requirements.",
        "chunks": [
            {
                "chunk_id": "wing_detail_1",
                "title": "WING's Acronym & Program Purpose",
                "intent": "Explain what WING's stands for and the program's objectives.",
                "content": "WING's stands for: W — Winning, I — Integrated Development, N — Nurturing Talent, G — Getting Ready for Success. The program's objectives are: Build a strong internal talent pipeline by identifying and developing high-potential employees. Ensure trained and promotion-ready team members are available to fill key vacancies. Reduce business disruption caused by sudden resignations, lack of trained replacements, and reliance on underperformers. Enable proactive hiring and development rather than reactive staffing decisions. Avoid loss of business opportunities due to manpower gaps. Support consistent café performance by strengthening the link between people capability, customer satisfaction, and business profitability. The program implements two key processes: Internal Development Process (IDP) and Bench Planning.",
                "tags": ["wings", "wing", "idp", "bench planning", "talent pipeline", "promotion", "internal development"],
                "qa_pairs": [
                    {"instruction": "What does WING's stand for?", "output": "WING's stands for W — Winning, I — Integrated Development, N — Nurturing Talent, G — Getting Ready for Success."},
                    {"instruction": "What is the full form of WING's?", "output": "WING's stands for Winning, Integrated Development, Nurturing Talent, Getting Ready for Success."},
                    {"instruction": "What are the objectives of the WING's program?", "output": "The objectives are: build a strong internal talent pipeline, ensure trained and promotion-ready team members are available for key vacancies, reduce business disruption from sudden resignations or lack of trained replacements, enable proactive hiring and development, avoid loss of business opportunities due to manpower gaps, and support consistent café performance by linking people capability, customer satisfaction, and business profitability."},
                    {"instruction": "What two key processes does WING's implement?", "output": "WING's implements two key processes: Internal Development Process (IDP) and Bench Planning."},
                    {"instruction": "Why is the WING's program important?", "output": "It prevents business disruption from sudden resignations, ensures trained replacements are ready, enables proactive development instead of reactive staffing, and strengthens the link between people capability, customer satisfaction, and profitability."}
                ]
            },
            {
                "chunk_id": "wing_detail_2",
                "title": "The Five-Step IDP Process",
                "intent": "Explain the five steps of the Internal Development Process in detail.",
                "content": "The IDP process has five steps: Step 1 — Identification: Match the eligibility criteria. Auto-selection happens through Zing based on tenure and mandate certifications. Step 2 — Readiness: Check readiness by filling the Readiness Checklist. This is done by the reporting manager. Step 3 — Assessment: Assess the candidate through an assessment centre. This is conducted by the Regional Trainer. Step 4 — Interview: Conduct the interview following the interview questionnaire based on RESPECT. This is conducted by the panel. Step 5 — Training: On clearing the interview with the panel, the candidate will start training for the next position.",
                "tags": ["idp", "identification", "readiness", "assessment", "interview", "training", "zing", "regional trainer", "respect"],
                "qa_pairs": [
                    {"instruction": "What are the five steps of the IDP process?", "output": "The five steps are: (1) Identification — match eligibility criteria via Zing based on tenure and certifications, (2) Readiness — fill the Readiness Checklist done by the reporting manager, (3) Assessment — assessment centre conducted by the Regional Trainer, (4) Interview — conducted by a panel using RESPECT-based questionnaire, (5) Training — start training for the next position after clearing the interview."},
                    {"instruction": "How does identification work in IDP?", "output": "Identification is auto-selection through Zing. It checks eligibility based on tenure and mandate certifications."},
                    {"instruction": "Who conducts the readiness check in IDP?", "output": "The readiness check is done by the reporting manager using a Readiness Checklist."},
                    {"instruction": "Who conducts the IDP assessment?", "output": "The assessment is conducted by the Regional Trainer through an assessment centre."},
                    {"instruction": "What happens after clearing the IDP interview?", "output": "After clearing the interview with the panel, the candidate starts training for the next position."},
                    {"instruction": "What is the IDP interview based on?", "output": "The IDP interview follows a questionnaire based on the RESPECT framework."}
                ]
            },
            {
                "chunk_id": "wing_detail_3",
                "title": "Employee Journey in WING's",
                "intent": "Describe the full employee journey from Barista to Store Manager through the WING's program.",
                "content": "The employee journey through WING's follows this path: Barista (3 months) → eligible to be Buddy Trainer (BT). BT certification includes a BT Workshop and BT Skill Check. BT (6 months) → eligible to become Shift Manager. Requires Readiness Checklist for BT, Aptitude & Attitude test, Panel Interview & Selection. Shift Manager → eligible to become ASM (9 months). Includes Practice Learning, Basic Certification (15 days), Food Safety Module Review, Advance Certification, Apply the Learning, Final Certification, SHLP Workshop, Readiness Checklist, Aptitude & Attitude test, Panel Interview & Selection. ASM → eligible to become Store Manager (SM). Each stage requires Readiness Checklist completion, assessment, and panel interview clearance.",
                "tags": ["employee journey", "barista", "buddy trainer", "shift manager", "asm", "store manager", "certification", "promotion path"],
                "qa_pairs": [
                    {"instruction": "What is the employee journey in the WING's program?", "output": "Barista (3 months) → Buddy Trainer → Shift Manager (6 months tenure) → ASM (9 months) → Store Manager. Each transition requires a Readiness Checklist, assessment, and panel interview."},
                    {"instruction": "How long before a Barista can become a Buddy Trainer?", "output": "A Barista is eligible to become a Buddy Trainer after 3 months."},
                    {"instruction": "How long before a BT can become a Shift Manager?", "output": "A Buddy Trainer is eligible to become a Shift Manager after 6 months tenure. They must complete a Readiness Checklist, Aptitude & Attitude test, and Panel Interview."},
                    {"instruction": "What certifications are needed for ASM?", "output": "To become ASM, a Shift Manager needs: Practice Learning, Basic Certification (15 days), Food Safety Module Review, Advance Certification, Final Certification, and SHLP Workshop, followed by Readiness Checklist, Aptitude & Attitude test, and Panel Interview."},
                    {"instruction": "What is the promotion path at TWC?", "output": "Barista → Buddy Trainer (3 months) → Shift Manager (6 months) → ASM (9 months) → Store Manager. Each step requires readiness assessment, aptitude test, and panel interview clearance."}
                ]
            },
            {
                "chunk_id": "wing_detail_4",
                "title": "Interview Panel Composition",
                "intent": "Define who sits on the interview panel for each promotion level.",
                "content": "Interview panel composition by promotion level: Buddy Trainer to Shift Manager: Area Manager, Trainer/Regional QA, HRBP. Shift Manager to ASM: Market Manager/Regional Manager, Regional Trainer/QA, Regional HRBP. ASM to Store Manager: Regional Manager, GM Operations, Training Head/QA Head, Regional HRBP. Area Manager/Cross-function: Director — Ops & Excellence, GM Operations/Cross-function Head, Finance Representative, Training Head, HR Head. The candidate gets a maximum of two opportunities to qualify. If they fail the first round, they must complete the development plan and be reassessed after 30 days. If they fail the second round, they are eligible for IDP again after 3 months from the second interview date.",
                "tags": ["interview panel", "promotion", "area manager", "hrbp", "regional trainer", "idp"],
                "qa_pairs": [
                    {"instruction": "Who is on the interview panel for Buddy Trainer to Shift Manager?", "output": "The panel includes the Area Manager, Trainer/Regional QA, and HRBP."},
                    {"instruction": "Who is on the interview panel for Shift Manager to ASM?", "output": "The panel includes the Market Manager/Regional Manager, Regional Trainer/QA, and Regional HRBP."},
                    {"instruction": "Who is on the interview panel for ASM to Store Manager?", "output": "The panel includes the Regional Manager, GM Operations, Training Head/QA Head, and Regional HRBP."},
                    {"instruction": "What happens if a candidate fails the IDP interview?", "output": "The candidate gets a maximum of two attempts. If they fail the first round, they must complete a development plan and be reassessed after 30 days. If they fail the second round, they become eligible again after 3 months from the second interview date."},
                    {"instruction": "How many chances does a candidate get in the IDP interview?", "output": "A maximum of two opportunities. After the first failure, reassessment after 30 days with a completed development plan. After the second failure, eligible again after 3 months."}
                ]
            },
            {
                "chunk_id": "wing_detail_5",
                "title": "Training Periods & Certifications by Role",
                "intent": "Detail the training period and review process for each role transition.",
                "content": "Training periods and certifications by promotion level: Barista to Shift Manager: Training period 30 days, in-store review weekly by Reporting Manager, final reviews and certifications by Trainer & SM/AM. Shift Manager to ASM: Training period 45 days, in-store review weekly by Store Manager, reviews and certifications by Trainer & SM/AM. ASM to Store Manager: Training period 15 days, in-store review weekly by Store Manager/AM, reviews and certifications by Trainer & AM. Area Manager/Cross-function: Training period 30 days, on-field review weekly by Reporting Manager, final review and certification by Training & Ops Head.",
                "tags": ["training period", "certification", "barista", "shift manager", "asm", "store manager", "area manager"],
                "qa_pairs": [
                    {"instruction": "What is the training period for Barista to Shift Manager?", "output": "30 days. In-store review is weekly by the Reporting Manager. Final reviews and certifications are by the Trainer & SM/AM."},
                    {"instruction": "What is the training period for Shift Manager to ASM?", "output": "45 days. In-store review is weekly by the Store Manager. Reviews and certifications by Trainer & SM/AM."},
                    {"instruction": "What is the training period for ASM to Store Manager?", "output": "15 days. In-store review is weekly by the Store Manager/AM. Reviews and certifications by Trainer & AM."},
                    {"instruction": "What is the training period for Area Manager?", "output": "30 days. On-field review is weekly by the Reporting Manager. Final review and certification by Training & Ops Head."},
                    {"instruction": "How long is each training period in WING's?", "output": "Barista to Shift Manager: 30 days. Shift Manager to ASM: 45 days. ASM to Store Manager: 15 days. Area Manager/Cross-function: 30 days."}
                ]
            }
        ]
    },

    # ━━━ MODULE: RESPECT Detailed Role Behaviors ━━━
    {
        "id": "respect_role_behaviors",
        "title": "RESPECT Framework — Role-Specific Behaviors",
        "description": "Detailed RESPECT framework behaviors expected from Baristas, Shift Managers, and Store Managers for each value: Responsibility, Empathy, Service Excellence, Performance with Purpose, Ethics & Integrity, Collaboration, and Trust.",
        "chunks": [
            {
                "chunk_id": "respect_role_1",
                "title": "RESPECT Full Form & Overview",
                "intent": "Explain what RESPECT stands for and provide the full form.",
                "content": "RESPECT is the core values framework at Third Wave Coffee. The full form of RESPECT is: R — Responsibility, E — Empathy, S — Service Excellence, P — Performance with Purpose, E — Ethics & Integrity, C — Collaboration, T — Trust. Each value has specific behavioral expectations for Baristas, Shift Managers, and Store Managers. RESPECT guides all employee behavior and decision-making at every level of the organization.",
                "tags": ["respect", "full form", "values", "R.E.S.P.E.C.T", "acronym", "framework"],
                "qa_pairs": [
                    {"instruction": "What is the full form of RESPECT?", "output": "R — Responsibility, E — Empathy, S — Service Excellence, P — Performance with Purpose, E — Ethics & Integrity, C — Collaboration, T — Trust."},
                    {"instruction": "What does R.E.S.P.E.C.T. stand for?", "output": "R.E.S.P.E.C.T. stands for Responsibility, Empathy, Service Excellence, Performance with Purpose, Ethics & Integrity, Collaboration, and Trust."},
                    {"instruction": "What is the RESPECT framework?", "output": "RESPECT is the core values framework at Third Wave Coffee. It stands for Responsibility, Empathy, Service Excellence, Performance with Purpose, Ethics & Integrity, Collaboration, and Trust. Each value has specific behavioral expectations for Baristas, Shift Managers, and Store Managers."},
                    {"instruction": "What are the seven RESPECT values?", "output": "The seven RESPECT values are: Responsibility, Empathy, Service Excellence, Performance with Purpose, Ethics & Integrity, Collaboration, and Trust."},
                    {"instruction": "How many values does RESPECT have?", "output": "RESPECT has seven values: Responsibility, Empathy, Service Excellence, Performance with Purpose, Ethics & Integrity, Collaboration, and Trust."}
                ]
            },
            {
                "chunk_id": "respect_role_2",
                "title": "Responsibility — Role-Specific Behaviors",
                "intent": "Detail what Responsibility means for each role level.",
                "content": "Responsibility: 'We take ownership of our actions, honour commitments, and uphold the highest standards of excellence in all that we do.' Barista responsibilities: Report at store as per schedule. Follow grooming standards. Maintain personal hygiene and follow CAYG while working on stations. Follow recipe and TWC standards to prepare and serve products. Take personal accountability to own the experience of customers and partners in the café. Shift Manager responsibilities: Divide work load by following the deployment. Take care of people on shift by providing breaks on time. Take accountability that all policies, standards, and procedures are followed. Be responsible to share honest feedback with the team to help them improve. Store Manager responsibilities: Ensure duty roster is prepared at least three days before the deployment date. Take responsibility that no one is working consecutively for 10 days without weekly off. Take ownership of actions and decisions. Take responsibility of café performance and take appropriate actions to improve. Take sustainability and social responsibility initiatives involving store teams. Don'ts: Making excuses or avoiding responsibility. Withholding information that affects the team or customers. Ignoring behaviors and actions that impact partners, customers, and business negatively. Don't waste resources (water, electricity, packaging material); adopt a mindset of shared responsibility.",
                "tags": ["responsibility", "respect", "barista", "shift manager", "store manager", "ownership", "accountability"],
                "qa_pairs": [
                    {"instruction": "What does Responsibility mean in RESPECT?", "output": "Responsibility means taking ownership of actions, honouring commitments, and upholding the highest standards of excellence. It covers respect for each other (being dependable and supportive), respect for process and SOPs, and respect for customer trust."},
                    {"instruction": "What are the Barista responsibilities under RESPECT?", "output": "Report as per schedule, follow grooming standards, maintain personal hygiene and CAYG, follow recipe and TWC standards, and take personal accountability for the experience of customers and partners."},
                    {"instruction": "What are the Shift Manager responsibilities under RESPECT?", "output": "Divide workload following deployment, provide breaks on time, ensure all policies and procedures are followed, and share honest feedback with the team to help them improve."},
                    {"instruction": "What are the Store Manager responsibilities under RESPECT?", "output": "Prepare duty roster at least 3 days before deployment, ensure no one works 10 consecutive days without weekly off, take ownership of decisions, take responsibility for café performance, and lead sustainability initiatives involving store teams."},
                    {"instruction": "What are the don'ts for Responsibility?", "output": "Don't make excuses or avoid responsibility. Don't withhold information affecting team or customers. Don't ignore negative behaviors impacting partners, customers, or business. Don't waste resources like water, electricity, or packaging material."}
                ]
            },
            {
                "chunk_id": "respect_role_3",
                "title": "Empathy — Role-Specific Behaviors",
                "intent": "Detail what Empathy means for each role level.",
                "content": "Empathy: 'We foster an inclusive environment where diverse perspectives are valued, and meaningful connections drive collaboration and innovation.' Barista: Welcome every team member with warmth. Help customers who may struggle (e.g., opening door, finding comfortable seat). Approach customers who appear upset or unhappy with care. Patiently teach skills multiple times to new team members. If a new partner struggles with a task, demonstrate an easier way. Shift Manager: Provide feedback patiently and repeatedly to help improve behaviors. Demonstrate difficult skills while ensuring partners feel supported. Understand that mistakes happen and avoid scolding; work collaboratively to find solutions. Appreciate and acknowledge the team's empathetic behavior. Store Manager: Accommodate scheduling requests when possible to support work-life balance. Foster an inclusive and welcoming culture where both partners and customers feel valued, respected, and included. Care for customers and partners with special needs. Accept feedback openly, even from equal level or junior employees. Empower the team to take empathetic actions (e.g., offering a coffee tasting to a lonely customer, celebrating a customer's birthday). Don'ts: Don't judge others. Don't be egoistic or uncomfortable receiving feedback from peers. Never ignore burnout signs. Don't dismiss feedback. Don't be unapproachable.",
                "tags": ["empathy", "respect", "barista", "shift manager", "store manager", "inclusion", "diversity", "feedback"],
                "qa_pairs": [
                    {"instruction": "What does Empathy mean in RESPECT?", "output": "Empathy means fostering an inclusive environment where diverse perspectives are valued and meaningful connections drive collaboration and innovation. It includes respect for diversity, customer needs, and engagement."},
                    {"instruction": "How should a Barista show empathy?", "output": "Welcome team members warmly, help struggling customers (open doors, find seats), approach upset customers with care, patiently teach new team members, and demonstrate easier ways to do tasks."},
                    {"instruction": "How should a Shift Manager show empathy?", "output": "Provide feedback patiently and repeatedly, demonstrate difficult skills while keeping partners supported, avoid scolding for mistakes — collaborate on solutions, and appreciate the team's empathetic behavior."},
                    {"instruction": "How should a Store Manager show empathy?", "output": "Accommodate scheduling requests for work-life balance, foster inclusive culture, care for people with special needs, accept feedback from any level, and empower the team to take empathetic actions like celebrating a customer's birthday."},
                    {"instruction": "What are the don'ts for Empathy?", "output": "Don't judge others. Don't be egoistic about receiving feedback from peers. Never ignore burnout signs. Don't dismiss feedback. Don't be unapproachable."}
                ]
            },
            {
                "chunk_id": "respect_role_4",
                "title": "Service Excellence — Role-Specific Behaviors",
                "intent": "Detail what Service Excellence means for each role level.",
                "content": "Service Excellence: 'We are relentless in delivering outstanding experiences, setting high standards, and continuously improving to exceed expectations.' Barista: Engage with customers and gather feedback on food and beverages. Remember customer names and preferred drinks. Maintain efficiency at station, stay hospitable, smile, and greet customers. Adhere to standards and recipes even during peak hours. Understand customer preferences and recommend products accordingly. Handle difficult or unhappy customers calmly and respectfully. Shift Manager: Monitor customer satisfaction and help team view the café from a customer's perspective. Ensure clear communication and all shift tasks are completed. Encourage product purchases through customer engagement. Act as a role model in resolving customer concerns. Store Manager: Be a role model, encourage café team to connect with customers by creating a recognition culture. Plan operational activities during non-peak hours to prioritize customers during peak hours. Consistently follow up to ensure store is clean and ready for service excellence. Adopt and motivate team to adopt new ways of working. Don'ts: Never prioritize cost control at the expense of customer experience. Never prioritize operational tasks over customers. Never ignore customer concerns or special requests. Never prove a point or assume customers are seeking free products.",
                "tags": ["service excellence", "respect", "barista", "shift manager", "store manager", "customer experience", "standards"],
                "qa_pairs": [
                    {"instruction": "What does Service Excellence mean in RESPECT?", "output": "Service Excellence means being relentless in delivering outstanding experiences, setting high standards, and continuously improving to exceed expectations."},
                    {"instruction": "How should a Barista practice Service Excellence?", "output": "Engage with customers and gather feedback, remember customer names and preferred drinks, maintain efficiency and hospitality, adhere to standards even during peak hours, recommend products based on preferences, and handle difficult customers calmly."},
                    {"instruction": "How should a Store Manager practice Service Excellence?", "output": "Be a role model creating a recognition culture, plan operational activities during non-peak hours to prioritize customers during peak hours, ensure store cleanliness and readiness, and motivate team to adopt new ways of working."},
                    {"instruction": "What are the don'ts for Service Excellence?", "output": "Never prioritize cost control over customer experience. Never prioritize operational tasks over customers. Never ignore concerns or special requests. Never assume customers are seeking free products."}
                ]
            },
            {
                "chunk_id": "respect_role_5",
                "title": "Performance with Purpose — Role-Specific Behaviors",
                "intent": "Detail what Performance with Purpose means for each role level.",
                "content": "Performance with Purpose: 'We are driven by a results-oriented mindset, where excellence, growth, and ethical leadership define success.' Barista: Complete all assigned tasks efficiently and timely. Demonstrate excellent suggestive and upselling skills. Understand why it's important to follow standards and policies. Follow all standards and guidelines all the time and inspire others. Stay curious and eager to learn new skills to deliver best results. Break bigger goals into smaller actions. Shift Manager: Keep a firm and professional approach to demand results. Adjust delivery style — tone, pace — to fit the message and audience. Set and maintain high standards by following company policies and procedures. Implement innovative ideas to achieve results. Develop new skills to deliver results. Believe in everyone. Store Manager: Communicate effectively, set expectations, monitor and coach team. Involve, motivate, and guide team to achieve results. Balance people, customer, and business results. Approach team on how small things like preparing best quality coffee, product availability, maintaining SOS, good VM, and customer connection at all touchpoints help drive sales and results. Recognize top performers based on objective performance metrics. Don'ts: Never approach aggressively and demand results. Don't perceive tasks as burden. Don't withhold financial goals from team. Never be rigid to adapt newer ways. Never discriminate based on caste, colour, sex, or ethnicity.",
                "tags": ["performance", "purpose", "respect", "results", "upselling", "standards", "coaching"],
                "qa_pairs": [
                    {"instruction": "What does Performance with Purpose mean in RESPECT?", "output": "Performance with Purpose means being driven by a results-oriented mindset where excellence, growth, and ethical leadership define success."},
                    {"instruction": "How should a Barista show Performance with Purpose?", "output": "Complete tasks efficiently, demonstrate excellent suggestive and upselling skills, follow standards consistently, stay curious to learn, and break bigger goals into smaller actions."},
                    {"instruction": "How should a Store Manager show Performance with Purpose?", "output": "Communicate effectively and coach team, involve and motivate team to achieve results, balance people/customer/business results, show how small things drive sales, and recognize top performers based on objective metrics."},
                    {"instruction": "What are the don'ts for Performance with Purpose?", "output": "Never demand results aggressively. Don't treat tasks as a burden. Don't withhold financial goals from team. Don't be rigid about adopting new ways. Never discriminate based on caste, colour, sex, or ethnicity."}
                ]
            },
            {
                "chunk_id": "respect_role_6",
                "title": "Ethics & Integrity — Role-Specific Behaviors",
                "intent": "Detail what Ethics & Integrity means for each role level.",
                "content": "Ethics & Integrity: 'We build trust through honesty, transparency, and ethical decision-making in every aspect of our business.' Barista: Always disclose important information which HR needs to know like relationships with vendors, partners, own health conditions. Do correct entries in the POS. Follow HR policies. Report if any mishappening is witnessed. Shift Manager: Consistently observe people while working and correct them when required. Effectively handle unexpected circumstances and incidents following Third Wave standards and policies. Reflect Third Wave transparency in every transaction. Store Manager: Provide equal opportunities to all employees to grow. Others consider him/her the most trustworthy person. Keep confidential information and pass on only required information to the team. Abide by law, ask if unaware. Share company information only with authorized persons. Observe, involve to ensure no mishappening in the store, report or take action if anything observed. Don'ts: Never do unlawful activities at the store (consuming drugs, alcohol, tobacco at workplace, carrying unlawful substances, reselling TWC products, mismanagement of compliance, workplace harassment, physical violence, POSH violations). Never accept gifts from vendors/customers worth more than Rs. 500. Never take unauthorized benefits (e.g., giving employee meal/discount to friends or customers). Never manipulate or hide information (incorrect inventories, wrong POS entries, false statements). Never submit fraudulent claims (forging attendance, overtime, bonus, marking wrong attendance, being absent during working hours, forging education/salary/experience). Never keep inventory for self. Never share confidential information with unauthorized persons.",
                "tags": ["ethics", "integrity", "respect", "honesty", "transparency", "compliance", "posh", "fraud"],
                "qa_pairs": [
                    {"instruction": "What does Ethics & Integrity mean in RESPECT?", "output": "Ethics & Integrity means building trust through honesty, transparency, and ethical decision-making in every aspect of business."},
                    {"instruction": "What are the ethics don'ts at TWC?", "output": "Never do unlawful activities (drugs, alcohol, tobacco at workplace, reselling products, harassment, POSH violations). Never accept gifts from vendors/customers over Rs. 500. Never take unauthorized benefits. Never manipulate information or submit fraudulent claims. Never share confidential information with unauthorized persons."},
                    {"instruction": "What should a Barista do for Ethics & Integrity?", "output": "Disclose important information to HR, do correct POS entries, follow HR policies, and report any mishappening witnessed."},
                    {"instruction": "What should a Store Manager do for Ethics & Integrity?", "output": "Provide equal growth opportunities, be the most trustworthy person, keep confidential information secure, abide by law, share company information only with authorized persons, and ensure no mishappening occurs in the store."}
                ]
            },
            {
                "chunk_id": "respect_role_7",
                "title": "Collaboration — Role-Specific Behaviors",
                "intent": "Detail what Collaboration means for each role level.",
                "content": "Collaboration: 'We believe in the power of teamwork, collective success, and creating a culture where everyone thrives together.' Barista: Work as a team — ask for help when needed and help when another partner needs support. Proactively introduce and get to know people, make everyone feel welcomed and part of the team. Build strong relationships with tenured and newly joined people. Make newly joined people comfortable and share knowledge. Shift Manager: Inspire and influence the team and engage them in doing more productive things. Take feedback from the team and check progress on received feedback. Take responsibility to create oneness in the team and create teamwork and positive work environment through one-on-ones, monthly meetings, and preparing PDP for each employee. Store Manager: Take effort to recognize people for their efforts and promote 'We' culture. Consistently involve team in solving problems — team feels highly motivated to share hurdles/ideas. People consider him/her the first person to seek solutions. Go beyond and involve support functions to achieve results. Don'ts: Never blame others for failures or mistakes. Never overshadow or undermine anyone's role or contribution. Refrain from taking credit for team efforts — acknowledge everyone's contributions. Don't dismiss ideas, creativity, or suggestions. Don't engage in unhealthy competition that disrupts team harmony. Don't resist feedback or constructive criticism.",
                "tags": ["collaboration", "respect", "teamwork", "team", "oneness", "pdp", "one on one"],
                "qa_pairs": [
                    {"instruction": "What does Collaboration mean in RESPECT?", "output": "Collaboration means believing in the power of teamwork, collective success, and creating a culture where everyone thrives together."},
                    {"instruction": "How should a Barista show Collaboration?", "output": "Work as a team, ask for help and offer help, proactively introduce yourself to people, make everyone feel welcomed, build strong relationships with tenured and new team members, and share knowledge with new joiners."},
                    {"instruction": "How should a Store Manager show Collaboration?", "output": "Recognize people's efforts, promote 'We' culture, involve team in solving problems, be the first person people seek for solutions, and involve support functions to achieve results."},
                    {"instruction": "What are the don'ts for Collaboration?", "output": "Never blame others for failures. Don't overshadow anyone's contribution. Don't take credit for team efforts. Don't dismiss ideas or suggestions. Avoid unhealthy competition. Don't resist feedback."}
                ]
            },
            {
                "chunk_id": "respect_role_8",
                "title": "Trust — Role-Specific Behaviors",
                "intent": "Detail what Trust means for each role level.",
                "content": "Trust: 'We cultivate trust through fairness, honesty, and clear communication, ensuring strong relationships and long-term success.' Barista: Communicate openly, clearly, and honestly. Treat colleagues and customers fairly and with respect. Align actions with customer trust and loyalty. Shift Manager: Share honest feedback firmly. Treat colleagues and customers fairly and with respect. Lead integrity and encourage ethical behaviors in the team. Store Manager: Honour commitments and fulfil promises made with partners and customers. Ensure consistency between words and actions as a leader. Handle issues and concerns transparently. Don'ts: Don't make false promises with customers or break commitments with customers and partners. Don't make decisions that prioritize short-term gains over long-term customer relationships. Never mislead or provide incomplete information. Never ignore ethical concerns or tolerate dishonesty. Don't engage in favouritism or unfair treatment.",
                "tags": ["trust", "respect", "honesty", "fairness", "communication", "leadership", "ethics"],
                "qa_pairs": [
                    {"instruction": "What does Trust mean in RESPECT?", "output": "Trust means cultivating trust through fairness, honesty, and clear communication, ensuring strong relationships and long-term success."},
                    {"instruction": "How should a Barista show Trust?", "output": "Communicate openly, clearly, and honestly. Treat colleagues and customers fairly and with respect. Align actions with customer trust and loyalty."},
                    {"instruction": "How should a Store Manager show Trust?", "output": "Honour commitments and fulfil promises to partners and customers. Ensure consistency between words and actions. Handle issues and concerns transparently."},
                    {"instruction": "What are the don'ts for Trust?", "output": "Don't make false promises or break commitments. Don't prioritize short-term gains over long-term relationships. Never mislead or give incomplete information. Never ignore ethical concerns or tolerate dishonesty. Don't engage in favouritism."}
                ]
            }
        ]
    }
]

# ── Append to data.json ──────────────────────────────────────────

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {m["id"] for m in data["modules"]}

added = 0
for mod in new_modules:
    if mod["id"] in existing_ids:
        print(f"SKIP (exists): {mod['id']}")
        continue
    data["modules"].append(mod)
    existing_ids.add(mod["id"])
    n_chunks = len(mod["chunks"])
    n_qa = sum(len(c.get("qa_pairs", [])) for c in mod["chunks"])
    print(f"ADDED: {mod['id']} — {n_chunks} chunks, {n_qa} QA pairs")
    added += 1

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

total_modules = len(data["modules"])
total_chunks = sum(len(m.get("chunks", [])) for m in data["modules"])
total_qa = sum(len(c.get("qa_pairs", [])) for m in data["modules"] for c in m.get("chunks", []))
print(f"\nDone. {added} modules added. Total: {total_modules} modules, {total_chunks} chunks, {total_qa} QA pairs")

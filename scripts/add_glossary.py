"""
Add a glossary / abbreviations module to data.json with full forms of all acronyms.
Run once, then delete this script.
"""
import json
import pathlib

DATA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"

glossary_module = {
    "id": "glossary_abbreviations",
    "title": "Glossary — Abbreviations & Full Forms",
    "description": "A comprehensive reference of all abbreviations, acronyms, and their full forms used across Third Wave Coffee / Third Rush operations, training, and customer experience.",
    "chunks": [
        {
            "title": "Company & Brand Abbreviations",
            "intent": "Provide full forms of company and brand-related abbreviations.",
            "content": (
                "TWC — Third Wave Coffee. "
                "TR — Third Rush. "
                "CX — Customer Experience. "
                "CPI — Customer Pulse Index (measures customer satisfaction; out of every 1,000 customers served, it tracks how many were unhappy or had complaints; a smaller CPI number means better service). "
                "SOP — Standard Operating Procedure. "
                "POS — Point of Sale (the billing counter/system used to take and process customer orders). "
                "MOD — Manager on Duty (the manager responsible for the shift). "
                "LMS — Learning Management System (the online platform used for training modules and certifications). "
                "UPI — Unified Payments Interface (a digital payment method accepted at Third Wave Coffee / Third Rush)."
            ),
            "tags": ["glossary", "abbreviations", "full_form", "twc", "tr", "cx", "cpi", "sop", "pos", "mod", "lms", "upi"],
            "qa_pairs": [
                {"instruction": "What is the full form of TWC?", "output": "Third Wave Coffee stands for Third Wave Coffee."},
                {"instruction": "What is the full form of TR?", "output": "TR stands for Third Rush."},
                {"instruction": "What is the full form of CX?", "output": "CX stands for Customer Experience."},
                {"instruction": "What is the full form of CPI?", "output": "CPI stands for Customer Pulse Index. It measures customer satisfaction — out of every 1,000 customers served, it tracks how many were unhappy or had complaints. A smaller CPI number means better service."},
                {"instruction": "What is the full form of SOP?", "output": "SOP stands for Standard Operating Procedure."},
                {"instruction": "What is the full form of POS?", "output": "POS stands for Point of Sale — the billing counter/system used to take and process customer orders."},
                {"instruction": "What is the full form of MOD?", "output": "MOD stands for Manager on Duty — the manager responsible for the shift."},
                {"instruction": "What is the full form of LMS?", "output": "LMS stands for Learning Management System — the online platform used for training modules and certifications."},
                {"instruction": "What is the full form of UPI?", "output": "UPI stands for Unified Payments Interface — a digital payment method accepted at Third Wave Coffee / Third Rush."},
                {"instruction": "What does Third Wave Coffee stand for?", "output": "Third Wave Coffee stands for Third Wave Coffee."},
                {"instruction": "What does CPI stand for?", "output": "CPI stands for Customer Pulse Index."},
                {"instruction": "What does MOD stand for?", "output": "MOD stands for Manager on Duty."}
            ]
        },
        {
            "title": "Role & Team Abbreviations",
            "intent": "Provide full forms of role and team-related abbreviations.",
            "content": (
                "SM — Shift Manager (when referring to the role between Buddy Trainer and ASM) or Store Manager (when referring to the café head). Context determines which meaning applies. "
                "ASM — Assistant Store Manager. "
                "BT — Buddy Trainer (a certified barista who mentors and trains new team members). "
                "HRBP — Human Resources Business Partner. "
                "QA — Quality Assurance (the team/person responsible for maintaining quality standards). "
                "GM — General Manager (e.g., GM Operations). "
                "LS — Latte Specialist (a certified team member qualified to handle POS and customer orders)."
            ),
            "tags": ["glossary", "abbreviations", "full_form", "sm", "asm", "bt", "hrbp", "qa", "gm", "ls", "roles"],
            "qa_pairs": [
                {"instruction": "What is the full form of ASM?", "output": "ASM stands for Assistant Store Manager."},
                {"instruction": "What is the full form of BT?", "output": "BT stands for Buddy Trainer — a certified barista who mentors and trains new team members."},
                {"instruction": "What is the full form of SM?", "output": "SM can stand for Shift Manager (the role between Buddy Trainer and ASM) or Store Manager (the café head), depending on context."},
                {"instruction": "What is the full form of HRBP?", "output": "HRBP stands for Human Resources Business Partner."},
                {"instruction": "What is the full form of QA?", "output": "QA stands for Quality Assurance — the team or person responsible for maintaining quality standards."},
                {"instruction": "What is the full form of GM?", "output": "GM stands for General Manager (e.g., GM Operations)."},
                {"instruction": "What is the full form of LS?", "output": "LS stands for Latte Specialist — a certified team member qualified to handle POS and customer orders."},
                {"instruction": "What does ASM stand for?", "output": "ASM stands for Assistant Store Manager."},
                {"instruction": "What does BT stand for?", "output": "BT stands for Buddy Trainer."},
                {"instruction": "What does HRBP stand for?", "output": "HRBP stands for Human Resources Business Partner."}
            ]
        },
        {
            "title": "Framework & Program Abbreviations",
            "intent": "Provide full forms of all framework and program acronyms used at Third Wave Coffee.",
            "content": (
                "WING's — W: Winning, I: Integrated Development, N: Nurturing Talent, G: Getting Ready for Success. A structured internal development program for building a strong talent pipeline. "
                "RESPECT — R: Responsibility, E: Empathy, S: Service Excellence, P: Performance with Purpose, E: Ethics & Integrity, C: Collaboration, T: Trust. The core values framework at Third Wave Coffee. "
                "BLEND — B: Brand Touchpoints, L: Learning & Leadership, E: Engage & Elevate, N: Notice & Nurture, D: Driven by R.E.S.P.E.C.T. The CX in-store execution framework. "
                "C.O.F.F.E.E. — C: Cheerful Welcome, O: Order Taking Assistance, F: Friendly & Accurate Service, F: Feedback With Solutions, E: Enjoyable Experience, E: Enthusiastic Exit. The six steps of customer experience at Third Wave Coffee. "
                "IDP — Internal Development Process (the step-by-step process within WING's for identifying and developing employees for promotion). "
                "RNR — Recognize & Reward (the program for recognizing team members who demonstrate RESPECT values). "
                "SHLP — Shift Leadership Program (a workshop required for Shift Managers progressing to ASM). "
                "HD — Home Delivery (HD Playbook covers standards and procedures for home delivery orders)."
            ),
            "tags": ["glossary", "abbreviations", "full_form", "wings", "respect", "blend", "coffee", "idp", "rnr", "shlp", "hd", "frameworks"],
            "qa_pairs": [
                {"instruction": "What is the full form of WING's?", "output": "WING's stands for: W — Winning, I — Integrated Development, N — Nurturing Talent, G — Getting Ready for Success. It is a structured internal development program for building a strong talent pipeline."},
                {"instruction": "What is the full form of RESPECT?", "output": "RESPECT stands for: R — Responsibility, E — Empathy, S — Service Excellence, P — Performance with Purpose, E — Ethics & Integrity, C — Collaboration, T — Trust. It is the core values framework at Third Wave Coffee."},
                {"instruction": "What is the full form of BLEND?", "output": "BLEND stands for: B — Brand Touchpoints, L — Learning & Leadership, E — Engage & Elevate, N — Notice & Nurture, D — Driven by R.E.S.P.E.C.T. It is the CX in-store execution framework."},
                {"instruction": "What is the full form of C.O.F.F.E.E.?", "output": "C.O.F.F.E.E. stands for: C — Cheerful Welcome, O — Order Taking Assistance, F — Friendly & Accurate Service, F — Feedback With Solutions, E — Enjoyable Experience, E — Enthusiastic Exit. These are the six steps of customer experience at Third Wave Coffee."},
                {"instruction": "What is the full form of IDP?", "output": "IDP stands for Internal Development Process — the step-by-step process within WING's for identifying and developing employees for promotion."},
                {"instruction": "What is the full form of RNR?", "output": "RNR stands for Recognize & Reward — the program for recognizing team members who demonstrate RESPECT values."},
                {"instruction": "What is the full form of SHLP?", "output": "SHLP stands for Shift Leadership Program — a workshop required for Shift Managers progressing to ASM."},
                {"instruction": "What is the full form of HD?", "output": "HD stands for Home Delivery. The HD Playbook covers standards and procedures for home delivery orders."},
                {"instruction": "What does BLEND stand for?", "output": "BLEND stands for Brand Touchpoints, Learning & Leadership, Engage & Elevate, Notice & Nurture, and Driven by R.E.S.P.E.C.T."},
                {"instruction": "What does C.O.F.F.E.E. stand for?", "output": "C.O.F.F.E.E. stands for Cheerful Welcome, Order Taking Assistance, Friendly & Accurate Service, Feedback With Solutions, Enjoyable Experience, and Enthusiastic Exit."},
                {"instruction": "What does IDP stand for?", "output": "IDP stands for Internal Development Process."},
                {"instruction": "What does SHLP stand for?", "output": "SHLP stands for Shift Leadership Program."},
                {"instruction": "What does RNR stand for?", "output": "RNR stands for Recognize & Reward."},
                {"instruction": "List all abbreviations used at Third Wave Coffee.", "output": "Key abbreviations: TWC (Third Wave Coffee), TR (Third Rush), CX (Customer Experience), CPI (Customer Pulse Index), SOP (Standard Operating Procedure), POS (Point of Sale), MOD (Manager on Duty), LMS (Learning Management System), UPI (Unified Payments Interface), SM (Shift Manager/Store Manager), ASM (Assistant Store Manager), BT (Buddy Trainer), HRBP (HR Business Partner), QA (Quality Assurance), GM (General Manager), LS (Latte Specialist), IDP (Internal Development Process), RNR (Recognize & Reward), SHLP (Shift Leadership Program), HD (Home Delivery). Frameworks: WING's, RESPECT, BLEND, C.O.F.F.E.E."},
                {"instruction": "What are the abbreviations and full forms used at Third Wave Coffee?", "output": "Third Wave Coffee — Third Wave Coffee, TR — Third Rush, CX — Customer Experience, CPI — Customer Pulse Index, SOP — Standard Operating Procedure, POS — Point of Sale, MOD — Manager on Duty, LMS — Learning Management System, UPI — Unified Payments Interface, SM — Shift Manager/Store Manager, ASM — Assistant Store Manager, BT — Buddy Trainer, HRBP — HR Business Partner, QA — Quality Assurance, GM — General Manager, LS — Latte Specialist, IDP — Internal Development Process, RNR — Recognize & Reward, SHLP — Shift Leadership Program, HD — Home Delivery, WING's — Winning/Integrated Development/Nurturing Talent/Getting Ready for Success, RESPECT — Responsibility/Empathy/Service Excellence/Performance with Purpose/Ethics & Integrity/Collaboration/Trust, BLEND — Brand Touchpoints/Learning & Leadership/Engage & Elevate/Notice & Nurture/Driven by R.E.S.P.E.C.T., C.O.F.F.E.E. — Cheerful Welcome/Order Taking Assistance/Friendly & Accurate Service/Feedback With Solutions/Enjoyable Experience/Enthusiastic Exit."}
            ]
        }
    ]
}


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {m["id"] for m in data["modules"]}
    if glossary_module["id"] in existing_ids:
        print(f"  SKIP (already exists): {glossary_module['id']}")
        return

    data["modules"].append(glossary_module)
    qa_count = sum(len(c.get("qa_pairs", [])) for c in glossary_module["chunks"])
    print(f"  ADDED: {glossary_module['id']} — {len(glossary_module['chunks'])} chunks, {qa_count} QA pairs")

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total_modules = len(data["modules"])
    total_chunks = sum(len(m["chunks"]) for m in data["modules"])
    total_qa = sum(len(c.get("qa_pairs", [])) for m in data["modules"] for c in m["chunks"])
    print(f"\nDone.")
    print(f"Total: {total_modules} modules, {total_chunks} chunks, {total_qa} QA pairs")


if __name__ == "__main__":
    main()

"""
One-time script: Add Home Delivery & Takeaway Process playbook to data.json.
Source: HD Process flow update.pdf
"""

import json
import pathlib

DATA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"

new_modules = [
    {
        "id": "hd_takeaway_process",
        "title": "Home Delivery & Takeaway Process (HD Playbook)",
        "description": "Complete Home Delivery & Takeaway process for Third Wave Coffee covering portal activation, order receiving, order preparation, packaging, and the ROAST framework for HD excellence.",
        "chunks": [
            {
                "chunk_id": "hd_overview",
                "title": "HD & Takeaway Process — Overview & Objective",
                "intent": "Explain the purpose and scope of the Home Delivery & Takeaway process at TWC.",
                "content": "Home Delivery & Takeaway Process — Objective: Emphasizing the 'Good to Amazing' journey, this document prioritizes absolutely amazing experiences for home delivery and takeaway customers. Detailed steps address key issues, including missing orders and spillage, enhancing the overall process. The aim is to establish a robust and sustainable home delivery and takeaway process for our at-home customers. Our focus is on delivering excellence and minimizing any potential challenges, ensuring a consistently exceptional Third Wave Coffee experience. The process covers 4 main touchpoints: (1) Introduction to the Brand — portal activation and menu accuracy, (2) Order Receiving — auto-acceptance and KOT flow, (3) Order Preparation — SOP adherence and special instructions, (4) Packaging — sealing, spill prevention, and clear identification.",
                "tags": ["home delivery", "takeaway", "hd", "process", "overview", "touchpoints"],
                "qa_pairs": [
                    {"instruction": "What is the Home Delivery process at TWC?", "output": "TWC's Home Delivery & Takeaway process focuses on the 'Good to Amazing' journey with 4 touchpoints: (1) Introduction to the Brand — portal activation and accurate menu display, (2) Order Receiving — auto-acceptance and KOT printing, (3) Order Preparation — following SOPs and special instructions, (4) Packaging — heat sealing, spill prevention, and labeling."},
                    {"instruction": "What are the 4 touchpoints of the HD process?", "output": "1. Introduction to the Brand — turning on portals, ensuring accurate product availability on Zomato/Swiggy/App\n2. Order Receiving — auto-accepting orders, KOT printing\n3. Order Preparation — following SOPs, handling special instructions\n4. Packaging — heat sealing cups, spill check, writing product names on cups"},
                    {"instruction": "What is the objective of the HD process?", "output": "To establish a robust and sustainable home delivery and takeaway process that delivers an 'absolutely amazing' experience for at-home customers, addresses issues like missing orders and spillage, and ensures a consistently exceptional TWC experience."},
                    {"instruction": "What does HD mean at TWC?", "output": "HD stands for Home Delivery. It refers to the complete process of fulfilling delivery orders from TWC cafés through platforms like Zomato and Swiggy, covering portal activation, order receiving, preparation, and packaging."}
                ]
            },
            {
                "chunk_id": "hd_smallwares",
                "title": "HD Smallwares & Equipment",
                "intent": "List all required smallwares and equipment for Home Delivery and Takeaway.",
                "content": "HD Smallwares and Equipment required: Takeaway cup (Hot), Hot Lids, TWC branded aluminium foil, Small Carry bag, Single cup holder, Big Carry bag, Brown Tape, Tamper proof sticker, Cold lids, Takeaway cup (Cold), Double cup holder, Consumables. Cup Sealer Guide: Don't overfill the cup as it may lead to spillage and ineffective sealing. DO leave a 5mm gap from the rim of the cup. Cup Holder Preparation: Fold the long side inwards and short side outwards. Fold the triangles outwards on all four sides. Tuck in the triangles in the groove. Unfold the holder along the seam to make a rectangle.",
                "tags": ["home delivery", "takeaway", "smallwares", "equipment", "cup holder", "cup sealer", "packaging"],
                "qa_pairs": [
                    {"instruction": "What equipment is needed for HD orders?", "output": "Takeaway cups (hot and cold), hot lids, cold lids, TWC branded aluminium foil, small and big carry bags, single and double cup holders, brown tape, tamper proof stickers, and consumables."},
                    {"instruction": "How do I prepare a cup holder for HD?", "output": "Fold the long side inwards and short side outwards. Fold the triangles outwards on all four sides. Tuck in the triangles in the groove. Unfold the holder along the seam to make a rectangle."},
                    {"instruction": "How much gap should I leave when filling a takeaway cup?", "output": "Leave a 5mm gap from the rim of the cup. Don't overfill as it causes spillage and ineffective sealing."}
                ]
            },
            {
                "chunk_id": "hd_touchpoint_1",
                "title": "HD Touchpoint 1 — Introduction to the Brand (Portal Activation)",
                "intent": "Explain the first HD touchpoint: portal activation and menu accuracy.",
                "content": "Touchpoint 1 — Introduction to the Brand. Objective: Create a positive first impression and enhance overall brand experience by ensuring cafés are shown online on Zomato, Swiggy, and for app pick-up on time with accurate product availability. This develops trust between the brand and customers. Having the café available to order from with accurate products ensures customers develop trust for the brand. Mitigates negative reviews by ensuring product availability is accurate. Process: Step 1 — Turn on HD portals on Urban Piper. Open Urban Piper on Chrome, click 'Session Settings', ensure Zomato, Swiggy and UrbanPiper are active, click 'Platforms'. Step 2 — Turn off out-of-stock products on Urban Piper and LS. On Urban Piper: Select 'Stock Control', look for unavailable products, turn them off. On LS (for App Pick-up): Click 'New Transaction' under 'In-Store Dine-in', click 'Food Lock', click 'Actions' then 'Lock', choose unavailable products. What if we miss this step? Customer frustration, lost sales, diminished trust, customer attrition, negative reviews, and revenue decline.",
                "tags": ["home delivery", "portal", "urban piper", "zomato", "swiggy", "stock control", "brand", "touchpoint 1"],
                "qa_pairs": [
                    {"instruction": "How do I activate HD portals?", "output": "Open Urban Piper on Chrome → click 'Session Settings' → ensure Zomato, Swiggy and UrbanPiper are active → click 'Platforms'. Then turn off any out-of-stock products under 'Stock Control'."},
                    {"instruction": "How do I turn off out-of-stock items for delivery?", "output": "On Urban Piper: Select 'Stock Control' and turn off unavailable products. On LS (for App Pick-up): Click 'New Transaction' under 'In-Store Dine-in' → 'Food Lock' → 'Actions' → 'Lock' → choose unavailable products."},
                    {"instruction": "What is Touchpoint 1 of the HD process?", "output": "Introduction to the Brand — ensuring cafés are live on Zomato, Swiggy, and app pick-up with accurate product availability. Process includes activating portals on Urban Piper and turning off out-of-stock items."},
                    {"instruction": "What happens if we don't activate HD portals?", "output": "Customer frustration, lost sales to competitors, diminished trust, customer attrition, negative online reviews, and overall revenue decline."},
                    {"instruction": "What is Urban Piper used for?", "output": "Urban Piper is the platform used to manage HD portal activation for Zomato, Swiggy, and app pick-up orders. It handles session settings, platform activation, and stock control for delivery menus."}
                ]
            },
            {
                "chunk_id": "hd_touchpoint_2",
                "title": "HD Touchpoint 2 — Order Receiving (Auto-Accept)",
                "intent": "Explain the second HD touchpoint: auto-accepting orders.",
                "content": "Touchpoint 2 — Order Receiving. Objective: Auto-accepting online orders ensures a seamless and quick process, enhancing the overall experience without any cancellations. This improves operational efficiency, order accuracy, consistency and reliability, and increases sales and loyalty. Process: The HD order is received and auto-accepted. It shows as 'KOT Printed' on LS and 'Acknowledged' on Urban Piper (Satellite). What if we miss this step? Customer dissatisfaction, lost sales, negative reviews, diminished trust, and operational challenges from handling order cancellations.",
                "tags": ["home delivery", "order receiving", "auto accept", "kot", "urban piper", "ls", "touchpoint 2"],
                "qa_pairs": [
                    {"instruction": "How are HD orders received?", "output": "HD orders are auto-accepted. They show as 'KOT Printed' on LS and 'Acknowledged' on Urban Piper (Satellite). No manual acceptance needed."},
                    {"instruction": "What is Touchpoint 2 of the HD process?", "output": "Order Receiving — orders are auto-accepted, showing as 'KOT Printed' on LS and 'Acknowledged' on Urban Piper. This ensures seamless processing without cancellations."},
                    {"instruction": "What happens if HD orders are not auto-accepted?", "output": "Customer dissatisfaction, lost sales to competitors, negative reviews, diminished trust, and operational challenges from handling cancellations."}
                ]
            },
            {
                "chunk_id": "hd_touchpoint_3",
                "title": "HD Touchpoint 3 — Order Preparation",
                "intent": "Explain the third HD touchpoint: preparing orders correctly.",
                "content": "Touchpoint 3 — Order Preparation. Objective: Following Standard Operating Procedures (SOP) ensures consistent preparation, maintaining quality for a uniform customer experience. Adhering to special instructions caters to individual preferences. A systematic approach streamlines the preparation process, promoting efficiency and reducing errors. Process: Immediately after the order is auto-accepted, KOTs for products are printed at respective stations, along with a 'Master KOT' at the POS Printer. Points to observe on a KOT: Order Type, Order ID, Special Instructions, Total Items. Cup Filling Guide: Don't overfill the cup — leave a 5mm gap from the rim for effective sealing. Prepare beverages as per SOP in a takeaway cup. What if we miss this step? Inconsistent quality, customer discontent, customer loss, negative reviews and reputation damage, operational inefficiencies.",
                "tags": ["home delivery", "order preparation", "sop", "kot", "master kot", "cup filling", "special instructions", "touchpoint 3"],
                "qa_pairs": [
                    {"instruction": "How are HD orders prepared?", "output": "After auto-acceptance, KOTs print at respective stations plus a Master KOT at POS. Check each KOT for: Order Type, Order ID, Special Instructions, Total Items. Prepare beverages per SOP in takeaway cups. Leave a 5mm gap from the rim for sealing."},
                    {"instruction": "What is the Master KOT?", "output": "The Master KOT is printed at the POS Printer when an HD order is auto-accepted. It contains the full order details alongside individual station KOTs that print at respective stations (bar, food, etc.)."},
                    {"instruction": "What should I check on a KOT for HD orders?", "output": "Check: Order Type (HD/Takeaway), Order ID, Special Instructions from the customer, and Total Items in the order."},
                    {"instruction": "What is Touchpoint 3 of the HD process?", "output": "Order Preparation — following SOPs to prepare orders consistently, adhering to special instructions, using takeaway cups with a 5mm gap from rim, and checking KOTs for all order details."}
                ]
            },
            {
                "chunk_id": "hd_touchpoint_4",
                "title": "HD Touchpoint 4 — Packaging",
                "intent": "Explain the fourth HD touchpoint: proper packaging for delivery.",
                "content": "Touchpoint 4 — Packaging. Objective: Heat sealing cups preserves freshness, ensuring customers receive orders in the best possible condition. Spill check and heat-sealing minimize spill risk during transportation. Writing special instructions or product name on the cup provides clarity, ensuring correct orders. Process: Heat seal all cups. Conduct a spill check. Write the product name or special instructions on the cup. Use tamper-proof stickers. Package in appropriate carry bags with cup holders. Impact: Positive first impressions, consistent satisfaction, enhanced brand reputation, operational efficiency. What if we miss this step? Negative first impressions, lost business, diminished trust, and reputation damage.",
                "tags": ["home delivery", "packaging", "heat seal", "spill check", "tamper proof", "carry bag", "cup holder", "touchpoint 4"],
                "qa_pairs": [
                    {"instruction": "How should HD orders be packaged?", "output": "Heat seal all cups → conduct a spill check → write product name or special instructions on the cup → apply tamper-proof stickers → package in appropriate carry bags with cup holders."},
                    {"instruction": "What is Touchpoint 4 of the HD process?", "output": "Packaging — heat sealing cups for freshness, conducting spill checks, writing product names on cups, using tamper-proof stickers, and packaging in carry bags with holders."},
                    {"instruction": "Why is heat sealing important for HD?", "output": "Heat sealing preserves freshness, minimizes spill risk during transportation, and ensures customers receive orders in the best possible condition."},
                    {"instruction": "What should be written on HD cups?", "output": "Write the product name or any special instructions on the cup to ensure the customer receives the correct order."}
                ]
            },
            {
                "chunk_id": "hd_roast_framework",
                "title": "ROAST — Home Delivery Excellence Framework",
                "intent": "Explain the ROAST acronym framework used in the HD playbook.",
                "content": "ROAST is the Home Delivery excellence framework at Third Wave Coffee. It stands for: R — Readiness (ensure portals are live, stock is accurate, and equipment is ready before orders come in), O — Order Accuracy (auto-accept orders, verify KOTs, follow special instructions precisely), A — Adherence to SOP (prepare every item per standard operating procedure, no shortcuts), S — Sealing & Packaging (heat seal cups, spill check, label clearly, use tamper-proof stickers), T — Timeliness (complete preparation and packaging quickly to meet delivery partner pickup times). ROAST captures the five pillars of the HD process touchpoints in a single framework. Following ROAST ensures every home delivery order meets TWC's quality standards from portal activation to rider handoff.",
                "tags": ["roast", "home delivery", "hd", "framework", "readiness", "order accuracy", "sop", "sealing", "packaging", "timeliness"],
                "qa_pairs": [
                    {"instruction": "What does ROAST stand for?", "output": "ROAST is the Home Delivery excellence framework: R — Readiness (portals live, stock accurate, equipment ready), O — Order Accuracy (auto-accept, verify KOTs, follow special instructions), A — Adherence to SOP (prepare per standard, no shortcuts), S — Sealing & Packaging (heat seal, spill check, label, tamper-proof stickers), T — Timeliness (complete prep and packaging for rider pickup)."},
                    {"instruction": "What is the ROAST framework?", "output": "ROAST is TWC's Home Delivery excellence framework with 5 pillars: Readiness, Order Accuracy, Adherence to SOP, Sealing & Packaging, and Timeliness. It captures the complete HD process from portal activation to rider handoff."},
                    {"instruction": "What is the R in ROAST?", "output": "R stands for Readiness — ensure portals are live on Zomato/Swiggy, stock is accurate with out-of-stock items turned off, and all equipment and packaging materials are ready before orders come in."},
                    {"instruction": "What is the O in ROAST?", "output": "O stands for Order Accuracy — auto-accept orders without cancellations, verify KOTs for order type/ID/special instructions/total items, and follow customer special instructions precisely."},
                    {"instruction": "What is the A in ROAST?", "output": "A stands for Adherence to SOP — prepare every item per the standard operating procedure with no shortcuts, even during peak hours."},
                    {"instruction": "What is the S in ROAST?", "output": "S stands for Sealing & Packaging — heat seal all cups, conduct spill checks, label cups with product name or special instructions, use tamper-proof stickers, and package in appropriate bags with holders."},
                    {"instruction": "What is the T in ROAST?", "output": "T stands for Timeliness — complete preparation and packaging quickly to meet delivery partner pickup times, ensuring freshness and customer satisfaction."},
                    {"instruction": "How does ROAST relate to the HD touchpoints?", "output": "ROAST maps to the 4 HD touchpoints: Readiness = Touchpoint 1 (portal activation), Order Accuracy = Touchpoint 2 (order receiving), Adherence to SOP = Touchpoint 3 (order preparation), Sealing & Packaging + Timeliness = Touchpoint 4 (packaging and handoff)."}
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
print("⚠ Delete backend/.faiss_cache/ to rebuild the index on next server start.")

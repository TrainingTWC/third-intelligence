"""
Enrich cx_coffee_framework and cx_blend_framework modules
with detailed content from COFFEE.pdf and Blend.pdf.
"""
import json, pathlib

DATA = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"

# --- New chunks for cx_coffee_framework ---
coffee_new_chunks = [
    {
        "title": "C.O.F.F.E.E. Pro Tips",
        "intent": "Practical pro tips for executing each C.O.F.F.E.E. step effectively.",
        "content": (
            "Pro Tips for executing the C.O.F.F.E.E. framework at TWC/TR. "
            "Cheerful Welcome Tips: Ensure your tone matches your words. A 'Welcome to Third Wave / Third Rush' with a cheerful tone lets the customer know you are happy to have them. Saying it in a dull manner with no enthusiasm makes the customer feel unwelcome and uneasy. "
            "A warm smile, eye contact, and a friendly greeting within a respectful 2-meter distance set the tone for the entire customer experience. "
            "Anticipate customer needs early. A small gesture like guiding them to a seat or opening the door for them creates a welcoming start. "
            "Order Taking Tips: Speak clearly, maintain positive body language, and keep your tone warm and professional in every interaction. "
            "Help customers make confident choices by guiding them through the menu and confirming their order and customizations before serving. "
            "Active listening is the key to an amazing order-taking assistance. "
            "Service Tips: Master salver management — never overload the salver, hold it while serving instead of placing it on the table, and when empty, carry it neatly under the arm. "
            "Present orders with confidence. Announce the items clearly and serve with a genuine smile to enhance the experience. "
            "A well-groomed and hygienic appearance reinforces trust and professionalism from the very first interaction. "
            "Feedback Tips: Choose the right moment for feedback. Approach customers once they are comfortable and have experienced the product. Do not approach while they are on calls, engaged in conversation, or visibly upset. "
            "Experience Tips: A well-maintained space elevates the experience. Keep tables, counters, and customer-facing stations clean and organized at all times. "
            "Let confident body language — standing upright, walking with a calm steady pace, avoiding hunched shoulders — reflect your knowledge and reassure customers they are in capable hands. "
            "Exit Tips: End every visit on a high note. Make eye contact, smile, and thank customers enthusiastically as they leave."
        ),
        "tags": [
            "coffee_framework", "pro_tips", "best_practices", "service_tips",
            "greeting_tips", "salver_management", "body_language", "hygiene"
        ],
        "qa_pairs": [
            {
                "instruction": "What are the pro tips for C.O.F.F.E.E.?",
                "output": "Key pro tips include: ensure your tone matches your words when welcoming, maintain a warm smile and eye contact within 2 meters, anticipate customer needs early, speak clearly with positive body language, guide customers through the menu, master salver management (never overload, hold while serving, carry neatly under the arm when empty), present orders with confidence, maintain a clean well-organized space, choose the right moment for feedback, keep confident body language, and end every visit on a high note."
            },
            {
                "instruction": "How should a barista manage the salver?",
                "output": "Never overload the salver. Hold it while serving instead of placing it on the table. When empty, carry it neatly under the arm. Present orders with confidence — announce items clearly and serve with a genuine smile."
            },
            {
                "instruction": "What body language should baristas maintain?",
                "output": "Stand upright, walk with a calm steady pace, avoid hunched shoulders. This confident body language reflects your knowledge and reassures customers they are in capable hands. Always maintain a warm smile and eye contact."
            },
            {
                "instruction": "When is the right time to ask for feedback?",
                "output": "Approach customers for feedback once they are comfortable and have experienced the product. Do not approach while they are on calls, engaged in conversation, or visibly upset. Choose the right moment — timing matters."
            },
            {
                "instruction": "How should a barista's appearance be?",
                "output": "A well-groomed and hygienic appearance reinforces trust and professionalism from the very first interaction. It sets the standard and builds customer confidence in the team."
            },
            {
                "instruction": "What are the greeting pro tips?",
                "output": "Ensure your tone matches your words — say 'Welcome to Third Wave / Third Rush' with genuine cheerfulness. Saying it dully makes customers feel unwelcome. Use a warm smile, eye contact, and friendly greeting within 2 meters. Anticipate needs early — guide them to a seat or open the door."
            }
        ]
    },
    {
        "title": "C.O.F.F.E.E. Absolute NOs",
        "intent": "Things that must never be done during customer interactions at TWC/TR.",
        "content": (
            "Absolute NOs — behaviors and actions that are strictly prohibited during customer interactions at TWC/TR. "
            "1. Avoid delaying or missing a greeting due to distractions like phones or internal conversations. "
            "2. Never invade a customer's personal space or touch children without permission. "
            "3. There is no place for rude behavior, impatience, or negative body language in customer interactions. "
            "4. Never discriminate against customers based on caste, creed, gender, religion, age, appearance, or ability. "
            "5. Avoid loud internal conversations or discussing operational matters where customers can hear them. "
            "6. Never ignore customers during ordering or service interactions. "
            "7. Do not argue with customers or prioritize internal tasks over customer service. "
            "8. Avoid approaching customers for feedback while they are on calls, engaged in conversation, or visibly upset. "
            "9. Never pressure customers to give feedback, post reviews, or bring more people. "
            "10. Do not overlook cleanliness, hygiene, or maintenance issues anywhere in the café. "
            "11. If an issue can be resolved during the dine-in experience without escalation, do not provide the customer care contact details."
        ),
        "tags": [
            "coffee_framework", "absolute_nos", "prohibited", "dont_do",
            "discrimination", "hygiene", "customer_service_rules"
        ],
        "qa_pairs": [
            {
                "instruction": "What are the Absolute NOs in C.O.F.F.E.E.?",
                "output": "The Absolute NOs are: (1) Don't delay or miss greetings due to phones or internal conversations. (2) Never invade personal space or touch children without permission. (3) No rude behavior, impatience, or negative body language. (4) Never discriminate based on caste, creed, gender, religion, age, appearance, or ability. (5) No loud internal conversations where customers can hear. (6) Never ignore customers during ordering or service. (7) Don't argue with customers or prioritize internal tasks over service. (8) Don't approach for feedback while customers are on calls or visibly upset. (9) Never pressure for feedback or reviews. (10) Don't overlook cleanliness or hygiene issues. (11) If an issue can be resolved during dine-in without escalation, don't give customer care contact details."
            },
            {
                "instruction": "What should baristas never do with customers?",
                "output": "Never ignore customers, argue with them, invade their personal space, discriminate against them, pressure them for feedback or reviews, or prioritize internal tasks over serving them. Also never have loud internal conversations where customers can hear, and never overlook cleanliness or hygiene anywhere in the café."
            },
            {
                "instruction": "Can we give customer care contact details to upset customers?",
                "output": "If an issue can be resolved during the dine-in experience without escalation, do not provide customer care contact details. Try to resolve it on the spot first."
            },
            {
                "instruction": "What discrimination is prohibited at TWC?",
                "output": "Never discriminate against customers based on caste, creed, gender, religion, age, appearance, or ability. Every customer must be treated fairly and respectfully regardless of who they are."
            },
            {
                "instruction": "When should baristas NOT ask for feedback?",
                "output": "Do not approach customers for feedback while they are on calls, engaged in conversation, or visibly upset. Never pressure customers to give feedback, post reviews, or bring more people."
            }
        ]
    },
    {
        "title": "C.O.F.F.E.E. Impact on Customer Segments",
        "intent": "How each C.O.F.F.E.E. step impacts new customers, existing customers, and the business.",
        "content": (
            "Impact of C.O.F.F.E.E. on different customer segments and business. "
            "Cheerful Welcome Impact: For new customers — a warm and polite welcome makes them feel at ease in a new place and situation, creates a positive first impression, and makes them feel valued for choosing our brand. "
            "For existing customers — it makes them feel acknowledged, respected, recognized, and valued for being a regular loyal customer. A bond builds between the customer and the team, driving high repeat frequency. "
            "For business — sets a standard for excellent customer service, helps build rapport with the customer, a good welcome sets the tone for the customer's entire stay, and enhances brand image. "
            "Always smile and say 'Hi welcome to Third Wave / Third Rush!' "
            "Order Taking Impact: For new customers — it makes customers feel at ease, recognized, and valued. Customers are happy to get discounts and offers with choice of billing options. "
            "For existing customers — customer feels recognized and valued, comfortable knowing staff knows their regular order and won't be bothered. "
            "For business — demonstrates professionalism, attention to detail, and commitment to customer satisfaction. Reduces errors and in-turn CPI improves. "
            "Friendly Service Impact: For new customers — the customer trusts that their expectations will be met as no order will be missed or inaccurate. The customer's mind builds a positive image of the team and TWC. "
            "For existing customers — customers feel comfortable, valued, and develop a sense of belonging. Strong customer service differentiates us from other brands and increases customer satisfaction. "
            "For business — excellent customer service differentiates us from competitors and influences customer choice. Exceptional service drives higher spending, builds brand loyalty, and encourages positive word-of-mouth. "
            "Feedback Impact: For new customers — opportunity to clear product-related doubts and assist with additional needs like straws or tissues. Chance to engage and build a lasting connection. "
            "For existing customers — customers can share their views about the product and feel heard. Being listened to makes customers feel valued and satisfied. "
            "For business — helps understanding customer expectations and satisfaction with products. Identifies areas that can be improved to enhance the customer experience. "
            "Enjoyable Experience Impact: For new customers — a great experience makes the customer feel the brand values them. Sets/meets their expectation standards. "
            "For existing customers — makes the customer feel at comfort and ease. Makes the brand more reliable. "
            "For business — a good customer experience sets the tone for the customer's future visits. Compels the brand to ensure all aspects of the business is set right to give great experience consistently. Aids the brand to be innovatively ahead of competition. "
            "Enthusiastic Exit Impact: For new customers — thanking leaves a positive impression and makes them feel like part of the family. Shows that our team genuinely cares. "
            "For existing customers — makes them feel acknowledged, respected, recognized, and valued for being a regular customer. Customer prefers TWC over competition and visits frequently. "
            "For business — enhances the overall customer experience, leaving a lasting positive impression. Customers feel great about coming to TWC and come more often."
        ),
        "tags": [
            "coffee_framework", "impact", "new_customers", "existing_customers",
            "business_impact", "customer_loyalty", "brand_image"
        ],
        "qa_pairs": [
            {
                "instruction": "What is the impact of C.O.F.F.E.E. on new customers?",
                "output": "For new customers: Cheerful Welcome makes them feel at ease and creates a positive first impression. Order Taking makes them feel recognized and valued with discount/offer options. Friendly Service builds trust that expectations will be met. Feedback clears product doubts and builds connections. Enjoyable Experience makes them feel valued. Enthusiastic Exit leaves a positive impression and makes them feel like family."
            },
            {
                "instruction": "How does C.O.F.F.E.E. impact existing customers?",
                "output": "For existing customers: They feel acknowledged, respected, and valued as regulars. A bond builds with the team driving repeat visits. They're comfortable knowing staff knows their order. They feel a sense of belonging. They can share product views and feel heard. They prefer TWC over competition and visit frequently."
            },
            {
                "instruction": "What is the business impact of C.O.F.F.E.E.?",
                "output": "For business: Sets standards for excellent service, builds rapport, enhances brand image, demonstrates professionalism, reduces errors and improves CPI, differentiates from competitors, drives higher spending, builds brand loyalty, encourages word-of-mouth, helps understand customer expectations, and sets the tone for future visits."
            },
            {
                "instruction": "How does a cheerful welcome impact customers?",
                "output": "For new customers, a warm welcome makes them feel at ease in a new situation, creates a positive first impression, and shows they made a good choice. For existing customers, it acknowledges and respects them as regulars, building a bond with the team and driving repeat visits. For business, it sets standards for excellent service and sets the tone for the entire stay."
            },
            {
                "instruction": "What happens when friendly service is consistently delivered?",
                "output": "New customers trust their expectations will be met. Existing customers feel valued and develop a sense of belonging. The business differentiates from competitors, exceptional service drives higher spending, builds brand loyalty, and encourages positive word-of-mouth."
            }
        ]
    }
]

# --- New chunks for cx_blend_framework ---
blend_new_chunks = [
    {
        "title": "Engage & Elevate — Enhancing the Café Experience",
        "intent": "How to engage with customers and elevate their order with thoughtful suggestions.",
        "content": (
            "Engage & Elevate is one of the five pillars of the BLEND CX framework. "
            "Every order is an opportunity to enhance the café experience. When customers choose a coffee, a thoughtful suggestion like a baked good, dessert, or savoury bite can make the moment even better. Offer one relevant recommendation that naturally pairs with their drink or food. "
            "Think of it like helping a friend complete a meal. If they order biryani, you might suggest raita or a cold drink because it makes the meal better. In a café, the idea is the same. "
            "How to Engage: Start with the customer's order. Acknowledge their choice and create a quick connection. This shows attention and makes the interaction feel friendly and personal. "
            "Example engagement phrases: 'Great choice with the cappuccino.' / 'Cold brew is a really refreshing pick.' / 'That's one of our popular drinks.' "
            "Think of it like greeting a guest at home before serving the meal. "
            "How to Elevate: Offer one simple pairing that complements the order. The goal is to enhance the experience, not push a sale. "
            "Example elevation suggestions: 'Our almond croissant goes really well with cappuccino.' / 'Cold brew pairs nicely with the tiramisu.' / 'Many guests enjoy the iced latte with a chocolate brownie.' "
            "Key principle: A small addition that makes the experience better. One suggestion. Friendly tone. No pressure."
        ),
        "tags": [
            "blend", "engage_elevate", "upselling", "pairing",
            "suggestion", "customer_experience", "scripts"
        ],
        "qa_pairs": [
            {
                "instruction": "What is Engage & Elevate in the BLEND framework?",
                "output": "Engage & Elevate is a BLEND pillar focused on enhancing the café experience through thoughtful food-drink pairing suggestions. Engage by acknowledging the customer's choice and creating a quick connection. Elevate by offering one simple pairing that complements their order — like suggesting an almond croissant with cappuccino."
            },
            {
                "instruction": "How do I engage with a customer's order?",
                "output": "Start with their order and acknowledge their choice. Examples: 'Great choice with the cappuccino.' / 'Cold brew is a really refreshing pick.' / 'That's one of our popular drinks.' This shows attention and makes the interaction feel friendly and personal."
            },
            {
                "instruction": "How do I elevate a customer's experience?",
                "output": "Offer one simple pairing that complements their order. Examples: 'Our almond croissant goes really well with cappuccino.' / 'Cold brew pairs nicely with the tiramisu.' / 'Many guests enjoy the iced latte with a chocolate brownie.' The goal is to enhance the experience, not push a sale. One suggestion, friendly tone, no pressure."
            },
            {
                "instruction": "What are good food pairing suggestions at TWC?",
                "output": "Some pairing suggestions: Almond croissant with cappuccino. Tiramisu with cold brew. Chocolate brownie with iced latte. Think of what naturally complements the drink or food — like how raita complements biryani."
            },
            {
                "instruction": "What is the key principle of Engage & Elevate?",
                "output": "A small addition that makes the experience better. One suggestion. Friendly tone. No pressure. The goal is to enhance the experience, not push a sale. Think of it like helping a friend complete a meal."
            }
        ]
    },
    {
        "title": "Notice & Nurture — Reading Cues and Responding Early",
        "intent": "How to observe customer cues and proactively offer support before frustration builds.",
        "content": (
            "Notice & Nurture is one of the five pillars of the BLEND CX framework. "
            "Great service comes from paying attention to small signals. Just like a good host notices when a guest's glass is empty before they ask, baristas can read simple cues and respond early to make the experience smoother. "
            "What is Noticing: Observe guest cues and the café environment. "
            "Examples of noticing: A guest looking repeatedly at the pickup counter. Someone scanning the menu for a long time. A customer checking their watch while waiting. A guest looking unsure about where to collect the order. A customer tasting the drink and looking uncertain. "
            "How to Nurture: Respond early and offer helpful support before frustration builds. "
            "Examples of nurturing: 'Your order will be ready in about a minute.' / 'Let me help you choose if you'd like a recommendation.' / 'We will serve the order at your table.' / 'If you prefer it less sweet, I can adjust that for you.' / Checking in with 'How is your coffee tasting?' "
            "The key is proactive service — anticipate needs and address them before the customer has to ask."
        ),
        "tags": [
            "blend", "notice_nurture", "proactive_service", "customer_cues",
            "observation", "anticipate_needs", "scripts"
        ],
        "qa_pairs": [
            {
                "instruction": "What is Notice & Nurture in the BLEND framework?",
                "output": "Notice & Nurture is a BLEND pillar about paying attention to small customer signals and responding early. Just like a good host notices when a guest's glass is empty before they ask, baristas should read simple cues and proactively offer support before frustration builds."
            },
            {
                "instruction": "What are examples of noticing customer cues?",
                "output": "Examples: A guest looking repeatedly at the pickup counter. Someone scanning the menu for a long time. A customer checking their watch while waiting. A guest looking unsure about where to collect an order. A customer tasting a drink and looking uncertain."
            },
            {
                "instruction": "How do I nurture a customer proactively?",
                "output": "Respond early before frustration builds. Examples: 'Your order will be ready in about a minute.' / 'Let me help you choose if you'd like a recommendation.' / 'We will serve the order at your table.' / 'If you prefer it less sweet, I can adjust that for you.' / Check in with 'How is your coffee tasting?'"
            },
            {
                "instruction": "What should I do if a customer looks confused at the pickup counter?",
                "output": "This is a noticing cue — approach them proactively. You can say 'We will serve the order at your table' or 'Your order will be ready in about a minute.' The key is to respond early and offer helpful support before frustration builds."
            },
            {
                "instruction": "What does proactive service mean?",
                "output": "Proactive service means anticipating customer needs and addressing them before the customer has to ask. Observe cues like someone scanning the menu too long, checking their watch, or looking uncertain — then approach with helpful support like recommendations, order updates, or customization offers."
            }
        ]
    },
    {
        "title": "Driven by R.E.S.P.E.C.T. — Values and RNR Recognition",
        "intent": "Detailed RESPECT behaviors for team culture and how they connect to RNR recognition.",
        "content": (
            "Driven by R.E.S.P.E.C.T. is the fifth pillar of the BLEND CX framework. "
            "RESPECT is the value system that guides how team members work, serve guests, and support each other. It represents the behaviors that create a strong team culture and exceptional café experiences. When team members demonstrate these values, they are to be recognized through RNR (Recognize & Reward) cards and digital badges. "
            "R — Responsibility: Taking responsibility for mistakes and fixing them quickly. Following café standards even during busy hours. Completing tasks without needing reminders. "
            "E — Empathy: Listening carefully to a guest concern and responding calmly. Helping a new teammate learn a process patiently. Offering support when a teammate is overwhelmed. "
            "S — Service Excellence: Greeting guests warmly and engaging with them. Checking back to ensure the guest enjoys their drink. Maintaining clean counters and organized workstations. "
            "P — Performance with Purpose: Practicing coffee skills to improve consistency. Maintaining speed and accuracy during busy periods. Learning more about coffee to guide guests better. "
            "E — Ethics: Following company policies and café standards. Being honest about errors or issues. Treating everyone fairly and respectfully. "
            "C — Collaboration: Sharing knowledge and supporting team learning. Recognizing good work through RNR cards. Communicating clearly with teammates. Being dependable during shifts and responsibilities. "
            "T — Trust: Helping teammates during busy periods. Being dependable during shifts and responsibilities. Following through on commitments and promises. "
            "Team members who demonstrate these RESPECT values are recognized through RNR cards and digital badges as a reward system."
        ),
        "tags": [
            "blend", "respect", "values", "rnr", "recognition",
            "team_culture", "responsibility", "empathy", "service_excellence",
            "performance", "ethics", "collaboration", "trust"
        ],
        "qa_pairs": [
            {
                "instruction": "How does RESPECT connect to the BLEND framework?",
                "output": "Driven by R.E.S.P.E.C.T. is the fifth pillar of BLEND (the D). RESPECT is the value system guiding how the team works, serves guests, and supports each other. Team members demonstrating these values are recognized through RNR cards and digital badges."
            },
            {
                "instruction": "What are RESPECT behaviors for each letter?",
                "output": "R — Responsibility: Fix mistakes quickly, follow standards, complete tasks without reminders. E — Empathy: Listen to concerns calmly, help new teammates patiently. S — Service Excellence: Greet warmly, check back, maintain clean stations. P — Performance with Purpose: Practice skills, maintain speed/accuracy, learn about coffee. E — Ethics: Follow policies, be honest, treat everyone fairly. C — Collaboration: Share knowledge, recognize good work, communicate clearly. T — Trust: Help during busy times, be dependable, follow through on promises."
            },
            {
                "instruction": "What is the RNR system?",
                "output": "RNR stands for Recognize & Reward. When team members demonstrate RESPECT values — like taking responsibility, showing empathy, delivering service excellence, or collaborating well — they are recognized through RNR cards and digital badges."
            },
            {
                "instruction": "What does Responsibility mean in RESPECT?",
                "output": "Responsibility means taking ownership of mistakes and fixing them quickly, following café standards even during busy hours, and completing tasks without needing reminders."
            },
            {
                "instruction": "What does Empathy mean in RESPECT?",
                "output": "Empathy means listening carefully to a guest's concern and responding calmly, helping a new teammate learn a process patiently, and offering support when a teammate is overwhelmed."
            },
            {
                "instruction": "What does Collaboration mean in RESPECT?",
                "output": "Collaboration means sharing knowledge and supporting team learning, recognizing good work through RNR cards, communicating clearly with teammates, and being dependable during shifts and responsibilities."
            },
            {
                "instruction": "How are RESPECT values recognized?",
                "output": "Team members who demonstrate RESPECT values are recognized through RNR (Recognize & Reward) cards and digital badges. This recognition system encourages everyone to consistently practice the behaviors that create a strong team culture and exceptional café experiences."
            }
        ]
    },
    {
        "title": "Grievance Handling — Apologize & Solutionize",
        "intent": "The two-step approach to handling customer grievances in-store.",
        "content": (
            "When a customer has a complaint or grievance, TWC/TR follows a two-step approach: Apologize and Solutionize. "
            "Step 1 — Apologize: Sincerely apologize for the inconvenience. Acknowledge the customer's concern without being defensive. Show empathy and let them know you understand their frustration. Use phrases like 'I'm really sorry about this' or 'I completely understand your concern.' "
            "Step 2 — Solutionize: Immediately offer a solution to resolve the issue. Take ownership and act quickly. If the product is wrong, remake it. If the service was slow, acknowledge and expedite. If there's a quality issue, replace the item. The goal is to turn a negative experience into a positive one. "
            "Key principle: If an issue can be resolved during the dine-in experience without escalation, resolve it on the spot. Do not provide customer care contact details unless the issue requires escalation beyond the store's capability."
        ),
        "tags": [
            "blend", "grievance", "complaint", "apologize",
            "solutionize", "customer_complaint", "resolution"
        ],
        "qa_pairs": [
            {
                "instruction": "How should grievances be handled at TWC?",
                "output": "Follow the two-step approach: Apologize and Solutionize. First, sincerely apologize and acknowledge the concern without being defensive. Then immediately offer a solution — remake the product, expedite the service, or replace the item. Resolve it on the spot if possible."
            },
            {
                "instruction": "What does Apologize and Solutionize mean?",
                "output": "It's TWC's two-step grievance handling approach. Apologize: sincerely acknowledge the customer's concern with empathy — 'I'm really sorry about this.' Solutionize: immediately take ownership and act — remake the product, replace the item, or expedite service. The goal is to turn a negative experience into a positive one."
            },
            {
                "instruction": "When should I escalate a customer complaint?",
                "output": "Only escalate if the issue cannot be resolved during the dine-in experience at the store level. If it can be resolved on the spot — by remaking a product, replacing an item, or fixing the service issue — do that first. Don't provide customer care contact details unless escalation is truly needed."
            }
        ]
    }
]


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))

    for mod in data["modules"]:
        if mod["id"] == "cx_coffee_framework":
            mod["chunks"].extend(coffee_new_chunks)
            print(f"  cx_coffee_framework: added {len(coffee_new_chunks)} chunks, "
                  f"now {len(mod['chunks'])} total")

        if mod["id"] == "cx_blend_framework":
            mod["chunks"].extend(blend_new_chunks)
            print(f"  cx_blend_framework: added {len(blend_new_chunks)} chunks, "
                  f"now {len(mod['chunks'])} total")

    total_chunks = sum(len(m["chunks"]) for m in data["modules"])
    total_qa = sum(
        len(qa)
        for m in data["modules"]
        for c in m["chunks"]
        for qa in [c.get("qa_pairs", [])]
    )
    print(f"\n  Total modules: {len(data['modules'])}")
    print(f"  Total chunks:  {total_chunks}")
    print(f"  Total QA pairs: {total_qa}")

    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\n  data.json updated successfully!")


if __name__ == "__main__":
    main()

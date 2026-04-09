"""
Append CX Playbook 2.0 content to data.json as new modules.
Run once, then delete this script.
"""
import json
import pathlib

DATA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"

new_modules = [
    # ── MODULE 1: BLEND Framework Overview ──
    {
        "id": "cx_blend_framework",
        "title": "BLEND — CX In-Store Execution Framework",
        "description": "The BLEND framework defines the five pillars of in-store customer experience execution at TWC/TR: Brand Touchpoints, Learning & Leadership, Engage & Elevate, Notice & Nurture, and Driven by R.E.S.P.E.C.T.",
        "chunks": [
            {
                "title": "BLEND Framework Overview",
                "intent": "Explain what the BLEND CX framework is and its five pillars.",
                "content": "BLEND is the CX in-store execution framework used at Third Wave Coffee and Third Rush. It stands for: B — Brand Touchpoints (consistent brand standards across every customer interaction), L — Learning & Leadership (training and development for team members), E — Engage & Elevate (connecting with customers and enhancing their experience), N — Notice & Nurture (observing guest cues and responding proactively), D — Driven by R.E.S.P.E.C.T. (values-based culture guiding team behavior). Together, these five pillars ensure every café delivers a consistently great customer experience.",
                "tags": ["blend", "framework", "cx", "in_store", "execution", "brand_touchpoints"],
                "qa_pairs": [
                    {"instruction": "What is the BLEND framework?", "output": "BLEND is the CX in-store execution framework used at Third Wave Coffee and Third Rush. It has five pillars: Brand Touchpoints, Learning & Leadership, Engage & Elevate, Notice & Nurture, and Driven by R.E.S.P.E.C.T."},
                    {"instruction": "What does BLEND stand for?", "output": "B stands for Brand Touchpoints, L for Learning & Leadership, E for Engage & Elevate, N for Notice & Nurture, and D for Driven by R.E.S.P.E.C.T."},
                    {"instruction": "What are the five pillars of CX execution at TWC?", "output": "The five pillars are: Brand Touchpoints, Learning & Leadership, Engage & Elevate, Notice & Nurture, and Driven by R.E.S.P.E.C.T. — collectively known as the BLEND framework."},
                    {"instruction": "What is the CX in-store execution framework?", "output": "It's called BLEND. It ensures consistent customer experience across all TWC/TR stores through five pillars: Brand Touchpoints, Learning & Leadership, Engage & Elevate, Notice & Nurture, and Driven by R.E.S.P.E.C.T."}
                ]
            },
            {
                "title": "Brand Touchpoints & Gold Standards",
                "intent": "Explain the brand touchpoint standards and gold standards for customer interactions.",
                "content": "TWC/TR Gold Standards define how every touchpoint should be executed. Cheerful Greeting (2M Rule): Any team member within 2 meters smiles, makes eye contact, and greets in a gentle audible tone — 'Hi, welcome to TWC/TR.' If farther away, acknowledge with eye contact and a smile. Go beyond by helping customers find a table, assisting with queries, greeting children warmly. We avoid loud greetings to ensure other customers are not disturbed. Order Taking Assistance: Certified LS or trained team member at POS engages the customer, confirms dine-in/takeaway, guides selection, repeats order for accuracy, recommends app offers, and confirms payment. Go beyond by recommending one suitable upsell and one suggestion. If the queue reaches three, open the second POS. We do not cheat the customer at TWC/TR. Friendly & Accurate Service: Team member on the floor confirms items and customizations with expeditor, carries items safely on the salver, introduces themselves, and announces items while serving. Go beyond by observing non-verbal cues and anticipating needs. We go the extra mile by saying 'Absolutely' to customers' requests and thanking them after every interaction. Feedback With Solutions: Team member serving the table conducts checkback once the customer has consumed about one-third of the product. Ask 'How is your food/beverage/dessert today?' Positive feedback: acknowledge and ask if they need anything else. Negative feedback: apologize sincerely and resolve concerns immediately. Forcing customers for feedback must be avoided as it takes away from the experience. Enjoyable Experience: All team members maintain a clean, organized café environment and respond positively to customer requests. Start with 'Absolutely' and offer suitable solutions. Ensure customers have a relaxed, enjoyable café experience. Enthusiastic Exit (2M Rule): Any team member or MOD thanks customers between table and exit with eye contact and a warm smile — 'Thank you ma'am/sir, see you soon.' A kind smile goes a long way. Leave customers with a positive final impression without disturbing others with loud thank yous.",
                "tags": ["brand_touchpoints", "gold_standards", "greeting", "2m_rule", "order_taking", "service", "feedback", "exit", "cheerful_welcome"],
                "qa_pairs": [
                    {"instruction": "What are the TWC/TR Gold Standards?", "output": "The Gold Standards define six touchpoints: Cheerful Greeting (2M Rule), Order Taking Assistance, Friendly & Accurate Service, Feedback With Solutions, Enjoyable Experience, and Enthusiastic Exit (2M Rule). Each has specific 'How' and 'Go Beyond' actions."},
                    {"instruction": "What is the 2-meter rule?", "output": "The 2-meter rule applies to greetings and exits. Any team member within 2 meters of a customer must acknowledge them — with a smile, eye contact, and a greeting at entry, and a thank-you at exit."},
                    {"instruction": "What are brand touchpoints at TWC?", "output": "Brand touchpoints are the six Gold Standard interactions: Cheerful Greeting (2M Rule), Order Taking Assistance, Friendly & Accurate Service, Feedback With Solutions, Enjoyable Experience, and Enthusiastic Exit (2M Rule)."},
                    {"instruction": "How should a barista greet customers at TWC?", "output": "Smile, make eye contact, and greet in a gentle audible tone: 'Hi, welcome to TWC/TR.' If the customer is farther away, acknowledge with eye contact and a smile. Go beyond by helping them find a table, assisting with queries, and greeting children warmly. Avoid loud greetings to not disturb other customers."},
                    {"instruction": "What is the checkback process?", "output": "Conduct a checkback once the customer has consumed about one-third of their product. Ask: 'How is your food/beverage/dessert today?' If positive, acknowledge and offer further assistance. If negative, apologize sincerely and resolve immediately. Never force customers for feedback."},
                    {"instruction": "How should the exit experience be handled?", "output": "Thank customers between table and exit with eye contact and a warm smile: 'Thank you ma'am/sir, see you soon.' A kind smile goes a long way. Leave a positive final impression without loud thank yous that disturb others."}
                ]
            },
            {
                "title": "Learning & Leadership — CX Training Levels",
                "intent": "Describe the training levels and learning resources for CX at TWC.",
                "content": "CX training is organized into two levels. Level 1 (Basic Barista, Orientation): What is CX, Importance of CX, Brand Touch Points, Grievance handling, Body Language and Tone, Packaging standards. Resources include CX Playbook, HD Playbook, Level-1 LMS, and Wisdom Wednesdays LMS. Level 2 (Advanced Barista): Advanced Coffee tasting, Merch Selling, Advanced Grievance handling. Resources include Advanced Barista Kit LMS. Leadership areas include Team Management on shift, Level 2 Grievance handling, and BT and SHLP Briefing & Acting upon CX.",
                "tags": ["training", "learning", "leadership", "barista", "orientation", "lms", "grievance", "cx_training"],
                "qa_pairs": [
                    {"instruction": "What CX training does a basic barista receive?", "output": "Basic baristas receive Level 1 training covering: What is CX, Importance of CX, Brand Touch Points, Grievance handling, Body Language and Tone, and Packaging standards. Resources include the CX Playbook, HD Playbook, Level-1 LMS, and Wisdom Wednesdays LMS."},
                    {"instruction": "What does Level 2 CX training cover?", "output": "Level 2 (Advanced Barista) covers Advanced Coffee tasting, Merch Selling, and Advanced Grievance handling. The resource is the Advanced Barista Kit on LMS."},
                    {"instruction": "What leadership areas are covered in CX training?", "output": "Leadership areas include Team Management on shift, Level 2 Grievance handling, and BT and SHLP Briefing & Acting upon CX."}
                ]
            }
        ]
    },

    # ── MODULE 2: C.O.F.F.E.E. Framework ──
    {
        "id": "cx_coffee_framework",
        "title": "C.O.F.F.E.E. — Customer Experience Steps",
        "description": "The C.O.F.F.E.E. framework defines the six steps of customer experience at TWC: Cheerful Welcome, Order Taking Assistance, Friendly & Accurate Service, Feedback With Solutions, Enjoyable Experience, and Enthusiastic Exit.",
        "chunks": [
            {
                "title": "C — Cheerful Welcome",
                "intent": "How to create a positive first impression and make customers feel valued.",
                "content": "Cheerful Welcome is the first step of C.O.F.F.E.E. Objectives: Create a positive first impression and enhance overall customer experience. Make customers feel valued and appreciated. When you enter a store and they welcome you warmly, you feel comfortable right away. Without that warmth, it feels awkward and uninviting. Our café should always feel like that warm welcome. Welcoming customers shows that you acknowledge their presence and appreciate their business, helping them feel valued.",
                "tags": ["cheerful_welcome", "greeting", "first_impression", "coffee_framework"],
                "qa_pairs": [
                    {"instruction": "What is the first step in the C.O.F.F.E.E. framework?", "output": "The first step is C — Cheerful Welcome. It focuses on creating a positive first impression and making customers feel valued and appreciated from the moment they walk in."},
                    {"instruction": "Why is the cheerful welcome important?", "output": "A warm welcome makes customers feel comfortable right away. Without it, the café feels awkward and uninviting. Welcoming customers acknowledges their presence and shows you appreciate their business."}
                ]
            },
            {
                "title": "O — Order Taking Assistance",
                "intent": "How to take orders accurately, efficiently, and with smart selling.",
                "content": "Order Taking Assistance is the second step of C.O.F.F.E.E. Objectives: Order Accuracy & Payment Clarity — record orders correctly to ensure the team prepares the right items and customers are charged accurately, reducing errors and disputes. Speed & Efficiency — take orders quickly and clearly to reduce queue time and help the team prepare beverages and food promptly. Customization & Smart Selling — accommodate special requests or dietary needs while suggesting complementary items (e.g., desserts with coffee) to enhance the guest experience.",
                "tags": ["order_taking", "accuracy", "payment", "upselling", "smart_selling", "coffee_framework"],
                "qa_pairs": [
                    {"instruction": "What is the Order Taking Assistance step about?", "output": "It's the O in C.O.F.F.E.E. — focused on order accuracy, payment clarity, speed and efficiency, and smart selling. Take orders correctly, reduce queue time, accommodate special requests, and suggest complementary items."},
                    {"instruction": "What is smart selling at TWC?", "output": "Smart selling means accommodating special requests or dietary needs while suggesting complementary items — like desserts with coffee — to enhance the guest experience without pushing extra products."}
                ]
            },
            {
                "title": "F — Friendly & Accurate Service",
                "intent": "How to deliver orders correctly and consistently with a friendly attitude.",
                "content": "Friendly & Accurate Service is the third step of C.O.F.F.E.E. Objectives: Accurate Orders & Customization — the customer is satisfied when the right order is served with accurate customizations. Timely Service — efficient and timely service is essential; customers should not have to wait excessively long, and service staff should be attentive. Consistency — strive for consistency in service across different shifts and days; customers should have a similar experience regardless of when they visit. Impact: New customers trust that their expectations will be met. Existing customers feel comfortable, valued, and develop a sense of belonging. For the business, strong customer service differentiates us from competitors and influences customer choice.",
                "tags": ["friendly_service", "accurate_service", "consistency", "timely_service", "coffee_framework"],
                "qa_pairs": [
                    {"instruction": "What does Friendly & Accurate Service mean in the C.O.F.F.E.E. framework?", "output": "It's the first F — focused on delivering accurate orders with correct customizations, providing timely service so customers don't wait too long, and maintaining consistency across shifts and days."},
                    {"instruction": "Why is consistency in service important?", "output": "Customers should have a similar experience regardless of when they visit. Consistency builds trust — new customers know expectations will be met, and existing customers feel comfortable and valued."}
                ]
            },
            {
                "title": "F — Feedback With Solutions",
                "intent": "How to gather feedback and resolve customer concerns.",
                "content": "Feedback With Solutions is the fourth step of C.O.F.F.E.E. Objectives: Improve Communication & Engagement — customer feedback creates a platform for open communication. Improve Customer Satisfaction — understanding customer opinions and concerns helps address issues promptly and enhance the overall experience. Improvement & Prevention of Issues — customer feedback helps identify areas for improvement; addressing concerns early prevents negative feedback from spreading online or in the public domain. Impact: New customers get clarity on product-related doubts. Existing customers feel heard, valued, and satisfied. For the business, it helps understand customer expectations and identifies areas for improvement.",
                "tags": ["feedback", "solutions", "checkback", "customer_satisfaction", "coffee_framework"],
                "qa_pairs": [
                    {"instruction": "What is Feedback With Solutions in the C.O.F.F.E.E. framework?", "output": "It's the second F — focused on gathering customer feedback through checkbacks, improving communication, and resolving concerns promptly. Addressing issues early prevents negative feedback from spreading."},
                    {"instruction": "How should feedback be collected from customers?", "output": "Conduct a checkback once the customer has consumed about one-third of their product. Ask 'How is your food/beverage/dessert today?' Listen attentively. For positive feedback, acknowledge and offer further help. For negative feedback, apologize sincerely and resolve immediately."}
                ]
            },
            {
                "title": "E — Enjoyable Experience",
                "intent": "How to create a great overall café experience for customers.",
                "content": "Enjoyable Experience is the fifth step of C.O.F.F.E.E. Objectives: Customer Satisfaction — ensure customers are satisfied with their interactions, leading to repeat visits, positive word-of-mouth, and strong brand advocacy. Customer Loyalty and Retention — build a loyal customer base that repeatedly chooses the brand, spends more, refers others, and reduces customer churn. Market Differentiation — set the business apart from competitors by offering a superior customer experience. Impact: A great experience makes the customer feel the brand values them, builds comfort and ease, and makes the brand more reliable. For the business, it sets the tone for future visits and helps the brand stay innovatively ahead of competition.",
                "tags": ["enjoyable_experience", "loyalty", "retention", "differentiation", "coffee_framework"],
                "qa_pairs": [
                    {"instruction": "What is the Enjoyable Experience step about?", "output": "It's the first E in C.O.F.F.E.E. — focused on customer satisfaction, loyalty and retention, and market differentiation. A great experience leads to repeat visits, positive word-of-mouth, and strong brand advocacy."},
                    {"instruction": "How does enjoyable experience affect customer loyalty?", "output": "It builds a loyal customer base that repeatedly chooses the brand, spends more, refers others, and reduces churn. It sets the business apart from competitors and helps the brand stay innovatively ahead."}
                ]
            },
            {
                "title": "E — Enthusiastic Exit",
                "intent": "How to end the customer visit on a positive note.",
                "content": "Enthusiastic Exit is the sixth and final step of C.O.F.F.E.E. Objectives: Customer Appreciation — expressing gratitude shows you value and appreciate the customer's business, acknowledging their contribution to your success. Positive Experience — feeling appreciated leaves a positive impression even after the transaction is complete. Mitigate Negative Feedback — if a customer had any issues, thanking them can be a step towards addressing those concerns and potentially turning a negative experience into a positive one. Impact: Thanking leaves a positive impression and makes customers feel like part of the family. It shows the team genuinely cares and makes customers feel acknowledged, respected, valued, and recognized for being regulars. For the business, a great goodbye enhances the overall experience, leaving a lasting positive impression, and customers feel great about coming to TWC and come more often.",
                "tags": ["enthusiastic_exit", "goodbye", "appreciation", "thanking", "coffee_framework"],
                "qa_pairs": [
                    {"instruction": "What is the Enthusiastic Exit in C.O.F.F.E.E.?", "output": "It's the final E — focused on ending the visit positively. Express gratitude, leave a positive impression, and mitigate any negative experiences. Thank customers with eye contact and a warm smile: 'Thank you ma'am/sir, see you soon.'"},
                    {"instruction": "Why is thanking customers at exit important?", "output": "Thanking leaves a positive impression and makes customers feel like part of the family. It shows the team genuinely cares, makes customers feel respected and valued, and encourages them to come back more often."},
                    {"instruction": "What are the six steps of the C.O.F.F.E.E. framework?", "output": "C — Cheerful Welcome, O — Order Taking Assistance, F — Friendly & Accurate Service, F — Feedback With Solutions, E — Enjoyable Experience, E — Enthusiastic Exit."},
                    {"instruction": "What does C.O.F.F.E.E. stand for?", "output": "C.O.F.F.E.E. stands for: Cheerful Welcome, Order Taking Assistance, Friendly & Accurate Service, Feedback With Solutions, Enjoyable Experience, and Enthusiastic Exit. These are the six steps of the customer experience framework at TWC."}
                ]
            }
        ]
    },

    # ── MODULE 3: CX Scenarios & Scripts ──
    {
        "id": "cx_scenarios_scripts",
        "title": "CX Scenarios — What to Say and Do",
        "description": "Detailed customer service scenarios with specific actions, tone, body language, and sample scripts for every stage of the café experience.",
        "chunks": [
            {
                "title": "Cheerful Welcome Scenarios",
                "intent": "How to greet different types of customers entering the café.",
                "content": "Scenario scripts for cheerful welcome. Family with small kid, senior citizens, and a young lady: Greet the kids first then the rest. Bend/kneel to talk to kids, stand and maintain eye contact with rest. Friendly and excited tone. Script: 'Hello (to the kids)! Good morning/evening. Welcome to Third Wave Coffee/Third Rush. Hello everyone!' Group of teenagers: Open the door if nearby. Wave and maintain eye contact. Script: 'Hi! Good morning/evening, welcome to TWC/TR.' Lady with multiple shopping bags: Open the door and offer help with bags. Hold the door and gesture toward bags. Script: 'Hi Ma'am, welcome to TWC/TR. May I carry those bags or help you find a table?' Physically handicapped customer: Open the door and offer assistance. Reach for the door quickly. Script: 'Hello Ma'am/Sir, welcome to TWC/TR. Please allow me to assist you.' Regular customer: Open the door if possible. Wave with a smile. Script: 'Hello Ma'am/Sir, welcome to TWC/TR. Good to see you again!' New customer: Acknowledge and guide inside. Smile, maintain eye contact, gesture toward counter or seating. Script: 'Good morning/evening Ma'am/Sir, welcome to TWC/TR.' Customer with baby and handbag: Open the door and offer help with bags. Reach the door quickly and gesture toward the bags. Script: 'Hi Ma'am/Sir, welcome to TWC/TR. Please allow me to assist you with the bags.' Customer talking on phone: Acknowledge without interrupting. Smile and nod, gesture toward seating. Script: 'Welcome to TWC/TR.' Confused customer looking for something: Approach and offer help. Maintain eye contact and gesture toward counter/menu. Script: 'Hello Ma'am/Sir, welcome to TWC/TR. May I help you?' Customer during busy rush: Acknowledge immediately. Make quick eye contact and smile. Script: 'Hi! Welcome to TWC/TR. We will be right with you.'",
                "tags": ["greeting", "welcome", "scenarios", "scripts", "family", "handicapped", "regular_customer", "busy_rush"],
                "qa_pairs": [
                    {"instruction": "How should I greet a family with kids at the café?", "output": "Greet the kids first, then the rest of the group. Bend or kneel to talk to the kids, then stand and maintain eye contact with others. Use a friendly, excited tone: 'Hello (to the kids)! Good morning/evening. Welcome to Third Wave Coffee/Third Rush. Hello everyone!'"},
                    {"instruction": "How do I greet a physically handicapped customer?", "output": "Open the door and offer assistance. Reach for the door quickly. Use a friendly and empathetic tone: 'Hello Ma'am/Sir, welcome to TWC/TR. Please allow me to assist you.'"},
                    {"instruction": "What should I say to a regular customer entering the café?", "output": "Open the door if possible, wave with a smile, and say: 'Hello Ma'am/Sir, welcome to TWC/TR. Good to see you again!'"},
                    {"instruction": "How should I handle greeting during a busy rush?", "output": "Acknowledge immediately with quick eye contact and a smile. Say: 'Hi! Welcome to TWC/TR. We will be right with you.'"},
                    {"instruction": "What if a customer is on the phone when entering?", "output": "Acknowledge without interrupting. Smile and nod, gesture toward seating. Simply say: 'Welcome to TWC/TR.'"},
                    {"instruction": "How do I greet a customer carrying shopping bags?", "output": "Open the door and offer help with bags. Hold the door and gesture toward the bags. Say: 'Hi Ma'am, welcome to TWC/TR. May I carry those bags or help you find a table?'"}
                ]
            },
            {
                "title": "Order Taking Scenarios",
                "intent": "How to handle different order-taking situations including upselling and payment.",
                "content": "Scenario scripts for order taking. Customer taking too long and holding up queue: Politely move to the next customer while they decide. Calm and patient tone. Script: 'Excuse me ma'am/sir, while you decide, may I take the next customer's order?' Customer asks for beverage recommendation: Ask preferences (coffee/non-coffee, hot/cold) and suggest 2 popular beverages. Friendly and excited tone. Script: 'Absolutely ma'am/sir. Would you like a hot/cold beverage? Coffee/non-coffee? I would recommend the...' Customer orders coffee — suggest dessert pairing: Script: 'Ma'am/Sir, this pairs really well with our Tiramisu. Would you like to try it with your coffee?' Customer orders dessert — suggest beverage pairing: Script: 'Ma'am/Sir, our chocolate brownie pairs really well with a latte. Would you like to add one?' New launch opportunity: Script: 'Ma'am/Sir, would you like to try our newly launched beverage/dessert?' Upsell combos or add-ons: Script: 'Ma'am/Sir, would you like to add a dessert or snack with your beverage today?' Customer asks about payment options: Script: 'Absolutely ma'am/sir, we accept cash, card, UPI, wallet and wave coins.' Customer wants to change item after billing: Script: 'Certainly ma'am/sir. We will cancel this order and refund it. The updated order will be billed separately. Is that okay?' POS system slow or not working: Script: 'Sorry ma'am/sir, our system is running slow. You may place the order through the app or kindly give us 2 min.' Customer needs menu assistance: Script: 'Absolutely ma'am/sir, I can help you with the menu and suggest some options.'",
                "tags": ["order_taking", "upselling", "pairing", "payment", "pos", "scenarios", "scripts"],
                "qa_pairs": [
                    {"instruction": "What should I do when a customer is taking too long to order and others are waiting?", "output": "Politely move to the next customer while they decide. Use a calm, patient tone: 'Excuse me ma'am/sir, while you decide, may I take the next customer's order?'"},
                    {"instruction": "How should I recommend a beverage to a customer?", "output": "Ask their preferences — coffee or non-coffee, hot or cold — then suggest 2 popular options. Say: 'Absolutely ma'am/sir. Would you like a hot/cold beverage? Coffee/non-coffee? I would recommend the...'"},
                    {"instruction": "How do I suggest a dessert pairing with coffee?", "output": "When a customer orders coffee, suggest a complementary dessert: 'Ma'am/Sir, this pairs really well with our Tiramisu. Would you like to try it with your coffee?'"},
                    {"instruction": "What payment options are available at TWC?", "output": "TWC accepts cash, card, UPI, wallet and wave coins. Say: 'Absolutely ma'am/sir, we accept cash, card, UPI, wallet and wave coins.'"},
                    {"instruction": "What do I do if the POS system is slow or not working?", "output": "Offer alternate ordering options. Say: 'Sorry ma'am/sir, our system is running slow. You may place the order through the app or kindly give us 2 min.'"},
                    {"instruction": "What if a customer wants to change their order after billing?", "output": "Inform them calmly that the order must be cancelled and re-billed: 'Certainly ma'am/sir. We will cancel this order and refund it. The updated order will be billed separately. Is that okay?'"}
                ]
            },
            {
                "title": "Friendly & Accurate Service Scenarios",
                "intent": "How to handle service situations at the table including complaints and special requests.",
                "content": "Scenario scripts for friendly and accurate service. Customer asks for extra cutlery or napkins: Provide immediately. Script: 'Absolutely Ma'am/Sir, I will get that for you right away.' Customer finds a foreign object in food (hair, insect, etc.): Apologize, remove the item immediately, and inform supervisor. Script: 'I am extremely sorry about this Ma'am/Sir. Let me replace this for you immediately.' Customer wants takeaway for leftover food: Pack if requested. Script: 'Absolutely Ma'am/Sir, I will get this packed for you.' Customer has unfinished food: Check if everything was okay and offer to pack. Script: 'Hi Ma'am/Sir, I see some of your order is remaining. Would you like me to pack it for you?' Customer did not like the product: Ask for feedback and offer replacement. Script: 'I'm sorry you didn't enjoy it Ma'am/Sir. May I replace it with something else for you?' Order serving is delayed: Check status and inform customer. Script: 'Hi Ma'am/Sir, we are sorry for the delay. Your order will be ready in about 2–3 minutes.' Customer removing ingredients from dish: Check if customization or replacement is needed. Script: 'Hi Ma'am/Sir, I noticed you are removing some ingredients. Is everything okay? I can replace it or modify it for you.' Customer looking around for assistance: Approach and offer help. Script: 'Hi Ma'am/Sir, may I help you with something?' Customer drops spoon/fork: Provide replacement immediately. Script: 'Hi Ma'am/Sir, here is a fresh spoon/fork for you.' Customer enjoyed the beverage/meal — suggest dessert: Acknowledge and suggest pairing. Script: 'I'm glad you enjoyed it Ma'am/Sir. Would you like to try one of our desserts to go with your beverage?'",
                "tags": ["service", "complaint", "foreign_object", "takeaway", "replacement", "delay", "scenarios", "scripts"],
                "qa_pairs": [
                    {"instruction": "What should I do if a customer finds a hair or insect in their food?", "output": "Apologize immediately, remove the item, and inform your supervisor. Say: 'I am extremely sorry about this Ma'am/Sir. Let me replace this for you immediately.'"},
                    {"instruction": "What if the customer's order is delayed?", "output": "Check the status and inform the customer with a time estimate. Say: 'Hi Ma'am/Sir, we are sorry for the delay. Your order will be ready in about 2–3 minutes.'"},
                    {"instruction": "How should I handle a customer who didn't like their product?", "output": "Ask for feedback and offer a replacement. Say: 'I'm sorry you didn't enjoy it Ma'am/Sir. May I replace it with something else for you?'"},
                    {"instruction": "What if a customer has unfinished food and seems done?", "output": "Check if everything was okay and offer to pack leftovers. Say: 'Hi Ma'am/Sir, I see some of your order is remaining. Would you like me to pack it for you?'"},
                    {"instruction": "What should I do if a customer drops their spoon or fork?", "output": "Provide a fresh replacement immediately. Say: 'Hi Ma'am/Sir, here is a fresh spoon/fork for you.'"}
                ]
            },
            {
                "title": "Feedback With Solutions Scenarios",
                "intent": "How to conduct checkbacks, handle positive and negative feedback.",
                "content": "Scenario scripts for feedback. Regular customer checkback: Approach the table briefly after serving. Smile and maintain eye contact. Script: 'Hi Ma'am/Sir, how is your food/beverage today?' Positive feedback: Acknowledge and offer further assistance. Script: 'Great to hear that Ma'am/Sir. Please let me know if there is anything else I can get for you.' Customer enjoyed their beverage — suggest dessert: Script: 'I'm glad you enjoyed the drink Ma'am/Sir. Would you like to try a dessert with it?' Customer finished beverage quickly: Offer another drink or food. Script: 'Would you like another beverage or perhaps something to eat?' Customer did not like the product: Apologize and offer replacement. Script: 'I'm sorry to hear that Ma'am/Sir. May I replace it or get you something else?' Customer requests different item after complaint: Replace or offer alternative. Script: 'Absolutely Ma'am/Sir, I will get that replaced for you right away.' Customer looking around for assistance: Walk to table with a smile. Script: 'Hi Ma'am/Sir, may I help you with something?' Group checkback: Address the table with a smile. Script: 'I hope everyone is enjoying the food and beverages. Please let me know if you need anything else.' Customer calls staff for feedback: Listen and respond. Script: 'Absolutely Ma'am/Sir, how can I help you?' Customer finished meal and seems satisfied — suggest dessert: Script: 'I hope you enjoyed your meal Ma'am/Sir. Would you like to try a dessert before you leave?'",
                "tags": ["feedback", "checkback", "positive_feedback", "negative_feedback", "replacement", "scenarios", "scripts"],
                "qa_pairs": [
                    {"instruction": "When should I do a checkback with the customer?", "output": "Approach the table once the customer has consumed about one-third of their product. Ask: 'Hi Ma'am/Sir, how is your food/beverage today?'"},
                    {"instruction": "How do I handle positive feedback from a customer?", "output": "Acknowledge it warmly and offer further help. Say: 'Great to hear that Ma'am/Sir. Please let me know if there is anything else I can get for you.'"},
                    {"instruction": "How do I handle negative feedback from a customer?", "output": "Listen attentively, apologize sincerely, and offer a replacement. Say: 'I'm sorry to hear that Ma'am/Sir. May I replace it or get you something else?'"},
                    {"instruction": "How should I do a group checkback?", "output": "Address the whole table with a smile and energetic tone: 'I hope everyone is enjoying the food and beverages. Please let me know if you need anything else.'"}
                ]
            },
            {
                "title": "Enjoyable Experience Scenarios",
                "intent": "How to handle environmental requests and café comfort situations.",
                "content": "Scenario scripts for enjoyable experience. Customer asks to adjust AC or temperature: Acknowledge and adjust if possible, or offer alternate seating. Script: 'Let me check that for you Ma'am/Sir. If it still feels uncomfortable, I can help you move to another table.' Customer asks to increase music volume: Inform politely about other customers and offer alternate seating. Script: 'Ma'am/sir since increasing the volume may disturb others, will you be okay to shift to another table?' Customer asks to change music genre: Politely explain policy. Script: 'I'm sorry Ma'am/Sir, the playlist is centrally managed at TWC/TR, so we're unable to change it.' Insects in the store: Apologize and help the customer shift. Script: 'I'm very sorry about that Ma'am/Sir. Let me move you to another table while we fix this.' Dirty or wobbling furniture: Apologize and offer another table. Script: 'I'm sorry about that Ma'am/Sir. Let me move you to another table while we fix this one.' Spillage on the floor: Thank customer and clean immediately. Script: 'Thank you for letting us know Ma'am/Sir. We'll clean it right away.' Restroom cleanliness complaint: Apologize and arrange immediate cleaning. Script: 'I'm very sorry about that Ma'am/Sir. We'll get it cleaned immediately.' Customer needs Wi-Fi help: Guide through connection steps. Script: 'Absolutely Ma'am/Sir, I'll help you connect to the guest Wi-Fi.' Customer brings pet inside: Inform about policy and suggest outdoor seating. Script: 'I'm sorry Ma'am/Sir, pets aren't allowed inside. You're welcome to sit in the outdoor seating area.' Customer asks about coffee equipment or merchandise: Assist and demonstrate if possible. Script: 'Of course Ma'am/Sir, I'll show you how it works.'",
                "tags": ["enjoyable_experience", "ac", "music", "cleanliness", "wifi", "pets", "environment", "scenarios", "scripts"],
                "qa_pairs": [
                    {"instruction": "What should I do if a customer complains about the temperature?", "output": "Acknowledge the request and adjust if possible, or offer alternate seating. Say: 'Let me check that for you Ma'am/Sir. If it still feels uncomfortable, I can help you move to another table.'"},
                    {"instruction": "Can we change the music genre for a customer?", "output": "No, the playlist is centrally managed. Politely explain: 'I'm sorry Ma'am/Sir, the playlist is centrally managed at TWC/TR, so we're unable to change it.'"},
                    {"instruction": "What should I do if a customer reports a spillage?", "output": "Thank them and clean immediately. Say: 'Thank you for letting us know Ma'am/Sir. We'll clean it right away.'"},
                    {"instruction": "Are pets allowed inside TWC?", "output": "No, pets aren't allowed inside. Politely suggest outdoor seating: 'I'm sorry Ma'am/Sir, pets aren't allowed inside. You're welcome to sit in the outdoor seating area.'"},
                    {"instruction": "What if a customer complains about restroom cleanliness?", "output": "Apologize and arrange immediate cleaning. Say: 'I'm very sorry about that Ma'am/Sir. We'll get it cleaned immediately.'"},
                    {"instruction": "What if a customer complains about dirty or wobbly furniture?", "output": "Apologize and offer another table. Say: 'I'm sorry about that Ma'am/Sir. Let me move you to another table while we fix this one.'"}
                ]
            },
            {
                "title": "Enthusiastic Exit Scenarios",
                "intent": "How to handle different exit situations with customers.",
                "content": "Scenario scripts for enthusiastic exit. Customer walking toward exit: Thank if within 2 meters. Smile and nod. Script: 'Thank you Ma'am/Sir. Have a great day.' Customer leaves table after finishing: Acknowledge and thank. Script: 'Thank you Ma'am/Sir. Hope you enjoyed your visit.' Customer makes eye contact while leaving: Verbal thank-you with slight wave. Script: 'Thank you Ma'am/Sir. See you again.' Customer leaving after takeaway order: Thank and wish well. Script: 'Thank you Ma'am/Sir. Enjoy your order.' Regular customer leaving: Warm thank-you with wave and smile. Script: 'Thank you Ma'am/Sir. See you again soon.' Customer compliments the experience: Acknowledge and thank them. Script: 'Thank you Ma'am/Sir. We're glad you enjoyed it.' Customer finishes dessert and prepares to leave: Thank and invite back. Script: 'Thank you Ma'am/Sir. Hope to see you again soon.' Customer waves goodbye from a distance: Wave back. Script: 'Thank you Ma'am/Sir. Have a great day.'",
                "tags": ["exit", "goodbye", "thanking", "farewell", "scenarios", "scripts"],
                "qa_pairs": [
                    {"instruction": "What should I say when a customer is leaving?", "output": "If within 2 meters, smile, nod, and say: 'Thank you Ma'am/Sir. Have a great day.' For regulars, add warmth: 'Thank you Ma'am/Sir. See you again soon.'"},
                    {"instruction": "What if a customer compliments the experience while leaving?", "output": "Acknowledge and thank them warmly: 'Thank you Ma'am/Sir. We're glad you enjoyed it.'"},
                    {"instruction": "How should I handle exit for a takeaway customer?", "output": "Thank them and wish them well: 'Thank you Ma'am/Sir. Enjoy your order.'"},
                    {"instruction": "What if a customer waves goodbye from far away?", "output": "Wave back with a smile and say: 'Thank you Ma'am/Sir. Have a great day.'"}
                ]
            }
        ]
    },

    # ── MODULE 4: Complaints, Etiquette & Standards ──
    {
        "id": "cx_standards_etiquette",
        "title": "CX Standards, Complaints & Etiquette",
        "description": "Complaint levels and empowerment, absolute NOs, pro tips, and etiquette guidelines for social media, telephone, and café interactions.",
        "chunks": [
            {
                "title": "Complaint Levels & Empowerment",
                "intent": "Define the three levels of complaints and who is empowered to handle them.",
                "content": "Complaints are classified into three levels. Level 1 — Taste & Personal Preference: Examples include dessert too sweet or bitter, coffee too strong or weak, cheesecake could be colder, brownie texture feels too dense, presentation could look better. Empowered roles: Basic Barista, Advanced Barista, Buddy Trainer, Shift Manager, Assistant Store Manager, Store Manager. Expected response: Listen politely, acknowledge feedback, and adjust if possible (less sugar, remake with preference, offer alternatives). Level 2 — Product or Service Issue: Examples include wrong dessert or drink served, item missing from order, stale pastry or melted ice cream, long wait time without communication, poor dessert plating or messy presentation. Empowered roles: Advanced Barista, Buddy Trainer, Shift Manager, Assistant Store Manager, Store Manager. Expected response: Apologize, correct the mistake immediately, remake or replace the item, inform the shift lead if needed. Partial refund can be processed by Shift Manager and above. Level 3 — Safety & Compliance Concern: Examples include allergen contamination (nuts, dairy, gluten), foreign object in dessert or drink, spoiled or expired food served, customer reports illness after consuming food, harassment or unsafe behaviour in the café. Empowered roles: Assistant Store Manager, Store Manager, Operations Manager. Expected response: Escalate immediately to Store Manager or Operations Manager. Follow incident reporting procedures.",
                "tags": ["complaints", "empowerment", "levels", "escalation", "refund", "safety", "allergen"],
                "qa_pairs": [
                    {"instruction": "What are the levels of customer complaints at TWC?", "output": "There are three levels. Level 1: Taste & Personal Preference (e.g., coffee too strong, dessert too sweet). Level 2: Product or Service Issue (e.g., wrong item served, long wait). Level 3: Safety & Compliance Concern (e.g., allergen contamination, foreign objects, illness)."},
                    {"instruction": "Who can handle a Level 1 complaint?", "output": "Level 1 (Taste & Personal Preference) can be handled by any role: Basic Barista, Advanced Barista, Buddy Trainer, Shift Manager, Assistant Store Manager, or Store Manager. Listen politely, acknowledge feedback, and adjust if possible."},
                    {"instruction": "Who can process a partial refund for a customer?", "output": "Partial refunds can only be processed by Shift Manager and above. This applies to Level 2 complaints (product or service issues)."},
                    {"instruction": "What constitutes a Level 3 complaint?", "output": "Level 3 — Safety & Compliance Concerns include: allergen contamination (nuts, dairy, gluten), foreign objects in food/drink, spoiled or expired food, customer illness after consuming food, or harassment/unsafe behaviour. Escalate immediately to Store Manager or Operations Manager."},
                    {"instruction": "What should I do if a customer reports an allergen contamination?", "output": "This is a Level 3 Safety & Compliance Concern. Escalate immediately to the Store Manager or Operations Manager. Follow incident reporting procedures. Do not try to handle this independently."},
                    {"instruction": "How should I handle a wrong item served to a customer?", "output": "This is a Level 2 complaint. Apologize, correct the mistake immediately, remake or replace the item, and inform the shift lead if needed. A partial refund can be processed by Shift Manager and above."}
                ]
            },
            {
                "title": "Absolute NOs — Things to Never Do",
                "intent": "List the absolute behaviors that must never happen in customer interactions.",
                "content": "Absolute NOs at TWC/TR: Never delay or miss a greeting due to distractions like phones or internal conversations. Never invade a customer's personal space or touch children without permission. There's no place for rude behavior, impatience, or negative body language in customer interactions. Never discriminate against customers based on caste, creed, gender, religion, age, appearance, or ability. Avoid loud internal conversations or discussing operational matters where customers can hear them. Never ignore customers during ordering or service interactions. Don't argue with customers or prioritize internal tasks over customer service. Avoid approaching customers for feedback while they are on calls, engaged in conversation, or visibly upset. Never pressure customers to give feedback, post reviews, or bring more people. Don't overlook cleanliness, hygiene, or maintenance issues anywhere in the café. If an issue can be resolved during the dine-in experience without escalation, don't provide the customer care contact details instead.",
                "tags": ["absolute_nos", "prohibited", "rules", "behavior", "discrimination", "hygiene"],
                "qa_pairs": [
                    {"instruction": "What are the absolute NOs at TWC?", "output": "Never miss greetings due to distractions. Never invade personal space or touch children without permission. No rude behavior or negative body language. Never discriminate. Avoid loud operational discussions near customers. Don't ignore customers during service. Don't argue with customers. Don't pressure customers for reviews. Don't overlook cleanliness issues."},
                    {"instruction": "Can I approach a customer for feedback while they're on a call?", "output": "No. Avoid approaching customers for feedback while they are on calls, engaged in conversation, or visibly upset. Wait until they are comfortable."},
                    {"instruction": "Should I give the customer care number if I can resolve the issue?", "output": "No. If an issue can be resolved during the dine-in experience without escalation, resolve it yourself. Don't provide customer care contact details instead of solving the problem."},
                    {"instruction": "Can I pressure a customer to post a review?", "output": "No. Never pressure customers to give feedback, post reviews, or bring more people. This is an Absolute NO at TWC/TR."}
                ]
            },
            {
                "title": "Coffee Pro Tips",
                "intent": "Key pro tips for delivering excellent C.O.F.F.E.E. experience.",
                "content": "Pro Tips for CX at TWC/TR: Ensure your tone matches your words. A 'Welcome to Third Wave/Third Rush' with a cheerful tone lets the customer know you are happy to have them. Saying it in a dull manner with no enthusiasm makes the customer feel unwelcome and uneasy. A warm smile, eye contact, and a friendly greeting within a respectful 2-meter distance set the tone for the entire customer experience. Speak clearly, maintain positive body language, and keep your tone warm and professional in every interaction. Anticipate customer needs early. A small gesture like guiding to a seat or opening the door creates a welcoming start. Help customers make confident choices by guiding them through the menu and confirming their order and customizations before serving. A well-groomed and hygienic appearance reinforces trust and professionalism from the very first interaction. Master salver management: never over-stack the salver, hold it while serving instead of placing it on the table, and when empty, carry it neatly under the arm. Present orders with confidence. Announce the items clearly and serve with a genuine smile to enhance the experience. Choose the right moment for feedback. Approach customers once they are comfortable and have experienced the product. Let confident body language (standing upright, walking with a calm steady pace, avoiding hunched shoulders) reflect your knowledge and reassure customers they are in capable hands. End every visit on a high note. Make eye contact, smile, and thank customers enthusiastically as they leave.",
                "tags": ["pro_tips", "tone", "body_language", "salver", "greeting", "professionalism"],
                "qa_pairs": [
                    {"instruction": "What are the CX pro tips for baristas?", "output": "Key pro tips: Match your tone to your words. Smile, make eye contact, and greet within 2 meters. Speak clearly with positive body language. Anticipate needs early. Guide through menu. Maintain a groomed, hygienic appearance. Master salver management. Present orders with confidence. Choose the right moment for feedback. Let confident body language reflect your knowledge. End every visit with a thank you."},
                    {"instruction": "What is proper salver management?", "output": "Never over-stack the salver. Hold it while serving instead of placing it on the table. When empty, carry it neatly under the arm."},
                    {"instruction": "When is the right time to approach a customer for feedback?", "output": "Approach once they are comfortable and have experienced the product — typically after they've consumed about one-third of it. Don't approach while they're on calls, in conversation, or visibly upset."}
                ]
            },
            {
                "title": "Social Media Etiquette",
                "intent": "What can and cannot be captured and posted on social media representing the café.",
                "content": "Social media etiquette for TWC café content. Hygiene: CAN capture — wearing gloves while making/garnishing beverages, handling food, touching ready-to-serve items, clean counters. MUST NOT capture — bare-hand contact, unclean counter/equipment, phone near food areas, spills, mess, or eating while preparing orders. Setup and Presentation: CAN capture — full uniform and neat appearance, organized stations. MUST NOT capture — incomplete uniform or untidy look, casual clothes inside café, cluttered setup or dull/empty café. Content: CAN capture — coffee making, latte art, café ambience, menu items, team moments (professional behavior only), happy customer moments (with permission). MUST NOT capture — inside kitchen/storage, billing screens, cash handling or customer data, staff conflicts, operational issues, empty café shown negatively. Product: CAN capture — products looking fresh and neat, correct cup sizes, logo visible. MUST NOT capture — unfinished drinks or rejected orders, incorrectly named products, messy tables. Communication: Use correct brand name 'Third Wave Coffee/Third Rush', correct product names, clear speech. MUST NOT — wrong pronunciation, wrong product names, misleading info or unverified offers. Audio: CAN use — soft music, clean original audio. MUST NOT — loud or offensive audio, songs in languages other than English. Brand: CAN post — clean, premium, customer-ready content. MUST NOT — anything that harms trust or image. 5·second check before posting: 1. Am I in proper uniform? 2. Am I wearing gloves while preparing orders? 3. Is the café clean? 4. Does the product look perfect? If not, fix first. 5. Does this make the brand look good?",
                "tags": ["social_media", "etiquette", "content_guidelines", "hygiene", "brand", "posting"],
                "qa_pairs": [
                    {"instruction": "What social media rules should café staff follow?", "output": "Only post clean, professional, brand-positive content. Show proper uniform, gloves while preparing, clean counters, and fresh products. Never post bare-hand food contact, messy tables, kitchen/storage areas, billing screens, customer data, or staff conflicts. Use correct brand names and product names. Do a 5-second check before posting."},
                    {"instruction": "Can I post a video of latte art on social media?", "output": "Yes, coffee making and latte art can be captured for social media, as long as hygiene standards are visible (wearing gloves), the setup is clean, and correct brand names are used."},
                    {"instruction": "What is the 5-second check before posting café content?", "output": "Before posting, check: 1. Am I in proper uniform? 2. Am I wearing gloves while preparing orders? 3. Is the café clean? 4. Does the product look perfect? If not, fix first. 5. Does this make the brand look good?"},
                    {"instruction": "Can I post customer photos on social media?", "output": "Happy customer moments can be captured only WITH permission. Never post customer data, billing screens, or anything that compromises customer privacy."}
                ]
            },
            {
                "title": "Telephone Etiquette",
                "intent": "How to handle phone calls professionally representing the café.",
                "content": "Telephone etiquette at TWC/TR. Best Practices: Start with 'Hi, thank you for calling Third Wave/Third Rush.' Introduce yourself and ask how you can help. Maintain a calm, kind, and polite tone. Inform clearly if an item is out of stock and offer an equal or better alternative including pricing. Prioritize in-store customers appropriately — if on call, ensure another team member assists the in-store customer. Stay fully present during the call. Return all missed calls. End the call politely. Keep communication clear and realistic. Avoid: Don't skip the greeting or sound abrupt. Don't jump into conversation without context. Don't sound rude, impatient, or distracted. Don't just say 'not available' without offering alternatives. Don't leave a customer hanging while on call. Don't multitask (POS, order prep, etc.) while on call. Don't ignore missed calls. Don't hang up mid-conversation. Don't make commitments or promises over the phone. Role-based phone handling: Basic Barista — handle queries (menu, recommendations, availability). Advanced Barista / Buddy Trainer — handle order issues (wrong/missing items, delays, taste concerns), but don't commit to refunds/replacements without approval. Shift Manager & above — handle escalations (unhappy customers, repeated issues, resolution requests), don't delay escalation in sensitive situations. ASM / Store Manager — handle serious concerns (refund demands, safety, health, hygiene issues), don't delegate high-risk situations downward.",
                "tags": ["telephone", "phone", "etiquette", "calls", "missed_calls", "escalation"],
                "qa_pairs": [
                    {"instruction": "How should I answer the phone at the café?", "output": "Start with: 'Hi, thank you for calling Third Wave/Third Rush.' Introduce yourself and ask how you can help. Maintain a calm, kind, and polite tone throughout."},
                    {"instruction": "What should I do if a customer calls and an item is out of stock?", "output": "Inform clearly that the item is out of stock and offer an equal or better alternative, including pricing. Never just say 'not available' without offering alternatives."},
                    {"instruction": "Should I return missed calls at the café?", "output": "Yes, return all missed calls. Every call is part of the customer experience and ignoring missed calls is not acceptable."},
                    {"instruction": "Who can handle phone complaints about refunds?", "output": "ASM or Store Manager handles serious concerns including refund demands. Shift Managers handle escalations. Advanced Baristas and Buddy Trainers can handle order issues but must not commit to refunds/replacements without approval."},
                    {"instruction": "Can I multitask while on a customer call?", "output": "No. Stay fully present during the call. Don't multitask with POS, order prep, etc. while on the call."}
                ]
            },
            {
                "title": "TWC App & Loyalty Program",
                "intent": "Explain what the TWC app offers and the loyalty program structure.",
                "content": "The TWC App allows customers to: Order for Dine-In (order while at the café), Order for Takeaway (skip the queue), Pay for orders using the app wallet or other payment options, Track loyalty progress and rewards, Pre-buy Packs to get discounted items and redeem them before expiry. Brew Journey loyalty program: After 5th order of Rs 300+, customer makes 1st order (minimum order value) and gets 3 Free Classic Coffee cups with 15-day validity plus a 10% OFF coupon. After 2nd order of Rs 300+, customer gets 20% OFF coupon with 15-day validity. Orders 2–5 must be Rs 300+ each, with 5 qualifying orders within 45 days to complete the brew journey. Unclaimed rewards expire after 45 days. Loyalty tiers: Partner (default tier, Rs 100 OFF as signing up bonus + 1 Free Coffee Cup), Influencer (6 successful orders, 10% Wave Coins, online-only payable, +2 Free Coffee Cups), Ambassador (12 successful orders, 15% Wave Coins, online-only payable). Cycle is 90 days — maintain 6 orders (Influencer) or 12 orders (Ambassador) to avoid downgrade. Only one discount (cup, coin, pack, etc.) can be used per order.",
                "tags": ["app", "loyalty", "brew_journey", "wave_coins", "partner", "influencer", "ambassador", "rewards"],
                "qa_pairs": [
                    {"instruction": "What can customers do on the TWC app?", "output": "Customers can order for dine-in, order for takeaway (skip the queue), pay using the app wallet or other options, track loyalty progress and rewards, and pre-buy packs for discounted items."},
                    {"instruction": "How does the Brew Journey loyalty program work?", "output": "After the 5th order of Rs 300+, customers get 3 Free Classic Coffee cups (15-day validity) and a 10% OFF coupon. After the 2nd order (Rs 300+), they get 20% OFF (15-day validity). Five qualifying orders of Rs 300+ within 45 days complete the journey. Unclaimed rewards expire after 45 days."},
                    {"instruction": "What are the loyalty tiers on the TWC app?", "output": "Three tiers: Partner (default — Rs 100 OFF + 1 Free Coffee), Influencer (6 orders — 10% Wave Coins + 2 Free Coffees), Ambassador (12 orders — 15% Wave Coins). Maintain order counts within 90-day cycles to keep your tier."},
                    {"instruction": "Can a customer use multiple discounts on one order?", "output": "No, only one discount (cup, coin, pack, etc.) can be used per order."},
                    {"instruction": "What are Wave Coins?", "output": "Wave Coins are loyalty rewards in the TWC app. Influencer tier members earn 10% Wave Coins and Ambassador tier members earn 15% Wave Coins. They can be used for payment (online only)."}
                ]
            },
            {
                "title": "Journey from Good to Amazing",
                "intent": "Explain the three levels of service quality: Consistency, Going Above & Beyond, and Beyond.",
                "content": "The CX Playbook defines the journey from good to amazing in three levels. Consistency: Same taste, same quality, every time. SOP adherence. Cleanliness and ambiance maintained daily. Reliable service standards. Consistency builds trust. Going Above & Beyond: Surprise with a thoughtful effort. Suggest pairing (coffee + dessert). Offer proactive help. Personalize recommendations. Eye contact, authentic smile. Beyond: Anticipate customer needs. Going beyond builds delight. The emotional differentiator. Impact on Customers: They can expect a premium standard of service. They develop trust and prioritize their needs. They notice us going above and beyond to help. Outcomes: Improvement in CPI (Customer Pulse Index), decrease in complaints, improved brand association. Impact on Teams: Upholding TWC standards through quality of coffee, beverage, food, desserts, and service. Motivation from making customers happy. Clear direction for customer experience. Outcomes: Employee pride, skilled people, internal growth.",
                "tags": ["consistency", "above_and_beyond", "cpi", "customer_pulse_index", "service_quality", "trust"],
                "qa_pairs": [
                    {"instruction": "What is the journey from good to amazing at TWC?", "output": "Three levels: 1. Consistency — same taste, quality, SOP adherence, reliable standards. 2. Going Above & Beyond — surprise with thoughtful effort, suggest pairings, proactive help, personalized recommendations. 3. Beyond — anticipate customer needs, the emotional differentiator."},
                    {"instruction": "What is the Customer Pulse Index (CPI)?", "output": "The CPI measures customer satisfaction. Out of every 1,000 customers served, it tracks how many were unhappy or had complaints. A smaller CPI number means better service. Improving CPI is an outcome of consistent, above-and-beyond customer experience."},
                    {"instruction": "What does consistency mean in CX at TWC?", "output": "Consistency means same taste, same quality, every time. It includes SOP adherence, maintaining cleanliness and ambiance daily, and reliable service standards. Consistency builds customer trust."},
                    {"instruction": "How does great CX impact the business?", "output": "Great CX leads to: improvement in CPI (Customer Pulse Index), decrease in complaints, improved brand association, employee pride, skilled workforce, and internal growth."}
                ]
            },
            {
                "title": "The Third Way — Place, People, Product, Process",
                "intent": "TWC's four pillars that define the brand identity.",
                "content": "The Third Way defines how TWC and Third Rush operate, built on four pillars. Place: We offer a clean, well-lit, and thoughtfully arranged space with comfortable seating and well-maintained elements that create a cozy, welcoming atmosphere. People: Our team is highly trained and understands customer experience deeply — not just as a process, but as something we genuinely believe in. Product: We serve specialty coffee crafted with care and precision, along with coffee beans and merchandise for customers to enjoy. We go the extra mile. Process: We say 'absolutely' wherever possible to show customers we are intentional in our care.",
                "tags": ["third_way", "place", "people", "product", "process", "brand_identity"],
                "qa_pairs": [
                    {"instruction": "What is The Third Way?", "output": "The Third Way defines how TWC and Third Rush operate, built on four pillars: Place (clean, cozy, welcoming space), People (highly trained team that genuinely believes in CX), Product (specialty coffee crafted with care and precision), and Process (saying 'absolutely' and being intentional in care)."},
                    {"instruction": "What are the four pillars of TWC's brand identity?", "output": "Place — welcoming, well-maintained space. People — trained team that understands CX deeply. Product — specialty coffee crafted with care. Process — intentional care, saying 'absolutely' wherever possible."}
                ]
            },
            {
                "title": "Coffee Tastings & Product Samplings",
                "intent": "Explain the value and impact of coffee tastings and product samplings in the café.",
                "content": "Coffee tastings and product samplings enhance the customer experience while strengthening trust, engagement, and sales. Showcases Barista Knowledge & Craft: Coffee tastings allow baristas to share their expertise by highlighting flavour notes, origins, and brewing methods. Highlights barista skill and knowledge. Helps customers better appreciate coffee. Shows customers that they are in good hands with experts. Builds Customer Trust: Offering tastings shows confidence in product quality and transparency in the customer experience. Reinforces trust in the brand. Makes customers feel valued. Builds confidence in product quality. Creates a memorable experience and builds connection. Makes customers feel appreciated. Boosts Sales: Allowing customers to try a product reduces hesitation and encourages them to order something new. Encourages customers to try unfamiliar or new items. Increases likelihood of purchase. Promotes repeat orders for products they enjoy. Builds long-term customer loyalty. Sets the base for suggestive and upselling. For more details, see Wisdom Wednesday — Back to Basics: Driving Coffee Culture.",
                "tags": ["coffee_tasting", "sampling", "product_sampling", "barista_knowledge", "trust", "upselling"],
                "qa_pairs": [
                    {"instruction": "Why are coffee tastings important at TWC?", "output": "Coffee tastings showcase barista knowledge and craft, build customer trust by showing confidence in product quality, and boost sales by reducing hesitation about new items. They create memorable experiences and build long-term customer loyalty."},
                    {"instruction": "How do product samplings help with sales?", "output": "Samplings allow customers to try products, reducing hesitation about ordering something new. This encourages trying unfamiliar items, increases purchase likelihood, promotes repeat orders, and sets the base for suggestive selling and upselling."},
                    {"instruction": "What does a barista showcase during a coffee tasting?", "output": "Baristas share expertise by highlighting flavour notes, origins, and brewing methods. This helps customers better appreciate coffee  and shows them they're in good hands with experts."}
                ]
            }
        ]
    }
]


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {m["id"] for m in data["modules"]}
    added = 0
    for mod in new_modules:
        if mod["id"] in existing_ids:
            print(f"  SKIP (already exists): {mod['id']}")
            continue
        data["modules"].append(mod)
        qa_count = sum(len(c.get("qa_pairs", [])) for c in mod["chunks"])
        print(f"  ADDED: {mod['id']} — {len(mod['chunks'])} chunks, {qa_count} QA pairs")
        added += 1

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total_modules = len(data["modules"])
    total_chunks = sum(len(m["chunks"]) for m in data["modules"])
    total_qa = sum(len(c.get("qa_pairs", [])) for m in data["modules"] for c in m["chunks"])
    print(f"\nDone. {added} modules added.")
    print(f"Total: {total_modules} modules, {total_chunks} chunks, {total_qa} QA pairs")


if __name__ == "__main__":
    main()

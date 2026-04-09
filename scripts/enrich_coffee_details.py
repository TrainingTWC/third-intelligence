"""
Enrich C.O.F.F.E.E. chunks with detailed impact chains, mottos, and additional QAs from images.
"""
import json, pathlib

DATA = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"

# Updated/enriched chunk content from images - includes impact chains and mottos
coffee_enrichments = {
    "C — Cheerful Welcome": {
        "content": (
            "Cheerful Welcome is the first step of C.O.F.F.E.E. "
            "Objectives: (1) Create a Positive First Impression & Enhance Overall Customer Experience — When you enter someone's home and they welcome you warmly, you feel comfortable right away. But without that warmth, it feels awkward and uninviting. Our café should always feel like that warm welcome. "
            "(2) Make Customers Feel Valued and Appreciated — Welcoming customers shows that you acknowledge their presence and appreciate their business. This helps them feel valued and respected. "
            "(3) Build Rapport — A friendly welcome helps in building a connection with the customer. "
            "Impact Chain: Great Welcome → Great Customer Experience → A bond builds between the customer and the team → High repeat frequency → Enhanced brand image. "
            "Why is this important? For NEW CUSTOMERS: A warm and polite welcome makes them feel at ease in a new place and situation. Creates a positive first impression. A warm welcome will make them feel valued and that they made a good choice by choosing our brand. "
            "For EXISTING CUSTOMERS: It makes them feel acknowledged and respected. It makes them feel recognised and valued for being a regular loyal customer. "
            "For BUSINESS: Sets a standard for excellent customer service. Helps in building a rapport with the customer. A good welcome sets the tone for the customer's entire stay. "
            "Key Motto: Always Smile and say, 'Hi welcome to Third Wave / Third Rush!'"
        ),
        "new_qa_pairs": [
            {
                "instruction": "What is the impact chain of Cheerful Welcome?",
                "output": "Great Welcome → Great Customer Experience → A bond builds between the customer and the team → High repeat frequency → Enhanced brand image."
            },
            {
                "instruction": "What is the motto for Cheerful Welcome?",
                "output": "Always Smile and say, 'Hi welcome to Third Wave / Third Rush!'"
            },
            {
                "instruction": "What are the three objectives of Cheerful Welcome?",
                "output": "1) Create a Positive First Impression & Enhance Overall Customer Experience, 2) Make Customers Feel Valued and Appreciated, 3) Build Rapport with the customer."
            }
        ]
    },
    "O — Order Taking Assistance": {
        "content": (
            "Order Taking Assistance is the second step of C.O.F.F.E.E. "
            "Objectives: (1) Accuracy & Payment Clarity — Record orders correctly to ensure the team prepares the right items and customers are charged accurately, reducing errors and disputes. "
            "(2) Speed & Efficiency — Take orders quickly and clearly to reduce queue time and help the team prepare beverages and food promptly. "
            "(3) Customization & Smart Selling — Accommodate special requests or dietary needs while suggesting complementary items (e.g., desserts with coffee) to enhance the guest experience and increase sales. "
            "Impact Chain: Well assisted order taking → Informed customer choice → Accurate and speedy service → Customer gets variety and value for money → Great Customer Experience. "
            "Why is this important? For NEW CUSTOMERS: It makes customer feel at ease, recognised and valued for being a regular loyal customer. Customers feel happy to get discounts and offers with choice of billing options. "
            "For EXISTING CUSTOMERS: The customer feels recognised and valued. Customer is happy to get best deals and value for money with suggestions. Customer feels comfortable knowing staff knows their regular order and won't be bothered. "
            "For BUSINESS: Demonstrates professionalism, attention to detail, and a commitment to customer satisfaction. Reduces errors and in-turn, CPI improves. "
            "Key Motto: Active listening is the key to an amazing Ordering taking assistance!"
        ),
        "new_qa_pairs": [
            {
                "instruction": "What is the impact chain of Order Taking Assistance?",
                "output": "Well assisted order taking → Informed customer choice → Accurate and speedy service → Customer gets variety and value for money → Great Customer Experience."
            },
            {
                "instruction": "What is the motto for Order Taking Assistance?",
                "output": "Active listening is the key to an amazing Order taking assistance!"
            },
            {
                "instruction": "What are the three objectives of Order Taking Assistance?",
                "output": "1) Accuracy & Payment Clarity — record orders correctly, 2) Speed & Efficiency — reduce queue time, 3) Customization & Smart Selling — accommodate special requests and suggest complementary items."
            },
            {
                "instruction": "What is CPI in the context of order taking?",
                "output": "CPI (Customer Preference Index) improves when errors are reduced through accurate order taking. Demonstrating professionalism and attention to detail during order taking contributes to better CPI."
            }
        ]
    },
    "F — Friendly & Accurate Service": {
        "content": (
            "Friendly & Accurate Service is the third step of C.O.F.F.E.E. "
            "Objectives: (1) Accurate Orders & Customization — The customer is satisfied when the right order is served with accurate customizations of their order. "
            "(2) Timely Service — Efficient and timely service is essential. Customers should not have to wait excessively long for their orders, and the service staff should be attentive to their needs. "
            "(3) Consistency — Strive for consistency in service across different shifts and days. Customers should have a similar experience regardless of when they visit. "
            "Impact Chain: Friendly & Accurate Service → Customer is happy with no complaints → Customer builds a bond with the team and TWC → Customer positively promotes TWC to others → Customer loves coming back to TWC. "
            "Why is this important? For NEW CUSTOMERS: The customer trusts that their expectations will be met as no order will be missed or inaccurate. The customer's mind builds a positive image of the team and TWC. "
            "For EXISTING CUSTOMERS: Customers feel comfortable, valued, and develop a sense of belonging. Strong customer service differentiates us from other brands and increases customer satisfaction. "
            "For BUSINESS: Excellent customer service differentiates us from competitors and influences customer choice. Exceptional service drives higher spending, builds brand loyalty, and encourages positive word-of-mouth. "
            "Key Motto: Deliver the right order, with the right care, at the right time!"
        ),
        "new_qa_pairs": [
            {
                "instruction": "What is the impact chain of Friendly & Accurate Service?",
                "output": "Friendly & Accurate Service → Customer is happy with no complaints → Customer builds a bond with the team and TWC → Customer positively promotes TWC to others → Customer loves coming back to TWC."
            },
            {
                "instruction": "What is the motto for Friendly & Accurate Service?",
                "output": "Deliver the right order, with the right care, at the right time!"
            },
            {
                "instruction": "What are the three objectives of Friendly & Accurate Service?",
                "output": "1) Accurate Orders & Customization — serve the right order with correct customizations, 2) Timely Service — don't make customers wait excessively long, 3) Consistency — deliver similar experience across all shifts and days."
            }
        ]
    },
    "F — Feedback With Solutions": {
        "content": (
            "Feedback With Solutions is the fourth step of C.O.F.F.E.E. "
            "Objectives: (1) Improve Communication & Engagement — Customer feedback creates a platform for open communication between the TWC team and customers, allowing them to share their experiences and opinions. "
            "(2) Improve Customer Satisfaction — Understanding customer opinions and concerns helps us address issues promptly and enhance the overall customer experience. "
            "(3) Improvement & Prevention of Issues — Customer feedback helps identify areas for improvement and addressing concerns early prevents negative feedback from spreading online or in the public domain. "
            "Impact Chain: Check back with Customers → Customers feel heard and valued → Opportunity to understand customers' needs → Opportunity to improve → Customer loves coming back to TWC. "
            "Why is this important? For NEW CUSTOMERS: Opportunity to clear product-related doubts and assist customers with additional needs like straws or tissues. Chance to engage with customers and build a lasting connection. "
            "For EXISTING CUSTOMERS: Customers can share their views about the product and feel heard. Being listened to makes customers feel valued and satisfied. "
            "For BUSINESS: Helps understanding customer expectations and satisfaction with our products. Identifies areas that can be improved to enhance the customer experience. "
            "Key Motto: Listen to feedback and respond with solutions!"
        ),
        "new_qa_pairs": [
            {
                "instruction": "What is the impact chain of Feedback With Solutions?",
                "output": "Check back with Customers → Customers feel heard and valued → Opportunity to understand customers' needs → Opportunity to improve → Customer loves coming back to TWC."
            },
            {
                "instruction": "What is the motto for Feedback With Solutions?",
                "output": "Listen to feedback and respond with solutions!"
            },
            {
                "instruction": "What are the three objectives of Feedback With Solutions?",
                "output": "1) Improve Communication & Engagement — create open communication platform, 2) Improve Customer Satisfaction — address issues promptly, 3) Improvement & Prevention of Issues — identify improvement areas and prevent negative feedback from spreading."
            }
        ]
    },
    "E — Enjoyable Experience": {
        "content": (
            "Enjoyable Experience is the fifth step of C.O.F.F.E.E. "
            "Objectives: (1) Customer Satisfaction — Ensuring customers are satisfied with their interactions with the brand, leading to repeat visits, positive word-of-mouth, and strong brand advocacy. "
            "(2) Customer Loyalty and Retention — Building a loyal customer base that repeatedly chooses the brand, spends more, refers others, and reduces customer churn. "
            "(3) Market Differentiation — Setting your business apart from competitors by offering a superior customer experience can be a powerful competitive advantage. "
            "Impact Chain: Great Customer Experience → Customer Satisfaction → New Customers & high repeat frequency → Enhancing brand image through word of mouth. "
            "Why is this important? For NEW CUSTOMERS: A great experience will make the customer feel the brand values them. Sets/meets their expectation standards. "
            "For EXISTING CUSTOMERS: It makes the customer feel at comfort and ease. Makes the brand more reliable. "
            "For BUSINESS: A good customer experience sets the tone for the customer's future visits. Compels the brand to ensure all the aspects of the business is set right to give great experience consistently. Aids the brand to be innovatively ahead of competition. "
            "Key Motto: Create a space customers would enjoy and want to revisit!"
        ),
        "new_qa_pairs": [
            {
                "instruction": "What is the impact chain of Enjoyable Experience?",
                "output": "Great Customer Experience → Customer Satisfaction → New Customers & high repeat frequency → Enhancing brand image through word of mouth."
            },
            {
                "instruction": "What is the motto for Enjoyable Experience?",
                "output": "Create a space customers would enjoy and want to revisit!"
            },
            {
                "instruction": "What are the three objectives of Enjoyable Experience?",
                "output": "1) Customer Satisfaction — ensure customers are satisfied leading to repeat visits and advocacy, 2) Customer Loyalty and Retention — build a loyal base that spends more and refers others, 3) Market Differentiation — set apart from competitors with superior experience."
            }
        ]
    },
    "E — Enthusiastic Exit": {
        "content": (
            "Enthusiastic Exit is the sixth and final step of C.O.F.F.E.E. "
            "Objectives: (1) Customer Appreciation — Expressing gratitude shows that you value and appreciate the customer's business. It acknowledges their contribution to your success. "
            "(2) Positive Experience — It enhances the overall customer experience. Feeling appreciated can leave a positive impression, even after the transaction is complete. "
            "(3) Mitigate Negative Feedback — If a customer had any issues or concerns, thanking them can be a step towards addressing those concerns and potentially turning a negative experience into a positive one. "
            "Impact Chain: Genuine Thanking → Seals the experience at TWC → Builds bond between customer and TWC → Gives the customer a sense of belonging → Customer prefers TWC over competition and visits frequently. "
            "Why is this important? For NEW CUSTOMERS: Thanking will leave a positive impression and make them feel like a part of the family. Shows that our team genuinely cares. "
            "For EXISTING CUSTOMERS: Makes them feel acknowledged and respected. Makes them feel recognized and valued for being a regular customer. "
            "For BUSINESS: It enhances the overall customer experience, leaving a lasting positive impression. Customers feel great about coming to TWC and come more often. "
            "Key Motto: A great goodbye ensures another welcome!"
        ),
        "new_qa_pairs": [
            {
                "instruction": "What is the impact chain of Enthusiastic Exit?",
                "output": "Genuine Thanking → Seals the experience at TWC → Builds bond between customer and TWC → Gives the customer a sense of belonging → Customer prefers TWC over competition and visits frequently."
            },
            {
                "instruction": "What is the motto for Enthusiastic Exit?",
                "output": "A great goodbye ensures another welcome!"
            },
            {
                "instruction": "What are the three objectives of Enthusiastic Exit?",
                "output": "1) Customer Appreciation — express gratitude and acknowledge their contribution, 2) Positive Experience — leave a positive impression even after transaction is complete, 3) Mitigate Negative Feedback — turn any negative experience into a positive one."
            }
        ]
    }
}


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))

    updated_chunks = 0
    added_qas = 0

    for mod in data["modules"]:
        if mod["id"] == "cx_coffee_framework":
            for chunk in mod["chunks"]:
                if chunk["title"] in coffee_enrichments:
                    enrichment = coffee_enrichments[chunk["title"]]
                    # Update content
                    chunk["content"] = enrichment["content"]
                    # Add new QA pairs
                    existing_instructions = {qa["instruction"] for qa in chunk.get("qa_pairs", [])}
                    for new_qa in enrichment["new_qa_pairs"]:
                        if new_qa["instruction"] not in existing_instructions:
                            chunk["qa_pairs"].append(new_qa)
                            added_qas += 1
                    updated_chunks += 1
                    print(f"  Updated: {chunk['title']}")

    total_chunks = sum(len(m["chunks"]) for m in data["modules"])
    total_qa = sum(
        len(c.get("qa_pairs", []))
        for m in data["modules"]
        for c in m["chunks"]
    )
    print(f"\n  Updated {updated_chunks} chunks, added {added_qas} new QA pairs")
    print(f"  Total modules: {len(data['modules'])}")
    print(f"  Total chunks:  {total_chunks}")
    print(f"  Total QA pairs: {total_qa}")

    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\n  data.json updated successfully!")


if __name__ == "__main__":
    main()

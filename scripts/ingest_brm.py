"""
One-time script: Ingest the Consolidated BRM (Beverage Resource Manual) PDF
into data.json as structured modules/chunks for RAG retrieval.

Handles:
  - Guidelines pages (pumps, syrups, scoops, calibration, cleaning)
  - Recipe ingredient table pages across 13 sections
  - Multiple table formats (REG/LRG, QUANTITY-only, single-size)
  - Doubled/corrupted header text (falls back to adjacent page names)
  - Visual step-by-step preparation pages
"""

import json
import pathlib
import re
import pdfplumber

DATA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "data.json"
PDF_PATH = r"C:\Users\TWC\Downloads\Consolidated BRM (Version - JAN 2026).pdf"

# ── Manual name overrides for pages with doubled/corrupted text ──
NAME_OVERRIDES = {
    23: "CARAMEL MACCHIATO",
    30: "CAPPUCCINO",
    38: "SIGNATURE FILTER COFFEE",
    54: "ICED CARAMEL MACCHIATO",
    56: "ICED TOFFEE NUT LATTE",
    60: "ICED AMERICANO",
    64: "ICED CHOCOLATE",
    66: "ICED SIGNATURE FILTER COFFEE",
    69: "CLASSIC COLD BREW",
    75: "VIETNAMESE SHAKERATO",
    85: "CARAMEL FRAPPE",
    88: "TOFFEE NUT FRAPPE",
    96: "COOKIES & CREAM MILKSHAKE",
    107: "MASALA CHAI LATTE (ICED)",
    130: "FRENCH PRESS",
    135: "AMERICANO (FLASK)",
    139: "LATTE (FLASK)",
    141: "CLASSIC MOCHA (FLASK)",
    143: "FLAVOURED LATTE (FLASK)",
    145: "MASALA CHAI LATTE (FLASK)",
    166: "CHEWY BOBA COOKING PROCESS",
    168: "TARO BOBBLE TEA",
    184: "JASMINE TEA PREPARATION",
}

# ── Manual recipe data for pages with fully-doubled ingredient tables ──
MANUAL_RECIPES = {
    60: {
        "name": "ICED AMERICANO",
        "category": "CLASSICS",
        "prep_time": "2 MINUTES",
        "cup_size": "360/480 ML",
        "allergens": "DAIRY + CAFFEINE",
        "classification": "UNSWEETENED BEVERAGE",
        "oneliner": "A rich shot of espresso, diluted with water, and served on ice.",
        "ingredients": [
            {"step": "1", "ingredient": "HOT ESPRESSO", "measure": "SHOT", "reg": "1", "lrg": "1"},
            {"step": "2", "ingredient": "COLD WATER", "measure": "ML (MEASURING JAR)", "reg": "150", "lrg": "200"},
            {"step": "3", "ingredient": "ICE CUBE", "measure": "SCOOP", "reg": "1", "lrg": "1"},
        ],
        "prep_steps": "Take a clean glass → Pour hot espresso into the glass → Measure and pour cold water → Stir to mix → Top up with ice cubes → Serve as per standard.",
    },
}

# ── Section definitions from BRM INDEX (page 14) ────────────────

SECTIONS = [
    {"id": "brm_special_hot",       "title": "BRM – Special Hot Beverages",       "start": 16, "end": 27,  "desc": "Specialty hot espresso-based beverages with flavoured syrups, sauces, and garnishes."},
    {"id": "brm_classic_hot",       "title": "BRM – Classic Hot Beverages",       "start": 28, "end": 42,  "desc": "Classic hot espresso-based beverages: Americano, Cappuccino, Latte, Flat White, Hot Chocolate, Affogato."},
    {"id": "brm_specials_cold",     "title": "BRM – Specials Cold Beverages",     "start": 43, "end": 58,  "desc": "Specialty iced/cold espresso-based beverages with flavoured syrups, sauces, and ice."},
    {"id": "brm_classics_cold",     "title": "BRM – Classics Cold Beverages",     "start": 59, "end": 68,  "desc": "Classic cold espresso-based beverages: Iced Americano, Iced Latte, Iced Mocha."},
    {"id": "brm_cold_brew",         "title": "BRM – Cold Brew & Iced Coffee",     "start": 69, "end": 78,  "desc": "Cold brew and iced coffee beverages including citrus and lemon variations."},
    {"id": "brm_blended",           "title": "BRM – Blended Beverages & Milkshakes", "start": 79, "end": 100, "desc": "Blended frappes, milkshakes, and frozen beverages using the blender."},
    {"id": "brm_hot_teas",          "title": "BRM – Hot Teas",                    "start": 101, "end": 106, "desc": "Hot tea beverages: green tea, chamomile, masala chai latte."},
    {"id": "brm_iced_teas",         "title": "BRM – Iced Teas & Lemonades",       "start": 107, "end": 117, "desc": "Iced teas and lemonade beverages: masala chai, citrus, strawberry, classic, and delight variants."},
    {"id": "brm_manual_brews",      "title": "BRM – Manual Brews",                "start": 118, "end": 134, "desc": "Manual brew methods: Pour Over, Aeropress, Syphon, French Press with specific coffee-to-water ratios."},
    {"id": "brm_flask",             "title": "BRM – Flask Teas & Coffee",          "start": 135, "end": 154, "desc": "Flask-sized (500ml) bulk beverages for home delivery: Americano, filter coffee, cold coffee, cold mocha, iced tea, lemonade."},
    {"id": "brm_matcha",            "title": "BRM – Matcha Beverages",             "start": 155, "end": 161, "desc": "Japanese Matcha latte beverages (hot and iced) with matcha powder, hand whisk, and sieve."},
    {"id": "brm_chewy_boba",        "title": "BRM – Bobbles (Chewy Boba)",         "start": 162, "end": 177, "desc": "Chewy boba bubble tea beverages: chewy boba cooking process, Taro, Thai, original milk, vanilla milk, vanilla matcha variants."},
    {"id": "brm_popping_boba",      "title": "BRM – Bobbles (Popping Boba)",       "start": 178, "end": 194, "desc": "Popping boba bubble tea beverages: strawberry matcha, orange strawberry, grapefruit orange, grapefruit strawberry, peach grapefruit."},
]


def clean_text(s):
    """Clean extracted text: collapse whitespace, strip."""
    if not s:
        return ""
    return re.sub(r"\s+", " ", s).strip()


def is_doubled(text):
    """Detect doubled/corrupted text from overlapping PDF layers."""
    if not text:
        return False
    # Doubled text has patterns like "BBEEVVEERR" instead of "BEVER"
    doubled_pattern = sum(1 for i in range(len(text)-1) if text[i] == text[i+1] and text[i].isalpha())
    return doubled_pattern > 5


def undouble_text(text):
    """Try to extract the first layer from doubled/interleaved text."""
    if not text or not is_doubled(text):
        return text
    # Take every other character when text appears doubled
    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        # Skip the next char if it's the same (doubled)
        if i + 1 < len(text) and text[i] == text[i + 1]:
            i += 2
        else:
            i += 1
    return "".join(result)


def extract_beverage_name_from_text(page_text):
    """Try to extract beverage name from page text."""
    for pattern in [
        r"BEVERAGE\s+NAME\s*:\s*(.+?)(?:PREPARATION|CLASSIFICATION|$)",
        r"PRODUCT\s+NAME\s*:\s*(.+?)(?:PREPARATION|CLASSIFICATION|$)",
    ]:
        m = re.search(pattern, page_text, re.IGNORECASE)
        if m:
            name = clean_text(m.group(1))
            if not is_doubled(name):
                return name
    return ""


def extract_beverage_name_from_tables(tables):
    """Try to extract beverage name from table headers."""
    for t in tables:
        for row in t:
            if row and row[0]:
                raw = str(row[0])
                for label in ["BEVERAGE NAME:", "PRODUCT NAME:"]:
                    if label in raw:
                        if not is_doubled(raw):
                            name = raw.split(label)[1].strip()
                            # Clean trailing content
                            for stop in ["PREPARATION", "CLASSIFICATION", "CATEGORY"]:
                                if stop in name:
                                    name = name[:name.index(stop)].strip()
                            return name
    return ""


def extract_recipe_from_page(pdf, page_idx):
    """
    Extract recipe data from a recipe ingredient page.
    Returns dict with name, category, cup_size, allergens, prep_time,
    classification, oneliner, ingredients list, serving info.
    """
    page = pdf.pages[page_idx]
    tables = page.extract_tables()
    text = page.extract_text() or ""

    # Check for manual recipe override (for fully-doubled pages)
    page_num = page_idx + 1
    if page_num in MANUAL_RECIPES:
        recipe = dict(MANUAL_RECIPES[page_num])
        recipe["page"] = page_num
        return recipe

    # 1. Get beverage name (check overrides first)
    page_num = page_idx + 1
    if page_num in NAME_OVERRIDES:
        name = NAME_OVERRIDES[page_num]
    else:
        name = extract_beverage_name_from_tables(tables)
    if not name:
        name = extract_beverage_name_from_text(text)
    if not name:
        # Try adjacent pages (±1, ±2) for clean name
        for offset in [1, -1, 2, -2]:
            adj_idx = page_idx + offset
            if 0 <= adj_idx < len(pdf.pages):
                adj_text = pdf.pages[adj_idx].extract_text() or ""
                adj_name = extract_beverage_name_from_text(adj_text)
                if adj_name:
                    name = adj_name
                    break

    if not name:
        name = f"Unknown Beverage (page {page_idx + 1})"

    # 2. Extract metadata from header table
    category = ""
    prep_time = ""
    cup_size = ""
    allergens = ""
    launch_type = ""
    classification = ""
    oneliner = ""

    for t in tables:
        for row in t:
            row_str = " ".join(str(c) for c in row if c)
            # Category
            m = re.search(r"CATEGORY[–:\s]+(.+?)(?:\s+LAUNCH|$)", row_str, re.I)
            if m and not is_doubled(m.group(1)):
                category = clean_text(m.group(1))
            # Menu/Type for flask
            m = re.search(r"MENU/?\s*TYPE[:\s]+(\w+)", row_str, re.I)
            if m:
                category = f"FLASK ({clean_text(m.group(1))})"
            # Prep time
            m = re.search(r"PREPARATION\s*TIME[:\s]+(.+?)(?:\s*$)", row_str, re.I)
            if m and not is_doubled(m.group(1)):
                prep_time = clean_text(m.group(1))
            # Cup/Glass/Flask/Portion size
            m = re.search(r"(?:CUP|GLASS|FLASK|PORTION)\s*SIZE[:/\s]+(.+?)(?:\s+ALLERGEN|$)", row_str, re.I)
            if m and not is_doubled(m.group(1)):
                cup_size = clean_text(m.group(1))
            # Allergens
            m = re.search(r"ALLERGENS?[:\s]+(.+?)$", row_str, re.I)
            if m and not is_doubled(m.group(1)):
                allergens = clean_text(m.group(1))
            # Classification
            if "CLASSIFICATION" in row_str:
                after = row_str.split("CLASSIFICATION")[-1].strip()
                for val in ["SWEETENED", "UNSWEETENED"]:
                    if val in row_str.upper():
                        classification = val + " BEVERAGE"
            # Oneliner
            if "ONELINER" in row_str.upper():
                m = re.search(r"ONELINER[:\s-]+(.+)", row_str, re.I)
                if m:
                    oneliner = clean_text(m.group(1))

    # Also check full text for classification and oneliner
    if not classification:
        if "SWEETENED BEVERAGE" in text.upper():
            classification = "SWEETENED BEVERAGE"
        elif "UNSWEETENED BEVERAGE" in text.upper():
            classification = "UNSWEETENED BEVERAGE"
    if not oneliner:
        m = re.search(r"ONELINER[:\s-]+(.+)", text, re.I)
        if m:
            oneliner = clean_text(m.group(1))

    # 3. Extract ingredient rows
    ingredients = []
    for t in tables:
        header_found = False
        has_lrg = False
        is_doubled_table = False
        for row in t:
            row_strs = [str(c).strip() if c else "" for c in row]
            joined = " ".join(row_strs).upper()

            # Detect header row (handles both normal and doubled text)
            if ("STEP" in joined or "SSTTEEPP" in joined) and "INGREDIENTS" in joined:
                header_found = True
                has_lrg = "LRG" in joined
                # Check if header itself is doubled (e.g., "SSTTEEPP")
                if "SSTTEEPP" in joined or "IINNGG" in joined:
                    is_doubled_table = True
                continue

            if not header_found:
                continue

            # Skip serving/dine-in rows and footer rows
            if any(kw in joined for kw in ["DINE IN", "DINE", "TAKE AWAY", "DELIVERY", "ESPRESSO SHOTS—", "ONELINER", "NOTE :", "CLASSIFICATION", "STORAGE"]):
                continue

            # Try to parse ingredient row
            cells = [str(c).replace("\n", " ").strip() if c else "" for c in row]

            step_num = ""
            ingredient = ""
            measure = ""
            reg = ""
            lrg = ""

            for j, c in enumerate(cells):
                if not c.strip():
                    continue
                stripped = c.strip()
                # Check for step number (handle doubled: "11" = 1, "22" = 2)
                is_step = False
                if stripped.isdigit() and not step_num:
                    if is_doubled_table and len(stripped) == 2 and stripped[0] == stripped[1]:
                        step_num = stripped[0]
                    else:
                        step_num = stripped
                    is_step = True
                elif is_doubled_table and len(stripped) >= 2 and stripped[0].isdigit() and stripped[0] == stripped[1] and not step_num:
                    step_num = stripped[0]
                    is_step = True

                if is_step:
                    remaining = [cells[k] for k in range(j+1, len(cells))]
                    remaining = [r for r in remaining if r.strip()]
                    # Undouble remaining cells if needed
                    if is_doubled_table:
                        remaining = [undouble_text(r) if is_doubled(r) else r for r in remaining]
                    if len(remaining) >= 3:
                        ingredient = remaining[0]
                        measure = remaining[1]
                        reg = remaining[2]
                        if has_lrg and len(remaining) >= 4:
                            lrg = remaining[3]
                    elif len(remaining) == 2:
                        ingredient = remaining[0]
                        measure = remaining[1]
                    break

            if step_num and ingredient:
                ing_data = {
                    "step": step_num,
                    "ingredient": clean_text(ingredient),
                    "measure": clean_text(measure),
                    "reg": clean_text(reg)
                }
                if lrg:
                    ing_data["lrg"] = clean_text(lrg)
                ingredients.append(ing_data)

    # 4. Extract visual preparation steps from adjacent page
    prep_steps = ""
    next_idx = page_idx + 1
    if next_idx < len(pdf.pages):
        next_text = pdf.pages[next_idx].extract_text() or ""
        next_tables = pdf.pages[next_idx].extract_tables()
        # Check if next page is a visual/prep page (same beverage, no ingredient table)
        has_ingr_table = False
        for t in next_tables:
            for row in t:
                if row and any(c and "INGREDIENTS" in str(c) for c in row):
                    has_ingr_table = True
        if not has_ingr_table and "BEVERAGE" in next_text.upper():
            # Extract prep text, removing headers/footers
            lines = next_text.split("\n")
            prep_lines = []
            for line in lines:
                line_clean = line.strip()
                if any(skip in line_clean.upper() for skip in [
                    "BEVERAGE RESOURCE MANUAL", "VERSION DATED", "THIRD WAVE COFFEE",
                    "CONFIDENTIAL", "LEARNING &", "DEVELOPMENT", "BEVERAGE NAME:",
                    "CATEGORY", "LAUNCH TYPE", "CUP SIZE", "GLASS SIZE", "FLASK SIZE",
                    "ALLERGENS", "PREPARATION TIME"
                ]):
                    continue
                if line_clean:
                    prep_lines.append(line_clean)
            if prep_lines:
                prep_steps = " → ".join(prep_lines)

    return {
        "name": name,
        "category": category,
        "prep_time": prep_time,
        "cup_size": cup_size,
        "allergens": allergens,
        "launch_type": launch_type,
        "classification": classification,
        "oneliner": oneliner,
        "ingredients": ingredients,
        "prep_steps": prep_steps,
        "page": page_idx + 1,
    }


def build_recipe_content(recipe):
    """Build natural-language content string for a recipe chunk."""
    parts = [f"{recipe['name']} Recipe"]
    if recipe["category"]:
        parts.append(f"Category: {recipe['category']}")
    if recipe["cup_size"]:
        parts.append(f"Size: {recipe['cup_size']}")
    if recipe["prep_time"]:
        parts.append(f"Preparation Time: {recipe['prep_time']}")
    if recipe["allergens"]:
        parts.append(f"Allergens: {recipe['allergens']}")
    if recipe["classification"]:
        parts.append(f"Classification: {recipe['classification']}")

    if recipe["ingredients"]:
        parts.append("Ingredients & Steps:")
        for ing in recipe["ingredients"]:
            line = f"  Step {ing['step']}: {ing['ingredient']}"
            if ing.get("measure"):
                line += f" ({ing['measure']})"
            if ing.get("reg"):
                line += f" — REG: {ing['reg']}"
            if ing.get("lrg"):
                line += f", LRG: {ing['lrg']}"
            parts.append(line)

    if recipe["oneliner"]:
        parts.append(f"Description: {recipe['oneliner']}")
    if recipe["prep_steps"]:
        parts.append(f"Preparation: {recipe['prep_steps']}")

    return "\n".join(parts)


def build_qa_pairs(recipe):
    """Generate QA pairs for a recipe."""
    name = recipe["name"]
    pairs = []

    # Basic recipe question
    if recipe["ingredients"]:
        steps_text = []
        for ing in recipe["ingredients"]:
            s = f"Step {ing['step']}: {ing['ingredient']}"
            if ing.get("measure"):
                s += f" ({ing['measure']})"
            if ing.get("reg"):
                s += f" — REG: {ing['reg']}"
            if ing.get("lrg"):
                s += f", LRG: {ing['lrg']}"
            steps_text.append(s)
        steps_str = "; ".join(steps_text)

        pairs.append({
            "instruction": f"How do I make {name}?",
            "output": f"To make {name}: {steps_str}."
        })
        pairs.append({
            "instruction": f"What are the ingredients for {name}?",
            "output": f"The ingredients for {name} are: {', '.join(ing['ingredient'] for ing in recipe['ingredients'])}."
        })
        # Quantities question
        pairs.append({
            "instruction": f"What are the quantities for {name}?",
            "output": f"{name} recipe: {steps_str}."
        })

    if recipe["cup_size"]:
        pairs.append({
            "instruction": f"What size is {name} served in?",
            "output": f"{name} is served in {recipe['cup_size']}."
        })

    if recipe["allergens"]:
        pairs.append({
            "instruction": f"What allergens does {name} contain?",
            "output": f"{name} contains: {recipe['allergens']}."
        })

    if recipe["oneliner"]:
        pairs.append({
            "instruction": f"What is {name}?",
            "output": f"{name}: {recipe['oneliner']}"
        })

    if recipe["classification"]:
        pairs.append({
            "instruction": f"Is {name} sweetened or unsweetened?",
            "output": f"{name} is a {recipe['classification'].lower()}."
        })

    if recipe["prep_time"]:
        pairs.append({
            "instruction": f"How long does it take to make {name}?",
            "output": f"{name} takes {recipe['prep_time'].lower()} to prepare."
        })

    return pairs


def build_recipe_tags(recipe):
    """Generate relevant tags for a recipe."""
    name_words = recipe["name"].lower().split()
    tags = ["brm", "recipe", "beverage"]
    tags.extend(name_words)

    if recipe["category"]:
        cat_lower = recipe["category"].lower()
        tags.append(cat_lower)
        if "special" in cat_lower:
            tags.append("specials")
        if "classic" in cat_lower:
            tags.append("classics")
        if "flask" in cat_lower:
            tags.append("flask")

    # Add ingredient names as tags
    for ing in recipe["ingredients"]:
        ing_lower = ing["ingredient"].lower()
        for word in ing_lower.split():
            if word not in ["ml", "gms", "shot", "scoop", "rounds", "the", "a", "in", "of"]:
                tags.append(word)

    if recipe["allergens"]:
        for a in recipe["allergens"].lower().replace("+", ",").split(","):
            a = a.strip()
            if a:
                tags.append(a)

    # Section-specific tags
    if recipe.get("classification"):
        tags.append(recipe["classification"].lower().replace(" ", "_"))

    return list(dict.fromkeys(tags))  # deduplicate, preserve order


def extract_guidelines(pdf):
    """Extract guideline pages (1-14) as a single module."""
    chunks = []

    # Pump guidelines (pages 3-4)
    pump_text = ""
    for p in range(2, 4):
        t = pdf.pages[p].extract_text() or ""
        pump_text += t + "\n"
    pump_text = clean_text(pump_text)
    if pump_text:
        chunks.append({
            "chunk_id": "brm_guide_pumps",
            "title": "BRM – Pump Types & Guidelines",
            "intent": "Explain the different pump sizes used in beverage preparation.",
            "content": "TWC uses five pump sizes for beverage preparation: 5 ML pump (narrow mouth) — used for Sugar Syrup, Jaggery Syrup. 7.5 ML pump (narrow mouth) — used for Hazelnut Syrup, Vanilla Syrup, Orange Zest Syrup. 10 ML pump (narrow mouth) — used for Iced Tea Syrup, Sweet & Sour Syrup, Grapefruit Syrup, Peach Syrup, Cold Espresso Concentrate. 10 ML pump (wide mouth) — used for Salted Caramel Sauce, Toffee Nut Sauce. 15 ML pump (wide mouth) — used for Chocolate Sauce, Strawberry Sauce. Squeeze bottles are used for: Caramel Topping, Chocolate Fudge Topping. Condensed Milk uses a FIFO bottle.",
            "tags": ["brm", "pumps", "syrup", "pump size", "5ml", "7.5ml", "10ml", "15ml", "equipment", "guidelines"],
            "qa_pairs": [
                {"instruction": "What pump sizes does TWC use?", "output": "TWC uses five pump sizes: 5 ML (narrow), 7.5 ML (narrow), 10 ML (narrow), 10 ML (wide), and 15 ML (wide mouth)."},
                {"instruction": "What pump size is used for chocolate sauce?", "output": "Chocolate sauce uses the 15 ML wide mouth pump."},
                {"instruction": "What pump size is used for vanilla syrup?", "output": "Vanilla syrup uses the 7.5 ML narrow mouth pump."},
                {"instruction": "What pump size is used for sugar syrup?", "output": "Sugar syrup uses the 5 ML narrow mouth pump."},
                {"instruction": "What pump is used for iced tea syrup?", "output": "Iced tea syrup uses the 10 ML narrow mouth pump."},
                {"instruction": "What pump is used for salted caramel sauce?", "output": "Salted caramel sauce uses the 10 ML wide mouth pump."},
                {"instruction": "What pump size for strawberry sauce?", "output": "Strawberry sauce uses the 15 ML wide mouth pump."},
                {"instruction": "What syrups use the 7.5ml pump?", "output": "The 7.5 ML pump is used for Hazelnut Syrup, Vanilla Syrup, and Orange Zest Syrup."},
                {"instruction": "What syrups use the 10ml narrow pump?", "output": "The 10 ML narrow pump is used for Iced Tea Syrup, Sweet & Sour Syrup, Grapefruit Syrup, Peach Syrup, and Cold Espresso Concentrate."},
                {"instruction": "How is caramel topping dispensed?", "output": "Caramel Topping is dispensed using a squeeze bottle, not a pump."},
                {"instruction": "How is condensed milk dispensed?", "output": "Condensed milk is dispensed using a FIFO bottle."}
            ]
        })

    # Pump calibration (page 7)
    chunks.append({
        "chunk_id": "brm_guide_calibration",
        "title": "BRM – Pump Calibration Standards",
        "intent": "Explain pump calibration weights and procedure.",
        "content": "Pump calibration standards (weight per pump): 5 ML pump = 6.2 grams. 7.5 ML pump = 10.03 grams. 15 ML wide mouth pump = 18.2 grams. 10 ML narrow mouth pump = 12.4 grams. 10 ML wide mouth pump = 12.4 grams. Calibration must be done weekly. Procedure: Place the measuring cup on the weighing scale, tare it, do 10 pumps, note the total weight, divide by 10 to get weight per pump. If the weight per pump does not match the standard, adjust the pump or replace it.",
        "tags": ["brm", "calibration", "pump", "weight", "grams", "weekly", "quality", "equipment"],
        "qa_pairs": [
            {"instruction": "How often should pumps be calibrated?", "output": "Pumps should be calibrated weekly."},
            {"instruction": "What is the calibration weight for the 5ml pump?", "output": "The 5 ML pump should dispense 6.2 grams per pump."},
            {"instruction": "What is the calibration weight for the 15ml pump?", "output": "The 15 ML wide mouth pump should dispense 18.2 grams per pump."},
            {"instruction": "How do you calibrate pumps?", "output": "Place a measuring cup on the scale, tare it, do 10 pumps, note the total weight, divide by 10 to get weight per pump. If it doesn't match the standard, adjust or replace the pump."},
            {"instruction": "What is the calibration weight for 7.5ml pump?", "output": "The 7.5 ML pump should dispense 10.03 grams per pump."},
            {"instruction": "What is the calibration weight for 10ml pump?", "output": "Both the 10 ML narrow and 10 ML wide pumps should dispense 12.4 grams per pump."}
        ]
    })

    # Pump cleaning (page 8)
    chunks.append({
        "chunk_id": "brm_guide_pump_cleaning",
        "title": "BRM – Pump Cleaning Procedure",
        "intent": "Explain how to clean syrup pumps.",
        "content": "Pump cleaning procedure: Step 1 — Remove the pump from the syrup bottle. Step 2 — Disassemble the pump (remove the cap and spring). Step 3 — Soak all parts in hot water for 10 minutes. Step 4 — Scrub with a brush to remove residue. Step 5 — Rinse under running water. Step 6 — Let all parts air dry completely before reassembly. Step 7 — Reassemble and place back on the bottle. Pumps should be cleaned daily at end of day (EOD).",
        "tags": ["brm", "pump", "cleaning", "eod", "hygiene", "maintenance", "equipment"],
        "qa_pairs": [
            {"instruction": "How do you clean pumps?", "output": "Remove pump from bottle, disassemble (remove cap and spring), soak in hot water for 10 minutes, scrub with brush, rinse under running water, air dry completely, then reassemble."},
            {"instruction": "How often should pumps be cleaned?", "output": "Pumps should be cleaned daily at end of day (EOD)."}
        ]
    })

    # Garnish preparation (page 10)
    chunks.append({
        "chunk_id": "brm_guide_garnish",
        "title": "BRM – Garnish Preparation (Mint & Lemon)",
        "intent": "Explain how to prepare mint and lemon garnishes.",
        "content": "Mint preparation: Cut the packet, rinse leaves under running RO water, remove black/damaged leaves, carefully pluck the top 2/3 leaves with the stem, store in 1/9 GN pan with lid. Lemon preparation: Cut the lemon packet, discard damaged/black spot/discolored lemons, wash under running RO water, cut into round slices of uniform thickness, remove seeds with knife, store in 1/9 GN pan with lid. IMPORTANT: Do NOT store mint and lemon in water.",
        "tags": ["brm", "garnish", "mint", "lemon", "preparation", "storage", "guidelines"],
        "qa_pairs": [
            {"instruction": "How do you prepare mint for garnish?", "output": "Cut the packet, rinse leaves under running RO water, remove black/damaged leaves, pluck the top 2/3 leaves with the stem, store in 1/9 GN pan with lid. Do NOT store in water."},
            {"instruction": "How do you prepare lemon for garnish?", "output": "Cut the packet, discard damaged lemons, wash under running RO water, cut into uniform round slices, remove seeds with knife, store in 1/9 GN pan with lid. Do NOT store in water."},
            {"instruction": "Can I store mint in water?", "output": "No. Do NOT store mint and lemon in water. Store in a 1/9 GN pan with a lid."}
        ]
    })

    # Scoop guidelines (page 11)
    chunks.append({
        "chunk_id": "brm_guide_scoops",
        "title": "BRM – Scoop Guidelines",
        "intent": "Explain which scoops to use for which ingredients.",
        "content": "Scoop types and their ingredients: 10 GM SS Scoop — used for Frappe Mix. 5 ML Plastic Scoop — used for Butter Crumbs, Choco Chunks, Choco Crumbs, Nata de Coco, Boba Tea Premix. 1 GM SS Scoop — used for Matcha Powder. Boba Scoop — used for Popping Boba and Chewy Boba.",
        "tags": ["brm", "scoop", "frappe", "matcha", "boba", "choco", "equipment", "guidelines"],
        "qa_pairs": [
            {"instruction": "What scoop is used for frappe mix?", "output": "Frappe mix uses the 10 GM SS (stainless steel) scoop."},
            {"instruction": "What scoop is used for matcha powder?", "output": "Matcha powder uses the 1 GM SS scoop (also referred to as 2.5 ML scoop in recipes)."},
            {"instruction": "What scoop is used for boba?", "output": "Popping Boba and Chewy Boba use the dedicated Boba Scoop."},
            {"instruction": "What ingredients use the 5ml plastic scoop?", "output": "The 5 ML plastic scoop is used for Butter Crumbs, Choco Chunks, Choco Crumbs, Nata de Coco, and Boba Tea Premix."}
        ]
    })

    # Sea salt grinder (pages 12-13)
    chunks.append({
        "chunk_id": "brm_guide_salt_grinder",
        "title": "BRM – Sea Salt Grinder Setup",
        "intent": "Explain how to set up the sea salt grinder.",
        "content": "Standard sea salt grinder setup: Step 1 — Turn the dial clockwise (large dot to small dot direction) until it locks. Step 2 — Turn anti-clockwise (small dot to large dot direction) making four 180-degree (half-circle) turns to set the right grind size. Step 3 — Keep dispensing area free from liquids and cap when not in use (moisture creates salt buildup). Orika sea salt grinder setup: Step 1 — Turn the RED dial to 'MIN' setting. Step 2 — Use per standard turns for REG and LRG sizes. Step 3 — Keep dispensing area free from liquids and cap when not in use.",
        "tags": ["brm", "sea salt", "grinder", "setup", "orika", "equipment", "guidelines"],
        "qa_pairs": [
            {"instruction": "How do I set up the sea salt grinder?", "output": "Turn the dial clockwise until locked, then turn anti-clockwise making four 180-degree turns. Keep dispensing area dry and capped when not in use."},
            {"instruction": "How do I set up the Orika sea salt grinder?", "output": "Turn the RED dial to 'MIN' setting. Use per standard turns for REG and LRG sizes. Keep dispensing area free from liquids and cap when not in use."}
        ]
    })

    # Hot beverage buildup (page 16)
    chunks.append({
        "chunk_id": "brm_guide_hot_buildup",
        "title": "BRM – Hot Beverage Buildup Method",
        "intent": "Explain the standard hot beverage buildup sequence.",
        "content": "Standard hot beverage buildup sequence: Step 1 — Pump in the flavored syrups into a pre-warmed cup. Step 2 — Brew espresso over the syrups. Step 3 — Swirl the cup about 3 times to blend the syrup and espresso. Step 4 — Pour steamed/frothed milk over it (as per latte consistency — uniform silky foam). Step 5 — Top with 2.5 rounds of whipped cream (if required). Step 6 — Garnish with relevant ingredients. This is the standard method for all hot espresso-based beverages.",
        "tags": ["brm", "hot", "buildup", "espresso", "milk", "syrup", "method", "guidelines"],
        "qa_pairs": [
            {"instruction": "What is the hot beverage buildup method?", "output": "1. Pump in flavored syrups into a pre-warmed cup. 2. Brew espresso over the syrups. 3. Swirl 3 times to blend. 4. Pour steamed/frothed milk. 5. Top with whipped cream (if required). 6. Garnish."},
            {"instruction": "What is the standard way to make hot beverages?", "output": "Start with syrups in a pre-warmed cup, brew espresso over it, swirl 3 times, pour steamed milk, add whipped cream if needed, then garnish."}
        ]
    })

    # Iced beverage buildup (page 43)
    chunks.append({
        "chunk_id": "brm_guide_cold_buildup",
        "title": "BRM – Iced Beverage Buildup Method",
        "intent": "Explain the standard iced/cold beverage buildup sequence.",
        "content": "Standard iced beverage buildup sequence: Step 1 — Add flavored syrups/sauces into the glass. Step 2 — Add fresh espresso. Step 3 — Add cold milk/water/soda/cold brew. Step 4 — Add ice cubes. Step 5 — Garnish with relevant ingredients. This is the standard method for all cold espresso-based beverages.",
        "tags": ["brm", "cold", "iced", "buildup", "espresso", "method", "guidelines"],
        "qa_pairs": [
            {"instruction": "What is the iced beverage buildup method?", "output": "1. Add syrups/sauces. 2. Add fresh espresso. 3. Add cold milk/water/soda/cold brew. 4. Add ice cubes. 5. Garnish."},
            {"instruction": "What is the standard way to make cold beverages?", "output": "Start with syrups/sauces in a glass, add espresso, then cold milk/water/soda, add ice, and garnish."}
        ]
    })

    # Blended beverage buildup (page 79)
    chunks.append({
        "chunk_id": "brm_guide_blended_buildup",
        "title": "BRM – Blended Beverage Buildup Method",
        "intent": "Explain the standard blended beverage buildup sequence.",
        "content": "Standard blended beverage buildup sequence: Step 1 — Add flavored syrups/sauces. Step 2 — Add cold espresso. Step 3 — Add cold milk. Step 4 — Add frappe mix (or thickshake mix for milkshakes). Step 5 — Add ice cubes. Step 6 — Blend. Step 7 — Glaze the inside of the glass (only for frappes — drizzle sauce inside the glass before pouring). Step 8 — Pour and garnish.",
        "tags": ["brm", "blended", "frappe", "milkshake", "buildup", "blender", "method", "guidelines"],
        "qa_pairs": [
            {"instruction": "What is the blended beverage buildup method?", "output": "1. Add syrups/sauces. 2. Add cold espresso. 3. Add cold milk. 4. Add frappe/thickshake mix. 5. Add ice. 6. Blend. 7. Glaze the glass (frappes only). 8. Pour and garnish."},
            {"instruction": "How do you make frappes?", "output": "Add syrups, cold espresso, cold milk, frappe mix, and ice to the blender. Blend. Glaze the inside of the glass with sauce, then pour the blended beverage and garnish."}
        ]
    })

    # Hot tea buildup (page 101)
    chunks.append({
        "chunk_id": "brm_guide_tea_buildup",
        "title": "BRM – Hot Tea Buildup Method",
        "intent": "Explain the standard hot tea preparation sequence.",
        "content": "Standard hot tea buildup sequence: Step 1 — Add tea bags as per the size. Step 2 — Fill the cup with hot water. Step 3 — Let it steep for 3 minutes. Step 4 — Remove the tea bag. Step 5 — Serve with saucer, honey on the side, and spoon.",
        "tags": ["brm", "tea", "hot tea", "buildup", "steep", "method", "guidelines"],
        "qa_pairs": [
            {"instruction": "How do you make hot tea?", "output": "Add tea bags, fill with hot water, steep for 3 minutes, remove tea bag. Serve with saucer, honey on side, and spoon."},
            {"instruction": "How long should tea steep?", "output": "Tea should steep for 3 minutes."}
        ]
    })

    # Matcha smallwares (page 157)
    chunks.append({
        "chunk_id": "brm_guide_matcha_tools",
        "title": "BRM – Matcha & Boba Smallwares",
        "intent": "Explain the tools used for matcha and boba preparation.",
        "content": "Matcha and Boba preparation tools: Measuring Jar (250 ML) — for measuring liquids. SS Scoop (2.5 ML) — for measuring matcha powder. Single Mesh Sieve — for sifting matcha powder (wash with plain water once a day at EOD; do NOT wash during operational hours; sieve must be 100% dry; if damp, tap dry with M-fold tissue). Electric Hand Whisk (with AA battery) — for blending matcha (approximately 3 cm diameter whisk head, 9 cm handle). Cleaning: Measuring jar and hand whisk — rinse under running tap water after every use.",
        "tags": ["brm", "matcha", "boba", "tools", "sieve", "whisk", "measuring jar", "equipment", "cleaning"],
        "qa_pairs": [
            {"instruction": "What tools are needed for matcha?", "output": "Measuring jar (250 ML), 2.5 ML SS scoop for matcha powder, single mesh sieve for sifting, and electric hand whisk with AA battery."},
            {"instruction": "How do you clean the matcha sieve?", "output": "Wash with plain water once a day at end of day (EOD). Do NOT wash during operational hours. The sieve must be 100% dry. If it gets damp, tap dry with M-fold tissue paper."},
            {"instruction": "How do you clean the hand whisk?", "output": "Rinse the hand whisk under running tap water after every use."}
        ]
    })

    return {
        "id": "brm_guidelines",
        "title": "BRM – Beverage Preparation Guidelines & Equipment",
        "description": "Consolidated Beverage Resource Manual guidelines: pump types and sizes, syrup-to-pump mapping, pump calibration standards, pump cleaning, garnish preparation, scoop guidelines, sea salt grinder setup, and standard buildup methods for hot, cold, blended, and tea beverages.",
        "chunks": chunks
    }


def main():
    print("Opening PDF...")
    pdf = pdfplumber.open(PDF_PATH)
    print(f"Total pages: {len(pdf.pages)}")

    # ── Extract guidelines module ────────────────────────────────
    print("\nExtracting guidelines...")
    guidelines_module = extract_guidelines(pdf)
    print(f"  {len(guidelines_module['chunks'])} guideline chunks")

    # ── Extract recipe modules by section ────────────────────────
    all_modules = [guidelines_module]

    for section in SECTIONS:
        print(f"\nProcessing: {section['title']} (pages {section['start']}-{section['end']})...")
        recipes = []

        for page_num in range(section["start"], section["end"] + 1):
            page_idx = page_num - 1
            if page_idx >= len(pdf.pages):
                break

            # Check if this page has an ingredient table
            tables = pdf.pages[page_idx].extract_tables()
            has_ingredient_table = False
            for t in tables:
                for row in t:
                    if row and any(c and "INGREDIENTS" in str(c) for c in row):
                        has_ingredient_table = True
                        break
                if has_ingredient_table:
                    break

            if has_ingredient_table:
                recipe = extract_recipe_from_page(pdf, page_idx)
                if recipe and recipe["ingredients"]:
                    recipes.append(recipe)

        if not recipes:
            print(f"  No recipes found, skipping.")
            continue

        # Build module
        chunks = []
        for i, recipe in enumerate(recipes, 1):
            chunk_id = f"{section['id']}_{i}"
            content = build_recipe_content(recipe)
            qa_pairs = build_qa_pairs(recipe)
            tags = build_recipe_tags(recipe)

            chunks.append({
                "chunk_id": chunk_id,
                "title": f"{recipe['name']} Recipe",
                "intent": f"Provide the recipe and preparation steps for {recipe['name']}.",
                "content": content,
                "tags": tags,
                "qa_pairs": qa_pairs
            })
            print(f"  [{i}] {recipe['name']} — {len(recipe['ingredients'])} ingredients, {len(qa_pairs)} QA pairs")

        module = {
            "id": section["id"],
            "title": section["title"],
            "description": section["desc"],
            "chunks": chunks
        }
        all_modules.append(module)

    pdf.close()

    # ── Load existing data.json and append ───────────────────────
    print(f"\nLoading {DATA_PATH}...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Remove any existing BRM modules (idempotent re-runs)
    brm_ids = {m["id"] for m in all_modules}
    data["modules"] = [m for m in data["modules"] if m["id"] not in brm_ids]

    # Append new modules
    data["modules"].extend(all_modules)

    total_chunks = sum(len(m["chunks"]) for m in all_modules)
    total_qa = sum(len(c["qa_pairs"]) for m in all_modules for c in m["chunks"])
    print(f"\nAdding {len(all_modules)} modules, {total_chunks} chunks, {total_qa} QA pairs")

    # Save
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {DATA_PATH}")

    # ── Summary ──────────────────────────────────────────────────
    print("\n═══ SUMMARY ═══")
    for m in all_modules:
        print(f"  {m['title']}: {len(m['chunks'])} chunks")
    print(f"\n  TOTAL: {len(all_modules)} modules, {total_chunks} chunks, {total_qa} QA pairs")


if __name__ == "__main__":
    main()

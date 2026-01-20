# ================================
# SALES ANALYTICS SYSTEM
# ================================

import os


# ---------- Helper Functions ----------

def read_sales_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    data = []
    # Skip header line
    for i, line in enumerate(lines):
        if i == 0:  # Skip header
            continue
        
        parts = line.strip().split("|")
        if len(parts) >= 8:
            try:
                transaction_id = parts[0]
                date = parts[1]
                product_id = parts[2]
                product_name = parts[3]
                quantity = int(parts[4])
                unit_price_str = parts[5].replace(",", "")  # Remove comma formatting
                unit_price = float(unit_price_str)
                customer_id = parts[6] if parts[6] else "Unknown"
                region = parts[7].strip() if len(parts) > 7 and parts[7].strip() else "Unknown"
                
                # Calculate total amount
                amount = quantity * unit_price
                
                data.append({
                    "id": transaction_id,
                    "date": date,
                    "region": region,
                    "product": product_name,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "amount": amount,
                    "customer_id": customer_id
                })
            except (ValueError, IndexError):
                # Skip malformed lines
                continue
    
    return data


def clean_sales_data(data):
    cleaned = []
    for d in data:
        if d["amount"] > 0 and d["quantity"] > 0:
            cleaned.append(d)
    return cleaned


def filter_transactions(data, region=None, min_amount=None, max_amount=None):
    result = data
    if region:
        result = [d for d in result if d["region"].lower() == region.lower()]
    if min_amount is not None:
        result = [d for d in result if d["amount"] >= min_amount]
    if max_amount is not None:
        result = [d for d in result if d["amount"] <= max_amount]
    return result


def validate_transactions(data):
    valid = []
    invalid = []

    for d in data:
        if d["amount"] > 0 and d["quantity"] > 0:
            valid.append(d)
        else:
            invalid.append(d)

    return valid, invalid


def analyze_sales(data):
    total_sales = sum(d["amount"] for d in data)
    avg_sales = total_sales / len(data) if data else 0

    return {
        "total_sales": total_sales,
        "average_sales": avg_sales,
        "transactions": len(data)
    }


def fetch_products_from_api():
    # Dummy API data (exam safe)
    return [
        {"product": "Laptop", "category": "Electronics"},
        {"product": "Phone", "category": "Electronics"},
        {"product": "Shoes", "category": "Fashion"}
    ]


def enrich_sales_data(sales, products):
    enriched = []
    for s in sales:
        category = "Unknown"
        for p in products:
            if p["product"].lower() == s["product"].lower():
                category = p["category"]
        s["category"] = category
        enriched.append(s)
    return enriched


def save_to_file(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        for d in data:
            f.write(str(d) + "\n")


def generate_report(analysis, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("SALES REPORT\n")
        f.write("================\n")
        f.write(f"Total Transactions: {analysis['transactions']}\n")
        f.write(f"Total Sales: ₹{analysis['total_sales']:,.2f}\n")
        f.write(f"Average Sale: ₹{analysis['average_sales']:,.2f}\n")


# ---------- MAIN FUNCTION ----------

def main():
    print("=" * 40)
    print("SALES ANALYTICS SYSTEM")
    print("=" * 40)

    try:
        print("\n[1/10] Reading sales data...")
        sales = read_sales_file("sales_data.txt")
        print(f"✓ Successfully read {len(sales)} transactions")

        print("\n[2/10] Parsing and cleaning data...")
        sales = clean_sales_data(sales)
        print(f"✓ Parsed {len(sales)} records")

        regions = sorted(set(s["region"] for s in sales))
        amounts = [s["amount"] for s in sales]

        print("\n[3/10] Filter Options Available:")
        print("Regions:", ", ".join(regions))
        if amounts:
            print(f"Amount Range: ₹{min(amounts):,.2f} - ₹{max(amounts):,.2f}")

        choice = input("\nDo you want to filter data? (y/n): ").lower()

        if choice == "y":
            region = input("Enter region (or press Enter to skip): ")
            min_amt = input("Enter min amount (or press Enter): ")
            max_amt = input("Enter max amount (or press Enter): ")

            sales = filter_transactions(
                sales,
                region if region else None,
                float(min_amt) if min_amt else None,
                float(max_amt) if max_amt else None
            )
            print(f"✓ Filtered data count: {len(sales)}")

        print("\n[4/10] Validating transactions...")
        valid, invalid = validate_transactions(sales)
        print(f"✓ Valid: {len(valid)} | Invalid: {len(invalid)}")

        print("\n[5/10] Analyzing sales data...")
        analysis = analyze_sales(valid)
        print("✓ Analysis complete")

        print("\n[6/10] Fetching product data from API...")
        products = fetch_products_from_api()
        print(f"✓ Fetched {len(products)} products")

        print("\n[7/10] Enriching sales data...")
        enriched = enrich_sales_data(valid, products)
        print(f"✓ Enriched {len(enriched)}/{len(valid)} transactions")

        print("\n[8/10] Saving enriched data...")
        save_to_file(enriched, "data/enriched_sales_data.txt")
        print("✓ Saved to: data/enriched_sales_data.txt")

        print("\n[9/10] Generating report...")
        generate_report(analysis, "output/sales_report.txt")
        print("✓ Report saved to: output/sales_report.txt")

        print("\n[10/10] Process Complete!")
        print("=" * 40)

    except FileNotFoundError:
        print("❌ Error: sales_data.txt not found")

    except Exception as e:
        print("❌ Unexpected error:", e)


# ---------- RUN ----------
if __name__ == "__main__":
    main()

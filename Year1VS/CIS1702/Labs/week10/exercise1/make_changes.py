"""
Order Processor:
This script processes raw order data, validates integrity, and calculates totals.
please keep in mind that this demo will be used on your first lab exercise
"""

# --- 1. Constants (Week 10: No "Magic Numbers") ---
# We define these at the top so they are easy to change later.
"""
Task 2: It's best to keep it a global variable so if the tax rate is changed, it can be changed in this one place and would then 
apply everywhere """
TAX_RATE = 0.15          # 15% Sales Tax
SHIPPING_COST = 5.99     # Flat rate shipping
FREE_SHIPPING_THRESHOLD = 50.00

# --- 2. Input Data (Simulating a JSON API response) ---
raw_orders = [
    {"id": "ORD-001", "item": "Wireless Mouse", "price": 25.00, "quantity": 2},
    {"id": "ORD-002", "item": "Gaming Monitor", "price": 300.00, "quantity": 1},
    {"id": "ORD-003", "item": "Corrupted Item", "price": -10.00, "quantity": 1}, # Error: Negative price
    {"id": "ORD-004", "item": "Ghost Item", "quantity": 5},                       # Error: Missing price
    {"id": "ORD-005", "item": "USB Cable", "price": 5.00, "quantity": 0},          # Error: Zero quantity

    # ... keep existing orders ...
    {"id": "ORD-006", "item": "Bulk Cables", "price": 5.00, "quantity": 10, "is_vip": False},
    # Should get 10% off, but pay shipping
    {"id": "ORD-007", "item": "VIP Mouse", "price": 45.00, "quantity": 1, "is_vip": True}
    # Should be < 50 but FREE shipping
]

# --- 3. Helper Functions (Week 4 & 10: Single Responsibility Principle) ---

def is_valid_order(order):
    """
    Checks if an order dictionary contains all necessary fields and valid values.
    Returns True if valid, False otherwise.
    """
    # Check for missing keys
    """Task 2:
    One of the items in raw_orders is missing the quantity key. Remvoing if not in price, would cause an indexing error in the if order['price'].
    """
    if "price" not in order or "quantity" not in order or "item" not in order:
        print(f"FAILED: Order {order.get('id', 'Unknown')} is missing data.")
        return False

    # Check for logical errors (business rules)
    if order["price"] <= 0:
        print(f"FAILED: Order {order['id']} has an invalid price: ${order['price']}")
        return False
    
    if order["quantity"] <= 0:
        print(f"FAILED: Order {order['id']} has an invalid quantity: {order['quantity']}")
        return False
    
    if 'is_vip' not in order:
        order['is_vip'] = False 

    return True

def calculate_final_price(price, quantity, vip_status):
    """
    Calculates total cost including tax and shipping logic.
    """
    subtotal = price * quantity

    # Bulk buy gives 10% discount
    if quantity >= 5:
        subtotal *= .9
    
    tax_amount = subtotal * TAX_RATE
    
    # Industry Logic: Conditional shipping costs
    if subtotal >= FREE_SHIPPING_THRESHOLD or vip_status == True:
        shipping = 0.00
    else:
        shipping = SHIPPING_COST
        
    total = subtotal + tax_amount + shipping
    return round(total, 2)

# --- 4. Main Logic (Week 3: Loops) ---

def process_order_batch(orders):
    """
    Main driver function to process a list of orders.
    """
    print("--- STARTING BATCH PROCESSING ---\n")
    
    valid_orders = []
    total_revenue = 0.00

    # Loop through every order in the list
    for current_order in orders:
        
        # Step A: Validate (Defensive Coding)
        if is_valid_order(current_order):
            
            # Step B: Calculate logic (only if valid)
            """Task 2:
            This function doesn't know how to apply tax, is it instead calls a function that does. This is best practice as modularity is
            easier to debug/change - if the way they calculate cost (including) task is changed, it doesn't need to be changed here too.
            """
            final_price = calculate_final_price(
                current_order["price"], 
                current_order["quantity"],
                current_order['is_vip']
            )
            
            # Step C: Store clean data
            # We create a new 'clean' dictionary rather than mutating the old one
            processed_record = {
                "id": current_order["id"],
                "product": current_order["item"],
                "final_bill": final_price
            }
            
            valid_orders.append(processed_record)
            total_revenue += final_price
            print(f"SUCCESS: Processed {current_order['id']} - Total: ${final_price}")

    print(f"\n--- BATCH COMPLETE ---")
    print(f"Total Valid Orders: {len(valid_orders)}")
    print(f"Total Revenue Generated: ${round(total_revenue, 2)}")
    
    return valid_orders

# --- 5. Execution ---
if __name__ == "__main__":
    clean_report = process_order_batch(raw_orders)
    # real world: we would now save 'clean_report' to a CSV or Database
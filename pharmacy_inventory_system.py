

'''Task 2 develop a Python application for a pharmacy to manage medicine inventory and calculate daily sales revenue.

Your application must:
1. Ask how many different medicines need to be processed.
2. Use a for loop to process each medicine.
3. Collect the medicine name, available stock, price per unit, and quantity sold.
4. Check whether the requested sales quantity is available in stock.
5. Calculate the total sales amount for each successfully processed medicine.
6. Calculate and display the remaining stock after each sale.
7. Display a low-stock warning if the remaining stock is below 10 units.
8. Maintain the total pharmacy revenue using an accumulator.
9. Count how many medicines require restocking.
10. Generate a final report containing total medicines processed, total revenue, and medicines requiring restocking'''


print("========== SMART PHARMACY SYSTEM ==========")

total_medicines = int(input("How many medicines do you want to process? "))

total_revenue = 0
restock_count = 0
processed_medicines = 0

if total_medicines <= 0:
    print("Invalid number of medicines.")

else:

    for medicine in range(1, total_medicines + 1):

        print(f"========== MEDICINE {medicine} ==========")

        medicine_name = input("Enter medicine name: ").strip()
        available_stock = int(input("Enter available stock: "))
        price_per_unit = float(input("Enter price per unit (Rs.): "))
        quantity_sold = int(input("Enter quantity sold: "))

        # Validate medicine information
        if (medicine_name == "" or available_stock < 0
                or price_per_unit < 0 or quantity_sold < 0):
            print("Invalid medicine information. Skipping this medicine.")
            continue

        processed_medicines += 1

        
        if quantity_sold <= available_stock:

            sales_amount = quantity_sold * price_per_unit
            remaining_stock = available_stock - quantity_sold

            
            total_revenue += sales_amount

            print("\nSale Successful!")
            print(f"Medicine: {medicine_name}")
            print(f"Sales Amount: Rs. {sales_amount:.2f}")
            print(f"Remaining Stock: {remaining_stock}")

        else:
            print("\nSale Rejected!")
            print("Reason: Insufficient stock.")
            print(f"Available Stock: {available_stock}")
            print(f"Requested Quantity: {quantity_sold}")

            remaining_stock = available_stock

        # Check low stock
        if remaining_stock < 10:
            print(f"WARNING: {medicine_name} requires restocking!")
            restock_count += 1

    # Final report
    print("\n========== FINAL PHARMACY REPORT ==========")

    print(f"Total Medicines Processed: {processed_medicines}")
    print(f"Total Pharmacy Revenue: Rs. {total_revenue:.2f}")
    print(f"Medicines Requiring Restocking: {restock_count}")

    print("=================================================")




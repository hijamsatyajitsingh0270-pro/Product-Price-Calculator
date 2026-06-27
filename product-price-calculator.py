# Product Price Calculator

original_price = float(input("Enter Original Price: "))
discount_percentage = float(input("Enter Discount %:"))

discount_amount= discount_percentage/100 * original_price
final_price = original_price - discount_amount

print(f"Final price after {discount_percentage}% discount: {final_price}")
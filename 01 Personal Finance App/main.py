# Expense Tracker Project 🧾💸

expensesList = []  # list of expenses in form of dictionary
print("🙏 Welcome to Expense Tracker : Kharcha kam karo 💰😄")

while True:
    print("\n==== 📋 MENU ====")
    print("1️⃣  Add Expense ➕💸")
    print("2️⃣  View All Expenses 📑👀")
    print("3️⃣  View Total Kharcha 🧮💰")
    print("4️⃣  Exit 🚪❌")

    choice = input("👉 Please Enter Your Choice : ")

    # 1. ADD EXPENSE:
    if choice == "1":
        date = input("📅 Kis date par kharcha kiya tha? : ")
        category = input("🏷️ Kis type ka kharcha kiya? (Food 🍔, Travel 🚕, Tech 🧑‍💻, Books 📚) : ")
        description = input("📝 Aur detail dedo : ")
        amount = float(input("💵 Enter the amount : ₹"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n✅ DONE! Expense successfully add ho gaya 🎉")

    # 2. VIEW ALL EXPENSES:
    elif choice == "2":
        if len(expensesList) == 0:
            print("😴 No Expenses Added. Jao pehle kharcha karke aawo 💸😂")
        else:
            print("\n===== 📊 Ye hai aapka saara expense =====")
            count = 1
            for eachKharcha in expensesList:
                print(
                    f"🔹 Kharcha {count} → 📅 {eachKharcha['date']} | "
                    f"🏷️ {eachKharcha['category']} | 📝 {eachKharcha['description']} | "
                    f"💰 Rs.{eachKharcha['amount']}"
                )
                count += 1

    # 3. VIEW TOTAL SPENDING:
    elif choice == "3":
        total = 0
        for eachKharcha in expensesList:
            total += eachKharcha["amount"]

        print(f"\n🧮 Total Kharcha = 💰 Rs.{total} 😮")

    # 4. EXIT:
    elif choice == "4":
        print("🙏 Dhanyawad! Aapne hamara system use kiya 😍✨")
        print("📉 Kharcha kam, savings zyada! 💪💸")
        break

    else:
        print("❌ INVALID CHOICE! Dobara try karo 😅")
from db import get_connection
import matplotlib.pyplot as plt

def show_expense_pie_chart(user_id, month=None):
    conn = get_connection()
    cursor = conn.cursor()

    # Query with optional month filtering
    if month:
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM transactions
            WHERE type='expense' AND user_id=? AND date LIKE ?
            GROUP BY category
        """, (user_id, f'{month}-%'))  # '2025-06%' format
    else:
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM transactions
            WHERE type='expense' AND user_id=?
            GROUP BY category
        """, (user_id,))

    data = cursor.fetchall()
    conn.close()

    if not data:
        print(" No expense data to show for this user.")
        return

    categories, totals = zip(*data)

    plt.figure(figsize=(7, 7))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    title = f' Expense Distribution'
    if month:
        title += f' – {month}'
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio
    plt.show()

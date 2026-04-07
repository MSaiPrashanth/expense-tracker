from flask import Flask, render_template, request, redirect
import mysql.connector
import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.use('Agg')   

app = Flask(__name__)

# DB connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YourPassword",  
        database="exp_db"
    )

# Home page
@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    total = sum(row[2] for row in data)
    #  Category-wise data
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    chart_data = cursor.fetchall()

    categories = [row[0] for row in chart_data]
    amounts = [row[1] for row in chart_data]


    #  Monthly
    cursor.execute("""
    SELECT DATE_FORMAT(date, '%Y-%m'), SUM(amount)
    FROM expenses
    GROUP BY DATE_FORMAT(date, '%Y-%m')
    ORDER BY DATE_FORMAT(date, '%Y-%m')
    """)
    monthly_data = cursor.fetchall()

    months = [row[0] for row in monthly_data]
    monthly_amounts = [row[1] for row in monthly_data]


    #  Yearly
    cursor.execute("""
    SELECT YEAR(date), SUM(amount)
    FROM expenses
    GROUP BY YEAR(date)
    ORDER BY YEAR(date)
    """)
    yearly_data = cursor.fetchall()

    years = [str(row[0]) for row in yearly_data]
    yearly_amounts = [row[1] for row in yearly_data]


    #  Daily
    cursor.execute("""
    SELECT date, SUM(amount)
    FROM expenses
    GROUP BY date
    ORDER BY date
    """)
    daily_data = cursor.fetchall()

    days = [row[0] for row in daily_data]
    daily_amounts = [row[1] for row in daily_data]

    #  Category-wise data
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    chart_data = cursor.fetchall()

    categories = [row[0] for row in chart_data]
    amounts = [row[1] for row in chart_data]

    # Create chart
    if amounts:
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    else:
        plt.text(0.5, 0.5, "No Data", ha='center')
    # ================= ADD BELOW =================

    #  Monthly Graph
    plt.figure()
    plt.plot(months, monthly_amounts, marker='o')
    plt.title("Monthly Expenses")

    img1 = io.BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)
    monthly_graph = base64.b64encode(img1.getvalue()).decode()
    plt.close()


    #  Yearly Graph
    plt.figure()
    plt.bar(years, yearly_amounts)
    plt.title("Yearly Expenses")

    img2 = io.BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    yearly_graph = base64.b64encode(img2.getvalue()).decode()
    plt.close()


    #  Daily Graph
    plt.figure()
    plt.plot(days, daily_amounts, marker='o')
    plt.title("Daily Expenses")

    img3 = io.BytesIO()
    plt.savefig(img3, format='png')
    img3.seek(0)
    daily_graph = base64.b64encode(img3.getvalue()).decode()
    plt.close()
    plt.title("Expense Distribution")

    # Save chart to memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    graph_url = base64.b64encode(img.getvalue()).decode()

    plt.close()

    db.close()

    return render_template(
        'index.html',
        expenses=data,
        total=total,
        graph_url=graph_url,
        monthly_graph=monthly_graph,
        yearly_graph=yearly_graph,
        daily_graph=daily_graph
    ) 
# Add expense
@app.route('/add', methods=['POST'])
def add():
    category = request.form['category']
    amount = request.form['amount']
    date = request.form['date']  

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO expenses (category, amount, date) VALUES (%s, %s, %s)",
        (category, amount, date)
    )

    db.commit()
    db.close()

    return redirect('/')
@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM expenses WHERE id = %s", (id,))
    db.commit()
    db.close()

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
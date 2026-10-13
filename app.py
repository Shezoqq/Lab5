       <li>Difference: {{ results['difference'] }}</li>
                <li>Product: {{ results['product'] }}</li>
                <li>QuotieemC</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            calc = Calculations(a, b)





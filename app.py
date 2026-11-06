from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- PAGE 1: THE MAIN TERMINAL ---
MAIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>FOREIGN 521631 // AUTHENTICATION</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Space+Mono&display=swap');
        
        body {
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Inter', sans-serif;
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-image: radial-gradient(circle at 50% 50%, #111 0%, #000 100%);
        }
        
        .container {
            width: 100%;
            max-width: 650px;
            padding: 40px;
            border: 1px solid #333;
            background: #000;
        }
        
        .header {
            display: flex;
            justify-content: space-between;
            border-bottom: 1px solid #333;
            padding-bottom: 15px;
            margin-bottom: 40px;
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            color: #888;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        
        .content {
            font-size: 15px;
            line-height: 1.8;
            margin-bottom: 50px;
            font-weight: 300;
        }
        
        .content b { font-weight: 600; }
        
        .input-group {
            display: flex;
            align-items: center;
            border-bottom: 1px solid #FFF;
            padding-bottom: 10px;
        }
        
        label {
            font-family: 'Space Mono', monospace;
            font-size: 14px;
            margin-right: 15px;
            font-weight: 600;
        }
        
        input[type="text"] {
            background: transparent;
            color: #FFF;
            border: none;
            font-family: 'Space Mono', monospace;
            font-size: 16px;
            width: 100%;
            outline: none;
            letter-spacing: 1px;
        }
        
        input[type="text"]::placeholder { color: #555; }
        
        input[type="submit"] {
            background: #FFF;
            color: #000;
            border: none;
            font-family: 'Space Mono', monospace;
            font-weight: bold;
            cursor: pointer;
            padding: 8px 20px;
            margin-left: 15px;
            text-transform: uppercase;
            transition: 0.2s;
            font-size: 14px;
        }
        
        input[type="submit"]:hover {
            background: #000;
            color: #FFF;
            outline: 1px solid #FFF;
        }
        
        .error {
            margin-top: 30px;
            padding: 15px;
            border: 1px solid #FFF;
            background: #FFF;
            color: #000;
            font-family: 'Space Mono', monospace;
            font-size: 13px;
            font-weight: bold;
            text-transform: uppercase;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <span>SYS: 521631</span>
            <span>CONNECTION: SECURE</span>
            <span>USER: GUEST</span>
        </div>
        
        <div class="content">
            <p><b>> Web browsers are useless here.</b></p>
            <p>> [File: 521631] The geometry is stable.</p>
            <br>
            <p style="color: #888; font-size: 13px;">Awaiting decryption key to proceed.</p>
        </div>
        
        <form method="POST" action="/">
            <div class="input-group">
                <label>DECRYPT ></label>
                <input type="text" name="code" autocomplete="off" autofocus placeholder="ENTER CODE HERE">
                <input type="submit" value="EXECUTE">
            </div>
        </form>
        
        {% if error %}
            <div class="error">[ERROR] INVALID CODE. THE <u>EYE</u> IS WATCHING.</div>
        {% endif %}
    </div>
</body>
</html>
"""

# --- PAGE 2: THE HIDDEN PAGE ---
HIDDEN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>521631 // ACCESS GRANTED</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&family=Space+Mono&display=swap');
        
        body { 
            background-color: #FFF; 
            color: #000; 
            font-family: 'Inter', sans-serif; 
            padding: 50px; 
            text-align: center; 
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        
        .box {
            border: 2px solid #000;
            padding: 60px;
            max-width: 600px;
        }
        
        h1 { 
            font-family: 'Space Mono', monospace;
            font-size: 2.5em;
            letter-spacing: -1px;
            margin-top: 0;
            border-bottom: 2px solid #000;
            padding-bottom: 20px;
        }
        
        p { 
            font-size: 16px; 
            line-height: 1.6;
        }
        
        .warning {
            font-family: 'Space Mono', monospace;
            font-weight: bold;
            background: #000;
            color: #FFF;
            padding: 10px;
            margin: 30px 0;
        }
        
        .blink { animation: blinker 1s step-start infinite; }
        @keyframes blinker { 50% { opacity: 0; } }
    </style>
</head>
<body>
    <div class="box">
        <h1>ACCESS GRANTED</h1>
        <p>WELCOME TO THE OTHER SIDE.</p>
        <p>FOREIGN FOREVER.</p>
        
        <div class="warning blink">>> YOUR IP HAS BEEN LOGGED <<</div>
        
        <p style="color: #555; font-size: 14px;">Search the book. Page 7, Line 5, Word 3.</p>
    </div>
</body>
</html>
"""

# --- PAGE 3: THE SECRET URL PATH ---
SECRET_URL_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>NULL</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono&display=swap');
        body { background-color: #000; color: #FFF; font-family: 'Space Mono', monospace; padding: 60px; line-height: 1.8; }
        h2 { border-bottom: 1px solid #FFF; padding-bottom: 20px; }
        b { background: #FFF; color: #000; padding: 2px 8px; }
    </style>
</head>
<body>
    <h2>DIRECTORY TRAVERSAL SUCCESSFUL.</h2>
    <p>You found the unlisted page.</p>
    <br>
    <p>The Vigenère password is: <b>NIGHTFALL</b></p>
    <br>
    <p style="color: #888;">Take this key back to the book cipher. Do not share it.</p>
</body>
</html>
"""

# --- THE LOGIC ---
@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        code = request.form['code'].upper()
        
        if code == '521631':
            return render_template_string(HIDDEN_PAGE)
        else:
            error = True 
            
    return render_template_string(MAIN_PAGE, error=error)

@app.route('/room')
def secret():
    return render_template_string(SECRET_URL_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
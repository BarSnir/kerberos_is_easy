import gssapi

# קבלת credentials מה־kinit (כבר מאוחסן ב־cache)
creds = gssapi.Credentials(usage='initiate')

# יצירת שם שירות (SPN של השרת)
service_name = gssapi.Name('HTTP/service.example.com@EXAMPLE.COM', name_type=gssapi.NameType.kerberos_principal)

# יצירת הקשר אבטחה (security context)
ctx = gssapi.SecurityContext(name=service_name, creds=creds)

# התחלת האימות
token = ctx.step()

print("Generated token:", token.hex())
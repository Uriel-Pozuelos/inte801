import html

def escape_html(text):
    return html.escape(text)

"""
utilidad para evitar ataques sql injection
"""
def escape_sql(text):
    unsafe_words = ["SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "TRUNCATE", "ALTER", "CREATE", "RENAME", "REPLACE", "JOIN", "UNION", "HAVING", "ORDER", "GROUP", "BY", "WHERE", "FROM", "INTO", "SET", "VALUES", "ALL", "ANY", "AS", "ASC", "BETWEEN", "CASE", "CROSS", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "DISTINCT", "EXISTS", "FALSE", "FULL", "IN", "INNER", "IS", "LIKE", "LIMIT", "NOT", "NULL", "ON", "OR", "OUTER", "SELECT", "TABLE", "TRUE", "WHERE", "XOR"]
    for word in unsafe_words:
        text = text.replace(word, "")
    return text

def safe(text):
    return escape_html(escape_sql(text))

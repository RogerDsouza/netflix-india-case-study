import sqlite3
import re

print("Running SQL queries...")

conn = sqlite3.connect('data/netflix_india.db')
cursor = conn.cursor()

with open('sql/analysis_queries.sql', 'r', encoding='utf-8') as f:
    sql_content = f.read()

# Remove comments
lines = sql_content.split('\n')
cleaned_lines = []
for line in lines:
    if not line.strip().startswith('--'):
        cleaned_lines.append(line)

cleaned_sql = '\n'.join(cleaned_lines)

# Split by semicolon
queries = cleaned_sql.split(';')

results_file = open('sql/query_results.txt', 'w', encoding='utf-8')

query_count = 0
for query in queries:
    query = query.strip()
    if len(query) > 20 and 'SELECT' in query.upper():
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            
            query_count += 1
            results_file.write(f"\n{'='*80}\n")
            results_file.write(f"QUERY {query_count}\n")
            results_file.write(f"{'='*80}\n")
            
            # Get column names
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                results_file.write("COLUMNS: " + ", ".join(columns) + "\n\n")
            
            if results:
                for row in results:
                    results_file.write(str(row) + '\n')
                results_file.write(f"\nTotal rows: {len(results)}\n")
            else:
                results_file.write("No results returned.\n")
                
            results_file.write("\n")
            print(f"✓ Query {query_count} completed - {len(results)} rows")
            
        except Exception as e:
            results_file.write(f"ERROR: {e}\n")
            print(f"✗ Query failed: {e}")

results_file.close()
conn.close()

print(f"\n✅ Done! {query_count} queries executed successfully.")
print("Results saved to: sql/query_results.txt")
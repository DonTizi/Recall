import sqlite3
import os

# Path to the SQLite database file
db_path = 'regular_data.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Assuming you have an image id to test
test_image_id = 5

# Retrieve the image data
cursor.execute("SELECT image FROM images WHERE id = ?", (test_image_id,))
image_data = cursor.fetchone()
if image_data:
    retrieved_image = image_data[0]

    # Save the retrieved image to a file for comparison
    output_file_path = f'retrieved_image_{test_image_id}.png'
    with open(output_file_path, 'wb') as file:
        file.write(retrieved_image) 

    # Check the size of the retrieved file
    file_size = os.path.getsize(output_file_path)
    print(f"Size of retrieved image file: {file_size} bytes")

# Close the database connection
conn.close()

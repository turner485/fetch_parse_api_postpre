import requests
import json
import psycopg2


# Function to fetch data from Twitch API
def fetch_clip_data():
    url = "https://twitch-api8.p.rapidapi.com/get_channel_videos"
    querystring = {"channel": "benjaminmcp0"}
    headers = {
        "x-rapidapi-key": "a1ae53b2afmsh9ae54f48b52754ap1a9484jsn4aabb4d8b11f",
        "x-rapidapi-host": "twitch-api8.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


# Function to insert data into PostgreSQL database
def insert_clip_data(data):
    conn = psycopg2.connect(
        dbname="twitch",
        user="postgres",
        password="test123",
        host="localhost",
        port="5432",
    )
    cursor = conn.cursor()

    for item in data:
        clip_id = item["id"]
        broadcaster_id = item["broadcaster"]["id"]
        broadcaster_display_name = item["broadcaster"]["displayName"]
        clip_title = item["clipTitle"]
        clip_view_count = item["clipViewCount"]
        created_at = item["createdAt"]
        curator_id = item["curator"]["id"]
        duration_seconds = item["durationSeconds"]
        game_id = item["clipGame"]["id"]
        game_name = item["clipGame"]["name"]
        slug = item["slug"]
        thumbnail_url = item["thumbnailURL"]
        profile_image_url = item["broadcaster"]["profileImageURL"]
        primary_color_hex = item["broadcaster"]["primaryColorHex"]

        # Insert data into the database
        cursor.execute(
            """
            INSERT INTO clips (id, broadcaster_id, broadcaster_display_name, clip_title, clip_view_count, created_at, curator_id, duration_seconds, game_id, game_name, slug, thumbnail_url, profile_image_url, primary_color_hex)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (
                clip_id,
                broadcaster_id,
                broadcaster_display_name,
                clip_title,
                clip_view_count,
                created_at,
                curator_id,
                duration_seconds,
                game_id,
                game_name,
                slug,
                thumbnail_url,
                profile_image_url,
                primary_color_hex,
            ),
        )

    conn.commit()
    conn.close()


def main():

    twitch_data = fetch_clip_data()

    if twitch_data:
        with open("twitch_data.json", "w") as json_file:
            json.dump(twitch_data, json_file, indent=4)

        # Step 3: Insert data into the PostgreSQL database
        insert_clip_data(
            twitch_data["user"]["videoShelves"]["edges"][0]["node"]["items"]
        )
        print("Data inserted into the database successfully.")


if __name__ == "__main__":
    main()
